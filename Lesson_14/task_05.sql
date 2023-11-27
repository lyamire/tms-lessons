SELECT country, age
FROM user
WHERE age = (SELECT MAX(age) FROM user)
LIMIT 1;

SELECT *
FROM user
WHERE country = (SELECT country
                 FROM user
                 WHERE age = (SELECT MAX(age) FROM user)
                 LIMIT 1);

SELECT *
FROM user
WHERE last_name IN (SELECT last_name
                    FROM user
                    GROUP BY last_name
                    HAVING COUNT(last_name) > 1)
ORDER BY last_name;