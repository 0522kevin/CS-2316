drop database if exists hogwarts;

create database hogwarts;

use hogwarts;

create table classes (c_name varchar(30), enrollment int, teacher varchar(40));

create table professors (p_name varchar(40),house enum("slytherin","hufflepuff","ravenclaw","gryffindor"));	

create table students (s_name varchar(40), house enum("slytherin","hufflepuff","ravenclaw","gryffindor"));

insert into students values ("harry potter", "gryffindor");

insert into students values ("ron weasley", "gryffindor");

insert into classes values ("potions",20,"snape");

insert into professors values ("snape","slytherin");

insert into professors (p_name) values ('dumbledore');

UPDATE students SET house = "gryffindor" WHERE house is null;

UPDATE classes SET enrollment = 0 where teacher = "snape";

UPDATE students SET s_name="harold" where s_name LIKE "h%";

update students set house = 'hufflepuff';

DELETE FROM classes where enrollment < 5;


