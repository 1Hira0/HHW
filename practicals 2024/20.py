print("Write a menu driven program in Python to print the Fibonacci series up to specified terms.")
n = ''
while True:
    c = input("""Menu->
Please choose from the following options of your choice:-
    choose [1] for Setting number of terms
    choose [2] for Displaying Fibonacci series
    anything else to exit
""")
    if c == '1':
        n = int(input('Enter number of terms: '))
    elif c == '2':
        if n =='':
            print('Number of terms not set')
            continue
        old = cur = 0
        nxt = 1
        if n < 0:print("Incorrect input")
        for i in range(n+1):
            print(cur, end=', ')
            if i == 1:
                print('1, ', end='')
            cur = old + nxt
            old = nxt
            nxt = cur
    else:break