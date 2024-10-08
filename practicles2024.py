print(r'''
  ____   ___ ____  _  _     ____                 _   _           _     
 |___ \ / _ \___ \| || |   |  _ \ _ __ __ _  ___| |_(_) ___ __ _| |___ 
   __) | | | |__) | || |_  | |_) | '__/ _` |/ __| __| |/ __/ _` | / __|
  / __/| |_| / __/|__   _| |  __/| | | (_| | (__| |_| | (_| (_| | \__ \
 |_____|\___/_____|  |_|   |_|   |_|  \__,_|\___|\__|_|\___\__,_|_|___/
                                                                       ''')

'''
Sabko bas #program starts....

se

#program ends here... tak likhna hai'''

_1 = '''To find average and grade for given marks of five subject as follows
    Marks Grade
=> 90. A
=> 75 and <90 B
=> 50 and <75 C
=> 33 and <50 D
< 33 E'''

def prac1():
    #program starts here(don't write anything from above this)
    avg = 0
    for i in range(5):
        avg += float(input('Enter #', i+1, ' marks(out of 100): '))
    avg /= 5
    if avg >= 90:
        grade = 'A'
    elif avg >=75:
        grade = 'B'
    elif avg >= 33:
        grade = 'D'
    else:
        grade = 'E'
    print('For an average of', avg, 'you got', grade)
    #program ends here
    

'''ii) To find and print the sale price of an item when user input the cost and percentage of
discount (%) as follows
Amount Discount
=>100,000. 20%
> 50,000 and < 100000. 15%
> 25000 and < 5000. 10%
< 5000. 5%'''

def prac2():
    cp = int(input('Enter cost price'))
    sp = cp*0.95
    if cp>100000:
        sp = cp*.8
    elif cp>50000:
        sp = cp*.85
    elif cp>25000:
        sp = cp*.9
    print("Sale price =", sp)


'''iii) To calculate perimeter / circumference and area of shapes such as triangle, rectangle,
square and circle when number sides inputted by user 3, 2 and 1 resp.'''

def prac3():
    sides = int(input('Enter no. of sides: '))
    if sides == 3:
        a = float(input('Enter first side of triangle: '))
        b = float(input('Enter second side of triangle: '))
        c = float(input('Enter third side of triangle: '))
        s = (a+b+c)/2
        ar, pmtr = (s(s-a)(s-b)(s-c))**0.5 , s*2
    if sides == 2:
        l = float(input('Enter first side of reactangle/square: '))
        b = float(input('Enter second side of reactangle/square: '))
        ar,pmtr = l*b,2*(l+b)
    if sides == 1:
        r = float(input("Enter radius of circle: "))
        ar, pmtr = 3.14*r**2, 2*3.14*r
    print("Area =", ar, 'Perimeter/circumference =', pmtr)


'''iv) To calculate Simple as well as Compound interest for given Principal amount, rate of
Interest and time period.'''

def prac4():
    p = float(input("Enter pricipal amount: "))
    r = float(input("Enter rate(out of 100): "))
    t = float(input("Enter time period: "))
    s = p*r*t/100
    c = p*(1 + r/100)**t
    print('Simple Interest =', s, 'Compund Interest =', c)


'''v) To calculate profit or loss percentage for a given Cost and Sell Price inputted by user.'''

def prac5():
    cp = float(input('Enter cost price: '   ))
    sp = float(input('Enter selling price: '))
    if sp>cp:
        print('Profit of', 100*(sp -cp)/cp, '%')
    elif sp<cp:
        print('Loss of',   100*(cp -sp)/cp, '%')


'''vi) To calculate EMI for the given Amount, Period and Interest.'''

def prac6():
     pass


'''vii) To calculate tax - GST Tax as per the following category of commodities and
inputted price.
Category of commodities GST
Food & beverages 5%
Motor Vehicles. 10%
Others. 15%'''

def prac7():
    pass


'''viii) To find the largest and smallest numbers in a list.'''

def prac8():
    array = []
    while True:
        inp = input('Enter a number or anything else for stopping: ')
        if not inp.isnumeric():
            break
        array.append(int(inp))
    l = s = array[0]
    for i in array:
        if l < array[i]:
            l = array[i]
        if s > array[i]:
            s = array[0]
    print('Largest =', l, 'Smallest =', s)



'''ix) To find the second largest/smallest number in a list.'''

def prac9():
    array = []
    while True:
        inp = input('Enter a number or anything else for stopping: ')
        if not inp.isnumeric():
            break
        array.append(int(inp))
    l1 = l2 = s1 = s2 = array[0]
    for i in array:
        if l1 < array[i]:
            l2 = l1
            l1 = array[i]
        if s1 > array[i]:
            s2 = s1
            s1 = array[i]
    print('2nd largest =', l2, '2nd smallest =', s2)


'''x) To find the sum of squares of the natural numbers upto nth term'''
def prac10():
    n = int(input('Enter value of n: '))
    s = 0
    for i in range(1, n+1):
        s += i**2