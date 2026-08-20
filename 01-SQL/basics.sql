-- class - 01 SQL Basics on movies database  (select , where , distinct , count )  19 Aug 2026
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


-- class-02 SQL baiscs ( BETWEEN , IN , IS , AND , OR , ARTHEMETIC OPERATOR , NULL , ORDER BY , LIMIT , OFFSET ) 20 Aug 2026

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


-- class-03 SQL baiscs ( MAX, MIN , AVG , GROUPBY CLAUSE , AS _ NAME )   20 Aug 2026

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
 
 
 
 
 
 



