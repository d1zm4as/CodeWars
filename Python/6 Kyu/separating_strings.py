# Create a function that takes a string and separates it into a sequence of letters.

# The array will be formatted as so:

# [['J','L','L','M']
# ,['u','i','i','a']
# ,['s','v','f','n']
# ,['t','e','e','']]

# The function should separate each word into individual letters, with the first word in the sentence having its letters in the 0th index of each 2nd dimension array, and so on.

# Shorter words will have an empty string in the place once the word has already been mapped out. (See the last element in the last part of the array.)

# Examples:

s = "Just Live Life Man"
# r = 
def sep_str(s):
    words = s.split() # separa a string em palavras
    max_len = max(len(word) for word in words) # pega o comprimento da palavra mais longa
    result = [['' for _ in range(len(words))] for _ in range(max_len)] # cria uma matriz de strings vazias com o número de linhas igual ao comprimento da palavra mais longa e o número de colunas igual ao número de palavras

    for i, word in enumerate(words): # esse loop percorre cada palavra e seu índice e preenche a matriz result com os caracteres correspondentes
        for j, char in enumerate(word):
            result[j][i] = char

    return result

print(sep_str(s))