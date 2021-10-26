#!/usr/bin/env python
import sys

NULL = "-9999.0"
minCheck = 0

for line in sys.stdin:
    # remove leading and trailing whitespace
    clean_line = line.strip()
    # parse the input we got from mapper.py
    temp, city = clean_line.split()
    if temp != NULL and minCheck == 0:
        print clean_line
        minCheck = 1
    max_line = clean_line
print max_line