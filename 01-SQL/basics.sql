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











 
 
 
 
 
 
 
 
 
 
 
 
 
 






 
 
 
 
 
 



