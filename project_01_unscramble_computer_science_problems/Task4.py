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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

callers = set()
callees = set()
text_sender = set()
text_receiver = set()
for call in calls: # n
    callers.add(call[0]) # n
    callees.add(call[1]) # n
for text in texts: # m
    text_sender.add(text[0]) # m
    text_receiver.add(text[1]) # m

possible_telemarketers = set()
for caller in callers: # n
    if caller not in callees and caller not in text_receiver and caller not in text_sender: # n
        possible_telemarketers.add(caller) # n

print("These numbers could be telemarketers: ")
for phone_num in sorted(possible_telemarketers): # n + nlogn
    print(phone_num) # n

