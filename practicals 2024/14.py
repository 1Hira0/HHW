print("Write  a  python  program  to  print  table  of  a  number  given  by  the  user as  an input.")
num = int(input("Enter a natural number for its table: "))
for i in range(1,11):
    print(num, '*', i, '=', num*i)