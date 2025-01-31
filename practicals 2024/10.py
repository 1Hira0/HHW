print('Write  a  Python  program  to  read  any  number  and  check  whether  the  no  is Positive or Negative or Zero')
n = float(input('Enter number: '))
s = ''
if n>0:
    s='Positive'
elif n<0:
    s='Negative'
else:
    s='Zero'
print(s)