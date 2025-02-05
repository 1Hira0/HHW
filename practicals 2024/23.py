print("Write a menu driven program in Python to check whether a character is an alphabet or not and also check its case.")
while True:
    c = input("""Menu->
    Please choose the number from the following options of your choice:-
        choose [a] to check if alphabet 
        choose [c] to check case
        anything else to exit
    Note: Combinations are allowed for multiple options - ac gives all\n""")
    char = input("Enter character: ")
    if 'a' in c:
        if char.isalpha():
            print("Is alphabet")
        else:
            print("Is not alphabet")
    if 'c' in c:
        print("Is lower" if char.islower() else 'Is upper' if char.isupper() else '')
    if not c in 'ac' :
        break