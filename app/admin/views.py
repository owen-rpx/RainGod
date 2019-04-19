#-*- coding:utf-8 -*-

import os
import time
import json
import datetime
from functools import wraps
from datetime import datetime,timedelta
from io import BytesIO
from flask_mail import Message
from werkzeug.security import generate_password_hash
from app.apps import db
from app.admin import admin
from flask import render_template, make_response, session, redirect, url_for, request, flash, abort
from app.admin.forms import LoginForm, RegisterForm, wjpasswd,XiaoQuForm,HuForm,LouPanForm
from app.admin.uilt import get_verify_code
from app.models import User,XiaoQu,RenYuan,HuXinXi,LouPan


def tsc():
    t = time.time()
    tsc = int(round(t * 1000))
    return tsc

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
    return render_template("admin/index.html",name=session["admin"],tscv=tsc())

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


## 基础设置模块
# 小区管理
@admin.route("/subdistrictmgr/")
@admin_login_req
def subdistrictMgr():
    #data=([{'id': '000001', 'name': 'test111','address': '喜马拉雅山'},{'id': '000002', 'name': 'test111','address': '喜马拉雅山'},{'id': '000002', 'name': 'test111','address': '喜马拉雅山'},{'id': '000002', 'name': 'test111','address': '喜马拉雅山'},{'id': '000002', 'name': 'test111','address': '喜马拉雅山'},{'id': '000002', 'name': 'test111','address': '喜马拉雅山'},{'id': '000002', 'name': 'test111','address': '喜马拉雅山'},{'id': '000002', 'name': 'test111','address': '喜马拉雅山'}])
    dataSet = XiaoQu.query.all();
    json_list = []
    for xiaoqu in dataSet:
        json_dict = {}
        json_dict["id"] = xiaoqu.id
        json_dict["name"] = xiaoqu.name
        json_dict["mgeaddr"] = xiaoqu.mgeaddr
        json_list.append(json_dict)
    return render_template("admin/subdistrictmgr.html",jsonData=json_list)

    

@admin.route("/subdistrictmgr_change/",methods=['GET','POST'])
@admin_login_req
def subdistrictmgr_change():
    form=XiaoQuForm()
    if form.validate_on_submit():
        data = form.data
        isExist = XiaoQu.query.filter_by(name=data['xiaoquName']).count()
        if isExist >0:
            flash('添加失败,已存在!')
            return redirect(url_for("admin.subdistrictmgr_change"))
        xiaoqu = XiaoQu(
            name=data['xiaoquName'],
            mgeaddr=data['xiaoquAdd'],
        )
        db.session.add(xiaoqu)
        db.session.commit()
        flash("添加成功")
        return redirect(url_for("admin.subdistrictmgr_change")+"?status=success")
    return render_template("admin/subdistrictmgr_change.html",form=form)

# 楼盘管理
@admin.route("/estatemgr/")
@admin_login_req
def estateMgr():
    #data={["name": "aaa", "id": "1"],["name": "aaa", "id": "1"],["name": "aaa", "id": "1"]}
    dataSet = LouPan.query.all();
    json_list = []
    for loupan in dataSet:
        json_dict = {}
        json_dict["id"] = loupan.id
        json_dict["buildingno"] = loupan.buildingno
        json_dict["xiaoqu_id"] = loupan.xiaoqu.name
        json_list.append(json_dict)
    return render_template("admin/estatemgr.html",jsonData=json_list)

@admin.route("/estatemgr_change/",methods=['GET','POST'])
@admin_login_req
def estateMgr_change():
    form=LouPanForm(XiaoQu)
    if form.validate_on_submit():
        data = form.data
        isExist = LouPan.query.filter_by(buildingno=data['Lou_number'],xiaoqu_id=data['xiaoqu_option']).count()
        if isExist > 0:
            flash('添加失败,已存在!')
            return redirect(url_for("admin.estateMgr_change"))
        loupan = LouPan(
            buildingno=data['Lou_number'],
            xiaoqu_id=data['xiaoqu_option']
        )
        db.session.add(loupan)
        db.session.commit()
        flash("添加成功")
        return redirect(url_for("admin.estateMgr_change")+"?status=success")
    return render_template("admin/estatemgr_change.html",form=form)

# 户管理模块
@admin.route("/householdmgr/")
@admin_login_req
def householdMgr():
    dataSet = HuXinXi.query.all();
    json_list = []
    for huxinxi in dataSet:
        json_dict = {}
        json_dict["id"] = huxinxi.id
        json_dict["roomno"] = huxinxi.roomno
        json_dict["house_type"] = huxinxi.house_type
        json_dict["squares"] = huxinxi.squares
        json_dict["house_by_dt"] =str(huxinxi.house_by_dt)
        json_dict["house_cert"] = "有证" if huxinxi.house_cert=="1" else "无证"
        json_dict["active"] = "有效" if huxinxi.active else "无效"
        json_dict["loupan_id"] = huxinxi.loupan.buildingno
        json_dict["xiaoqu_id"] = huxinxi.loupan.xiaoqu.name
        json_list.append(json_dict)
    return render_template("admin/householdmgr.html",jsonData=json_list)
    
@admin.route("/householdmgr_change/",methods=['GET','POST'])
@admin_login_req
def householdmgr_change():
    form=HuForm(LouPan)
    if form.validate_on_submit():
        data = form.data
        isExist = HuXinXi.query.filter_by(roomno=data['huxinxiRoomno'],loupan_id=data['loupan_option']).count()
        if isExist >0:
            flash('添加失败,已存在!')
            return redirect(url_for("admin.householdmgr_change"))
        huXinxi = HuXinXi(
            roomno=data['huxinxiRoomno'],
            house_type=data['huxinxiHouse_type'],
            squares=data['huxinxiSquares'],
            house_by_dt=datetime.strptime(data['huxinxiHouse_by_dt'], "%Y-%m-%d") ,
            house_cert=data['huxinxiHouse_cer'],
            active=1,
            loupan_id=data['loupan_option'],  
        )
        db.session.add(huXinxi)
        db.session.commit()
        flash("添加成功")
        return redirect(url_for("admin.householdmgr_change")+"?status=success")
    return render_template("admin/householdmgr_change.html",form=form)
## 住户管理模块
# 新增住户
@admin.route("/createresident/")
@admin_login_req
def createResident():
    return render_template("admin/createresident.html",tscv=tsc())

# 编辑住户
@admin.route("/residentedit/<int:id>",methods=['GET'])
@admin_login_req
def residentEdit(id):
    return render_template("admin/editresident.html",tscv=tsc())

# 住户管理
@admin.route("/residentmgr/")
@admin_login_req
def residentMgr():
    data = ([
        {'id': '000001', 'name': '张三', 'sex': '男', 'renyuan_relationship': '本人', 'birthday': '1996-10-01', 'shenfenzheng': 211000199402126521,
            'minzu': '汉', 'hukou_type': '居民家庭户口', 'married_status': '未婚', 'juzhu_zhuangtai': '不住，户在', 'renyuan_type': '买', 'renkou_type': '居民'},
        {'id': '000002', 'name': '李四', 'sex': '男', 'renyuan_relationship': '丈夫', 'birthday': '1987-08-15', 'shenfenzheng': 211220199602126521,
            'minzu': '汉', 'hukou_type': '非农业户口', 'married_status': '未婚', 'juzhu_zhuangtai': '空挂', 'renyuan_type': '买', 'renkou_type': '跨省'},
        {'id': '000003', 'name': '王五', 'sex': '女', 'renyuan_relationship': '本人', 'birthday': '1991-08-11', 'shenfenzheng': 211220199702126521,
            'minzu': '汉', 'hukou_type': '居民家庭户口', 'married_status': '未婚', 'juzhu_zhuangtai': '常住，户在', 'renyuan_type': '买', 'renkou_type': '跨省'},
        {'id': '000004', 'name': '赵六', 'sex': '女', 'renyuan_relationship': '妻子', 'birthday': '1992-06-11', 'shenfenzheng': 211220198202126521,
            'minzu': '汉', 'hukou_type': '非农业户口', 'married_status': '已婚', 'juzhu_zhuangtai': '空挂', 'renyuan_type': '买', 'renkou_type': '跨省'},
        {'id': '000005', 'name': '蔡徐坤', 'sex': '女', 'renyuan_relationship': '儿子', 'birthday': '1996-08-01', 'shenfenzheng': 211220199402126521,
            'minzu': '汉', 'hukou_type': '农业户口', 'married_status': '未婚', 'juzhu_zhuangtai': '常住，户在', 'renyuan_type': '买', 'renkou_type': '跨省'},
        {'id': '000006', 'name': '无邪', 'sex': '男', 'renyuan_relationship': '本人', 'birthday': '1996-11-11', 'shenfenzheng': 211220199402126521,
            'minzu': '汉', 'hukou_type': '居民家庭户口', 'married_status': '再婚', 'juzhu_zhuangtai': '空挂', 'renyuan_type': '租', 'renkou_type': '村民'}
    ])
    jsonData = json.dumps(data)
    return render_template("admin/residentmgr.html",tscv=tsc(),jsonData=jsonData)

# 加载成员模板
@admin.route("/dynresidenttable/<id>")
@admin_login_req
def dynResidentTable(id):
    return render_template("admin/_resident_frm.html",dynId=id)

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
#人员 search
@admin.route("/residentquery/",methods=['GET'])
@admin_login_req
def r_search():
	name=request.args.get("rname","")
	sfz=request.args.get("sfz","")
	
	result=[];
	if name !="" and sfz!="":
		result=RenYuan.query.filter(RenYuan.name==name & RenYuan.shenfenzheng==sfz)
	elif name!="":
		result=RenYuan.query.filter(RenYuan.name==name)
	elif sfz!="":
		result=RenYuan.query.filter(RenYuan.shenfenzheng==sfz)
	else:
		result=RenYuan.query.all()
	d_result=[row.as_dict() for row in result];
	rr={"code":0,"msg":"","count":"","data":d_result}
	return json.dumps(rr)


#人员 search id
@admin.route("/residenteidtid/<int:id>",methods=['GET'])
@admin_login_req
def r_search_id(id):	
    result=[];
    result=RenYuan.query.filter(RenYuan.id==id)
    d_result=[row.as_dict() for row in result];
    rr={"code":0,"msg":"","count":"","data":d_result}
    # return json.dumps(rr)
    jsonData = json.dumps(rr)
    return render_template("admin/editresident.html",tscv=tsc(),jsonData=jsonData)


@admin.route("/xiao_lou")
def  get_xiaoqu_loupan():
        xqs=XiaoQu.query.all()
        result=[]
        for xiaoqu in xqs:
                r=xiaoqu.as_dict()
                t=[]
                for loupan in xiaoqu.loupans:
                        t.append(loupan.as_dict())
                r["loupans"]=t
                result.append(r)
        rr={"code":0,"msg":"","count":"","data":result}
        return json.dumps(rr)


@admin.route("/insertresident", methods=['POST'])
# @admin_login_req
def insertResident():
    data = request.get_json()
    print(len(data))
    # print(data[0]['birthday'])
    try:
        for item in data:
            r = RenYuan()
            if(item['name'] != ""):
                r.name = item['name']
            r.sex = item['sex']
            r.minzu = item['minzu']
            r.wenhua = item['wenhua']
            r.hukou_type = item['hukou_type']
            r.zhengzhi_mianmao = item['zhengzhi_mianmao']
            if(item['join_party_dt'] != ''):
                r.join_party_dt = datetime.strptime(
                    item['join_party_dt'], '%Y-%m-%d').date()
            r.belief = item['belief']
            r.huji_addr = item['huji_addr']
            if(item['huji_in_dt'] != ''):
                r.huji_in_dt = datetime.strptime(
                    item['huji_in_dt'], '%Y-%m-%d').date()
            if(item['huji_out_dt'] != ''):
                    r.huji_out_dt = datetime.strptime(
                        item['huji_out_dt'], '%Y-%m-%d').date()
            if(item['birthday'] != ''):
                    birthday = datetime.strptime(
                        item['birthday'], '%Y-%m-%d').date()
            r.shenfenzheng = item['shenfenzheng']
            r.phone = item['phone']
            r.work_addr_title = item['work_addr_title']
            r.juzhu_zhuangtai = item['juzhu_zhuangtai']
            r.yibao_qingkuang = item['yibao_qingkuang']
            r.yanglao_baoxian = item['yanglao_baoxian']
            r.jiuye_yixiang = item['jiuye_yixiang']
            r.married_status = item['married_status']
            if(item['married_dt'] != ''):
                r.married_dt = datetime.strptime(
                    item['married_dt'], '%Y-%m-%d').date()
            r.dusheng_zinv = item['dusheng_zinv']
            r.dusheng_zinv_id = item['dusheng_zinv_id']
            if(item['dusheng_zinv_dt'] != ''):
                r.dusheng_zinv_dt = datetime.strptime(
                    item['dusheng_zinv_dt'], '%Y-%m-%d').date()
            r.jieyu_cuoshi = item['jieyu_cuoshi']
            r.plan_more_child = item['plan_more_child']
            r.renkou_type = item['renkou_type']
            r.has_car = item['has_car']
            r.is_dibao = item['is_dibao']
            r.is_kongchao = item['is_kongchao']
            r.is_duju = item['is_duju']
            r.is_lichao = item['is_lichao']
            r.join_community_management = item['join_community_management']
            r.join_community_activity = item['join_community_activity']
            r.join_comminity_volunteer = item['join_comminity_volunteer']
            r.join_party = item['join_party']
            r.has_dog = item['has_dog']
            if(item['ruzhu_dt'] != ''):
                r.ruzhu_dt = datetime.strptime(item['ruzhu_dt'], '%Y-%m-%d').date()
            if(item['ruhu_dt'] != ''):
                r.ruhu_dt = datetime.strptime(item['ruhu_dt'], '%Y-%m-%d').date()
            r.suggestion = item['suggestion']
            r.comment = item['comment']
            r.renyuan_type = item['renyuan_type']
            r.renyuan_relationship = item['renyuan_relationship']
            if(item['hu_id']!=''):
                r.hu_id = int(item['hu_id'])
            r.active = 1
            # 
            db.session.add(r)
        db.session.commit()
    except:
            db.session.rollback()
            db.session.flush()
    rr={"code": 0, "msg": "ok", "count": "", "data": []}
    return json.dumps(rr)
