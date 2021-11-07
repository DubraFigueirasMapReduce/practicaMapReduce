#!/usr/bin/env python

import os
import sys

for line in sys.stdin:
  # remove leading and trailing whitespace
  line = line.strip()
  # split the line into values
  entries = line.split()
  # Get User
  user = entries[2]
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
