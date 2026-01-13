# Write a Python program to implement a stack using a list data-structure.  
def push(stack, item):
    stack.append(item)

def pop(stack):
    if not len(stack) == 0 :
        return stack.pop()
    else:
        return "Stack is empty"

