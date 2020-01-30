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
longest_call = { 'caller' : calls[0][0], 'time' : int(calls[0][-1]) }
for call in calls[1:]:
    if int(call[-1]) > longest_call['time']:
        longest_call['caller'] = call[0]
        longest_call['time'] = int(call[-1])
print('{} spent the longest time, {} seconds, on the phone during September 2016.'.format(
    longest_call['caller'], longest_call['time']))

