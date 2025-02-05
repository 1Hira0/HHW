print("Write  a  menu  driven  program  in  Python  to  check  whether  the  number  is Armstrong,  check  whether  the  number  is  prime  and  check  whether  the number is palindrome.")
while True:
    c = input("""Menu->
Please choose the number from the following options of your choice:-
    choose [a] to check Armstrong number case
    choose [p] to check Prime number case
    choose [r] to check Palindrome number case
    anything else to exit
Note: Combinations are allowed for multiple options - apr gives all\n""")
    n = m = int(input("Enter number: "))

    if 'a' in c:
        nl = []
        while m>0:
            nl.append(m%10)
            m = m//10
        p = len(nl)
        s = 0
        for i in nl:
            s += i**p
        if s == n:
            print('Is armstrong')
        else:
            print('Is not armstrong')
        m = n
    if 'p' in c:
        for i in range(2, n//2):
            if n%i==0:
                print('Is prime')
                break
        else:
            print('Is not prime')
    if 'r' in c:
        rev = 0
        while m>0:
            rev = rev*10 + m%10
            m = m//10
        if rev == n:
            print('Is palindrome')
        else:
            print('Is not palindrome')
        if not 'apr'.strip(c) :
            break