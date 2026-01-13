#WAP to pass an integer list as stack to a function and push only those elements in the 
#stack which are divisible by 5.
def push_divisible_by_five(stack):
    li = []
    for item in stack:
        if item % 5 == 0:
            li.append(item)
    stack = li