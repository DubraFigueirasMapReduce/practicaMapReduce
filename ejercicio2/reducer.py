#!/usr/bin/env python


### Nota: el framework de hadoop garantiza que todos los
###  valores asociados con la misma clave (palabra) van al mismo reducer

from operator import itemgetter #No lo esta usando
import sys

current_user = None
current_url = None
current_count_user = 0
current_count_url = 0
user = None
url = None
max_user = None
max_url = None
max_count_user = 0
max_count_url = 0
first_user = True
first_url = True


def isUser(item):
    lineType = item[0:4]
    if lineType == "USR-":
        return True
    return False

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    item, count = line.split('\t', 1)
    
    # convert count (currently a string) to int
    try:
        count = int(count)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue
    
    if isUser(item) and first_user:
        max_user = item
        max_count_user = count
        first_user = False
    elif first_url:
        max_url = item
        max_count_url = count
        first_url = False

    if isUser(item):
      # this IF-switch only works because Hadoop sorts map output
      # by key (here: user) before it is passed to the reducer
      if current_user == item:
          current_count_user += count
          # It is checked if after the increment the user has the most accesess
          if current_count_user >= max_count_user:
              max_user = item
              max_count_user = current_count_user
      else:
          current_count_user = count
          current_user = item
    else:
      # this IF-switch only works because Hadoop sorts map output
      # by key (here: url) before it is passed to the reducer
      if current_url == item:
          current_count_url += count
          # It is checked if after the increment the user has the most accesess
          if current_count_url >= max_count_url:
              max_url = item
              max_count_url = current_count_url
      else:
          current_count_url = count
          current_url = item

print '%s\t%s' % (max_user, max_count_user)
print '%s\t%s' % (max_url, max_count_url)