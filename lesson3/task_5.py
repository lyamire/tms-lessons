list_of_elements = [1, 2, 3]

list_of_elements.append("four")
print(list_of_elements)

list_of_elements[1] = "two"
print(list_of_elements)

mnojestvo = {5, 6}
list_of_elements.append(mnojestvo)
print(list_of_elements)

mnojestvo.add(7)
print(list_of_elements)

list_of_elements.insert(2, (2.5,  2.6))
print(list_of_elements)
