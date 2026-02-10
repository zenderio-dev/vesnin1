def sum(a, b):
    return a + b

def devide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b