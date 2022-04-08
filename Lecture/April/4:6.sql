select * from assistants cross join homework;

select * from assistants join homework on assistants.name = homework.creator;

select count(*) from assistants join homework on name = creator where age < 21;

select hw_name from assistants join homework on name = creator where year = 2;

select avg(age) from assistants join homework on name = creator;

select hw_name, name from assistants join homework on name = creator order by age;

# might get values from the left table that don't have a corresponding match in the right table,
# but they are still included with null for the right table spots

select * from assistants left join homework on name = creator;

select * from assistants right join homework on name = creator;

select name, age from assistants limit 3;

select count(name) from assistants left join homework on name = creator where hw_name is null;

select name, count(hw_name) from assistants full join homework on name = creator;