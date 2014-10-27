#!/bin/bash

# Command List for talk

## Unix Shell Commands

# grep counting
grep -c '>' fastas/GUAB.fasta
grep -c '>' fastas/*.fasta
grep ">" -c -r *
grep -c -r --include *.fasta* '>' *
grep -c -r --include *INX043*.fasta* '>' *
grep -c '>' fastas/sub_dir*/*fasta
grep -c -r --exclude '*.fasta' '>' *

# standard grep
grep -n '>*b1' fastas/GUAB.fasta
grep -A 1  '>*b1' fastas/GUAB.fasta

# writing to a file
grep -A 1  '>*b1' fastas/GUAB.fasta > my_fasta.fasta

