#Create a binary file with name and roll number. Search for a given roll number and 
#display the name, if not found display appropriate message.  

import pickle
roll = int(input("Enter roll number to search: "))
found = False
with open("dummy data/studs.bin", "rb") as file:
    data = pickle.load(file)
    print(data.get(roll, "Roll number not found"))
