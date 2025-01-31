print("Write a  program in Python to search a specified element in a given list.")
l = []

n = input('How many elements in the list: ')
for i in range(int(n)):
    l.append(input("Enter #"+str(i)+" item: "))
it = input("Enter the item to search: ")
try:
    it = eval(it)
except: pass
if it in l:
    print(it, 'is present at', l.index(it))
else:
    print(it, 'is not present')