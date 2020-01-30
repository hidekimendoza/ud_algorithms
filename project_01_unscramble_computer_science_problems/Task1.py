"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""


# unique_number = set()
# for call in calls:
#     unique_number.add(call[0])
# print len(unique_number)

print('There are {} different telephone numbers in the records.'.format(len(
    set([call [0] for call in calls]))))
