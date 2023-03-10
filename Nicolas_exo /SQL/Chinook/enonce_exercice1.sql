Use Chinook;
-- QUERY 1
-- Exploration of the Customer table in the Chinook database
SELECT * FROM Customer;

-- QUERY 2
-- Extract CustomerId, Company and City data from the customer table in the Chinook database


-- QUERY 3
-- Extract the Lastname, Firstname, email and city from the same table


-- QUERY 4
-- Extract the Lastname, Firstname, email, city and country from the same table
-- and select only the country starting with "AUSTR"
-- What do you observe? 2 RESULT


-- QUERY 5
-- Extract the Lastname, Firstname, email, city and country from the same table
-- only from USA and Canada


-- QUERY 6
-- Use the previous query and order the extracted data by lastname ascending


-- QUERY 7
-- Show the top 5 data in alphabetical order


-- QUERY 8
-- Extract the Top 5 data starting at row 5



-- QUERY 9
-- Count the number of clients you have in USA
-- Count the number of clients you have in Canada
SELECT DISTINCT Country, COUNT(CustomerId)
FROM customers
GROUP BY Country
HAVING Country IN ("USA", "Canada");

SELECT * FROM Customer;



-- QUERY 10
-- Count the number of clients you have in Berlin and in Paris (1 request and 1 line per cities)
SELECT City, COUNT(CustomerId)
FROM customers
WHERE City IN ("Paris", "Berlin")
GROUP BY City


-- QUERY 11
-- How many states are there and how many cities per state ?
SELECT State, COUNT(City)
FROM customers
GROUP BY State

-- QUERY 12
-- Count the number of clients per country and order them from the largest to the smallest.
SELECT Country, COUNT(CustomerId) as NoC
FROM customers
GROUP BY Country
ORDER BY  NoC DESC

--------------------------------
-- Let's change table !
-- Explore the Track table
Use Track;
SELECT * FROM Track;


-- QUERY 13
-- Extract the data about songs with name starting by let'
SELECT *
FROM tracks
WHERE Name LIKE "let'%"
-- Extract the data about songs with name containing good in it
SELECT *
FROM tracks
WHERE Name LIKE "%good%"
-- Extract the data about songs with name ending by you
SELECT *
FROM tracks
WHERE Name LIKE "%you"


-- QUERY 14
-- Extract the data about songs which length is from 230 et 240 seconds and order them from the longest to the shortest
SELECT *
FROM tracks
WHERE Milliseconds/1E3 BETWEEN 230 AND 240

-- QUERY 15
-- Extract data from the top 10 long songs which cost 0.99
SELECT *
FROM tracks
WHERE UnitPrice = 0.99
ORDER BY Milliseconds DESC
LIMIT 10

-- QUERY 16
-- Extract the different prices apply to the songs
SELECT DISTINCT UnitPrice
FROM tracks

-- Extract the different composer from the table
SELECT DISTINCT Composer
FROM tracks
-- Extract song where the price is bigger than the average price
SELECT *
FROM tracks
WHERE UnitPrice >  ( SELECT AVG(UnitPrice)  FROM tracks)


-- QUERY 17
-- Extract data of songs which genreid is 20 and album id is 253.
SELECT name
FROM tracks
WHERE AlbumId = "253" AND GenreId = "20"
-- Order them by the id of each track
SELECT name
FROM tracks
WHERE AlbumId = "253" AND GenreId = "20"
ORDER BY TrackId



-- QUERY 18
-- Calculate the length of songs in seconds
SELECT name,  Milliseconds*1.0 / 1000
FROM tracks
-- Count the number of songs whose songs are longer than the average length of song (eventually use a CASE)
SELECT COUNT(TrackId)
FROM tracks
WHERE Milliseconds  > (SELECT AVG(Milliseconds) FROM tracks)


-- QUERY 19
-- Calculate the average length of songs by album and count the number of songs by album
-- order by the number of songs descending
SELECT AlbumId,  AVG(Milliseconds*1.0 / 1000), COUNT(name)
FROM tracks
GROUP BY AlbumId
ORDER BY COUNT(name) DESC



-- QUERY 20 / Review
-- Extract the top 10 composers order from the longest average length of tracks and count the number of album the composer appear in
SELECT Composer, Milliseconds, COUNT(albumId)
FROM tracks
WHERE Composer IS NOT NULL
GROUP BY Composer
ORDER BY AVG(Milliseconds) DESC
LIMIT 10


-- Bonus:
-- QUERY 21 (line count : 58)
-- Name the composers whose total of length songs are longer than the total of the length songs of queen
SELECT Composer, SUM(Milliseconds), (SELECT  SUM(Milliseconds) FROM tracks WHERE  Composer LIKE "%QUEEN%") as queen
	FROM tracks
		WHERE Composer IS NOT NULL
			GROUP BY Composer
				HAVING SUM(Milliseconds) > queen


-- QUERY 22
-- How many composers did not compose any songs ?
SELECT COUNT(composer), COUNT(name)
FROM tracks
WHERE name IS NULL and composer IS  NULL
GROUP BY Composer
-- How many of songs are not refered to a composer ?
SELECT COUNT(name)
FROM tracks
WHERE composer IS  NULL


-- QUERY 23 (line count : 10)
-- Select the top 10 of composers by their number of tracks
SELECT composer, COUNT(name)
FROM tracks
GROUP BY Composer
LIMIT 10
-- You will see that the first one on the top is no-one

-- How is that possible? Comment here in 1 sentence
