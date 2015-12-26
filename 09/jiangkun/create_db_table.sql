-- create db jiangkun
create database if not exists jiangkun default charset utf8;

-- create database if not exists jiangkun default charset utf8 collate utf8_general_ci;
use jiangkun;

drop table user;
drop table server;

-- create user table
create table user (
    id int not null auto_increment comment 'increment user id',
    name varchar(100) not null comment 'user name',
    passwd varchar(100) not null comment 'password',
    -- role varchar(10) not null default 'user' comment 'role of the user',
    primary key (id),
    unique key (name)
);

-- create server table
create table server (
    id int not null auto_increment comment 'increament server id',
    host varchar(100) not null comment 'host name',
    memory int not null comment 'memory size',
    expiration_time timestamp not null comment 'the server invalid time',
    primary key (id),
    unique key (host)
);

-- insert testing data
insert into user (name, passwd) values ('admin', 'admin');
insert into user (name, passwd) values ('user', 'pwd');
insert into user (name, passwd) values ('reboot', '123');
insert into user (name, passwd) values ('xiaoming', '456');
insert into user (name, passwd) values ('wd', 'uuu');

--update user set passwd='1234uuu' where name='wd';
insert into server (host, memory, expiration_time) values ('reboot01', 24, '2017-1-1 00:00:00');
insert into server (host, memory, expiration_time) values ('reboot02', 16, '2017-2-1');