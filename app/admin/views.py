#-*- coding:utf-8 -*-

import os
import time
from functools import wraps
from io import BytesIO
from flask_mail import Message
from werkzeug.security import generate_password_hash
from app.apps import db
from app.admin import admin
from flask import render_template, make_response, session, redirect, url_for, request, flash, abort
from app.admin.forms import LoginForm, RegisterForm, wjpasswd
from app.admin.uilt import get_verify_code
from app.models import User

def admin_login_req(f):
    @wraps(f)
    def decorated_function(*args,**kwargs):
        if 'admin' not in session:
            return redirect(url_for("admin.login",next=request.url))
        return f(*args,**kwargs)
    return decorated_function

def admin_power(f):
    @wraps(f)
    def admin_function(*args,**kwargs):
        # if session['power']!='root' :
        #     return render_template("admin/errorroot.html")
        return f(*args,**kwargs)
    return admin_function

# 登陆模块
@admin.route("/login/",methods=["GET","POST"])
def login():
    """登陆路由"""

    form=LoginForm()
    if form.validate_on_submit():
        data = form.data
        admin = User.query.filter_by(user_count=data['account']).first()
        if admin == None:
            flash("账号错误")
            return redirect(url_for("admin.login"))
        if not admin.check_pwd(data['pwd']):
            flash("密码错误")
            return redirect(url_for("admin.login"))
        session["admin"] = data['account']
        return redirect(request.args.get("next") or url_for("admin.index"))
    return render_template("admin/login.html", form=form)


# 验证码路由
@admin.route('/code/')
def code():
    """生成验证码图片流"""
    image, code = get_verify_code()
    buf = BytesIO()
    image.save(buf, 'jpeg')
    buf_str = buf.getvalue()
    response = make_response(buf_str)
    response.headers['Content-Type'] = 'image/gif'
    session['image'] = code
    return response

# 注册路由
@admin.route("/register/",methods=["GET","POST"])
def register():
    """注册路由"""
    form=RegisterForm()
    if form.validate_on_submit():
        data = form.data
        names = User.query.filter_by(user_count=data['account']).count()
        if names == 1:
            flash('注册失败')
            return redirect(url_for("admin.register"))
        ses=['','男','女']
        names = User(
            user_count=data['account'],
            user_pwd=generate_password_hash((data['pwd'])),
            user_name=data['name'],
            user_sex=ses[data['sex']],
            user_phone=data['phone'],
            user_mail=data['mail']
        )

        db.session.add(names)
        db.session.commit()
        flash("注册成功")

        return redirect(url_for("admin.login"))
    return render_template("admin/register.html",form=form)

# 忘记密码路由
@admin.route("/forgetpws/")
def forgetpws():
    pass

# 忘记密码
@admin.route("/wjmm/",methods=['GET','POST'])
def wjmm():
    form = wjpasswd()
    if form.validate_on_submit():
        usermessage = User.query.filter(User.user_count == form.data["countname"]).first()
        if usermessage is None:
            flash("账号错误！")
            return render_template("admin/wjmm.html", form=form)
        admin = User.query.filter_by(user_count=usermessage.user_count).first()

        if admin.user_mail != form.data['account']:
            flash('请输入正确的邮箱地址，或联系管理员修改')
            return render_template("admin/wjmm.html", form=form)

        admin.user_pwd = generate_password_hash((form.data['pwd']))
        mails=[]
        mails.append(form.data['account'])
        try:
            msg = Message('修改密码通知', sender='gchase@163.com', recipients=mails)
            msg.html = '<span>尊敬的</span>'+usermessage.user_name+'，您好：<br>您在we商贸中申请找回密码<br><b style="background-color: #FF0000">重设密码已完成,若非本人操作</b><br>请及时联系管理员修改<b>ganiner@163.com</b>'
            mail.send(msg)
            flash("修改成功")
            db.session.commit()
        except:
            db.session.rollback()
            db.session.flush()
        return redirect(url_for('admin.login'))
    return render_template("admin/wjmm.html", form=form)

# 首页
@admin.route("/")
@admin_login_req
def index():
    return render_template("admin/index.html",name=session["admin"])

@admin.route("/workPlatform/")
@admin_login_req
def workPlatform():
    return render_template("admin/workPlatform.html",name=session["admin"])

# 退出
@admin.route('/logout')
@admin_login_req
def logout():
    session.pop('admin',None)
    return redirect(url_for("admin.login"))


# 基础设置模块
# 小区管理
@admin.route("/subdistrictmgr/")
@admin_login_req
def subdistrictMgr():
    return render_template("admin/subdistrictmgr.html")
# 楼盘管理
@admin.route("/estatemgr/")
@admin_login_req
def estateMgr():
    return render_template("admin/estatemgr.html")

# 住户管理模块
@admin.route("/residentmgr/")
@admin_login_req
def residentMgr():
    return render_template("admin/residentmgr.html")

# 数据统计模块
@admin.route("/analysismgr/")
@admin_login_req
def analysisMgr():
    return render_template("admin/analysismgr.html")

# 系统工具模块
@admin.route("/importmgr/")
@admin_login_req
def importMgr():
    return render_template("admin/importmgr.html")
