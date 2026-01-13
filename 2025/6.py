#Remove all the lines that contain the character `a' in a file and write it to another file. 
o = []
with open("myfile.txt", "r+") as file:
    lines = file.readlines()
    for line in lines:
        if 'a' in line:
            o.append(line)


with open("myfile.txt", "w") as file:
    for line in lines:
        if line not in o:
            file.write(line)
with open("f.txt", "w") as file:
    file.writelines(o)