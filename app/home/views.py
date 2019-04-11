# -*- coding:utf-8 -*-

from app.home import home
from flask import render_template, session, redirect, url_for, request


@home.route("/")
def index():
    if 'admin' not in session:
        return redirect(url_for("admin.login", next=request.url))
    return render_template("admin/index.html", name=session["admin"])
