print(" Write  a  program  to  print  sum  of  even  and  odd  integers  of  first  n  natural numbers. ")
n = int(input('Enter n: '))
se = so = 0
for i in range(1, n+1):
    if i%2:
        so += i
    else:
        se += i
print('Sum of odd:', so, 'Sum of even: ', se)