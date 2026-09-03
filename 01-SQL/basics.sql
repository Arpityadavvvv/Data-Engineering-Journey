-- class - 01 SQL Basics on movies database  (select , where , distinct , count )
USE moviesdb;
SELECT title , release_year from movies;    -- give title and relase year from movies 
SELECT count(*) FROM movies where industry = "hollywood"; -- all hollywood movies 
SELECT DISTINCT industry from movies;              -- diffrent industry 
SELECT * from movies where studio = "";            -- query for where studio is null
SELECT * from movies where title like 'captain%';  -- query for movies start with captain 

-- PRACTICE SHEET 1 FOR SQL BASICS
--  Q1 Print all movie titles and release year for all Marvel Studios movies.
SELECT title,release_year FROM movies where studio = "Marvel Studios";

-- 	Q2  Print all movies that have Avenger in their name.
SELECT * from movies where title like '%Avenger%';

-- Q3   Print the year when the movie "The Godfather" was released.
SELECT release_year FROM movies where title = "The Godfather";

-- Q4   Print all distinct movie studios in the Bollywood industry.
SELECT DISTINCT * FROM movies where  industry = "bollywood";

---------------------------------------------------------------------------------------------------------

-- class-02 SQL baiscs ( BETWEEN , IN , IS , AND , OR , ARTHEMETIC OPERATOR , NULL , ORDER BY , LIMIT , OFFSET )

-- OPERATORS (<,> ,<=,>=,=) ,(AND ,OR) ,BETWEEN
SELECT * FROM movies where imdb_rating > 9;  
SELECT * FROM movies where imdb_rating > 6 AND imdb_rating <= 9;  -- THIS IS ONE WAY , WE CAN ALSO DO IT BY SUING BETWEEN 
SELECT * FROM movies where imdb_rating BETWEEN 6 AND 8 ;          -- In this , it includes both 6 and 8 

SELECT *
FROM movies
where release_year = 2018 OR release_year = 2020 OR release_year = 2021;  -- THIS is also good but we can also use IN operator for this 

-- IN OPERATOR 
SELECT *
FROM movies 
where release_year  IN (2018,2020,2022); -- we can use this IN operator with text too

SELECT *
FROM movies 
where studio IN ("Hombale Films","Marvel Studios"); 

-- NULL = it means we dont have the value avialable 
SELECT * FROM movies where imdb_rating IS NULL ;
SELECT *  FROM movies where imdb_rating IS NOT NULL;

-- ordery BY CLAUSE (It is by default ascending order )
SELECT *
FROM movies 
where industry = "bollywood"
ORDER BY imdb_rating ;

SELECT *
FROM movies 
where industry = "bollywood"
ORDER BY imdb_rating DESC ;

-- LIMIT CLAUSE 

SELECT *
FROM movies 
where industry = "bollywood"
ORDER BY imdb_rating DESC 
LIMIT 5 ; -- IT will only give you top 5 from entire list 

-- OFFSET 
SELECT *
FROM movies 
where industry = "hollywood"
ORDER BY imdb_rating DESC
LIMIT 3 
OFFSET 1;  -- AFTER skipping one movie it will give you list of three 

-- PRACTICE SHEET 2 FOR SQL BASICS

-- Q1 Print all movies in the order of their release year (latest first)
SELECT * from movies 
order by release_year DESC;

-- Q2 All movies released in the year 2022
SELECT * FROM movies where release_year  = 2022;  -- quotes or either without quotes both will work 

-- Q3 Now all the movies released after 2020
SELECT * FROM movies WHERE release_year > 2020 ;

-- Q4  All movies after the year 2020 that have more than 8 rating
SELECT * FROM movies where release_year > 2020 AND imdb_rating > 8;

-- Q5 Select all movies that are by Marvel studios and Hombale Films
SELECT * FROM movies where studio IN ("Marvel studios","Hombale Films");

-- Q6 Select all THOR movies by their release year
SELECT * FROM movies where title LIKE '%Thor%' order by release_year DESC ;

-- Q7 Select all movies that are not from Marvel Studios
SELECT * FROM movies where studio NOT IN ("Marvel Studios");  

----------------------------------------------------------------------------------------------------------

-- class-03 SQL baiscs ( MAX, MIN , AVG , GROUPBY CLAUSE , AS _ NAME )

-- MAX,MIN function 
SELECT MAX(imdb_rating) FROM movies where studio = "Marvel Studios";
SELECT MIN(imdb_rating) FROM movies where studio = "Marvel Studios";
SELECT AVG(imdb_rating) FROM movies where studio = "Marvel Studios";
SELECT ROUND(AVG(imdb_rating),2) FROM movies where studio = "Marvel Studios"; -- ROUND FUNCTION WILL GIVE YOU ANSWER UPTO PARTICULAR DECIMAL , IF I GIVE 0 AS A PARAMTER IT WILL GICE ME A CIEL VALUE 
SELECT ROUND(AVG(imdb_rating),2) AS avg_rating  FROM movies where studio = "Marvel Studios"; 

SELECT MAX(imdb_rating) as max_Rating ,
 MIN(imdb_rating) as min_rating , 
 ROUND(AVG(imdb_rating),2) as avg_Rating 
 from movies  
 where studio = "Marvel Studios";
 
 -- group by clause 
 
 -- industry with movies count 
 SELECT industry , count(*) as cnt
 from movies 
 group by industry;
 
 SELECT industry , count(*) as cnt , avg(imdb_rating) as imrt
 from movies 
 group by industry
 order by cnt DESC;
 
 -- in this query one in one row there will be wmpty studio
 SELECT studio ,
 count(studio) as cnt , 
 round(avg(imdb_Rating),1)as rnt
 from movies 
 GROUP BY studio;
 
 
 -- in this query there will be no empty studion name 
 SELECT studio ,
 count(studio) as cnt , 
 round(avg(imdb_Rating),1)as rnt
 from movies 
 where studio != ""
 GROUP BY studio;
 
 
 
 SELECT studio , count(*) as mvcnt 
 from movies 
 group by studio;
 
 -- Quiz learnigns related too group by 
 -- 01 State whether the below statement is True or False. The columns used in the GROUP BY clause must be present in the Select clause. = TRUE
 
 -- 02 GROUP BY column → need not be in SELECT.
 --    But non-aggregated columns in SELECT → generally must be in GROUP BY.

 
 -- PRACTICE SHEET 3 FOR SQL BASICS
 
 -- Q1  How many movies were released between 2015 and 2022
 SELECT COUNT(*) FROM movies where release_year between 2015 AND 2022 ;
 
 -- Q2  Print the max and min movie release year
 SELECT MAX(release_year) as mxyr , MIN(release_year) as minyr 
 from movies ;
 
 -- Q3 Print each year along with the number of movies released in that year, starting from the most recent year
 SELECT release_year , COUNT(release_year) as no_of_movies  
 from movies 
 group by release_year 
 order by release_year DESC;
 
 -- class-03  SQL baiscs ( HAVING clause only  )
 
 select release_year , count(*) as movies_count
 from movies 
 where movies_count> 2   -- this query will not run because of the execution order of the sql
 group by release_year 
 order by movies_count desc;
 
 -- THE ORDER OF  EXECUTION OF SQL IS 
 -- FROM --> WHERE --> GROUP BY --> HAVING BY --> ORDER BY
 -- HAVING IS SAME AS WHERE , THE ONLY DIFFRENCE IS THAT IT WILL DO ANYTHING AFTER GROUPING BY 
 -- having is mainly used with group by operations 
 -- the main idffrence b/w where and having by is that , in case of where clause we can use any coloum without restrictions 
 -- but in having by , if we use any colum it must be stated in the select coloum 
 
 SELECT release_year , count(*) as movies_count
 FROM  movies 
 GROUP By release_year 
 having  movies_count>2
 ORDER BY movies_count desc;
 
 
 --------------------------------------------------------------------------------------------------------
 
 
 -- class - 04 Basic sql ( currdate , other funcions , operations , IF , CASE )
 -- we have to calculate current  age of every actor from actor table , where there birth year is given 
 
 SELECT *, YEAR(CURDATE()) - birth_year as age FROM actors;
 
 SELECT * , (revenue-budget) as profit FROM financials; -- but we cant comapare it to each other cause , currency is different 
 
 -- IF in sql
 
 -- syntax of if 
 -- IF( CONDITION , WHAT YOU WANT IF CONDIITON IS TRUE , WHAT YOU WANT IF CONDITION IS FALSE )
 -- if(condition, true , if not true )
 
 SELECT * ,
 IF (currency = 'USD' , revenue*95.70 , revenue) as revenue_in_INR  -- 95.70 is current diffrence of dollar and inr
 from financials;
 
 -- converting everything in million 
 -- for billion = rev * 1000
--  for thousand = rev/1000

 SELECT * ,
 IF (unit = 'Billions' , revenue * 1000 , IF( unit = 'Thousands' , revenue/1000 , revenue)) -- this is wrong way 
 AS revenue_mln ;
 
 -- we will use case statement 
 
--  CASE
--   WHEN condition1 THEN result1
--   WHEN condition2 THEN result2
--   WHEN conditionN THEN resultN
--   ELSE default_result
-- END;


 SELECT * ,
 CASE
    WHEN unit = 'Billions' THEN revenue*1000 
    WHEN unit = 'Thousands' THEN revenue/1000
    ELSE revenue
 END AS revenue_in_million
 FROM financials;

-- practice sheet class - 04 
-- Q1. Print profit % for all the movies
SELECT * , (revenue - budget)/100 as profit , (revenue - budget)*100/budget as profit_pct
from financials;

----------------------------------------------------------------------------------------------------------
-- SQL class 05 (Joins in sql , inner join , outer join (right , left , full) , union )

-- why we need joins , whats problem with single table ?
-- 01 To Reduce Data redunduncy , 02 organize data better , 03 make updates easily 

-- 01 INNER JOIN , by default in sql any join is called INNER JOIN if we didn't specify 
-- INNER JOIN - it will only give the content which is common in both tables 

-- in this query you will get error because , movie_id is in both table so you have to choose , which table you re prefering 
SELECT movie_id , title , budget , revenue , revenue-budget as profit , unit , currency 
FROM movies 
JOIN financials 
ON movies.movie_id = financials.movie_id;

-- this query will run 
SELECT movies.movie_id , title , budget , revenue , revenue-budget as profit , unit , currency 
FROM movies 
JOIN financials   -- by default inner join hi rhega yeh 
ON movies.movie_id = financials.movie_id;

-- for short notaion 
SELECT m.movie_id , title , budget , revenue , revenue-budget as profit , unit , currency 
FROM movies m
INNER JOIN financials f
ON m.movie_id = f.movie_id;  -- 37 rows 
-- IN this you will not get every movie or revenue of every movie , you will only get the entries which is common in both 

-- 02 LEFT JOIN 

-- In this , everything from choosen table will come in final table , and also all common things from second table , main table is that which we mention after from

SELECT m.movie_id , title , budget , revenue , revenue-budget as profit , unit , currency 
FROM movies m  -- (LEFT TABLE ) this is table which is main in left join and contain all entry of movies table and only common entry of financial table 
LEFT JOIN financials f -- (RIGHT TABLE )
ON m.movie_id = f.movie_id; -- 39 rows 
-- here you will get all the entries of movies table and only common entries of financial table 


-- 03 RIGHT JOIN  // we can also say RIGHT OUTER JOIN 

SELECT f.movie_id , title , budget , revenue , revenue-budget as profit , unit , currency 
FROM movies m -- left table 
RIGHT JOIN financials f -- right table 
ON m.movie_id = f.movie_id;  -- 40 rows 
-- in this it will contain each entry of right table and only common entry of left table 

-- 04 Full Outer Join 
-- Here we use union to join the both left join and right join to get full outer join 

SELECT m.movie_id , title , budget , revenue , revenue-budget as profit , unit , currency 
FROM movies m
LEFT JOIN financials f
ON m.movie_id = f.movie_id  -- 37 rows 

UNION

SELECT f.movie_id , title , budget , revenue , revenue-budget as profit , unit , currency 
FROM movies m
RIGHT JOIN financials f
ON m.movie_id = f.movie_id;  -- 37 rows 

-- USING clause 
-- it is used in case of ON when we are joining tables on some common colums , it can be one colum , or it can be multiple coloum 

SELECT movie_id , title , budget , revenue , revenue-budget as profit , unit , currency 
FROM movies m
INNER JOIN financials f
USING (movie_id);  -- 37 rows 

SELECT movie_id , title , budget , revenue , revenue-budget as profit , unit , currency 
FROM movies m
LEFT JOIN financials f
USING (movie_id);  -- 39 rows 

SELECT movie_id , title , budget , revenue , revenue-budget as profit , unit , currency 
FROM movies m
RIGHT JOIN financials f
USING (movie_id);  -- 40 rows  -- using bracket means we can also join on the basis of multiple coloum 

-- Examples of joinig table on multiple coloum
SELECT movie_id , title , budget , revenue , revenue-budget as profit , unit , currency 
FROM movies m
INNER JOIN financials f
ON m.movie_id = f.movie_id AND m.col2 = f.col2;  -- just a example it is 

-- practice sheet class - 05 
-- Q1 Show all the movies with their language names ?
SELECT m.title , l.name
FROM movies m
LEFT JOIN languages l
ON m.language_id = l.language_id; -- 39 rows 

SELECT m.title , l.name
FROM movies m
LEFT JOIN languages l
USING (language_id); -- 39 rows   -- in this question it was cleary meationed that they want all movies so i choose left join 


-- Q2 Show all Telugu movie names (assuming you don't know the language id for Telugu) ?
SELECT m.title                                   -- step 01 => do the join , and then filter the movie where language.name is telgue 
FROM movies m
LEFT JOIN languages l
ON m.language_id = l.language_id
WHERE l.name = 'Telugu';

-- Q3 Show the language and number of movies released in that language
SELECT l.name ,  Count(m.title) 
FROM movies m
RIGHT JOIN languages l
ON m.language_id = l.language_id
group by l.language_id;  -- here you have to tell l.language _id cause it will not work only with language_id


-- SQL Basics class 07  ( outer joines , and analytics after the results )
-- cross join analytics on movies db , for class 6 refer sql 02 file 

-- now we have to do some analytics or have to genrate some reprt 

SELECT m.movie_id,title,industry , revenue , budget ,unit ,currency
FROM movies m
LEFT JOIN financials f 
ON m.movie_id = f.movie_id
where industry = "bollywood";

-- now give me movie with list based on high profit 
SELECT m.movie_id,title,industry , revenue , budget ,unit ,currency ,revenue-budget as profit
FROM movies m
LEFT JOIN financials f 
ON m.movie_id = f.movie_id
where industry = "bollywood"
order by profit DESC;

-- But now here is the catch , pathar panchali is on top but not geniunly because three is diffrence in units , so make it all in million
SELECT m.movie_id,title,industry , revenue , budget ,unit ,currency ,
CASE
  WHEN unit="Thousands" THEN (revenue-budget)/1000 
  WHEN unit="Billions" THEN (revenue-budget)*1000 
  ELSE (revenue-budget) 
END as profit_mln
FROM movies m
LEFT JOIN financials f 
ON m.movie_id = f.movie_id
where industry = "bollywood"
order by profit_mln DESC;

 -- but there were too many zeros after profit_mln , so reduce them 
 
 SELECT m.movie_id,title,industry , revenue , budget ,unit ,currency ,
CASE
  WHEN unit="Thousands" THEN round((revenue-budget)/1000,1 )
  WHEN unit="Billions" THEN round((revenue-budget)*1000 ,1)
  ELSE round((revenue-budget) ,1)
END as profit_mln
FROM movies m
LEFT JOIN financials f 
ON m.movie_id = f.movie_id
where industry = "Bollywood"
order by profit_mln DESC;

----------------------------------------------------------------------------------------------------------
-- SQL basics class - 08 (Joining more than two tables , group_concat() function )
-- you have to draw the entity relationship diagram for that you have the website which is called 
-- (dbdiagram.io)
-- read about group_concat() function 
-- now i will join multiple table 

-- give me movie title with actors working in it by joining multiple tables

select m.title , aa.name
from movies m    -- table 1
inner join movie_actor ma -- table 2
on m.movie_id = ma.movie_id   -- inner join of 1 and 2 
inner join actors aa  -- table 3
on ma.actor_id = aa.actor_id; -- inner join of 2 and 3 

-- but in above result there is diffrent actor for same movie in diffrent rows , we want to be them in single rows

-- here we use group concat function 
select m.title , group_concat(name)
from movies m    -- table 1
inner join movie_actor ma -- table 2
on m.movie_id = ma.movie_id   -- inner join of 1 and 2 
inner join actors aa  -- table 3
on ma.actor_id = aa.actor_id -- inner join of 2 and 3 
group by m.movie_id;


-- its working fine but that the names should be seprated by some other stuff 
select m.title , group_concat(name SEPARATOR ' | ')
from movies m    -- table 1
inner join movie_actor ma -- table 2
on m.movie_id = ma.movie_id   -- inner join of 1 and 2 
inner join actors aa  -- table 3
on ma.actor_id = aa.actor_id -- inner join of 2 and 3 
group by m.movie_id;


-- now we want that one actor is in how many movies 

select aa.name , group_concat(title SEPARATOR ' | ')
from movies m    -- table 1
inner join movie_actor ma -- table 2
on m.movie_id = ma.movie_id   -- inner join of 1 and 2 
inner join actors aa  -- table 3
on ma.actor_id = aa.actor_id
group by aa.name;

-- still good way is this 

select aa.name , group_concat(title SEPARATOR ' | ') ,count(m.title) as movie_count
from actors aa    -- table 1
inner join movie_actor ma -- table 2
on aa.actor_id = ma.actor_id  -- inner join of 1 and 2 
inner join movies m  -- table 3
on ma.movie_id = m.movie_id
group by aa.name
order by movie_count DESC;

-- updation 24 aug to 31 aug 
-- practice sheet class - 08

-- Q1 1. Generate a report of all Hindi movies sorted by their revenue amount in millions. Print movie name, revenue, currency, and unit 
 SELECT m.title ,revenue, currency , unit ,
 CASE 
  WHEN unit="Thousands" THEN  revenue/1000 
  WHEN unit = "Billions" THEN revenue*1000
  ELSE revenue
 END  AS revenue_mln
 FROM financials f
 INNER JOIN movies m 
 ON m.movie_id = f.movie_id
 INNER JOIN languages l
 ON l.language_id = m.language_id
 where l.name = "Hindi"
 order by revenue_mln DESC;


------------------------------------------------------------------------ sheet 2 of workbench starts from here---------------------------------------------------------------

-- Class - 06 
-- CROSS JOIN  in sql ( IT IS ALSO KNOWN AS CARTESIAN PROJECT 3 ROWS IN TABLE 1 AND 3 ROWS IN TABLE 2 THEN AFTER CROSS JOIN IN FINAL TABLE THERE WILL BE 9  ROWS   )
-- CROSS JOIN is usefull when we dont have any common coloum in both tables 

USE food_db;
SELECT *
FROM items 
CROSS JOIN variants;

-- but we want full name like sandwich-plain in final , so to do this try googling and then get the concat function related to this 
SELECT * , concat(name , "-" ,variant_name) as full_name
FROM items 
CROSS JOIN variants;

-- now i also want price for full_name as well , so 
SELECT * , CONCAT(name , "-" ,variant_name) , price + variant_price as final_price
FROM items 
CROSS JOIN variants;

-- read about concatination function as well in 

---------------------------------------------------------------------------------------------------------

-- class - 08 ( subqueries )
# try to select movie with highest imdb rating ( we can do this by order by and limit 1 , but there is othre way too)

-- by using subqueris 
# subqueries return single value  01
# subqueries return multiple value  02
# subqueries return table   03

-- 01 
SELECT * FROM movies 
where imdb_rating =  max(imdb_rating) ; -- this will eventually fail 

SELECT * FROM movies 
where imdb_rating = (select max(imdb_rating) from movies); -- This is sub query , it is also called nested query , this ubquery return the single value 

SELECT * FROM movies                                   -- (subquery return sngle value)
where imdb_rating = (select min(imdb_rating) from movies);


-- 02
-- now what if i want min and max both in single query    (subquery return multiple value)
SELECT * FROM movies 
where imdb_rating IN ((select min(imdb_rating) from movies ),(select max(imdb_rating) from movies));
                         -- ( -- min                  ,                  max)
						

-- 03 subquery return a table 

# select the actor whos age >70 and <85
-- we can do it by having also , we can't do it by where 

-- IN this query you will get problem because , select is executed after the where clause and where clause using the age alias , so this will not work 
       select name,
       year(curdate())-birth_year as age
       from actors
       where age >70 AND age<85 ;
/*
Clause	   SELECT alias?
WHERE	   ❌ Generally no
HAVING	    ✅ MySQL mein often yes
ORDER BY	✅ Yes

-- Remeber this point , WHERE cannot use the alias of SELECT , but HAVING and ORDER BY can use the alias of SELECT
       
FROM
↓
WHERE
↓
GROUP BY
↓
HAVING  ( It will get the alias of SELECT )
↓
SELECT
↓
ORDER BY

*/

-- so now we will know how subquery return as table 
SELECT*
from 
(SELECT name , 
year(curdate())-birth_year as age   -- this result is a table
FROM actors ) as tbl
where age>70 AND age<85;

/* IMP NOTE 

01  A SELECT alias cannot normally be used directly in WHERE, but after putting the query inside a subquery,
 the alias becomes a column of the derived table and can be used by the outer WHERE. 
 
02 In MySQL, a derived table in the FROM clause must have an alias, such as AS tbl
*/
	
-- class - 09 ( ANY , ALL ,IN )

-- ANY -  ANY is used in similar fashion as IN operator 

# select actors who acted in any of these movies ( 101 , 110 , 121)

-- No this is not working 
SELECT name
from actors 
where actor_id IN (101,110,121);

-- 
select * from actors where actor_id = ANY (
  select actor_id from movies where movie_id IN (101,110,121)
);

# select all the movies whose rating is grater than ANY of the marvel movies 

-- movies which are greater imdb  than smallest of all 
select * from movies where  imdb_rating > Any(
select imdb_rating from movies where studio = "Marvel studios"  
);


-- all the movies which having greater rating then all the marvel movies 
select * from movies where  imdb_rating > ALL(
select imdb_rating from movies where studio = "Marvel studios"
);

-- we can also write this query instead of all 
select * from movies where imdb_rating > (
select max(imdb_rating) from movies where studio = "Marvel studios");

--------------------------------------------------------------------------------------------------------

-- class - 10 sql ( Co-related queries )

# select the actor id ,actor name and the total number of movies they acted in 

-- way -01 
explain analyze
select a.actor_id ,a.name ,count(*) as movie_count
from movie_actor ma 
join actors a 
ON a.actor_id = ma.actor_id
group by a.actor_id
order by movie_count desc;

-- way -02 by using co related query ( it seems tough but by repeating you will get it )
explain analyze
select 
    name ,
	actor_id ,
    (select count(*) from movie_actor ma where ma.actor_id = a.actor_id) as movies_count  -- this is subquery and it has refrence of outer table called a ,thats why it is called corelated query 
    from actors a
    order by movies_count desc ;
                        
  -- [EXPLAIN ANALYZE] => THIS is used for performance analysis 

-- practice sheet class 10 
-- Q1 Select all the movies with minimum and maximum release_year. Note that there
-- can be more than one movie in min and a max year hence output rows can be more than 2

select *
from movies 
where release_year IN ((select max(release_year) from movies ) ,(select min(release_year) from movies ));

-- Q2  Select all the rows from the movies table whose imdb_rating is higher than the average rating
select * from movies where imdb_rating > (
select avg(imdb_rating) as avgr from movies );

-- Q3 return all the movies which is released in a particular year 
select release_year , group_concat(title SEPARATOR '  | ') AS MOVI , count(title) as movi_count
from movies 
group by release_year
ORDER BY release_year desc;

-------------------------------------------------------------------------------------------------------

-- class 11 (common table expression )

-- This is like a temporary table which we can use for our diffrent results 

# select the actor whos age >70 and <85 ( we will do with CTE )

with actors_age as 
(
select                                       -- this is our temporary stored table on which we are working 
name as n,
year(current_date())- birth_year as age
 from actors
)

select n , age 
from actors_age 
where age>70 and age<85;

/*
Think of a CTE as a temporary named result of a query that you can use in the query immediately after it.

CTE = Common Table Expression

First, create a temporary result and call it actor_age.
Now use that temporary result

WITH actor_age AS (...)
          ↓
   Temporary result
          ↓
     actor_age
          ↓
SELECT * FROM actor_age
          ↓
     WHERE age > 70
     
The main advantage of a CTE is readability, especially when your query becomes large.

One important thing

A CTE is generally not a permanent table. It exists for the duration of that single SQL statement.

we can have multiple cte 

WITH
    CTE 1,
    CTE 2
    ↓
Main Query

WITH actor_age AS (
    SELECT name, YEAR(CURDATE()) - birth_year AS age
    FROM actors
),
old_actors AS (
    SELECT *
    FROM actor_age
    WHERE age > 70
)
SELECT *
FROM old_actors;

*/

# movies that produced 500% profit or more  and thier rating was less than avg rating for all movies 

-- self approach 
/* 
with avg_rating as 
(
select avg(imdb_rating) as avgr from movies 
)
,
prc_profit as 
(
select m.title , f.revenue , f.budget ,m.imdb_rating  ((f.revenue- f.budget )/f.budget*100) as profit_percent
from movies m 
join financials f 
on m.movie_id = f.movie_id
having profit_percent >= 500 
)

select p
from prc_profit pp
cross join avg_rating a
where pp.imdb_rating < a.avgr;

*/

-- solving by using sub queries (vv immp) (revison)

select t2.title , t2.imdb_Rating , t1.revenue , t1.budget
from (select * , (revenue-budget)*100/budget as prft from financials) t1
join (select * from movies where imdb_Rating < (select avg(imdb_Rating) from movies)) t2
on t1.movie_id = t2.movie_id
where prft >= 500;

-- by using CTE 
with
avg_Rating as 
(
 select * from movies where imdb_rating < (select avg(imdb_rating) as avgr from movies )
)
,
prft as 
(
select * , (revenue-budget)*100/budget as pp from financials 
)

select t1.title ,t2.revenue ,t1.imdb_Rating
from avg_Rating  t1
join prft t2
on t1.movie_id = t2.movie_id
where t2.pp >= 500;


-- Benifits  Of CTE
/*
01 simple queries 
02 good redability 
03 same results can be refrenced anywhere within the scope 
04 gives potential candidate for views 

https://dev.mysql.com/doc/refman/8.0/en/with.html   
ADVANCE CONCEPT OF RECURSIVE SUB QUERIES 
*/

-- PRACTICE SHEET CLASS 11  (revision)
/* Q1 Select all Hollywood movies released after the year 2000 that made more than 500 million $ profit 
or more profit. Note that all Hollywood movies have millions as a unit hence you don't need to do the 
unit conversion. Also, you can write this query without CTE as well but you should try to write this
 using CTE only */
 
 -- WITHOUT CTE 
 select t1.title , t1.industry , t2.profit ,t2.revenue , t2.unit
 from ( select * from movies where industry = "hollywood" AND release_year>2000) t1
 join (select * , (revenue-budget) as profit  from financials) t2
 on t1.movie_id = t2.movie_id
 where t2.profit>500
 order by t2.profit desc;
 
 -- WITH CTE 
 
 with 
 t1 as ( select * from movies where industry = "hollywood" AND release_year>2000) ,
 t2 as ( select * , (revenue-budget) as profit  from financials)
 
 select t1.title,t1.industry,t2.revenue,t2.profit,t2.unit
 from t1 
 join t2 
 on t1.movie_id = t2.movie_id
 where t2.profit>500
 order by t2.profit desc;
 
 -- or , more short than this 
 
 with cte as (select title, release_year, (revenue-budget) as profit
			from movies m
			join financials f
			on m.movie_id=f.movie_id
			where release_year>2000 and industry="hollywood"
	)
	select * from cte where profit>500;languages

-- ---------------------------------------------------------------------------------------------------------------------------------------------------------

-- Sql Class 12  (data intigrity and normalization)

/*
why we need multiple tables  => (data duplicacy , redundancy , more database storage )


01 Data intigrity = Data Integrity is the measure of consistency and accuracy of data over its life cycle.

02 ‘Link table’ is a term used to describe a table that acts as the link between the two tables.

03 Normalization is a process of organizing a database to avoid duplication, and improve data integrity

*/

-- Sql class 13 (ERD Diageam )

/*

*/


-- Sql class 14 (Data types in SQL ) difrent data types has diffrent storage spaces 
/*
01 Numeric data types =  these are used for whole numbers , and based on our requirements we will use this 

02 Floating point  =  (float 4 accuracy , double 8bytes precision , decimal ) float and double store  approximate value and decimal use exact value which is used in financial transaction 

03 String =  (char :  it is fixed length , char(3)=> depicts it always contain lengt as 3 not less not more ), 
              (Varchar : it is variable length , varchar(10) =>   it depicts 10 as a maximum size )
    
04 Enum  = (we use this when we know what we are storing has limited options , and you cannot edit a random value in the colum where you defined enum 
for ag :  units can be only thousand , billion , million , but if u try to use hundered there than it will be error )

05 Blob = (we can use image base encoding using BLOB )

06 data and time = (YEAR() , DATETIME() , TIME() , TIMESTAMP() , DATE)


SQL: YEAR vs INT

Storage: YEAR uses 1 Byte | INT uses 4 Bytes (75% memory waste)

Allowed Range: YEAR (1901 to 2155) | INT (-2.14B to +2.14B)

Data Validation: YEAR is auto-validated | INT requires a manual CHECK constraint

Index Speed: YEAR has smaller indexes, keeping queries faster in RAM

Takeaway:

Use YEAR for modern 4-digit years (1901–2155).

Use SMALLINT (2 Bytes) for historical years before 1901 or future years beyond 2155.


07  JSON => ()

*/


-- ---------------------------------------------------------------------------------------------------------------------------------------------------------

-- sql class -13 (Primary key )

/*

Primary key 
01  It is a natural key because it is a part of our data , and we use this for unique identification  ,
02 = it can have multiple coloums ,
03 it shouldnt be null
04 AI(auto increment) => this actually on inserting , auto increment the value , you can check it in movies_db by inserting new value in movies table

surrogate key =  primary key that is genrated by user artifically is called surrogate key , It is a artifically created for uniqely identify the record 

PK - primary key 

NN - not null 

UQ - unique index (: Ensures all values in the column are distinct across rows (allows one NULL value unless NN is also checked)

B  - binary (Stores data as binary byte strings instead of character data (used for VARBINARY, BLOB, or case-sensitive binary text matching)

ZF - Pads empty leading spaces with zeros up to the defined display width (e.g., displaying 7 as 0007).

AI - auto increment  (Automatically generates a sequential integer (+1) for every new inserted row.)

G  - genrated  - (it states for new coloum which we genrated like , we create new coloum for profit as revenue - budget in financials )

*/



-- ------------------------------------------------------------------------------------------------------------------------------------------------------

-- SQL class 14 (foriegn key) 31 aug
 /*

(movies -> language) defining a relationship 
=> first click child table then choose relationship and then click parent table 
01  language_id is forirgn key of movies table becuase language_id is primary key of language table which is refrenced in movie table 
02 it is one to many relationship , from right(language ) to left (movies) 
03 -> we choose unidentified one to many relationship because language_id is not a primary key for movies table and we cant identify anything by language_id 

02 can a table have one or more foriegn key ?
ANS =  

03 


04 

 1) on delete cascade  = it means on deleting in parent table , entry is also delted in child table 
 2) on delete null = it means on deleting in parent table , that entry in child table becomes null 
 3) on update cascade = it means the value which is updated in parent table will be simeltaniously updated in child table 
 4) on update null = it means on update the value in parent table , the value  became null in child table 
 
 forward enginnering -  by this option we can make the database schema from the ERD diagram .
 
 Reverse Engineering (synchronize function )- by this option we can make the changes in schema by refroming/renovating ERD diagram 
 
*/

-- How to add data in the table 

-- backfilling = Filling missing or newly added column data into existing past rows.

/*
The Problem: Running a direct full-table UPDATE locks the entire table, causing performance spikes and freezing live applications.

The Solution (Chunking): Updating historical data in small batches (1,000–5,000 rows at a time) using Primary Key ranges with short pauses in between.

Key Rule: Never execute an unbatched mass UPDATE on large production tables.
*/

-- Import csv from system 
/* 
01 first we will import languaes table because it is presnet in movies so before movies we will choose this 

02  choose some a defalut schhemalanguages

03  truncate = empty the table before isertion 

*/

----------------------------------------------------------------------------------------------------------
-- Sql class 14 (Insertion) 01 sept

insert into movies
values(default,"bahubali 5","bollywood","2037",null,null,2,null);  -- forgrign key constraint will fail here becuase of we cant give new value to language_id 

-- multiple insertion 
insert into movies
  (title , industry , language_id)
values
  ("inception 2" , "hollywood" , 5),
  ("inception 3" , "hollywood" , 5),
  ("inception 4" , "hollywood" , 5);
  
  select * from movies;
  

select * from my_movies.movies;
/*
Insert =  multiple ways to insert in table 
01) NORMAL directly in table via workbench 
02) if in schemaa we didnt make it NN , so it is not neccassary to use that colums 

*we have to apply every time to do proper changes because , just on the basis of visiblty of table we cant say anything *
*/

-------------------------------------------------------------------------------------------------------
-- Sql class 16 (update and delete )

-- updating single record 
UPDATE movies
SET 
    studio = "warner bros",
    release_year= 2028
    where movie_id = 144;

select * from movies;

-- multiple updation 
-- 01 
SET SQL_SAFE_UPDATES = 0; -- without this sql will not make you direct chnage in big database 
UPDATE movies
SET 
    studio = "warner bros",
    language_id =5
    where title LIKE "%inception%";
    
-- 02 safe way 
select movie_id from movies where title LIKE "%inception%"; -- then use this id for change using IN operator 

select * from movies;

-- DELETE
delete from movies where movie_id = 145;

-- learn the diffrence between delete , drop and truncate ?
/*
delete :Use to selectively remove specific rows while keeping everything else intact.
truncate : Use to wipe all data and reset a table to a clean state without destroying its schema/structure.
drop : Use when a table is no longer needed and should be completely removed from the database.
*/


-- quiz learnings 
/*
Q5. You are adding a column in your table to store USA phone numbers in this format (732)111-4567 What will be the most appropriate data type for this column?

CHAR(13) - this is ans because char also stores numner and special character 
VARCHAR(45)
DOUBLE
INT

here char(13) is a fix answer because , it has always 13 charcaters not more than that and 
*/


--------------------------------------------------------------------------------------------------------
-- Sql class 17 (Over clause )
-- over clause = The OVER clause in SQL is used with Window Functions to perform calculations across a specific set of rows (a "window") while retaining all original rows in the result set.
/*
diffrence between group by and over clause ?
GROUP BY vs. OVER()
GROUP BY: Reduces 100 individual rows into 5 grouped summary rows.

OVER(): Keeps all 100 individual rows and adds the aggregated/calculated value to each row. (it will consider whole table as a window 
over(partiton by category) = now it will consider windows by diffrent category 


Key Components
PARTITION BY: Divides the query result set into partitions/groups. The window function is calculated separately for each partition.

ORDER BY: Defines the logical order of rows within each partition. Crucial for rankings, running totals, or moving averages.
*/

select sum(amount)  as total from expenses; -- we only get total sum in one row 

select sum(amount) OVER()  as total from expenses; -- Now here you will get sun but with all rows

select category,sum(amount) as total from expenses  group by category;  -- here you will get sum amount of all category , so three rows cuz only three category there 

select *,sum(Amount) OVER(partition by category order by amount desc ) as total from expenses;   -- here you willl get all rows but total as partioned by category 

select * , sum(amount) OVER(partition by category order by date ) as total_till_date 
from expenses
order by total_till_date;

-- Sql class 18 (Rank , dense rank ,row number  )
/*

Think of these three functions as different ways a school teacher gives out ranks based on exam marks.

The Scenario
Four students get these test scores:

Rahul: 95 marks

Priya: 85 marks

Amit: 85 marks (Tie with Priya)

Suresh: 75 marks

1. ROW_NUMBER() — The Strict Counter
It ignores ties completely and just counts rows 1, 2, 3, 4 like giving out serial numbers.

Rahul: 1

Priya: 2

Amit: 3

Suresh: 4

Rule: Every row gets a unique number, even if scores are identical.
Best For: Deduplicating data or giving each row a unique sequence number.

2. RANK() — Standard School Ranking
If two students tie for 2nd place, both get 2nd place. But the next rank (3rd) is skipped because two people took up 2nd place.

Rahul: 1

Priya: 2

Amit: 2

Suresh: 4 (Rank 3 is skipped!)

Rule: Ties get the same rank, gaps are left in the numbers.
Best For: Official leaderboards, sports competitions, or exam results.

3. DENSE_RANK() — Compact Ranking (No Gaps)
Works like RANK(), but never skips numbers. It ranks unique levels/tiers rather than rows.

Rahul: 1

Priya: 2

Amit: 2

Suresh: 3 (No gaps!)

Rule: Ties get the same rank, no numbers are skipped.
Best For: Finding "Top 3 highest budgets" or "Top 3 highest salaries", where equal values should count as a single tier.

*/
select * , 
row_number() over (partition by category order by amount desc) as rn , -- it will do in order 1,2,3,4
rank() over( partition by category order by amount desc) as rr  ,-- it will do in order 1,2,2,4
dense_rank() over(partition by category order by amount desc) as dr -- it will do in order 1,2,2,3
from expenses;

-- by using CTE 
with cte1 as (
select * , 
row_number() over (partition by category order by amount desc) as rn , -- it will do in order 1,2,3,4
rank() over( partition by category order by amount desc) as rr  ,-- it will do in order 1,2,2,4
dense_rank() over(partition by category order by amount desc) as dr -- it will do in order 1,2,2,3
from expenses
order by category
)
select * from cte1 where rn>=3;










 
 
 
 
 
 



