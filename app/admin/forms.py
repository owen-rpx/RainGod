# -*- coding:utf-8 -*-

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, TextAreaField, FloatField, IntegerField
from wtforms.validators import DataRequired
from app.models import User


# 登陆表单
class LoginForm(FlaskForm):
    account = StringField(
        label="用户名",
        validators=[
            DataRequired()
        ],
        description="账号",
        render_kw={
            "type": "text",
            "lay-verify": "required",
            "class": "layui-input",
            "placeholder": "请输入账号！",
        }

    )
    pwd = PasswordField(
        label="密码",
        validators=[
            DataRequired()
        ],
        description="密码",
        render_kw={
            "type": "password",
            "class": "layui-input",
            "placeholder": "请输入密码！",
            "lay-verify": "required",
        }
    )
    submit = SubmitField(
        "登陆",
        render_kw={
            "type": "submit",
            "lay-filter": "login",
            "style": "width:100%;",
            "onclick": "mesg()"
        }
    )


# 注册表单
class RegisterForm(FlaskForm):
    account = StringField(
        label='请输入用户名',
        validators=[
            DataRequired()
        ],
        description="输入用户名的输入框",
        render_kw={
            "type": "text",
            "lay-verify": "required",
            "class": "layui-input",
            "placeholder": "请输入登录名！",
        }
    )
    pwd = PasswordField(
        label='请输入密码',
        validators=[
            DataRequired()
        ],
        description="输入密码的输入框",
        render_kw={
            "type": "password",
            "class": "layui-input",
            "placeholder": "请输入密码！",
            "lay-verify": "required",
        }
    )
    repwd = PasswordField(
        label='请确认密码',
        validators=[
            DataRequired()
        ],
        description="确认密码的输入框",
        render_kw={
            "type": "password",
            "class": "layui-input",
            "placeholder": "请确认密码！",
            "lay-verify": "required",
        }
    )
    name = StringField(
        label='请输入真实姓名',
        validators=[
            DataRequired()
        ],
        description="请输入真实姓名输入框",
        render_kw={
            "type": "text",
            "class": "layui-input",
            "placeholder": "请输入真实姓名！",
            "lay-verify": "required",
        }
    )
    sex = SelectField(
        label="请选择性别",
        validators=[
            DataRequired()
        ],
        coerce=int,
        choices=[(0, "性别"), (1, "男"), (2, "女")],
        description="请选择性别",

        render_kw={
            "class": "contrller",
        }
    )
    phone = StringField(
        label='请输入电话号码',
        validators=[
            DataRequired()
        ],
        description="请输入电话号码",
        render_kw={
            "type": "text",
            "class": "layui-input",
            "placeholder": "请输入电话号码！",
            "lay-verify": "required",
        }
    )
    mail = StringField(
        label='请输入邮箱',
        validators=[
            DataRequired()
        ],
        description="请输入邮箱",
        render_kw={
            "type": "text",
            "class": "layui-input",
            "placeholder": "请输入邮箱！",
            "lay-verify": "required",
        }
    )
    submit = SubmitField(
        "注册",
        render_kw={
            "class": "layui-btn",
            "lay-filter": "subm",
            "onclick": "mesg()"
        }
    )



# 忘记密码
class wjpasswd(FlaskForm):
    countname = StringField(
        label='请输入登录名',
        validators=[
            DataRequired()
        ],
        description="请输入登录名",
        render_kw={
            "type": "text",
            "lay-verify": "required",
            "class": "layui-input",
            "placeholder": "请输入登录名！",
            'autocomplete': 'off'
        }
    )
    account = StringField(
        label='请输入邮箱',
        validators=[
            DataRequired()
        ],
        description="请输入邮箱",
        render_kw={
            "type": "text",
            "lay-verify": "required",
            "class": "layui-input",
            "placeholder": "请输入邮箱！",
            'autocomplete': 'off'
        }
    )
    pwd = PasswordField(
        label='请输入新密码',
        validators=[
            DataRequired()
        ],
        description="输入密码的输入框",
        render_kw={
            "type": "password",
            "class": "layui-input",
            "placeholder": "请输入新密码！",
            "lay-verify": "required",
            'autocomplete': 'off'
        }
    )
    repwd = PasswordField(
        label='请确认密码',
        validators=[
            DataRequired()
        ],
        description="确认密码的输入框",
        render_kw={
            "type": "password",
            "class": "layui-input",
            "placeholder": "请确认密码！",
            "lay-verify": "required",
            'autocomplete': 'off'
        }
    )
    submit = SubmitField(
        "修改密码",
        render_kw={
            "class": "layui-btn",
            "lay-filter": "subm",
        }
    )



#添加小区
class XiaoQuForm(FlaskForm):
    xiaoquName = StringField(
        label="小区名称",
        validators=[
            DataRequired()
        ],
        description="小区名称",
        render_kw={
            "type": "text",
            "lay-verify": "required",
            "class": "layui-input",
            "placeholder": "请输入小区名称！",
        }
    )
    xiaoquAdd= StringField(
        label="管理地址",
        validators=[
            DataRequired()
        ],
        description="管理地址",
        render_kw={
            "type": "text",
            "lay-verify": "required",
            "class": "layui-input",
            "placeholder": "请输入管理地址！",
        }
    )
    submit = SubmitField(
        "提交",
        render_kw={
            "type": "submit",
            "lay-filter": "submit",
            "style": "width:100px; height:30px;",
            "onclick": ""
        }
    )
#添加楼盘
class LouPanForm(FlaskForm):
    Lou_number = StringField(
        label="楼号",
        validators=[
            DataRequired()
        ],
        description="楼号",
        render_kw={
            "type": "text",
            "lay-verify": "required",
            "class": "layui-input",
            "placeholder": "请输入楼号！",
        }
    )
    xiaoqu_number = StringField(
        label="小区编号",
        validators=[
            DataRequired()
        ],
        description="小区编号",
        render_kw={
            "type": "text",
            "lay-verify": "required",
            "class": "layui-input",
            "placeholder": "请输入小区编号！",
        }
    )
    submit = SubmitField(
        "提交",
        render_kw={
            "type": "submit",
            "lay-filter": "submit",
            "style": "width:100px; height:30px;",
            "onclick": "mesg()"
        }
    )

    #添加户
class HuForm(FlaskForm):
    huxinxiRoomno = StringField(
        label="房间号",
        validators=[
            DataRequired()
        ],
        description="房间号",
        render_kw={
            "type":"text",
            "lay-verify":"required",
            "class":"layui-input",
            "placeholder":"请输入房间号！",
        }
    )
    huxinxiHouse_type=StringField(
        label="房屋类型",
        validators=[
            DataRequired()
        ],
        description="房屋类型",
        render_kw={
            "type":"text",
            "lay-verify":"requied",
            "class":"layui-input",
            "placeholder":"请输入房屋类型！",
        }
    )
    huxinxiSquares=StringField(
        label="面积",
        validators=[
            DataRequired()
        ],
        description="面积",
        render_kw={
            "type":"text",
            "lay-verify":"requied",
            "class":"layui-input",
            "placeholder":"请输入房屋面积！",
        }
    )
    huxinxiHouse_by_dt=StringField(
        label="购买日期",
        validators=[
            DataRequired()
        ],
        description="购买日期",
        render_kw={
            "type":"text",
            "lay-verify":"requied",
            "class":"layui-input",
            "placeholder":"请输入房屋购买日期！",
        }
    )
    huxinxiHouse_cer=StringField(
        label="房屋证明",
        validators=[
            DataRequired()
        ],
        description="房屋证明",
        render_kw={
            "type":"text",
            "lay-verify":"requied",
            "class":"layui-input",
            "placeholder":"请输入房屋证明！",
        }
    )
    huxinxiActive=StringField(
        label="有效",
        validators=[
            DataRequired()
        ],
        description="有效",
        render_kw={
            "type":"text",
            "lay-verify":"requied",
            "class":"layui-input",
            "placeholder":"请输入是否有效！",
        }
    )
    huxinxiLoupan_id=StringField(
        label="楼盘号",
        validators=[
            DataRequired()
        ],
        description="楼盘号",
        render_kw={
            "type":"text",
            "lay-verify":"requied",
            "class":"layui-input",
            "placeholder":"请输入楼盘号！",
        }
    )
    submit = SubmitField(
        "提交",
        render_kw={
            "type": "submit",
            "lay-filter": "submit",
            "style": "width:100px; height:30px;",
            "onclick": "mesg()"
        }
    )