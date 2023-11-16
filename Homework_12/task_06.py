def generate_words(stroke: str):
    for word in stroke.split():
        yield word


if __name__ == '__main__':
    text = 'мама мыла раму'
    for w in generate_words(text):
        print(w)

    assert [i for i in generate_words("Abra abracadabra Abracadabra")] == ["Abra", "abracadabra", "Abracadabra"]
