use university;

select last_name, gtid from students;

select * from enrolled;

select * from students where last_name = "Tentacles";

SELECT * FROM students ORDER BY birthday DESC;

select * from students order by last_name, first_name;

select birthday, count(*) FROM students GROUP BY birthday;

SELECT birthday, count(*) FROM students GROUP BY birthday HAVING birthday like "1977%" or birthday like "1998%";

use teaching;

select count(*) from assistants where name like "%h";

select * from assistants where year = 2;

select min(age) from assistants where year = 3;

select year, round(avg(age), 2) from assistants group by year;