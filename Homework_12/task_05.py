import re
class WordIterable:
    def __init__(self, stroke: str):
        self.stroke = re.findall(r'[A-ZА-Яa-zа-я]+', stroke)
        self.index_word = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index_word >= len(self.stroke):
            raise StopIteration()
        self.index_word += 1
        return self.stroke[self.index_word-1]


if __name__ == '__main__':
    text = 'Мама. Мыла? раму!'
    for w in WordIterable(text):
        print(w)

    assert [i for i in WordIterable("Abra? !abracadabra! &Abracadabra%")] == ["Abra", "abracadabra", "Abracadabra"]
    assert [i for i in WordIterable("123Alohomora123123Expelliarmus12313Lumos123Obliviate123")] == ["Alohomora",
                                                                                                      "Expelliarmus",
                                                                                                      "Lumos",
                                                                                                      "Obliviate"]