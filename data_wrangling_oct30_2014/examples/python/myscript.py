#!/usr/bin/python

# import libraries
import sys # for argument vector
import optparse # to parse arguments

# describe what the script does
what_i_do = "A simple script for printing files"
usage = "myscript.py -i <input_file>"

# initialize the parser
parser = optparse.OptionParser(usage = usage, epilog = what_i_do)
parser.add_option("-i", "--input_file", dest="input_file", default=None,
                   help='file to print out to the screen [Required]')

# the main function of the script
def main():
    (opts, args) = parser.parse_args()
    # opts is a dictionary that contains all the options
    if not opts.input_file:
        print "Error: Input file not specified"
        print usage
        exit()

    # open the file 
    fh = open(opts.input_file, "r")

    # read lines from file
    lines = fh.readlines()

    # iterate through each line and print out content
    for line in lines:
        print line

    # close the file
    fh.close()

if __name__ == "__main__":
    main()
