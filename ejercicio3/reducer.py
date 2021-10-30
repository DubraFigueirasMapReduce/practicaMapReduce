#!/usr/bin/env python

import sys

first_execution = True

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    winesubtypeAttribute, value = line.split('\t', 1)
    
    # convert value (currently a string) to int
    try:
        value = int(value)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue
    
    if first_execution:
        previous_attribute = winesubtypeAttribute
        mean = value
        attributeCounter = 1
        first_execution = False

    if winesubtypeAttribute == previous_attribute:
    	mean += value
    	attributeCounter += 1
    else:
    	mean = mean / attributeCounter
    	print '%s\t%s' % (winesubtypeAttribute, mean)
        previous_attribute = winesubtypeAttribute
        mean = value
        attributeCounter = 1
    	
    	

