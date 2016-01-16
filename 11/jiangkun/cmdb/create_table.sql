use jiangkun;

create table server10(
    id int not null auto_increment primary key,
    name varchar(200),
    memory int,
    end_date varchar(30)
);

insert into server10 (name, memory, end_date) values ('reboot server', 4, '2016-10-01');
insert into server10 (name, memory, end_date) values ('woniu server', 2, '2016-05-01');