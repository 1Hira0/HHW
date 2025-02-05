print("Write  a  menu  driven  program  in  Python  to  find  the  sum,  minimum  and maximum of given numbers. ")

l = []
it = 1
while True:
    c = input("""Menu->
Please choose from the following options of your choice:-
    choose [s] for sum
    choose [n] for minimum
    choose [x] for maximun
    anything else to exit
Note: Combinations are allowed for multiple options - snx gives all\n""")
    
    print('Enter the numbers 1 by 1. Enter an alphabet/symbol when you are done.')
    while True:
        inp = input("Enter #"+str(it)+" no.: ")
        if not inp.replace('.', '').isnumeric():
            break
        l.append(float(inp))
        it+=1
    s = 0
    n = x = l[0]
    for i in l:
        if 's' in c:
            s += i
        if 'n' in c:
            if i < n:
                n = i
        if 'x' in c:
            if i > x:
                x = i
    
    if 's' in c:
        print("Sum =", s)
    if 'n' in c:
        print('Minumun =', n)
    if 'x' in c:
        print("Maximum =", x)
    if not 'snx'.strip(c) :
        break