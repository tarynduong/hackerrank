"""
The first line contains an integer, n, denoting the number of entries in the phone book.
Each of the n subsequent lines describes an entry in the form of 2 space-separated values on a single line.
The first value is a friend's name and the second value is an 8-digit phone number. 
After the lines of phone book entries, there is an unknown number of lines of queries.
Each line contains a name to look up, and you must continue reading lines until there is no more input.
Note: Names consist of lowercase English alphabetic letters and are first names only.

We add the following n=3 (Key, Value) pairs to our map so it looks like this:
phoneBook = {(same, 1934769295), (harry, 42886197490), (kevin, 07365728744)}
Then we process each query and print key=value if the queried key is found in the map; otherwise, print Not found.
Query 0: sam
Sam is one of the keys in our dictionary, so we print sam=1934769295.
Query 1: edward
Edward is not one of the keys in our dictionary, so we print Not found.
"""
import sys

n = int(input()) # size of the dictionary
phoneBook = {}

for i in range(n):
    entry = input().split() # enter element into dictionary
    phoneBook[entry[0]] = entry[1]

lines = sys.stdin.readlines() # because there are an unknown number of lines of queries
for i in lines:
    name = i.strip()
    if name in phoneBook:
        print(name + '=' + str(phoneBook[name]))
    else:
        print('Not found')
