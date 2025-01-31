print("Write a menu driven program in Python to print the grade of a student based on the marks. Have minimum 5 grade levels.")

#initialisation
m = {'marks':{}, 'total':0}
mm = int(input('Enter maximum marks(the 80 from 70/80): '))

#collect marks
while True:
    n = input("Enter name of subject: ")
    m['marks'][n] = float(input("Enter marks of subject(out of max marks): "))
    if input("Do you want to add more subjects(y/n): ") == 'n':
        break

#calc percentage
for i in m['marks'].values():
    m['total'] += i
m['total'] = m['total']*100/(mm*len(m['marks']))

#grading
g = chr(75 - (int(-(m['total']//-10))))
print('grade =', g)