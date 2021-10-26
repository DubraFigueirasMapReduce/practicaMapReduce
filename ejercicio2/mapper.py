#!/usr/bin/env python

import os
import sys


file_name=os.environ['mapreduce_map_input_file']
s1=file_name.split('/')
file_name=s1[-1]
file_name=file_name.split('.')
user = file_name[0] #conXX
  
for line in sys.stdin:
  # remove leading and trailing whitespace
  line = line.strip()
  # split the line into values
  entries = line.split()
  url = entries[3]
  urlfiletype = split(".")
  urlfiletype = urlfiletype[-1]
  if urlfiletype == "ps":	
    print '%s\t%s' % (user, 1) 
  
