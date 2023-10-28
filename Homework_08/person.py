from datetime import date


current_year = date.today().year

class Person:
    full_name: str
    age: int
    gender: str

    def __init__(self, full_name, age, gender: str):
        self.full_name = full_name
        self.age = age
        self.gender = gender

    def print_person_info(self):
        print(f"Person: {self.full_name} ({self.gender}), {self.age} years old")

    def get_birth_year(self):
        return current_year - self.age



