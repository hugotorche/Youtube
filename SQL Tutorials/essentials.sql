-- Final script for Corey Schafer SQL Tutorials (6 videos ~35min)

-- Part 1: 
-- 1) Getting started with PostGreSQL and dbeaver 
-- 2) Create our first database and table 
-- 3) Add records with INSERT 

-- Install Postgre SQL and create Database with terminal 

-- Create a new table people
drop table people ;

create table people (id INTEGER, first_name VARCHAR (255), last_name VARCHAR (255)) ;

-- Add the records 
insert into people values (1, 'Hugo', 'Torche') ;

insert into people values (2, 'Travis', 'Scott') ;

insert into people values (3, 'Novak', 'Djokovic') ;

insert into people values  (4, 'Naruto', 'Uzumaki'), 
                           (5, 'Erwin', 'Smith'), 
                           (6, 'Corey', 'Schafer'),
						   (7, 'John', 'Cena'), 
						   (8, 'Son', 'Goku'), 
						   (9, 'Peter', 'Parker'), 
						   (10, 'Harry', 'Potter') ;

-- Part 2: 
-- 1) Retreive records with SELECT 
-- 2) Modify records with UPDATE, ALTER and DELETE 
	  
select * from people ; 
-- Result: all the rows of the people table 

select * from people 
where last_name = 'Uzumaki'
or id > 8 ;
-- Result: Naruto Uzumaki, Peter Parker and Harry Potter 

select * from people 
where first_name like 'N%'
order by id desc ; 
-- Result: Naruto Uzumaki and Novak Djokovic 

-- Modify the records
delete from people
where last_name like 'S%' ;

alter table people
ADD category VARCHAR (255) ;

update people 
set category = 'IRL'
where last_name in ('Torche', 'Djokovic', 'Cena') ;

update people 
set category = 'Manga'
where last_name in ('Uzumaki', 'Goku') ;

update people 
set category = 'Film'
where last_name in ('Parker', 'Potter') ;

select * from people;
-- Result: final 7 rows table
