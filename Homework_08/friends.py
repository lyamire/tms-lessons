from person import Person


def get_oldest_person(persons: list[Person]) -> Person:
    return max(persons, key=lambda x: x.age)

def filter_male_person(persons: list[Person]) -> Person:
    return filter(lambda person: person.gender == "M", persons)


my_friend = [
    Person("Harry James Potter", 43, "M"),
    Person("Hermione Jean Granger", 44, "F"),
    Person("Ronald Bilius Weasley", 43, "M"),
    Person("Ginevra Molly Weasley", 42, "F"),
    Person("Neville Longbottom", 43, "M")
]

print("All my friends:")
for friend in my_friend:
    friend.print_person_info()

print("My the oldest friend:")
get_oldest_person(my_friend).print_person_info()

print("My male friends:")
male_persons = filter_male_person(my_friend)
for person in male_persons:
    person.print_person_info()
