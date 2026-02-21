
def initialize_names(name):
    parts = name.split()
    if len(parts) <= 2:
        return name
    else:
        first = parts[0]
        last = parts[-1]
        middle_initials = [f"{part[0]}." for part in parts[1:-1]]
        return f"{first} {' '.join(middle_initials)} {last}"