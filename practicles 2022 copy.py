
def pract1():
    print("""\n\n#Practicle 1
#Write a progrm to input a "Welcome" message and display it\n""")
    name = input("Enter your name: ")
    display_length = len(name) + len("Enter your name: ")
    print(f"{f'Welcome {name}!':^20}")


def pract2(): 
    print("""\n\n#Practicle 2
#Write a program that accepts radius of a circle and prints its area\n""")
    radius = float(input("Enter the radius as meters: "))
    print(f"Area of circle {radius *2 * 3.14:,} m²")


def pract3():
    print("""\n\n#Practicle 3
#Write a progrm that inputs a student's marks in three subjects (out of 100) and prints the percentage marks\n""")
    subs={"sub1":{}, "sub2":{}, "sub3":{}}
    for i in range(1,4):
        subs[f'sub{i}']['name'] = input(f"Enter {i}st subject's name: ")
        subs[f'sub{i}']['score'] = input(f"Enter {subs[f'sub{i}']['name']}'s score (out of 100): ")
    for sub in subs:print(f"{subs[sub]['name']+':':<10} {subs[sub]['score']}%")


def pract4(): 
    print("""\n\n#Practicle 4
#Write a program that reads the number n and print the value of n², n³ and n⁴. \n""")
    n = float(input("Enter the number 'n': "))
    print(f"{n=:,} \nn\u00B2={n**2:,} \nn\u00B3={n**3:,} \nn\u2074={n**4:,}")


def pract5(): 
    print("""\n\n#Practicle 5
#Write a program to calculate simple interest. \n""")
    principal=float(input('Enter the principal amount: '))
    rate=float(input('Enter the rate: '))
    time=float(input('Enter the time amount: '))
    print(f"Simple Interest= {principal*rate*time/100:,} units")


def pract6(): 
    print("""\n\n#Practicle 6
#Write a program to input length and breadth of rectangle and calculate its area.\n""") 
    length =float(input('Enter the length in meters: '))
    breadth=float(input('Enter the breadth in meters: '))
    print(f"Area of reactangle={length*breadth:,}m\u00B2")


def pract7(): 
    print("""\n\n#Practicle 7
#write a program to obtain temperature in Celsius and convert it into Fahrenheit.
#Formula : F = C*(9/5 + 32)\n""")
    cel=float(input('Enter temperature in degree celsius: '))
    print(f"{cel:,}℃ = {cel*9/5+32:,}℉")


def pract8(): 
    print("""\n\n#Practicle 8
#Write a program to read details like name, class, age of a student and then print the details in same line and then in separate lines.
#(Make sure to have two blank lines in these two different types of prints.)\n""")
    student = dict()
    student['name']  = input("Enter the student's name: ")
    student['class'] = input("Enter the student's class (#Section): ")
    student['age']   = input("Enter student's age(years): ")
    print("\n\n"+'\n'.join([f"student's {item+':':<6} {student[item]}" for item in student]))


def pract9():
    print("""\n\n#Practicle 9
#Write a program to enter a number and check if it is a prime number or a composite number.\n""")
    num = int(input('Enter an integer: '))
    if num > 1:
        for i in range(2, int(num**0.5) + 1):
            if not num%i:print(f'{num:,} is composite.')
            return
        print(f'{num:,} is prime')
    else:print(f"{num:,} is not prime nor composite")


def pract10():
    print("""\n\n#Practicle 10
#Write a Program to display the n terms of Fibonacci series.\n""")
    old, nxt = 0, 1
    n = int(input("Enter a whole number: "))
    if n < 0:print("Incorrect input")
    elif n == old or n == nxt:
        print(n)
        return
    else:
        for _ in range(1, n): 
            new = old + nxt
            old = nxt
            nxt = new
    print(nxt)


def pract11():
    print("""\n\n#Practicle 11
#Write a Program to input a number is perfect number, an Armstrong number or a palindrome.\n""")
    num = int(input("Enter a whole number: "))
    strNum = str(num)
    #perfect number check
    dSum = int()
    for _ in range(1,num):
        if not num%_:dSum+=_
    if num == dSum:print(f'{num:,} is a perfect number')

    #Armstrong numbers
    pSum = int()
    power=len(strNum)
    for _ in range(power):
        pSum+=int(strNum[_])**power
    if num == pSum:print(f"{num:,} is an Armstrong number")

    #Palindrome
    if strNum[::-1] == str(num):print(f"{num:,} a Palindrome number")


def pract12():
    print("""\n\n#Practicle 12
#Write a program to input two numbers and display the largest/smallest number\n""")
    nums = [int(input("Enter the first number: ")), int(input("Enter the second number: "))]
    if nums[0] == nums[1]:
        print(f"{nums[0]} is equal to {nums[1]}")
        return
    print(f"Largest:{max(nums):,} \nSmallest:{min(nums):,}")


def pract13():
    print("""\n\n#Practicle 13
#Write a program to input three integers and display the largest/smaller number.\n""")
    nums = [int(input("Enter first number: ")), 
            int(input("Enter the second number: ")), 
            int(input("Enter the first number: "))]
    if max(nums) == min(nums): 
        print(f"{nums[0]:,} , {nums[1]:,} and {nums[2]:,} are equal")
    print(f"Largest:{max(nums):,} \nSmallest:{min(nums):,}")


Animals=["cat", "dog", "mouse", "hamster"]
def pract14(array:list=Animals):
    print("""\n\n#Practicle 14
#Write a program to take a list of items and print each item in the list using for loop.\n""")
    for animal in array:
        print(animal)


import random
def pract15():
    print("""\n\n#Practicle 15
#Write a program to create a list namely test having at least 3 integers, 2 floating point numbers and two strings.
#test=[11, 33,99, 20.25, 95.2,‘Apple’, ‘Pencil’]\n""")
    with open("words.txt","r") as f:
        rawList = f.readlines()
    twoStrings = [random.choice(rawList).replace('\n',''),random.choice(rawList).replace('\n','')]
    threeInts = [random.randint(1,100),random.randint(1,100),random.randint(1,100)]
    twoFloats = [random.randint(1,100)/random.randint(1,100),random.randint(1,100)/random.randint(1,100)]
    test = twoStrings+threeInts+twoFloats
    random.shuffle(test)
    print(test)

for i in range(15,16):
    exec(f"pract{i}()")