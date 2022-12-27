import time, math

def myInput(msg:str=''):
    print_slow(msg=msg[0:-1],end=' ')
    return input()
def print_slow(msg:str,*,sep=" ",end='\n'):
    msgs=[msg]
    if "\n" in msg:msgs = msg.split('\n')
    else:msgs = [msg]
    for i in range(len(msgs)):
        msgs[i];outext=''
        for idx in range(len(msgs[i])):outext=outext + msgs[i][idx];print(outext, end='\r');time.sleep(1/25)
        if "\n" in msg:print()
    if "\n" not in msg:print(msg, sep=sep,end=end)
#Practicle 1
#Write a progrm to input a "Welcome" message and display it
def pract1():name = myInput("Enter your name: "); print_slow(f"Welcome {name}!")

#Practicle 2
#Write a program that accepts radius of a circle and prints its area
def pract2(): 
    while True: 
        radius = myInput("Enter the radius as meters: ")
        try:radius = float(radius);print_slow(f"Area of circle {radius *2 * math.pi:,} m²");break
        except ValueError: print_slow(f"You didn't enter a valid number({radius=}). \nPlease try again")

#Practicle 3
#Write a progrm that inputs a student's marks in three subjects (out of 100) and prints the percentage marks
def pract3():
    subs={"sub1":{}, "sub2":{}, "sub3":{}}
    for i in range(1,4):subs[f'sub{i}']['name'] = myInput(f"Enter {i}st subject's name: ");subs[f'sub{i}']['score'] = myInput(f"Enter {subs[f'sub{i}']['name']}'s score (out of 100): ")
    for sub in subs:print_slow(f"{subs[sub]['name']+':':<10} {subs[sub]['score']}%")


#Practicle 4
#Write a program that reads the number n and print the value of n², n³ and n⁴. 
def pract4():
    while True:
        n = myInput("Enter the number 'n': ")
        try:n=float(n);print_slow(f"{n=:,} \nn\u00B2={n**2:,} \nn\u00B3={n**3:,} \nn\u2074={n**4:,}");break
        except ValueError: print_slow(f"You didn't enter a valid number({n=}). \nPlease try again")

#Practicle 5
#Write a program to calculate simple interest. 
def pract5():
    while True:
        principal=myInput('Enter the principal amount: ')
        try:p=float(principal);break
        except ValueError:print_slow(f"The entered {principal=} amount is not a valid number. \nPlease try again")
    while True:
        rate=myInput('Enter the rate: ')
        try:r=float(rate);break
        except ValueError:print_slow(f"The entered {rate=} is not a valid number. \nPlease try again")
    while True:
        _time=myInput('Enter the time amount: ')
        try:t=float(_time);break
        except ValueError:print_slow(f"The entered time={_time} is not a valid number. \nPlease try again")
    print_slow(s_i:=(f"Simple Interest= {p*r*t/100:,} units"))

#Practicle 6
#Write a program to input length and breadth of rectangle and calculate its area. 
def pract6():
    while True:
        length=myInput('Enter the length in meters: ')
        try:l=float(length);break
        except ValueError:print_slow(f"The entered {length=} is not a valid number. \nPlease try again")
    while True:
        breadth=myInput('Enter the breadth in meters: ')
        try:b=float(breadth);break
        except ValueError:print_slow(f"The entered {breadth=} is not a valid number. \nPlease try again")
    print_slow(f"Area of reactangle={l*b:,}m\u00B2")

#Practicle 7
#write a program to obtain temperature in Celsius and convert it into Fahrenheit.
#Formula : F = C*(9/5 + 32)
def pract7():
    while True:
        celsius=myInput('Enter temperature in degree celsius: ')
        try:cel=float(celsius);print_slow(f"{cel:,}℃ = {cel*9/5+32:,}℉");break
        except ValueError:print_slow(f"The entered {celsius=} is not a valid number. \nPlease try again")

#Practicle 8
#Write a program to read details like name, class, age of a student and then print the details in same line and then in separate lines.
#(Make sure to have two blank lines in these two different types of prints.)

    