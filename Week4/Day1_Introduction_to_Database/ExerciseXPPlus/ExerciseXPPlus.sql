-- create table students (
-- id serial primary key,
-- 	last_name varchar (50),
-- 	first_name varchar (50),
-- 	birth_date date
-- );


-- insert into students (last_name, first_name, birth_date)
-- values 
-- ('Mark', 'Benichou', '1998-11-02'),
-- ('Yoan', 'Cohen', '2010-12-03'),
-- ('Lea', 'Benichou', '1987-07-27'),
-- ('Amelia', 'Dux', '1996-04-07'),
-- ('David', 'Grez', '2003-04-14'),
-- ('Omer', 'Simpson', '1980-10-03'),
-- ('Vladlena', 'Sotnikova', '1993-10-03');

-- select * from students

-- update students
-- set birth_date = '1993-07-14' where first_name = 'Sotnikova'

-- select * from students

-- select first_name,last_name from students

-- select first_name,last_name from students where id = 2

-- select first_name,last_name from students where last_name = 'Mark' and first_name = 'Benichou'

-- select first_name,last_name from students where last_name = 'Mark' or first_name = 'Benichou'

-- select last_name from students where last_name like '%a%'

-- select last_name from students where last_name ilike 'a%'

-- select last_name from students where last_name ilike '%a'

-- select last_name from students where last_name like '%a_'

-- select last_name from students where id in (1,3)

-- select last_name,first_name from students where birth_date >= '2000-01-01'


