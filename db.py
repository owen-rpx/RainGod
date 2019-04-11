# -*- coding:utf-8 -*-

import sqlite3

conn = sqlite3.connect('lwt.db')
print("Opened database successfully")
cursor = conn.cursor()
sql_scripts = '''
DROP TABLE IF EXISTS user;
CREATE TABLE user  (
  user_id INTEGER PRIMARY KEY AUTOINCREMENT,
  user_count CHAR(50) NULL DEFAULT NULL,
  user_name CHAR(50) NULL DEFAULT NULL,
  user_sex CHAR(50) NULL DEFAULT NULL,
  user_pwd CHAR(50) NULL DEFAULT NULL,
  user_mail CHAR(50) NULL DEFAULT NULL,
  user_phone CHAR(50) NULL DEFAULT NULL,
  user_addtime datetime(0) NULL DEFAULT NULL,
  user_photo CHAR(50) NULL DEFAULT NULL,
  user_ispass tinyint(1) NULL DEFAULT NULL
);

INSERT INTO user VALUES (1, 'root', '超级管理员', '男', 'pbkdf2:sha256:50000$WuO0dDYG$bc6abb402d99663d82737a36898bc862d672465cece851764078845cb0445f25', '916149179@qq.com', '13000000000', '2018-11-08 19:00:56', NULL, 1);

'''
cursor.executescript(sql_scripts)

conn.commit()
print("Update database successfully")
conn.close()
print("Close database successfully")
