def word_splitter(string):
    special = {':', '+', '*', '!', '|', '#', '&', '=', ';', '%', '>', '<', '?', ','}
    answer = ""
    for char in string:
        if char in special:
            answer += " "
        else:
            answer += char
    return answer.split(' ')