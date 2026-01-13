#Read a CSV file (containing item no, name, rate, QOH) from hard disc and print all the 
#items whose rate is between Rs 500 and Rs 1000.  
import csv

with open('items.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        item_no, name, rate, qoh = row
        if 500 <= float(rate) <= 1000:
            print(row)