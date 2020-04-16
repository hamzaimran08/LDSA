#!/usr/bin/env python3
"""mapper.py"""

import sys
import json
import re

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    if len(line) == 0:
     continue
    pronouns = ["han", "hon", "den", "det", "denna", "denne","hen"]
    # split the line into words
#     words = line.split()
    myJson = json.loads(line)
    print('%s\t%s' % ("TOTAL", 1))
    if 'retweeted_status' not in myJson:
     print('%s\t%s' % ("UNIQUE", 1))
     #print(myJson['retweeted_status'])
     text = myJson['text'].lower()
     textArray = text.split(" ")
     #print(*textArray)
     for word in pronouns:
      if textArray.count(word) > 0:
       print('%s\t%s' % (word, 1))
#       print(x)
    # increase counters
#     for word in words:
        # write the results to STDOUT (standard output);
        # what we output here will be the input for the
        # Reduce step, i.e. the input for reducer.py
        #
        # tab-delimited; the trivial word count is 1
        # print('%s\t%s' % (word, 1))
