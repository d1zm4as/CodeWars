    # Counting in Lojban, an artificial language developed over the last forty years, is easier than in most languages. The numbers from zero to nine are:

    # 1 pa 4 vo 7 ze
    # 2 re 5 mu 8 bi 0 no
    # 3 ci 6 xa 9 so

    # Larger numbers are created by gluing the digits together. For example, 123 is pareci.

    # Write a program that reads in a Lojban string (representing a number less than or equal to 1,000,000) and outputs it in numbers.
    # Example:

    # renonore  # Lojban string
    # 2002  # Number

    # Input/Output

    #     [input] string representing the number in Lojban pareci
    #     Constraints: Lojban number ≤ 1,000,000
    #     [output] integer representing the Lojban number 123

def lojban_number(s):
    return int(s.replace("no", "0").replace("pa", "1").replace("re", "2").replace("ci", "3").replace("vo", "4").replace("mu", "5").replace("xa", "6").replace("ze", "7").replace("bi", "8").replace("so", "9"))