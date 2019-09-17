#!/usr/bin/env python
"""mapper.py"""

import sys

# input comes from STDIN (standard input)
for line in sys.stdin:
    # split the line into CSV fields
    line = line.strip()
    words = line.split(",")
    if len(words) == 4:
        #
        # It's the citation with state info intermediary
        #
        try:
            # Check if the states for citing & cited cities are the same
            if (words[1] == words[3] and words[1].strip()!= "None"):
                print('%s\t%s' % (int(words[0]), 'y'))
        except Exception as e:
            # improperly formed citation number
            print("Exception ", e);
            pass
    else:
        #
        # It's patent info 
        #
        try:
            print('%s\t%s' % (int(words[0]), ','.join(words[1:])))
        except Exception as e:
            # improperly formed citation number
            print("Exception ", e)
            pass
