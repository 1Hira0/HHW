#Write a program to create a text file and print the lines starting with ‘T’ or ‘P’. (Both 
#uppercase and lowercase). 

with open("f.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        if line.lower()[0] in ['t', 'p']:
            print(line)