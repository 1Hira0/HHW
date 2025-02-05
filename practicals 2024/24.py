print("Write  a  menu  driven  program  in  Python  to  find  the  largest  and  smallest element in a list.")

l = []
it = 1
while True:
    c = input("""Menu->
    Please choose from the following options of your choice:-
        choose [set] for setting up the list
        choose [max] for minimum
        choose [min] for maximun
        anything else to exit
    Note: Combinations are allowed for 2 options - maxmin gives both\n""")

    print('Enter the numbers 1 by 1. Enter an alphabet/symbol when you are done.')
    if 'set' in c:
        while True:
            inp = input("Enter #"+str(it)+" no.: ")
            if not inp.replace('.', '').isnumeric():
                break
            l.append(float(inp))
            it+=1
        n = x = l[0]
        for i in l:
            if 'min' in c:
                if i < n:
                    n = i
            if 'max' in c:
                if i > x:
                    x = i

    if 'min' in c:
        print('Minumun =', n)
    if 'max' in c:
        print("Maximum =", x)
    if not c in 'setmaxmin' :
        break