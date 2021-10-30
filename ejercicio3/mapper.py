#!/usr/bin/env python

import os
import sys

first_execution = True

# Get winetype
file_name=os.environ['mapreduce_map_input_file']
s1=file_name.split('/')
file_name=s1[-1]
file_name=file_name[12:len(file_name)-4] 

for line in sys.stdin:
  # remove leading and trailing whitespace
  line = line.strip()
  # split the line into values
  winesubtype = line.split(";")
  
  if first_execution:
        attributes = winesubtype
        first_execution = False
        
  if (!first_execution)
    nAttr = 0;
    for attr in winetype:
      print '%s\t%s' % (file_name + "-" + attributes[nAttr], attr) 
      nAttr += 1
