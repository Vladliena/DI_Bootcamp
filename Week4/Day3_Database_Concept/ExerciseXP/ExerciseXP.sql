--Exercise 1

-- select language.name
-- from language

-- select film.title,description,language.name
-- from film
-- join language
-- on language.language_id = film.language_id;

-- select * from film
-- where language_id is Null

-- select film.title,description,language.name
-- from film
-- full outer join language
-- on language.language_id = film.language_id;

-- create table new_film(
-- id serial primary key,
-- name varchar (50) not NULL
-- );

-- insert into new_film(name)
-- values
-- ('Titanic'),
-- ('Harry Potter'),
-- ('Indiana Jones')


-- create table customer_review(
-- review_id serial primary key,
-- film_id int references new_film (id),
-- language_id int references language (language_id),
-- title varchar (50) not NULL,
-- score int check (score between 1 and 10) not NULL,
-- review_text text not NULL,
-- last_update date not NULL
-- );

-- insert into customer_review(film_id,language_id,title,score,review_text,last_update)
-- values
-- ((select id from new_film where name = 'Titanic'),(select language_id from language where name = 'Japanese'),'レオナルド', 8,'レオナルド・ディカプリオとケイト・ウィンスレットの演技が素晴らしい', '2023-12-01');
-- insert into customer_review(film_id,language_id,title,score,review_text,last_update)
-- values
-- ((select id from new_film where name = 'Harry Potter'),(select language_id from language where name = 'English'),'Excellent', 9,'The film is excellent','2022-10-11');
-- insert into customer_review(film_id,language_id,title,score,review_text,last_update)
-- values
-- ((select id from new_film where name = 'Indiana Jones'),(select language_id from language where name = 'English'),'Could be better', 6,'Im just not a fan.','2022-12-11');
-- SELECT * FROM customer_review

-- alter table public.customer_review
-- drop constraint customer_review_film_id_fkey,
-- add constraint customer_review_film_id_fkey
-- foreign key (film_id)
-- references new_film (id)
-- on delete cascade
-- on update cascade;

-- alter table public.customer_review
-- drop constraint customer_review_language_id_fkey,
-- add constraint customer_review_language_id_fkey
-- foreign key (language_id)
-- references language (language_id)
-- on delete cascade
-- on update cascade;

-- delete from new_film
-- where name = 'Harry Potter';

-- select * from customer_review

-- Exercise 2

-- update film
-- set language_id = 2
-- where title = 'African Egg'

-- question: Which foreign keys (references) are defined for the customer table? 
-- How does this affect the way in which we INSERT into the customer table? -- We are connecting film id with new_film id and languages in my new table and language for customer reviw table which we had before

-- drop table customer_review
-- dont need extra check

-- select count(*) from rental where return_date is Null

-- select title,replacement_cost
-- from rental
-- inner join inventory
-- on rental.inventory_id = inventory.inventory_id
-- left join film on inventory.film_id=film.film_id
-- where rental.return_date is NULL
-- order by replacement_cost desc limit 30

-- select film.film_id,film.title,film.description
-- from film_actor
-- inner join film
-- on film.film_id = film_actor.film_id
-- where (film_actor.actor_id = (select actor_id from actor where (first_name = 'Penelope' and last_name = 'Monroe' ) and film.fulltext @@ to_tsquery('english','sumo')))

-- select film.rating, film.length,film.title
-- from film
-- inner join film_category
-- on film.film_id = film_category.film_id
-- where (film_category.category_id = (select category_id from category where (rating = 'R' and length < 60) and category.name = 'Documentary' ))

-- select film.title, film.description from inventory
-- inner join film on film.film_id = inventory.inventory_id
-- inner join rental on rental.inventory_id = inventory.inventory_id
-- inner join customer on customer.customer_id = rental.customer_id
-- where customer.first_name = 'Matthew'and customer.last_name = 'Mahan' and film.rental_rate > 4
-- and rental.return_date between '2005-07-28' and '2005-08-01'

-- select * from inventory
-- inner join film on film.film_id = inventory.inventory_id
-- inner join rental on rental.inventory_id = inventory.inventory_id
-- inner join customer on customer.customer_id = rental.customer_id
-- where customer.first_name = 'Matthew'  and customer.last_name = 'Mahan' and film.description ilike '%boat%' or film.title ilike '%boat%'
-- order by film.replacement_cost desc 
