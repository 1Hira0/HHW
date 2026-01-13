#Create a binary file with roll number, name and marks. Input a roll number and update 
#the marks. 
import pickle
roll = int(input("Enter roll number to update marks: "))
new_marks = int(input("Enter new marks: "))
with open("dummy data/studs.bin", "rb+") as file:
    data:dict = pickle.load(file)
    stud = data.get(roll)
    if not stud:
        print("Roll number not found")
    else:
        old = stud['marks']
        data[roll]['marks'] = new_marks
        file.seek(0)
        pickle.dump(data, file)
        file.truncate()
        print(f"Marks updated for {data[roll]['name']}({roll}) from {old} to {new_marks}")