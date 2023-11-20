import sqlite3
from random import randint


class Config:
    BANK_DB = 'bank.db'

class BankAccount:
    card_holder: str
    money: float
    card_number: str
    account_number: str

    def __init__(self, card_holder: str, money: float = 0, card_number: str = None, account_number: str = None):
        self.card_holder = card_holder.upper()
        self.money = money
        self.card_number = card_number or self.get_random_digits(16)
        self.account_number = account_number or self.get_random_digits(20)

    @staticmethod
    def get_random_digits(count: int) -> str:
        """Создание случайной строки заданной длины"""
        result = ''
        for _ in range(count):
            result += str(randint(0, 9))
        return result


class Bank:
    __db: sqlite3.Connection
    __bank_accounts: dict[str, BankAccount] = []

    def __init__(self):
        self.__db = sqlite3.connect(Config.BANK_DB)
        self.__db.execute('''CREATE TABLE IF NOT EXISTS bank_accounts (
            account_number text NOT NULL PRIMARY KEY,
            card_holder text NOT NULL,
            money decimal(12,2) NOT NULL,
            card_number text NOT NULL);''')

        self.load_accounts()

    def open_account(self, card_holder: str) -> BankAccount:
        account = BankAccount(card_holder)
        self.create_account(account)
        self.__bank_accounts[account.account_number] = account
        return account

    def create_account(self, account):
        self.__db.execute(
            'INSERT INTO bank_accounts (card_holder, money, card_number, account_number) '
            'VALUES(?, ?, ?, ?)',
            [account.card_holder, account.money, account.card_number, account.account_number])
        self.__db.commit()

    def __get_account(self, account_number: str) -> BankAccount:
        return self.__bank_accounts[account_number]

    def get_all_bank_accounts(self) -> list[BankAccount]:
        return list(self.__bank_accounts.values())

    def add_money(self, account_number: str, money: float) -> float:
        account = self.__get_account(account_number)
        account.money += money
        self.update_account(account)
        return account.money

    def update_account(self, account):
        self.__db.execute(
            'UPDATE bank_accounts SET money = ? where account_number = ?',
            [account.money, account.account_number])
        self.__db.commit()

    def transfer_money(self, from_account_number: str, to_account_number: str, money: float):
        self.add_money(from_account_number, -money)
        self.add_money(to_account_number, money)
        print("Операция по переводу между счетами прошла успешно")

    def external_transfer(self, from_account_number: str, to_external_number: str, money: float):
        self.add_money(from_account_number, -money)
        print(f"Банк перевёл {money}$ с вашего счёта {from_account_number} на внешний счёт {to_external_number}")

    def load_accounts(self):
        bank_accounts = [BankAccount(*acc) for acc in
             self.__db.execute('SELECT card_holder, money, card_number, account_number FROM bank_accounts').fetchall()]
        self.__bank_accounts = {account.account_number: account for account in bank_accounts or []}


class Menu:
    EXIT: int = 0
    OPEN_REPORT = 1
    SHOW_ACCOUNTS = 2
    ADD_MONEY = 3
    TRANSFER = 4
    PAY = 5


class Controller:
    bank: Bank

    def __init__(self):
        self.bank = Bank()

    def run(self):
        print("Здравствуйте, наш банк открылся!")
        while True:
            try:
                print("Выберите действие:")
                print(f"{Menu.EXIT}. Завершить программу")
                print(f"{Menu.OPEN_REPORT}. Открыть новый счёт")
                print(f"{Menu.SHOW_ACCOUNTS}. Просмотреть открытые счета")
                print(f"{Menu.ADD_MONEY}. Положить деньги на счёт")
                print(f"{Menu.TRANSFER}. Перевести деньги между счетами")
                print(f"{Menu.PAY}. Совершить платёж")
                number_to_select = int(input())
                match number_to_select:
                    case Menu.EXIT:
                        print("До свидания!")
                        break
                    case Menu.OPEN_REPORT:
                        name_card_holder = input("Введите имя и фамилию:")
                        account = self.bank.open_account(name_card_holder)
                        print(f"Счёт {account.account_number} создан для {name_card_holder}")
                    case Menu.SHOW_ACCOUNTS:
                        for account in self.bank.get_all_bank_accounts():
                            print(f"Счет: {account.account_number}")
                            print(f"Номер карты: {account.card_number}")
                            print(f"Держатель карты: {account.card_holder}")
                            print(f"Остаток на счете: {account.money}")
                            print("-" * 30)
                    case Menu.ADD_MONEY:
                        account_number = input("Введите номер счета: ")
                        money = int(input("Введите сумму: "))
                        new_value = self.bank.add_money(account_number, money)
                        print(f"Поступила сумма {money}, на данный момент на счету {new_value}")
                    case Menu.TRANSFER:
                        from_account = input("Введите номер отправителя: ")
                        to_account = input("Введите номер получателя: ")
                        money = int(input("Введите сумму: "))
                        self.bank.transfer_money(from_account, to_account, money)
                    case Menu.PAY:
                        from_account = input("Введите номер отправителя: ")
                        to_external_number = input("Введите номер внешнего счета: ")
                        money = int(input("Введите сумму: "))
                        self.bank.external_transfer(from_account, to_external_number, money)
            except Exception as e:
                print(e)


if __name__ == '__main__':
    controller = Controller()
    controller.run()
