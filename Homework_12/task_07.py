import re
def generate_words(stroke: str):
    for word in re.findall(r'[A-ZА-Яa-zа-я]+', stroke):
        yield word


if __name__ == '__main__':
    text = 'Мама. Мыла? раму!'
    for w in generate_words(text):
        print(w)

    assert [i for i in generate_words("Abra? !abracadabra! &Abracadabra%")] == ["Abra", "abracadabra", "Abracadabra"]
    assert [i for i in generate_words("123Alohomora123123Expelliarmus12313Lumos123Obliviate123")] == ["Alohomora",
                                                                                                      "Expelliarmus",
                                                                                                      "Lumos",
                                                                                                      "Obliviate"]