#!/bin/bash

# Command List for talk

## Unix Shell Commands

# grep
grep -c '>' fastas/GUAB.fasta
grep -c '>' fastas/*.fasta
grep ">" -c -r *
grep -c -r --include *.fasta* '>' *
grep -c -r --include *INX043*.fasta* '>' *
grep -c '>' fastas/sub_dir*/*fasta
grep -c -r --exclude '*.fasta' '>' *