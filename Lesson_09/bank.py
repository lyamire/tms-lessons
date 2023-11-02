"""
Эмулятор банка
"""
import json
import os.path
from random import randint


class BankAccount:
    """Аккаунт пользователя"""
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
    """
    Банк
    """
    def __init__(self, bank_accounts: list[BankAccount] = None):
        self.__bank_accounts: dict[str, BankAccount] = {
            account.account_number: account for account in bank_accounts or []
        }

    def open_account(self, card_holder: str) -> BankAccount:
        """
        Открыть счет
        """
        account = BankAccount(card_holder)
        self.__bank_accounts[account.account_number] = account
        return account

    def __get_account(self, account_number: str) -> BankAccount:
        return self.__bank_accounts[account_number]

    def get_all_bank_accounts(self) -> list[BankAccount]:
        """
        Получить список аккаунтов
        """
        return list(self.__bank_accounts.values())

    def add_money(self, account_number: str, money: float) -> float:
        """
        Пополнение счета
        """
        account = self.__get_account(account_number)
        account.money += money
        return account.money

    def transfer_money(self, from_account_number: str, to_account_number: str, money: float):
        """
        Перевод денег между счетами
        """
        self.add_money(from_account_number, -money)
        self.add_money(to_account_number, money)
        print("Операция по переводу между счетами прошла успешно")

    def external_transfer(self, from_account_number: str, to_external_number: str, money: float):
        """
        Перевод денег на внешний счет
        """
        self.add_money(from_account_number, -money)
        print(f"Банк перевёл {money}$ с вашего счёта {from_account_number} на внешний счёт {to_external_number}")


class Menu:
    """
    Пункты меню
    """
    EXIT: int = 0
    OPEN_REPORT = 1
    SHOW_ACCOUNTS = 2
    ADD_MONEY = 3
    TRANSFER = 4
    PAY = 5


class Controller:
    """
    Управление банком
    """
    data_file_name: str
    bank: Bank

    def __init__(self, data_file_name: str):
        self.data_file_name = data_file_name
        bank_accounts: list[BankAccount] = self.load_accounts(data_file_name)
        self.bank = Bank(bank_accounts)

    def run(self):
        """
        Главный исполняемый цикл контроллера
        """
        print("Здравствуйте, наш банк открылся!")
        while True:
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
                    self.save_accounts(self.bank.get_all_bank_accounts(), self.data_file_name)
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

    @staticmethod
    def convert_bank_account_to_dict(bank_account: BankAccount) -> dict:
        """
        Конвертация аккаунта в словарь
        """
        return {
            "card_holder": bank_account.card_holder,
            "money": bank_account.money,
            "card_number": bank_account.card_number,
            "account_number": bank_account.account_number
        }

    def save_accounts(self, bank_accounts: list[BankAccount], file_name: str):
        """
        Сохранение аккаунтов
        """
        data = [self.convert_bank_account_to_dict(account) for account in bank_accounts]
        with open(file_name, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=2)

    @staticmethod
    def load_accounts(file_name: str) -> list[BankAccount]:
        """
        Загрузка аккаунтов
        """
        if not os.path.exists(file_name):
            return []
        with open(file_name, "r", encoding="utf-8") as file:
            return [BankAccount(**data) for data in json.load(file)]


if __name__ == '__main__':
    controller = Controller('data.json')
    controller.run()
