#!/usr/bin/env python

import sys
import re

column_name_header = 1
for line in sys.stdin:
        if column_name_header:
                column_name_header = 0      # changing the header bool to 0
                continue                    # We will skip this row since it only consists of column names
        line = line.strip()                 # Stripping off the whitespaces from each line
        line = re.sub(r'".*"', ' ', line)   # We will also replace the pattern with whitespaces in each line
        words = line.split(",")             # Since these are CSVs lets split the line string into separate words
        req_words = words[24:]              # We Only select the columns >= 24 (the ones that have vehicle types)
        if len(req_words) != 5:             # there are a few rows with new line character in the "OFF STREET NAME"
                continue                    # I am ignoring that row to save complexity
        for vehicle_type in req_words:      # For all vehicle type(words) found, add 1 to count
                if vehicle_type:            # append count only if the vechile type is not empty
                        print '%s\t%s' % (vehicle_type, 1)  # inserting the ouput to stdout for reducer to act
