print("Determine whether a number is an Armstrong number or not.")
n = m = int(input("Enter number: "))
nl = []
while m>0:
    nl.append(m%10)
    m = m//10
p = len(nl)
s = 0
for i in nl:
    s += i**p
if s == n:
    print("Armstrong number")