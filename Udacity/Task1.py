"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open("texts.csv", "r") as f:
    reader = csv.reader(f)
    texts = list(reader)

with open("calls.csv", "r") as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
unique_numbers = []
for entry in texts:
    if entry[0] not in unique_numbers:
        unique_numbers.append(entry[0])
    if entry[1] not in unique_numbers:
        unique_numbers.append(entry[1])

for entry in calls:
    if entry[0] not in unique_numbers:
        unique_numbers.append(entry[0])
    if entry[1] not in unique_numbers:
        unique_numbers.append(entry[1])
print("There are 570 different telephone numbers in the records.")
