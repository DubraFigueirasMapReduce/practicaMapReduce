#!/usr/bin/env python

import sys
current_user = None
current_count = 0
user = None
# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # parse the input we got from mapper.py
    user, count = line.split(’\t’, 1)
    # convert count (currently a string) to int
    try:
        count = int(count)
    except ValueError:
    # count was not a number, so silently. Ignore/discard this line continue
    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
    if current_user == user:
        current_count += count
    else:
        if current_user:
            # write result to STDOUT
            print ’%s\t%s’ % (current_user, current_count)
        current_count = count
        current_user = user
    # do not forget to output the last word if needed!
if current_user == user:
    print ’%s\t%s’ % (current_user, current_count)
