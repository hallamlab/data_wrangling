#!/usr/bin/python

# import libraries
import sys # for argument vector
import optparse # to parse arguments

# describe what the script does
what_i_do = "A simple script for printing files"
usage = "myscript.py -i <input_file> -o output_file"

# initialize the parser
parser = optparse.OptionParser(usage = usage, epilog = what_i_do)
parser.add_option("-i", "--input_file", dest="input_file", default=None,
                   help='file to print out to the screen [Required]')
parser.add_option("-o", "--output_file", dest="output_file", default=None,
                   help='output file to write to')

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
    
    # close the file
    fh.close()
    
    taxa_to_count = {} # dictionary for taxa count
    
    # iterate through each line and print out content
    for line in lines:
        # split fields by tab
        fields = line.split("\t")
        
        # do some cleanup
        for i in range(len(fields)):
            fields[i] = fields[i].strip()
            fields[i] = fields[i].strip("\n") # strip tailing \n
        
        taxa = fields[8] # pull out taxa from current line
        
        # create a place in if taxa new
        if taxa not in taxa_to_count:
            taxa_to_count[taxa] = 0
    
        # add to current taxa count
        taxa_to_count[taxa] = taxa_to_count[taxa] + 1
    
    if opts.output_file:
        ## write out custom output
        # open a file to write to
        out_fh = open(opts.output_file, "w")

        # create a header for our file
        header = "Taxa" + "\t" + "Count" +"\n"
        out_fh.write(header)

        # iterate through our taxa count dictionary
        for taxa in taxa_to_count:
            out_line = taxa + "\t" + str(taxa_to_count[taxa]) + "\n"
            out_fh.write(out_line)
    
        out_fh.close()

if __name__ == "__main__":
    main()
