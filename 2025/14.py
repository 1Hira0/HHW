# Write a random number generator that generates random numbers between 1 and 6 
#(simulates a dice). Throw the two dices for 10 times and print their total.
import random
for _ in range(10):
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    total = die1 + die2
    print(f"Die 1: {die1}, Die 2: {die2}, Total: {total}")  