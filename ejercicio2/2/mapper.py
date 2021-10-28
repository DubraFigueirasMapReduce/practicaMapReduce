#!/usr/bin/env python

import os
import sys

for line in sys.stdin:
  # remove leading and trailing whitespace
  line = line.strip()
  # split the line into values
  entries = line.split()
  # Get URL
  url = entries[3]
  print '%s\t%s' % (url, 1)
