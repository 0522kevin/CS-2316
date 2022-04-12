use tv;

select * from shows where title like "%d" or title like "e";

select title from shows where num_seasons > 2;

select * from shows where title like "%c%";

select count(*) from actors where fname like "%a%" or lname like "%a%";

select fname, lname from actors order by actor_id limit 1;

select* from actors order by fname;

select count(*) from actors join shows on acts_on = show_id;

select title from actors join shows on acts_on = show_id where fname like "J%" or lname like "J%";

select fname, lname from actors join shows where lname like "C%" and genre = "Drama";

select * from tv.best_eps;

select title from best_eps join shows on s_id = show_id where ep_id in (101, 106, 108);