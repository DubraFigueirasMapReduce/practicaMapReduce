#!/usr/bin/env python

import os
import sys

# Get city name
file_name=os.environ['mapreduce_map_input_file']
s1=file_name.split('/')
file_name=s1[-1]
file_name=file_name[17:len(file_name)-11] 

for line in sys.stdin:
  # remove leading and trailing whitespace
  line = line.strip()
  # split the line into values
  values = line.split()
  #min temp
  print '%s\t%s' % (values[12], file_name)
  #max temp
  print '%s\t%s' % ( values[13], file_name)
