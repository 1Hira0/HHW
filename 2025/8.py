#Read a text file to print the frequency of the word ‘He’ and ‘She’ found in the file. 
with open("f.txt", "r") as f:
    content = f.read().lower()
    he_count = content.split().count('he')
    she_count = content.split().count('she')
    print(f"Frequency of 'He': {he_count}")
    print(f"Frequency of 'She': {she_count}")