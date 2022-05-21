#!/usr/bin/env python
import sys

""" ways to use this script:
    $ cat names.log | python namescount.py | sort -rn
    $ cat names.log | python namescount.py | sort -rn | head -n 5

"""


if __name__ == "__main__":
    names = {}
    # sys.stdin is a file object. All the same functions that can be applied to a file object can be applied to sys.stdin
    
    for name in sys.stdin.readlines():
        # each line with have a newline on the end that should be removed 
        name = name.strip()
        if name in names:
            names[name] += 1
            
        else:
            names[name] = 1
    # iterating over the dict and print results:
    for name, count in names.items():
        sys.stdout.write(f"{count, name}\n" )