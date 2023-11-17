def alias_gen(f_name: str, l_name: str) -> str:
    try:
        return f"{FIRST_NAME[f_name[0].upper()]} {SURNAME[l_name[0].upper()]}"
    except KeyError:
        return "Your name must start with a letter from A - Z."
