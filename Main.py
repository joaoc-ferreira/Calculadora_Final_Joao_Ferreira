    elif operador == '-':
        result = num1 - num2
    elif operador == 'X':
        result = num1 * num2
    elif operador == '/':
        result = num1 / num2
        "-": lambda: num1 - num2,
        "X": lambda: num1 * num2,
        "/": lambda: num1 / num2
