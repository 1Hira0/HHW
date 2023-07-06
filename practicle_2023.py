import re
from calendar import month_name
from matplotlib import pyplot as plot
from practicles_2022_EXTRA_FANCY import print_slow, myInput

_1 = """
Write a program to input two numbers and swap them."""
def prac1():
    first = eval(myInput("Enter the first number: "))
    second = eval(myInput("Enter the second number: "))
    print_slow(f'{first=}, {second=}')
    second, first = first, second
    print_slow(f'{first=}, {second=}')

_2 = """
Write a program to input three numbers and swap them as this: 
 1st number becomes 2nd number, 2nd number becomes 3rd number and 3rd number becomes 1st number"""
def prac2():
    first = myInput("Enter the first number: ")
    second = myInput("Enter the second number: ")
    third = myInput("Enter the third number: ")
    print_slow(f'{first=}, {second=}, {third=}')
    first, second, third = second, third, first
    print_slow(f'{first=}, {second=}, {third=}')

_3 = """
Write a program that reads two numbers and an arithmetic operator and displays the computed result."""
def prac3(): 
    operators = '+,-,*,/'
    n1 = myInput("Enter first number: ")
    op = myInput(f"Enter operator({operators}): ")
    if not op in operators: print_slow("Invalid operator");return
    n2 = myInput("Enter second number: ")
    try:
        print_slow(f"{n1} {op} {n2}={eval(f'{n1} {op} {n2}')}")
    except SyntaxError:
        print_slow("Input was invalid")
    
_4 = """
Write a program to accept the year and check if it is a leap year or not."""
def prac4():
    year = int(myInput(f"Enter year: "))
    print_slow(f"{year} is{' not' if year%4 else ''} a leap year")

_5 = """
Write a program to find largest among three integers. Make use of if-else statement"""
def prac5():
    a,b,c = map(float, map(myInput, map(lambda n: 'Enter number #'+str(n+1)+': ', range(3))))
    print_slow(f'{a if a>b and a>c else b if b>a and b>c else c}')

_6 = """
Write a program to calculate and print the sum of even and odd integers of the first n natural numbers."""
def prac6():
    n = int(myInput("Enter 'n': "))
    print_slow(f"Sum of even integers of the first n natural numbers: {n**2 + n}\nSum of odd integers of the first n natural numbers: {n**2}")

_7 = """
Write a program to input a number and print the sum of digits in the given number."""
def prac7():
    num = myInput("Enter the number: ")
    print_slow(f"{sum([int(i) for i in num if i!='.'])}")

_8 = """
Write a program to accept a character from the user and display whether it is vowel or consonant.
"""
def prac8():
    char = myInput('Enter a character: ')
    print_slow(f"'{char}' is a {'vowel' if char in 'aeiou' else 'consonant'}")

_9 = """
Write a program to accept a month number from the user and display whether Month name in character"""
def prac9():
    monNum = eval(myInput("Enter month number: "))
    if 0<monNum<12 and str(monNum).isdigit():
        print_slow(month_name[monNum])
    else: print_slow("There are only 12 months- try 1 to 12")

_10 = """
Write a program to input a number and display the table of that number."""
def prac10():
    num = int(myInput("Enter a natural number for its table: "))
    [print_slow(f'{num} * {i:>2} = {num*i}') for i in range(1,11)]
    
_11 = """
Write a program to enter a number and check if its prime or not."""
def prac11():
    num = int(myInput("Enter a natural number: "))
    print(f"{num} is{' not ' if not not re.search(regex:=r'^1?$|^(11+?)\1+$', '1'*num) else ' '}a prime.") #supported in py 3.12
    
_12 = """
Write a Program to generate the following patterns using nested loops."""
def prac12():
    ...# what 'following' patterns?

_13 = """
Write a program to find sum of series : s=1+x+x²+x³+x⁴…+xⁿ"""
def prac13():
    n = int(myInput('Enter a natural number(n): '))
    x = float(myInput('Enter an integer(x): '))
    if n>=0 and x!=1:
        print_slow(f"{x**n - 1 / (x - 1)}")
    else: print_slow("n can't be negative and x can't be 1")

_14 = """
Write a program in python to compute the Greatest Common Divisor and Least Common Multiple of two integers."""
def prac14():
    x,y = int(myInput('Enter first integer: ')), int(myInput('Enter second integer: '))
    for i in range(1, min([x,y])+1):
        if((x % i == 0) and (y % i == 0)):
            hcf = i
    lcm = (x*y)//hcf
    print_slow(f"{hcf=}, {lcm=}")

_15 = """
Write a program in python to visualization plots bar and pie chart using matplotlib library."""
def prac15():
    for_ = int(myInput("Enter the number of items in the data to be graphed: "))
    bottom,height = [],[]
    for i in range(1,for_+1):
        bottom.append(myInput(f"Name of the {i}{'st' if str(i).endswith('1') else 'nd' if str(i).endswith('2') else 'rd' if str(i).endswith('3') else 'th'} item: "))
        height.append(eval(myInput(f"Value of '{bottom[i-1]}': ")))
    plot.bar(bottom, height)
    plot.ylim(ymax=int(myInput('Height limit: ')))
    plot.xlabel(myInput("Bottom layer label: "))
    plot.ylabel(myInput("Left layer label: "))
    plot.title(myInput("Title: "))
    plot.show()
for i in range(1,16):
    print_slow((f'{i}. {eval(f"_{i}")[1:]}'))
    exec(f"prac{i}()")
