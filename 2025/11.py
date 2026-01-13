#Read a CSV file from hard disc and print all the details on the screen.
import csv
with open('items.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)