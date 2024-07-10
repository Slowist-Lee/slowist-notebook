drop database if exists sqli_test;
create database sqli_test;
use sqli_test;

create table `users`
(
    id int,
    username char(32) not null,
    passwd char(32) not null
);

insert into users values(1, 'admin','123456');
insert into users values(2, 'root','654321');
insert into users values(3, 'jerry','play_signalis');

create table `chars`
(
    id int,
    name char(32) not null
);

insert into chars values(1, 'Yukikaze');
insert into chars values(2, 'Mia');
insert into chars values(3, 'Marimo');
