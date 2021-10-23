#!/usr/bin/env python

import os
import sys

for line in sys.stdin:
  # remove leading and trailing whitespace
  line = line.strip()
  ## split the line into values
  values = line.split()
  file_name=os.environ['mapreduce_map_input_file']
  s1=file_name.split('/')
  file_name=s1[-1]
  file_name=filename[16:len(file_name)-11) #get city name
  print '%s\t%s' % (value[12], file_name) #min temp
  print '%s\t%s' % (value[13], file_name) #max temp
