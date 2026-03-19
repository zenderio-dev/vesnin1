def add(a, b):
    return a + b

def add_with_bug(a, b):
    return a * b

def calculate_tax_bagged(income):
    return income * 0.15

def calculate_tax(income):
    if income < 0:
        raise ValueError("Income cannot be negative")
    return int(income * 0.15 * 100) / 100

