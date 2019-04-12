# -*- coding:utf-8 -*-

import time
from app.home import home
from flask import render_template, session, redirect, url_for, request


def tsc():
    t = time.time()
    tsc = int(round(t * 1000))
    return tsc

@home.route("/")
def index():
    if 'admin' not in session:
        return redirect(url_for("admin.login", next=request.url))
    return render_template("admin/index.html", name=session["admin"],tscv=tsc())
