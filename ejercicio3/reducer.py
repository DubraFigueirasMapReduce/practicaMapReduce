#!/usr/bin/env python

from operator import itemgetter #No lo esta usando
import sys


# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    user, count = line.split('\t', 1)

print '%s\t%s' % (max_user, max_count)
