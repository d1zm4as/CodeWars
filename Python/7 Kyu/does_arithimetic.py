def arithmetic(a, b, operator):
    op = {"add":"+","subtract":"-","multiply":"*","divide":"/"}
    """
    lista  = [str(a),str(b)]
    a = f"{op[operator]}".join(lista)
    return eval(a)
    """
    return eval(f"{op[operator].join([str(a),str(b)])}")
  # i liked this one :)
