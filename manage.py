#-*- coding:utf-8 -*-

from app.apps import app

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True,port=8080)