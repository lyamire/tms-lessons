SELECT *
FROM user
WHERE country = 'Япония';

SELECT COUNT(*)
FROM user
WHERE country = 'Япония';

SELECT *
FROM user
WHERE first_name = 'Мария';

SELECT *
FROM user
WHERE age > 116;

SELECT *
FROM user
ORDER BY age;

SELECT *
FROM user
ORDER BY age DESC LIMIT 1;

SELECT country, COUNT(country) as peoples
FROM user
GROUP BY country
ORDER BY peoples DESC








