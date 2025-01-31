print("Write a menu driven program in Python to print the Fibonacci series up to specified terms.")
n = int(input('Enter number of terms: '))
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