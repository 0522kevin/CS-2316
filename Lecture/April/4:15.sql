drop database if exists hogwarts;

create database hogwarts;

use hogwarts;

create table professors (
    p_name varchar(40),
    house enum("slytherin","hufflepuff", "ravenclaw","gryffindor"),
    primary key (p_name));

create table students (
    s_name varchar(40),
	house enum("slytherin","hufflepuff", "ravenclaw","gryffindor"),
	primary key (s_name));

create table classes (
   c_name varchar(30),
	enrollment int not null,
	teacher varchar(40),
	primary key (c_name),
	foreign key (teacher) REFERENCES professors(p_name));

insert into students values ("harry", "slytherin");

insert into students values ("harry", "gryffindor");

select * from students;