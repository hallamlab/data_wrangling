#!/usr/bin/python

# import libraries
import sys # for argument vector

def split_and_clean(line, delim="\t"):
    """
    Splits and cleans a line from a character delimited file
    """
    line = line.split(delim)
    line = map(str.strip, line)
    line = map(str.strip, line, "\n")
    return line
    
def make_matrix(file):
    """
    Takes a tab delimited file as input and returns a matrix-like
    structure implemented with dictionaries and lists
    """
    matrix = {} # matrix to return
    
    # extract lines from file
    fh = open(file, "r")
    lines = fh.readlines()
    fh.close()
    
    # create rows and column indexies
    cols = split_and_clean(lines[0])
    cols = cols[1:] # one element empty
    rows = []
    
    # run through lines and split
    for line in lines[1:]:
        fields = split_and_clean(line)
        row = fields[0]
        
        # add row to our list
        rows.append(row)
        
        # add index to hash
        if row not in matrix:
            matrix[row] = {}
        
        # get values of row
        values = fields[1:]
        
        # add values by column
        for i in range(len(cols)):
            if cols[i] not in matrix[row]:
                matrix[row][cols[i]] = values[i]
    
    # return dictionary matrix and rows and columns
    return (matrix, rows, cols)


# collect matrix file from command line
matrix_file = sys.argv[1]

(matrix, rows, cols) = make_matrix(matrix_file)

print "Second row, third column:", matrix["two"]["cherry"]

# print out the matrix
for r in rows:
    for c in cols:
        print "(%s,%s): %s" % (r,c, matrix[r][c])


    