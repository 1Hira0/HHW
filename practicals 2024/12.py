print("Determine whether a number is a perfect number or not.")
n = int(input("Enter number: "))
s = 0
for i in range(1, n//2):
    if not n%i:
        s += i
if n == s:
    print("Number is perfect")