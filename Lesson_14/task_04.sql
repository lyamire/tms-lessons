SELECT country, COUNT(country)
FROM user
GROUP BY country
ORDER BY COUNT(country);

SELECT first_name, COUNT(*) as c
FROM user
GROUP BY first_name
ORDER BY c DESC;

SELECT country, SUM(age)
FROM user
GROUP BY country;

SELECT country, ROUND(AVG(age), 1)
FROM user
GROUP BY country;

SELECT country, MAX(age)
FROM user
GROUP BY country;

SELECT country, COUNT(*) as c
FROM user
GROUP BY country
HAVING c >= 5
ORDER BY c DESC;

SELECT last_name, COUNT(*) as c
FROM user
GROUP BY last_name
HAVING c > 1;




