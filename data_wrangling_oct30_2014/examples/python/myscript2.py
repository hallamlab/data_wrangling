#!/usr/bin/python

# import libraries
import sys # for argument vector
import argparse # to parse arguments

# describe what the script does
what_i_do = "A simple script for printing files"

# initialize the parser
parser = argparse.ArgumentParser(description=what_i_do)
parser.add_argument("-i", "--input_file", type=str, dest="input_file", default=None,
                   required=True, nargs=1, help='file to print out to the screen [Required]')

# the main function of the script
def main():
    args = vars(parser.parse_args())
    # args is a dictionary that contains all the options
    
    print args["input_file"][0]
    
    # open the input_file *
    fh = open(args["input_file"][0], "r")

    # read lines from file
    lines = fh.readlines()

    # iterate through each line and print out content
    for line in lines:
        # split fields by tab
        fields = line.split("\t")
        
        # do some cleanup
        for i in range(len(fields)):
            fields[i] = fields[i].strip()
            fields[i] = fields[i].strip("\n") # strip tailing \n
        
        

    # close the file
    fh.close()

if __name__ == "__main__":
    main()

