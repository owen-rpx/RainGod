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
