-- create db jiangkun
create database if not exists jiangkun default charset utf8;
-- create database if not exists jiangkun default charset utf8 collate utf8_general_ci;
use jiangkun;
-- create user table
create table user (
    id int not null auto_increment comment 'increment id',
    name varchar(100) not null comment 'user name',
    passwd varchar(100) not null comment 'password',
    primary key (id),
    unique key (name)
);

-- insert testing data
insert into user (name, passwd) values ('admin', 'admin');
insert into user (name, passwd) values ('user', 'pwd');
insert into user (name, passwd) values ('reboot', '123');
insert into user (name, passwd) values ('xiaoming', '456');
insert into user (name, passwd) values ('wd', 'uuu');

update user set passwd='1234uuu' where name='wd';
