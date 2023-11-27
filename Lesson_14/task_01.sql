SELECT COUNT(*)
FROM user
WHERE age > 116;

SELECT SUM(age) as сумма_возрастов,
       AVG(age) as средний_возраст,
       SUM(age) / CAST(COUNT(*) as float) as средний_возраст,
       MIN(age) as минимальный_возраст,
       MAX(age) as максимальный_возраст,
       MAX(age) - MIN(age) as разница
FROM user;


