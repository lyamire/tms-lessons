from student import Student

def calc_sum_scholarship(peoples: list[Student]) -> int:
    return sum([x.get_scholarship() for x in peoples])


def get_excellent_student_count(peoples: list[Student]) -> int:
    return len([x for x in peoples if x.is_excellent()])


students = [
    Student("Tom Donelly", 5.3),
    Student("Mabon Berg", 9.8),
    Student("Aeron Banks", 9),
    Student("Ursula Duhame", 7.5),
    Student("Aedon Ackermann", 6.4),
    Student("Manawyddan Methestel", 4.5),
    Student("Winfried Ryan", 8.3)
]

print(calc_sum_scholarship(students))
print(get_excellent_student_count(students))
