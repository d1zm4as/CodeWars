
def sort_by_language(lst):
    return sorted(lst, key=lambda x: (x['language'], x['first_name']))