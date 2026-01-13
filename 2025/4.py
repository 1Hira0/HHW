#WAP to read a text file “myfile.txt” line by line and display each word separated by a #. 
with open("myfile.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        line = line.replace(" ", "#")
        print(line)