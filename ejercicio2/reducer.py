#!/usr/bin/env python
import sys


for line in sys.stdin:
    # remove leading and trailing whitespace
    clean_line = line.strip()
    # parse the input we got from mapper.py
    temp, city = clean_line.split()
