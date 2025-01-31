print("Count and display the number of vowels, consonants, uppercase, lowercase characters in string ")
inp = input("Enter string: ")
d = {'vowels':0, 'consonants':0, 'uppercase':0, 'lowercase':0}
for i in inp:
    if i.lower() in 'aeiou':
        d['vowels'] += 1
    if i.lower() not in 'aeiou':
        d['consonants'] += 1
    if i.isupper():
        d['uppercase'] += 1
    if i.islower():
        d['lowercase'] += 1

for i in d:
    print('Count of ' + i + ' is', d[i])