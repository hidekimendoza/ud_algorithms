"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
call_time_spent = dict()
for call in calls:
    call_time_spent[call[0]] = call_time_spent.get(call[0],0) + int(call[-1])
    call_time_spent[call[1]] = call_time_spent.get(call[1],0) + int(call[-1])
max_time_number = max(call_time_spent, key= lambda k: call_time_spent[k])

print('{} spent the longest time, {} seconds, on the phone during September 2016.'.format(
    max_time_number, call_time_spent[max_time_number]))
