print("Write a program to print factorial of a number using both while and for loop.")
f = 1
n = int(input("Enter a number: "))
for i in range(n, 1, -1):
    f *= i
print('for loop:', f)

F = 1
i = n
while i>1:
    F *= i
    i -= 1
print('while loop:', F)