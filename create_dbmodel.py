from app.apps import db
from app.models import User,XiaoQu,LouPan,HuXinXi,RenYuan
if __name__=="__main__":
	db.create_all() #自动创建表结构
	db.session.commit()
	#x=XiaoQu(name="龙王塘1号",mgeaddr="use1")
	x=XiaoQu(name="滨海家园",mgeaddr="use1")
	db.session.add(x)
	db.session.commit()
	print(x.id)
	l=LouPan(buildingno="1号楼",xiaoqu_id=x.id);
	db.session.add(l)
	db.session.commit()
	print(l.id)
	h=HuXinXi(roomno="1010",squares=80.4,loupan_id=l.id)
	db.session.add(h)
	db.session.commit()
	print(h.id)	

