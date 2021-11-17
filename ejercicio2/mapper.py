#!/usr/bin/env python

import os
import sys

file_name=os.environ['mapreduce_map_input_file']
s1=file_name.split('/')
file_name=s1[-1]
file_name=file_name.split('.')
user = file_name[0]

for line in sys.stdin:
  # remove leading and trailing whitespace
  line = line.strip()
  # split the line into values
  entries = line.split()
  # Get URL
  url = entries[3]
  # Print for exercise 2.2
  print '%s\t%s' % ("URL-" + url, 1)
  # From this point the lines correspond to exercise 2.1
  urlfiletype = url.split(".")
  urlfiletype = urlfiletype[-1]
  # Compare if the filetype is ps
  if urlfiletype[:-1] == "ps":
    print '%s\t%s' % ("USR-" + user, 1) 
