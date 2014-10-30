#!/bin/bash

# Command List for talk

### Unix Shell Commands
## grep
# grep counting
grep -c '>' fastas/GUAB.fasta
grep -c '>' fastas/*.fasta
grep ">" -c -r *
grep -c -r --include '*.fasta*' '>' *
grep -c -r --include '*INX043*.fasta*' '>' *
grep -c '>' fastas/sub_dir*/*fasta
grep -c -r --exclude '*.fasta' '>' *

# standard grep
grep '>*b1' fastas/GUAB.fasta
grep -n '>*b1' fastas/GUAB.fasta
grep -A 1  '>*b1' fastas/GUAB.fasta

# writing to a file
grep -A 1  '>*b1' fastas/GUAB.fasta > my_fasta.fasta
# appending to an existing file
grep -A 1  '>*b1' fastas/GUAB.fasta >> my_fasta.fasta

## sed
sed '' command_list.sh
sed 's/grep/echo/' command_list.sh | head
grep -A 1  '>*b1' fastas/GUAB.fasta | sed 's/\-\-//'g > my_fasta.fasta
grep -A 1  '>*g1' fastas/GUAB.fasta | sed 's/\-\-//'g >> my_fasta.fasta

# input from a file with < or cat
sed < my_fasta.fasta 's/\-\-//'g > my_fasta_clean.fasta
cat my_fasta.fasta | sed 's/\-\-//'g > my_fasta_clean.fasta

# more examples
grep -c 'Pseudomonas' HOT_fosmids_small/*/blast_results/*RefSeq*.LASTout.parsed.txt |\
sed 's/HOT_fosmids_small.*blast_results\///'
grep -c 'Pseudomonas' HOT_fosmids_small/*/blast_results/*RefSeq*.LASTout.parsed.txt |\
 sed 's/HOT_fosmids_small.*blast_results\///' |\
  sed 's/.RefSeq_complete_nr_v62_dec2013.LASTout.parsed.txt//'

# multiple matchs with g
echo 'old old old old old old old old' | sed 's/old/new/g'
# print line with p
echo 'old old old old new new new' | sed 's/old/new/gp'
echo 'one two three four' | sed 's/\(one\)\ \(two\)\ \(three\)\ \(four\)/\4 \3 \2 \1/'
echo 'one two three four' | sed 's/\(.+\)\ \(.+\)\ \(.+\)\ \(.+\)/\4 \3 \2 \1/'
echo 'one two three four' | sed 's/\([A-z]+\)\ \([A-z]+\)\ \([A-z]+\)\ \([A-z]+\)/\4 \3 \2 \1/'

## awk
awk '{ print }' HOT_fosmids_small/below_euphotic_200m/results/annotation_table/functional_and_taxonomic_table.txt
awk '/proteo/ {print $1,"\t", $2, "\t", $3;}' HOT_fosmids_small/below_euphotic_200m/results/annotation_table/functional_and_taxonomic_table.txt
awk '/proteo/ {print $0;}' HOT_fosmids_small/below_euphotic_200m/results/annotation_table/functional_and_taxonomic_table.txt
awk '/proteo/ {print $3,"\t", $2, "\t", $1 ;}' HOT_fosmids_small/below_euphotic_200m/results/annotation_table/functional_and_taxonomic_table.txt
awk '/proteobacteria/ {FS="\t"; print $1,"\t",$9;}' HOT_fosmids_small/below_euphotic_200m/results/annotation_table/functional_and_taxonomic_table.txt
awk '/proteobacteria/ {FS="\t"; OFS=","; print $1,$9;}' HOT_fosmids_small/below_euphotic_200m/results/annotation_table/functional_and_taxonomic_table.txt
cut -f9 HOT_fosmids_small/below_euphotic_200m/results/annotation_table/functional_and_taxonomic_table.txt
awk 'BEGIN {FS="\t"; OFS="\t"; print "ORF_ID","Taxonomy"} /proteobacteria/ { print $1,$9;}' HOT_fosmids_small/below_euphotic_200m/results/annotation_table/functional_and_taxonomic_table.txt
awk 'BEGIN {FS="\t"; OFS="\t"; print "ORF_ID","Taxonomy"} /proteobacteria/ { print $1,$9;}' HOT_fosmids_small/below_euphotic_200m/results/annotation_table/functional_and_taxonomic_table.txt > my_little_tabby.txt