import sqlite3
import re

def validate_number(number: str):
    if not re.fullmatch(r'\+375 ?\(?(29|25|33|44)\)? ?\d{3}-?\d{2}-?\d{2}', number):
        raise Exception('Wrong number')

class Contact:
    id: int
    first_name: str
    last_name: str
    phone: str

    def __init__(self, id: int, fname: str, lname: str, phone: str):
        self.id = id
        self.first_name = fname
        self.last_name = lname
        self.phone = phone


class PhoneBook:
    __db: sqlite3.Connection

    def __init__(self, filename: str):
        self.__db = sqlite3.connect(filename)
        self.__db.execute('''CREATE TABLE IF NOT EXISTS contacts (
            id integer PRIMARY KEY AUTOINCREMENT,
            name text NOT NULL,
            lastname text NOT NULL,
            phone text
            );''')

    def close(self):
        self.__db.close()

    def add_contact(self, contact_name: str, contact_lastname: str, contact_phone: str):
        self.__db.execute('INSERT INTO contacts (name, lastname, phone) VALUES (?, ?, ?)',
                          [contact_name, contact_lastname, contact_phone])
        self.__db.commit()

    def get_contacts(self):
        records = self.__db.execute('SELECT * FROM contacts ORDER BY name').fetchall()
        return [Contact(*rec) for rec in records]

    def update_contact(self, id: int, contact_name: str, contact_lastname: str, contact_phone: str):
        old = self.__db.execute('SELECT * FROM contacts WHERE id = ?', [id]).fetchone()
        if not old:
            raise Exception(f'No id={id} found')
        params = [
            contact_name or old[1],
            contact_lastname or old[2],
            contact_phone or old[3],
            id
        ]
        self.__db.execute('UPDATE contacts SET name = ?, lastname = ?, phone = ? WHERE id = ?', params)
        self.__db.commit()

class Menu:
    EXIT = 0
    ADD_CONTACT = 1
    GET_CONTACTS = 2
    UPDATE_CONTACT = 3

def run():
    book = PhoneBook('db.sqlite')
    while True:
        try:
            print(f"Выберите действие: ")
            print(f"{Menu.EXIT}. Выйти из программы")
            print(f"{Menu.ADD_CONTACT}. Добавить новый контакт")
            print(f"{Menu.GET_CONTACTS}. Вывести весь список контактов в алфавитном порядке.")
            print(f"{Menu.UPDATE_CONTACT}. Обновить номер контакта")
            number_to_select = int(input())
            match number_to_select:
                case Menu.EXIT:
                    print("До свидания!")
                    break
                case Menu.ADD_CONTACT:
                    contact_name = input('Введите имя: ')
                    contact_lastname = input('Введите фамилию: ')
                    contact_phone = input('Введите номер: ')
                    validate_number(contact_phone)
                    book.add_contact(contact_name, contact_lastname, contact_phone)
                case Menu.GET_CONTACTS:
                    contacts = book.get_contacts()
                    for contact in contacts:
                        print(f"{contact.first_name} {contact.last_name}: {contact.phone}\n")

                case Menu.UPDATE_CONTACT:
                    primary_key = int(input("Введите ID контакта: "))
                    contact_name = input('Введите имя: ')
                    contact_lastname = input('Введите фамилию: ')
                    contact_phone = input('Введите номер: ')
                    if len(contact_phone) > 0:
                        validate_number(contact_phone)
                    book.update_contact(primary_key, contact_name, contact_lastname, contact_phone)
        except Exception as e:
            print(e)
    book.close()


if __name__ == "__main__":
    run()
