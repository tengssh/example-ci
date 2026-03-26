def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def convert_fahrenheit_to_celsius(fahrenheit):
    if fahrenheit < -459.67:
        raise AssertionError("This temperature is lower than 0K!")
    return multiply(subtract(fahrenheit, 32), 5 / 9)
