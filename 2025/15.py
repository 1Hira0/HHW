#WAP in Python to demonstrate linear search. 
def linear(li, target):
    for i in range(len(li)):
        if li[i] == target:
            return i
    return -1

import random, time
lst = [f for f in range(1, 10000000)]
target = random.choice(lst)
start = time.time()
result = linear(lst, target)
if result != -1:
    print(f"Element found at index {result} with time taken: {time.time() - start} seconds")
