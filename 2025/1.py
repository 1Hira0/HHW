#WAP to show functionality of a basic calculator using functions.
o = input("Enter operation (+, -, *, /): ")
def calc(a, o, b):
    if o == '+':
        return a + b
    elif o == '-':
        return a - b
    elif o == '*':
        return a * b
    elif o == '/':
        return a / b
    
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
x = calc(a, o, b)
print(x)