#!/usr/bin/python
"""Mapper1.py"""

import sys

# input comes from STDIN (standard input)
for line in sys.stdin:
    # split the line into CSV fields
    words = line.split(",")

    if len(words) == 2:
        #
        # It's a citation
        #
        try:
            print('%d\t%s' % (int(words[0]), words[1]), end='')
        except Exception as e:
            # improperly formed citation number
            print("Exception ", e)
            pass
    else:
        #
        # It's patent info 
        #
        try:
            print('%d\t%s' % (int(words[0]), ','.join(words[1:])), end='')
        except Exception as e:
            # improperly formed citation number
            print("Exception ", e)
            pass
