#!/usr/bin/env python


### Nota: el framework de hadoop garantiza que todos los
###  valores asociados con la misma clave (palabra) van al mismo reducer

from operator import itemgetter #No lo esta usando
import sys

current_url = None
current_count = 0
url = None
max_url = None
max_count = 0
first_execution = True

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    url, count = line.split('\t', 1)

    # convert count (currently a string) to int
    try:
        count = int(count)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue

    if first_execution:
        max_url = url
        max_count = count
        first_execution = False

    # this IF-switch only works because Hadoop sorts map output
    # by key (here: url) before it is passed to the reducer
    if current_url == url:
        current_count += count
        # It is checked if after the increment the user has the most accesess
        if current_count >= max_count:
            max_url = url
            max_count = current_count
    else:
        current_count = count
        current_url = url
print '%s\t%s' % (max_url, max_count)