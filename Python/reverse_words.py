def reverse_words(text):
    #lista = [x for x in text.split(" ")]
    return " ".join([x[::-1] for x in text.split(" ") ])
