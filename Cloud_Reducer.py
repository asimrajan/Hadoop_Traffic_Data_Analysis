#!/usr/bin/env python

import sys
from operator import itemgetter

# Initializing variables
crnt_word = None
word = None
crnt_count = 0

listoflist=[]
for line in sys.stdin:     		   # for each line in mapper output
        line = line.strip() 		   # remove the whitespaces
        word, count = line.split('\t', 1)  # split the input on tab space and make only one split
        count = int(count)                 # Typecast the count variable as integer 
        if crnt_word == word:              # if its the same word increment count
                crnt_count += count
        else:
                if crnt_word:              # if new word came in and we have seen a word already print that seen word's statistic
			listoflist.append((crnt_word,crnt_count))  # append (current_word, current_count) to list
                crnt_count = count         # Now the new word becomes the current word
                crnt_word = word
if crnt_word == word:                      # Appending the last element to list
	listoflist.append((crnt_word,crnt_count))


listoflist = (sorted(listoflist,key=itemgetter(1),reverse=True))  # Sorting the list on values in descending order.
for element in listoflist:
	print(element)
