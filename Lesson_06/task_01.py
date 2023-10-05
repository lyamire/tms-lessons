def input_list(prompt="", sep=" ", element_type=int) -> list:
    return list(map(element_type, input(prompt).split(sep)))
