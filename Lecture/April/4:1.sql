DROP Database if exists CS2316;
Create Database CS2316;
Use CS2316;

drop table if exists students;
create table students 
(fname varchar(64),
lname varchar(64),
age int);

insert into students (fname,lname,age) values ("Bohong","Cheng",21);

select * from students;

-- select * FROM students WHERE fname LIKE "q%";