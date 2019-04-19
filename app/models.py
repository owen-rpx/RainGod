#-*- coding:utf-8 -*-

from .apps import db

class User(db.Model):
    __tablename__ = 'user'

    user_id = db.Column(db.Integer, primary_key=True)
    user_count = db.Column(db.String(100), unique=True)
    user_name = db.Column(db.String(100), unique=True)
    user_sex = db.Column(db.String(100))
    user_pwd = db.Column(db.String(100))
    user_mail = db.Column(db.String(100))
    user_phone = db.Column(db.String(100))
    user_addtime = db.Column(db.DateTime, index=True)
    user_photo = db.Column(db.String(100))
    user_ispass = db.Column(db.Integer)

    def check_pwd(self,pwd):
        from werkzeug.security import check_password_hash
        return check_password_hash(self.user_pwd,pwd)
class XiaoQu(db.Model):
	__tablename__="xiaoqu"
	id=db.Column(db.Integer,primary_key=True, autoincrement=True)
	name=db.Column(db.String(50),unique=True)
	mgeaddr=db.Column(db.String(100))
	loupans=db.relationship("LouPan",backref="xiaoqu",lazy=True)
	def as_dict(self):
                return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class LouPan(db.Model):
	__tablename__="loupan"
	id=db.Column(db.Integer,primary_key=True, autoincrement=True)
	buildingno=db.Column(db.String(30))
	xiaoqu_id=db.Column(db.Integer,db.ForeignKey("xiaoqu.id"))
	def as_dict(self):
                return {c.name: getattr(self, c.name) for c in self.__table__.columns}
	huxinxis=db.relationship("HuXinXi",backref="loupan",lazy=True)
	def as_dict(self):
                return {c.name: getattr(self, c.name) for c in self.__table__.columns}
	

class HuXinXi(db.Model):
	__tablename__="huxinxi"
	id=db.Column(db.Integer,primary_key=True, autoincrement=True)
	renyuans=db.relationship("RenYuan",backref="huxinxi",lazy=True)
	roomno=db.Column(db.String(20),nullable=False)
	house_type=db.Column(db.String(20))
	squares=db.Column(db.Float);
	house_by_dt=db.Column(db.Date())
	house_cert=db.Column(db.String(10))
	active=db.Column(db.Integer,default=1)
	loupan_id=db.Column(db.Integer,db.ForeignKey("loupan.id"))
	def as_dict(self):
                return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class RenYuan(db.Model):
	__tablename__="renyuan"
	id=db.Column(db.Integer,primary_key=True, autoincrement=True)
	name=db.Column(db.String(30),nullable=False)
	sex=db.Column(db.String(8))
	minzu=db.Column(db.String(20))
	wenhua=db.Column(db.String(20))
	hukou_type=db.Column(db.String(20))
	zhengzhi_mianmao=db.Column(db.String(20))
	join_party_dt=db.Column(db.Date())
	belief=db.Column(db.String(20))
	huji_addr=db.Column(db.String(100))
	huji_in_dt=db.Column(db.Date())
	huji_out_dt=db.Column(db.Date())
	birthday=db.Column(db.Date())
	shenfenzheng=db.Column(db.String(18))
	phone=db.Column(db.String(12))
	work_addr_title=db.Column(db.String(100))
	juzhu_zhuangtai=db.Column(db.String(20))
	jiank_zhuangtai=db.Column(db.String(20))
	yibao_qingkuang=db.Column(db.String(20)) 
	yanglao_baoxian=db.Column(db.String(20))
	jiuye_yixiang=db.Column(db.String(20)) 
	married_status=db.Column(db.String(8))
	married_dt  =db.Column(db.Date())
	dusheng_zinv =db.Column(db.String(8))
	dusheng_zinv_id=db.Column(db.String(30))
	dusheng_zinv_dt=db.Column(db.Date())
	jieyu_cuoshi=db.Column(db.String(20)) 
	plan_more_child=db.Column(db.String(8))
	renkou_type=db.Column(db.String(8))
	has_car=db.Column(db.String(8)) 
	is_dibao=db.Column(db.String(8))
	is_kongchao=db.Column(db.String(8)) 
	is_duju =db.Column(db.String(8))
	is_lichao=db.Column(db.String(8))
	join_community_management=db.Column(db.String(8))
	join_community_activity=db.Column(db.String(8))
	join_comminity_volunteer=db.Column(db.String(8))
	join_party =db.Column(db.String(8))
	has_dog=db.Column(db.String(8))
	ruzhu_dt =db.Column(db.Date())
	ruhu_dt =db.Column(db.Date())
	suggestion=db.Column(db.String(100))
	comment=db.Column(db.String(100))
	renyuan_type=db.Column(db.String(10))
	renyuan_relationship=db.Column(db.String(30))
	active=db.Column(db.Integer,default=1)
	hu_id=db.Column(db.Integer,db.ForeignKey("huxinxi.id"))
	def as_dict(self):
		return {c.name: getattr(self, c.name) for c in self.__table__.columns}
