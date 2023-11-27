SELECT ROUND((age / 100.0), 1) as Количество_столетий
FROM user;

SELECT LENGTH(first_name)
FROM user;

SELECT LENGTH(last_name)
FROM user;

SELECT LENGTH(first_name || ' ' || last_name)
FROM user;

SELECT SUBSTR(last_name, 1, 1) || '.' || SUBSTR(first_name, 1, 1) || '.' as инициалы
FROM user