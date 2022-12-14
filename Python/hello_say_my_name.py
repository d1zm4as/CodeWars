def hello(name = ""):
    name = name.lower()
    name = name.title()
    return "Hello, World!" if name == "" else f"Hello, {name}!"
