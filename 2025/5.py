#WAP to read a text file “myfile.txt” and display the number of vowels/ consonants/ 
#uppercase/ lowercase characters in the file. 
with open("myfile.txt", "r") as file:
    text = file.read()
    v = c = u = l = 0
    for char in text:
        if char.isalpha():
            if char.lower() in 'aeiou': v += 1
            else: c += 1
            if char.isupper(): u += 1
            else: l += 1
    print(f"Vowels: {v}, Consonants: {c}, Uppercase: {u}, Lowercase: {l}")