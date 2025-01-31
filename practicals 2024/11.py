print("Write  a  Program  in  Python  to  read  Three numbers  from  user  and  print  the largest among them.")
a,b,c = input('Enter 1st no.: '), input('Enter 2nd no.: '), input('Enter 3rd no.: ')
print(a if a>b and a>c else b if b>a and b>c else c)