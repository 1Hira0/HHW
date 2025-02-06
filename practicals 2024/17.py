print("Write a menu driven program in Python to print the grade of a student based on the marks. Have minimum 5 grade levels.")
 
#initialisation
mm = 0
m = {'marks':{}, 'total':0}
while True:
    c = input("""Menu->
Please choose from the following options of your choice:-
    choose [1] for Setting maximum marks
    choose [2] for Entering marks
    choose [3] for Calculating grades
    anything else to exit
""")

    if c == '1':
        mm = int(input('Enter maximum marks(the 80 from 70/80): '))

    #collect marks
    elif c == '2':
        while True:
            n = input("Enter name of subject: ")
            m['marks'][n] = float(input("Enter marks of subject(out of max marks): "))
            if input("Do you want to add more subjects(y/n): ") == 'n':
                break

    #calc percentage
    elif c == '3':
        if not mm or m['marks']:
            print(f"{'Maximum marks' if not mm else 'Subject Marks'} not set")
            continue
        for i in m['marks'].values():
            m['total'] += i
        m['total'] = m['total']*100/(mm*len(m['marks']))
        g = chr(75 - (int(-(m['total']//-10))))
        print('grade =', g)

    else:
        break