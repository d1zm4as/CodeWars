def reverse_words(text):
    #lista = [x for x in text.split(" ")]
    return " ".join([x for x in text.split(" ")[::-1] ])