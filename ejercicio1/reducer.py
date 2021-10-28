#!/usr/bin/env python
import sys

NULL = "-9999.0"
minCheck = 0

for line in sys.stdin:
    # remove leading and trailing whitespace
    clean_line = line.strip()
    # parse the input we got from mapper.py
    temp, city = clean_line.split()
    # Check if the value is valid and it's the first time it enters
    if temp != NULL and minCheck == 0:
        print clean_line
        minCheck = 1
    # The last time the loop asigns this variable is the last line, so it's the
    # max temperature
    max_line = clean_line
print max_line
