-- drop the xiaoqu table first
drop table if exists xiaoqu;
-- then create the xiaoqu table
-- Add more fields if you like
create table xiaoqu(id integer primary key autoincrement,name varchar(50
),mgeaddr varchar(100));



--drop the loupan table first
drop table if exists loupan;
-- then create the loupan table
-- add more fields if you like

create table loupan(id integer primary key autoincrement,
buildingno varchar(30),
xiaoqu_id integer,
foreign key(xiaoqu_id) references xiaoqu(id)
);

-- drop the huxinxin table first
drop table if exists huxinxi;

-- then creat the huxinx table 
-- Add more fields if you like
create table huxinxi(id varchar(30) primary key,
roomno varchar(20),
house_type tinyint,
squares float,
house_by_dt date,
house_cert tinyint,
active int, -- determine if the item is history data
--xiaoqu_id integer not null,  -- relationship with table xiaoqu
-- foreign key(xiaoqu_id) references xiaoqu(id)
loupan_id int, -- relationship with table loupan
foreign key(loupan_id) references loupan(id)
);


--drop the renyuan table first
drop table if exists renyuan;
-- then create the renyuan table
-- Add more fields if you like
create table renyuan(id integer primary key autoincrement,
name varchar(20) not null,
sex  varchar(8),
minzu varchar(20),
wenhua varchar(20) ,
hukou_type varchar(20),
zhengzhi_mianmao varchar(20),
join_party_dt date,
belief tinyint,
huji_addr varchar(100),
huji_in_dt date,
huji_out_dt date,
birthday date,
shenfenzheng varchar(18),
phone varchar(12),
work_addr_title varchar(100),
juzhu_zhuangtai varchar(20),
jiank_zhuangtai varchar(20),
yibao_qingkuang varchar(20),
yanglao_baoxian varchar(20),
jiuye_yixiang varchar(20),
married_status  varchar(8),
married_dt  date,
dusheng_zinv int,
dusheng_zinv_id varchar(30),
dusheng_zinv_dt date,
jieyu_cuoshi varchar(20),
plan_more_child varchar(8),
has_car varchar(8),
is_dibao varchar(8),
is_kongchao varchar(8),
is_duju varchar(8),
is_lichao varchar(8),
join_community_management varchar(8),
join_community_activity varchar(8),
join_comminity_volunteer varchar(8),
join_party varchar(8),
has_dog varchar(8),
ruzhu_dt date,
ruhu_dt date,
suggestion varchar(100),
comment varchar(100),
active int, -- determine if the item is history data
hu_id integer, -- relationship with table huxinxi
foreign key(hu_id) references huxinxi(id)
);




