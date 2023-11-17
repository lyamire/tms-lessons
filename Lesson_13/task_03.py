import sqlite3

def find_user():
    min_age = int(input('Введите минимальный возраст: '))
    with sqlite3.connect('sqlite.db') as connection:
        result = connection.execute('SELECT first_name, last_name, age, country '
                                    'FROM user WHERE age > ? ORDER BY age;',
                                    [min_age])
        for p in result.fetchall():
            print(p)


if __name__ == "__main__":
    find_user()
