SELECT *
FROM user
ORDER BY age DESC;

SELECT *
FROM user
ORDER BY last_name, first_name;

SELECT *
FROM user
ORDER BY country, age DESC;

SELECT *
FROM user
ORDER BY LENGTH(first_name) + LENGTH(last_name);

SELECT *
FROM user
ORDER BY SUBSTR(last_name, 1, 1), SUBSTR(first_name, 1, 1)