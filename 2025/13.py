#Create a CSV file by entering user-id and password, read and search the password for 
#given userid. 
import csv
def createUser(userid=None, password=None):
    password = ''.join([chr(ord(c)+3) for c in password])
    with open('dummy data/users.csv', 'a', newline='\n') as file:
        writer = csv.writer(file)
        writer.writerow([userid, password])

def searchPassword(userid):
    with open('dummy data/users.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == userid:
                return ''.join([chr(ord(c)-3) for c in row[1]])
    return "Not found"

user = input("Enter new user ID: ")
pas = input(f"Enter password for {user}: ")
createUser(user, pas)

sUser = input("Enter user ID to search password: ")
print(f"Password for {sUser}: {searchPassword(sUser)}")