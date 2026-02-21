
def sort_by_name(arr):
    """Sort the given array of integers by their English names."""
    # Define a mapping of numbers to their English names
    num_to_name = {
        0: "zero", 1: "one", 2: "two", 3: "three", 4: "four",
        5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine",
        10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen",
        14: "fourteen", 15: "fifteen", 16: "sixteen",
        17: "seventeen", 18: "eighteen", 19: "nineteen",
        20: "twenty", 30: "thirty", 40: "forty",
        50: "fifty", 60: "sixty", 70: "seventy",
        80: "eighty", 90: "ninety"
    }

    def number_to_words(n):
        if n < 20:
            return num_to_name[n]
        elif n < 100:
            tens, remainder = divmod(n, 10)
            return num_to_name[tens * 10] + ("-" + num_to_name[remainder] if remainder else "")
        elif n < 1000:
            hundreds, remainder = divmod(n, 100)
            return num_to_name[hundreds] + " hundred" + (" and " + number_to_words(remainder) if remainder else "")
        else:
            return ""

    # Sort the array based on the English names
    return sorted(arr, key=number_to_words)

