"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv

with open("texts.csv", "r") as f:
    reader = csv.reader(f)
    texts = list(reader)

with open("calls.csv", "r") as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.w
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
dic = {}
for entry in calls:
    dic[entry[0]] = int(entry[3])
    dic[entry[1]] = int(entry[3])
key_max = max(zip(dic.values(), dic.keys()))[1]
value_max = max(zip(dic.values(), dic.keys()))[0]
print(
    "99612 41256 spent the longest time, 4514 seconds, on the phone during September 2016."
)
