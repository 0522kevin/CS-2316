use tv;

select count(*) from shows left join actors on show_id = acts_on where fname like "j%" group by shows.show_id;

select fname, lname from shows left join actors on show_id = acts_on where title like "%o%";

select avg(num_seasons) from shows left join actors on show_id = acts_on where lname like "%e%";

select title from shows where num_seasons between 5 and 9;

select title from shows where num_seasons < (select avg(num_seasons) from shows);

select fname, lname from actors where actor_id = (select max(actor_id) from actors);

use teaching;

select avg(age) from assistants where name in (select creator from homework);

select max(age) from assistants where name in (select creator from homework where hw_name like "H%");