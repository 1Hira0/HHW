#Write a function in python which accepts a number from user to return True, if the number is a prime number else False.Use this function to print all primne numbers from 1 to 100.

def is_prime(n):
    if n < 2:return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

n = int(input("Enter number: "))
print(f"Your number is {"prime" if is_prime(n) else "not prime"}")

for i in range(1, 101):
    if is_prime(i):
        print(i, end=' ')