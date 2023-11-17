import sqlite3

def find_user(min_age: int):
    with sqlite3.connect('sqlite.db') as connection:
        result = connection.execute('SELECT first_name, last_name, age, country '
                                    'FROM user WHERE age > ? ORDER BY age;',
                                    [min_age])
        for p in result.fetchall():
            print(p)


find_user(118)

