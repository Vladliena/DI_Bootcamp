--Part 1

-- create table customer(
-- id int primary key,
-- first_name varchar (50) not null,
-- last_name varchar (50) not null
-- );

-- create CustomerProfile (
--     id int PRIMARY KEY,
--     isLoggedIn BOOLEAN DEFAULT false,
--     customer_id INT UNIQUE,
--     FOREIGN KEY (customer_id) REFERENCES Customer(id)
-- );

-- insert into customer (id,first_name,last_name)
-- values
-- (1, 'Victor', 'Doe'),
-- (2, 'Pavel', 'Lelat'),
-- (3, 'Lea', 'Milner');

-- INSERT INTO CustomerProfile (id, isLoggedIn, customer_id)
-- VALUES
-- (1, true, (SELECT id FROM Customer WHERE first_name = 'Victor')),
-- (2, false, (SELECT id FROM Customer WHERE first_name = 'Pavel'));

-- select first_name
-- from customer
-- join CustomerProfile
-- on customer.id = CustomerProfile.id
-- where isLoggedIn = True

-- select first_name,isLoggedIn
-- from customer
-- left join CustomerProfile
-- on customer.id = CustomerProfile.id

-- select count (*)
-- from customer
-- join CustomerProfile
-- on customer.id = CustomerProfile.id
-- where CustomerProfile.isLoggedIn is Null or CustomerProfile.isLoggedIn = false

-- Part 2

-- CREATE TABLE Book (
--     book_id SERIAL PRIMARY KEY,
--     title VARCHAR(100) NOT NULL,
--     author VARCHAR(100) NOT NULL
-- );

-- INSERT INTO Book (title, author)
-- VALUES
--     ('Alice In Wonderland', 'Lewis Carroll'),
--     ('Harry Potter', 'J.K. Rowling'),
--     ('To Kill a Mockingbird', 'Harper Lee');
	
-- CREATE TABLE Student(
-- student_id Serial PRIMARY KEY,
-- name VARCHAR(50) NOT NULL UNIQUE,
-- age INT CHECK (age <= 15)
-- );

-- INSERT INTO Student (name, age)
-- VALUES
--('John', 12),
--('Lera', 11),
--('Patrick', 10),
--('Bob', 14);

-- CREATE TABLE Library (
--  book_fk_id INT REFERENCES Book (book_id) ON DELETE CASCADE ON UPDATE CASCADE,
--  student_fk_id INT REFERENCES Student (student_id) ON DELETE CASCADE ON UPDATE CASCADE,
--  borrowed_date DATE,
--  PRIMARY KEY (book_fk_id,student_fk_id)
-- );

-- INSERT INTO Library (student_fk_id, book_fk_id, borrowed_date)
-- VALUES
-- ((SELECT student_id FROM Student WHERE name = 'John'),(SELECT book_id FROM Book WHERE title = 'Alice In Wonderland'),'2022-02-15'),
-- ((SELECT student_id FROM Student WHERE name = 'Bob'),(SELECT book_id FROM Book WHERE title = 'To Kill a Mockingbird'), '2021-03-03'),
-- ((SELECT student_id FROM Student WHERE name = 'Lera'),(SELECT book_id FROM Book WHERE title = 'Alice In Wonderland'),'2021-05-23'),
-- ((SELECT student_id FROM Student WHERE name = 'Bob'),(SELECT book_id FROM Book WHERE title = 'Harry Potter'), '2021-08-12');

-- SELECT * FROM Library

-- SELECT Student.name, Book.title
-- FROM Library
-- JOIN Student
-- ON Student.student_id = Library.student_fk_id
-- JOIN Book
-- ON Book.book_id = Library.book_fk_id

-- SELECT AVG(Student.age)
-- FROM Student
-- WHERE student_id IN 
-- (SELECT student_fk_id 
--  FROM Library 
--  JOIN Book 
--  ON Book.book_id = Library.book_fk_id WHERE title = 'Alice In Wonderland' )
 
 
-- DELETE FROM Student WHERE NAME = 'Patric'
-- DELETE FROM Student WHERE NAME = 'Bob'

-- SELECT * FROM Library






