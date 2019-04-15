-- drop the xiaoqu table first
drop table if exists xiaoqu;
-- then create the xiaoqu table
-- Add more fields if you like
create table xiaoqu(id integer primary key autoincrement,name varchar(50
),mgeaddr varchar(100));


-- drop the huxinxin table first
drop table if exists huxinxi;

-- then creat the huxinx table 
-- Add more fields if you like
create table huxinxi(id varchar(30) primary key,
buildingno varchar(20),
roomno varchar(20),
xiaoqu_id integer not null,  foreign key(xiaoqu_id) references xiaoqu(id),
house_type varchar(20),
squares float,
house_by_dt date,
has_house_cert int);


--drop the renyuan table first
drop table if exists renyuan;
-- then create the renyuan table
-- Add more fields if you like
create table renyuan(id integer primary key autoincrement,
name varchar(20) not null,
sex  varchar(4),
minzu varchar(10),
wenhu varchar(10),
hukou_type varchar(12),
zhengzhi_mianmao varchar(10),
join_party_dt date,
zongjiao_xinyang varchar(12),
huji_addr varchar(100),
huji_in_dt date,
huji_out_dt date,
birthday date,
hukou_id varchar(18),
phone varchar(12),
work_addr_title varchar(100),
juzhu_zhuangtai varchar(20),
jiank_zhuangtai varchar(20),
yibao_qingkuang varchar(10),
yanglao_baoxian varchar(10),
has_jiuye_yixiang varchar(10),
is_married  varchar(1),
married_dt  date,
dusheng_zinv int,
dusheng_zinv_id varchar(30),
dusheng_zinv_dt date,
jieyu_cuoshi varchar(20),
plan_more_child varchar(1),
has_car varchar(1),
is_dibao varchar(1),
is_kongchao varchar(1),
is_duju varchar(1),
is_lichao varchar(1),
want_join_community varchar(1),
has_dog varchar(1),
ruzhu_dt date,
ruhu_dt date,
suggestion varchar(100),
comment varchar(100)
);




