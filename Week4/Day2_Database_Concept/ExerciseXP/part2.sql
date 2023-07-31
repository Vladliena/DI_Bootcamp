--1 select * from customer

--2 select first_name || ' ' || last_name as full_name from customer

--3 select distinct(create_date) from customer 

--4 select * from customer order by first_name

--5 select film_id,title,description,release_year,rental_rate from film order by rental_rate

--6 select address,phone from address where district = 'Texas'

--7 select title,description,release_year from film where film_id in(15,150)

--8 select film_id, title,description,release_year from film where title = 'Alter Victory'

--9 select film_id, title, description, release_year from film where title ilike 'al%'

--10 select title from film order by rental_rate fetch first 10 rows only

--11 select title from film order by rental_rate fetch first 10 rows only offset 10

--12 SELECT customer.first_name, customer.last_name, payment.amount, payment.payment_date
-- FROM customer
-- INNER JOIN payment
-- ON customer.customer_id = payment.customer_id;

--13 select film.title, inventory.inventory_id from film
-- left join inventory
-- on film.film_id = inventory.film_id
-- where inventory.film_id is null

--14 select city.city, country.country from city
-- inner join country
-- on city.country_id = country.country_id

--15 select payment.staff_id, customer.customer_id, concat(customer.first_name, ' ' ,customer.last_name),payment.amount,payment.payment_date
-- from customer
-- inner join payment
-- on customer.customer_id = payment.customer_id
-- order by payment.staff_id





