#!/usr/bin/python

# import python packages
import sys

# pull filename from the command-line arguments
filename = sys.argv[1]

# open the file 
fh = open(filename, "r")

# read lines from file
lines = fh.readlines()

# iterate through each line and print out content
for line in lines:
    print line

# close the file
fh.close()


