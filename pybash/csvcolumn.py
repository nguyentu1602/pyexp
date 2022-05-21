#!/usr/bin/env python
# csv module that comes with the python standard library
import csv
import sys

""" cat emailcomments.csv | python csvcolumn.py 0 
    Each argument that is provided to a Python script is exposed through the sys.argv array, 
    which can be accessed by first importing sys.
"""

if __name__ == "__main__":
    # the csv module exposes a reader object that takes a file object to read
    # in this example sys.stdin, which is what "pipe" sends into the python program
    
    csvfile = csv.reader(sys.stdin)
    
    # the script should take one argument that is a column number
    # command line arguments are accessessed via sys.argv list. If you type 0, that's the first column
    # if you type 1 that's  the second column
    column_number = 0
    if len(sys.argv) > 1:
        column_number = int(sys.argv[1])
        
    # each row in the csv file is a list with each comma-separated value for that line
    for row in csvfile:
        print(row[column_number])  # print use stdout as its output file
        

    
    
    