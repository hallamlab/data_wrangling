# Basic Data Wrangling
Niels Hanson  
October 30, 2014  

Pourpose of this document is to summarize some basic data wrangling tasks that commonly occuring with metagenomic datasets in the Hallam Lab.

## Unix Shell Commands: grep, awk, sed, and others

Some very-simple first-pass analyses can be performed with common Unix commands. Although there are others, many analysis and sanity checking tasks can be accomplished by the following commands:

* `grep`: `g`eneral `r`egular `e`xpression `p` program -- at its simplist a program that can **find text patterns** in the **names and contents of files**.
* `sed`: `s`tream `ed`itor -- a general pourpose program to modify a stream of text, which generally is a file or program output
* `awk`: (pronounced 'auk' or 'ach') is a **basic text processing** and **report generating language** developed by Alfred `a`ho, Peter `w`einberger, and Brian `k`ernighan at Bell Labs in the 1970s

### When to use?

Lets discuss some advantages and disadvantages and when these commands (by themselves) are a good option.

#### Advantages 

* these commands are basically found on every Unix environment
* fairly efficient and low-level and so will scale to fairly large files
* excellent for making back-of-the-envelope kinds of calculations to make sure files are properly formatted, the correct size, simple 'one-off' analyses

#### Disadvantages

* small isocyncracies in system experience needed to know command's behavior
* small mistakes can lead to huge headaches permenant data loss
* many commands have their GNU open-source sister program (e.g., `gawk` has different behavior than `awk`, but not always installed on every system) 
* behavior changes depending on version installed on OS (annoying)
* unless process is scripted (see next section) and documented carefully, complicated commands can be very diffcult to follow and reproduce (best to keep things simple)

### Examples

Lets go through an number of examples where I personally use these in the lab.

* if you're following along in the terminal, change directory `cd` to the `examples/unix_commands/` directory

```
cd examples/unix_commands/
```

#### grep

The `grep` is generally used to identify and print lines in files that match a particular pattern. The basic command has the form:

```
grep 'pattern' file
```

* Counting the number of sequences in a fasta file
    * the `-c` option means 'count'
    * this will return he number of times the `'>'` pattern is observed in the fasta file
    * if the file is well-formatted, this will accurately tell you how many sequences there are in the file

```
grep -c '>' fastas/GUAB.fasta
9948
```

* this can also be done to every file that matches a particular file-name pattern in a directory with the **unix glob operator** (e.g., `*.fasta`)

```
grep -c '>' fastas/*.fasta
```

* count the number of sequences in all files in all subdirectories

```
grep ">" -c -r *
fastas/.DS_Store:0
fastas/GUAB.fasta:9948
fastas/GUAC.fasta:8850
fastas/INX043_RawGSCdata_min2000.fasta.NR00314_J24.fasta:1
fastas/sub_dir1/INX043_RawGSCdata_min2000.fasta.NO00111_F15.fasta:1
fastas/sub_dir1/INX043_RawGSCdata_min2000.fasta.NO00111_J19.fasta:1
fastas/sub_dir1/INX043_RawGSCdata_min2000.fasta.NR0031_K08.fasta:1
fastas/sub_dir2/INX043_RawGSCdata_min2000.fasta.SCR021_C16.fasta:1
fastas/sub_dir2/INX043_RawGSCdata_min2000.fasta.SCR044_H13.fasta:1
fastas/sub_dir2/NapDC_July06_2011_trimmed.fasta:15360
fastas/TOLDC_Feb22_2011_trimmed.fasta:3072
```

* but, if we were only interested in the `fasta` files use the `--include '.fasta'` option

```
grep -c -r --include *.fasta* '>' *
fastas/GUAB.fasta:9948
fastas/GUAC.fasta:8850
fastas/INX043_RawGSCdata_min2000.fasta.NR00314_J24.fasta:1
fastas/sub_dir1/INX043_RawGSCdata_min2000.fasta.NO00111_F15.fasta:1
fastas/sub_dir1/INX043_RawGSCdata_min2000.fasta.NO00111_J19.fasta:1
fastas/sub_dir1/INX043_RawGSCdata_min2000.fasta.NR0031_K08.fasta:1
fastas/sub_dir2/INX043_RawGSCdata_min2000.fasta.SCR021_C16.fasta:1
fastas/sub_dir2/INX043_RawGSCdata_min2000.fasta.SCR044_H13.fasta:1
fastas/sub_dir2/NapDC_July06_2011_trimmed.fasta:15360
fastas/TOLDC_Feb22_2011_trimmed.fasta:3072
```

* how about if were only interested in files that had `INX043` and were `.fasta` files anywhere in the folder `fastas/`
   * use the anycharacter glob (`*`) to select text on both sides

```
grep -c -r --include *INX043*.fasta* '>' *
fastas/INX043_RawGSCdata_min2000.fasta.NR00314_J24.fasta:1
fastas/sub_dir1/INX043_RawGSCdata_min2000.fasta.NO00111_F15.fasta:1
fastas/sub_dir1/INX043_RawGSCdata_min2000.fasta.NO00111_J19.fasta:1
fastas/sub_dir1/INX043_RawGSCdata_min2000.fasta.NR0031_K08.fasta:1
fastas/sub_dir2/INX043_RawGSCdata_min2000.fasta.SCR021_C16.fasta:1
fastas/sub_dir2/INX043_RawGSCdata_min2000.fasta.SCR044_H13.fasta:1
```

* and if I just wanted to look into directories that had the pattern `sub_dir*`

```
grep -c '>' fastas/sub_dir*/*fasta
fastas/sub_dir1/INX043_RawGSCdata_min2000.fasta.NO00111_F15.fasta:1
fastas/sub_dir1/INX043_RawGSCdata_min2000.fasta.NO00111_J19.fasta:1
fastas/sub_dir1/INX043_RawGSCdata_min2000.fasta.NR0031_K08.fasta:1
fastas/sub_dir2/INX043_RawGSCdata_min2000.fasta.SCR021_C16.fasta:1
fastas/sub_dir2/INX043_RawGSCdata_min2000.fasta.SCR044_H13.fasta:1
fastas/sub_dir2/NapDC_July06_2011_trimmed.fasta:15360
```

* there is also an `--exclude` to do the opposite of `--include`
    * here we look for `'>'` for all files in all subdirectories that do not end in `fasta`

```
grep -c -r --exclude '*.fasta' '>' *
command_list.sh:6
fastas/.DS_Store:0
```

##### Asside: Unix globs

* Note that there is quite a bit of power to these Unix 'glob' operators:
    * `*`: means any number of characters
        * `beginning*end`: selects files with a particular `beginning` and `end` patterns
        * `beginning*middle*end`: selects files with particular `beginning`, `middle`, and `end` text
        * `sample*/blast_results/*parsed_blast.txt`: matches all `parsed_blast.txt` files that can be found in sub-directories `blast_results/` below directries starting with `sample*`
    * `?`: matches exactly one unknown character
        * `?at`: matches `fat`, `cat`, `hat`, `sat`, etc.
    * `[]`: specifies a range or set of characters to match
        * `[BC]at`: matches `Bat` or `Cat` but not `bat` or `cat`
        * `sample_[0-9][0-9]`: matches `sample_01`, `sample_02`, etc.
    * `\`: 'escapes' the following character (where you actually want to match it)
        * `\[*proteobacteria*\]: matches text that have RefSeq-style taxonomy in square brackets
* the linux command `ls` can be used to list the set of files that are hit by a glob pattern
    * this is very important when writing critical commands like 'move' (`mv`) or 'remove' (`rm`)
        * everyone eventually burns themselves, its a fact of life while working on with the Unix command line
* *Note: Unix globs are not as sophisicated as full blown Perl or grep-based regular expressions. They don't have a complete feature set. Some things just can not be done with command line globs*

#### `grep` (con't)

* use glob patterns and to count the number of lines that match `Pseudomonas` in the Hawaii-ocean Time Series RefSeq LAST output (truncated data to fit on GitHub).

```
grep -c 'Pseudomonas' HOT_fosmids_small/*/blast_results/*RefSeq*.LASTout.parsed.txt
HOT_fosmids_small/below_euphotic_200m/blast_results/below_euphotic_200m.RefSeq_complete_nr_v62_dec2013.LASTout.parsed.txt:99
HOT_fosmids_small/chlorophyllmax_130m/blast_results/chlorophyllmax_130m.RefSeq_complete_nr_v62_dec2013.LASTout.parsed.txt:153
HOT_fosmids_small/deepabyss_4000m/blast_results/deepabyss_4000m.RefSeq_complete_nr_v62_dec2013.LASTout.parsed.txt:208
HOT_fosmids_small/omz_770m/blast_results/omz_770m.RefSeq_complete_nr_v62_dec2013.LASTout.parsed.txt:182
HOT_fosmids_small/upper_euphotic_10m/blast_results/upper_euphotic_10m.RefSeq_complete_nr_v62_dec2013.LASTout.parsed.txt:167
HOT_fosmids_small/upper_euphotic_70m/blast_results/upper_euphotic_70m.RefSeq_complete_nr_v62_dec2013.LASTout.parsed.txt:193
HOT_fosmids_small/uppermesopelagic_500m/blast_results/uppermesopelagic_500m.RefSeq_complete_nr_v62_dec2013.LASTout.parsed.txt:190
```

* dropping the `-c`, `grep` will just print the matching line
    * match all fasta headers that end in `b1`

```
grep '>*b1' fastas/GUAB.fasta
>GUAB5590.b1
>GUAB3843.b1
>GUAB6002.b1
>GUAB6573.b1
```

* the `-n` option will print out the line number where the match was found
    if more than one file being searched the filename will be printed as well

```
grep -n '>*b1' fastas/GUAB.fasta
1:>GUAB5590.b1
3:>GUAB3843.b1
7:>GUAB6002.b1
11:>GUAB6573.b1
...
```

* if the fasta file format is well-formatted (contains the sequence only on one line after matching header), then you can use the 'after' `-A` flag to print a number of lines after the match.
    * *Note: there are also 'before' `-B` and 'context' `-C` flags that print out lines before the match and on both sides, respectively.* 
    * here we use it to get the sequence along with header patterns that end in `.b1`, because we know that it is the first line below in a well-formatted `.fasta` file
        * *Note: this won't work for fasta files where the sequence in on multiple lines

```
grep -A 1  '>*b1' fastas/GUAB.fasta
>GUAB5590.b1
ATCGAGTGTGTTCTTTTGCGCGATGGTATTCGACGTACCGTTTGCATTTCATCACAAGTCGGCTGTGCAATGGGGTGTGTATTCTGTGCAAGCGGTCTTGATGGAGTTATCCGAAATTTGACAACCGGTGAGATCATCGAGCAGTTATTACGACTCACTCGTTTACTCCCAACAGAAGAACGACTAAGTCATATTGTTGTCATGGGAATGGGTGAACCACTAGCAAACCTCGATCGTTTATTACCTGCTCTTGCAATCGCACAAAGTCCTGAGGGACTTGGTATATCTCAACGACGAATCACTATTTCAACTGTCGGGTTGCCATCGGCAATTGATCGGCTGTGTCAAGAAAATCCTGGATATCATCTTGCCGTATCACTCCATGCCGCTGACGATCCACTCCGAACAAAACTCGTTCCAGTCAATAAGTCGATCGGAGTTCATGCCATTTTAGCCGCAGCTGACCGATACTGGGAAACATCTGGCCGACGACTTACTTTCGAATATGTCTTACTCGGAAATCTTAATGATTCTCCAGATCATGCCCGTTCGTTAGCTCGGTTTATCGGCAAACGTGCAGCGCTCGTAAACATTATTCCGTACAACACAGTCGATGGCCTACCGTGGGAAGAGCCTACTGACATTTCTCGTGAACGATTTCTTGATGTCCTTTCGAATGCTGGCGTGAATGTTCAGACTCGAAAAAGGAG
--
>GUAB3843.b1
CTGGGTGGCAGCGGTGTAGAGAAAATAGTTGAACTTTCGCTTTTGCCAGATGAAAAAGTGGCATTCAATAAAAGTATCGATGCAGTTCGGGAACTTGTTGGCGCAATGGAGAGCCTGACGCCATAACAGAAGCCCCCCAGTCCTCCCAGCCTCCCTCTGTCGGCTAGTTTCGCGAAAGCTCTTCATTTTCACACGGAAATGCTGCCATTGCCCGGAGTGTGTGACTGCGTTAGAAACCTCCGACGCATTGCCATAAGTCAAATCTCTTGTGGCAATGCGTTAGCAATCACGCTGTGTATTTTTGCAAAAGGTTACGCGGAGGATCTGGAATGGTGCATCAGTCGACAGTATTTGATTATGAATTCAATCATTGTTCACCAAGCAGTAGAGGCTTTTTGTGCAACGAGGTGAATCTCCCTTCGAGTAAACCAGAGCAACTGTTTTTACCACGAGGGTATGAGTCGGGATACGACTACCCACTCCTCGTGTGGCTTCCGCAGTCAGACGATGCTCACTTTGACTTAGGTCGCACCATGATGCGAATGAGTTTAAGGAATTACATTGCAGTAGTACCTGCTGTCACGTCTGATTTGGAGAGTTGTTTTGAAGCTATTGACGGAATAATGAGTCAATATAGCGTTCACTCTCGCAGATTTTATCTTATTGGTGTTGAGGAAGGTGGAGAGAATGCCTTTCGTTATGCTTGCCAAAATC
...
```

* we can now use 'write to file' operator `>` to safe this output to separate `.fasta` file
* whatever is print to the terminal (standard out) will be saved in the file `my_fasta.fasta`

```
grep -A 1  '>*b1' fastas/GUAB.fasta > my_fasta.fasta
```

* *Note: this isn't totally correct, because `grep` puts `--` characters between matches, which could cause fasta parsers to choke on the input. Solving this problem actually takes us into our next section which is on the Uinx 'Sequence Editor' program `sed`*

#### `Sed`

`Sed`, or the stream editor program is used to do precicely that, edit a stream of text. So this can be used to modify a string of text, usually using **regular expresisons**:

```
sed [options] commands [file-to-edit]
```

Basically `sed` reads in a file, performs editing operations on it and then prints it to the screen. If we give it no commands it just prints the text, akin to the `cat` program. You can 

```
sed '' command_list.sh
```

The biggest use of `sed` is to replace one some text with another piece of text. This has the famous 3-slashes format: `s/old_word/new_word/`

* here for example this goes through the command list file and replaces all instances of `grep` to `echo`.
* now might be a good time to also introduce the pipe operator `|` this takes the output (what is printed to the screen) of one program and feeds it as input to another.
   * many Unix commands can be created in this manner by 'chaining' commands together
   * here I chain the results of `sed` to another program called `head` which, by default, prints the first six lines of a file

```
sed 's/grep/echo/' command_list.sh | head
#!/bin/bash

# Command List for talk

## Unix Shell Commands

# echo counting
echo -c '>' fastas/GUAB.fasta
echo -c '>' fastas/*.fasta
echo ">" -c -r *
```

* we already have a useful example, when we printed out those bacterial counts before all the filenames made it hard to read the output, lets see if we can correct that with `sed`

```
grep -c 'Pseudomonas' HOT_fosmids_small/*/blast_results/*RefSeq*.LASTout.parsed.txt | sed 's/HOT_fosmids_small.*blast_results\///'
below_euphotic_200m.RefSeq_complete_nr_v62_dec2013.LASTout.parsed.txt:99
chlorophyllmax_130m.RefSeq_complete_nr_v62_dec2013.LASTout.parsed.txt:153
deepabyss_4000m.RefSeq_complete_nr_v62_dec2013.LASTout.parsed.txt:208
omz_770m.RefSeq_complete_nr_v62_dec2013.LASTout.parsed.txt:182
upper_euphotic_10m.RefSeq_complete_nr_v62_dec2013.LASTout.parsed.txt:167
upper_euphotic_70m.RefSeq_complete_nr_v62_dec2013.LASTout.parsed.txt:193
uppermesopelagic_500m.RefSeq_complete_nr_v62_dec2013.LASTout.parsed.txt:190
```

* we can even pass the command through `sed` again to clear the other side of the output, making it much more readable:

```
grep -c 'Pseudomonas' HOT_fosmids_small/*/blast_results/*RefSeq*.LASTout.parsed.txt | sed 's/HOT_fosmids_small.*blast_results\///' | sed 's/.RefSeq_complete_nr_v62_dec2013.LASTout.parsed.txt//'
below_euphotic_200m:99
chlorophyllmax_130m:153
deepabyss_4000m:208
omz_770m:182
upper_euphotic_10m:167
upper_euphotic_70m:193
uppermesopelagic_500m:190
```

* one quick got-ya with `sed` is that by default it only finds one match per line
* you can change it to find all matches per line by enabling 'global matches' by adding a `g` to the end of the three slashes command `'s/old_word/new_word/g'`
    * below we should see out with the `old` text and in with the `new`:

```
echo 'old old old old old old old old' | sed 's/old/new/g'
new new new new new new new new
```

* other thing is the 'print lines' (`p`) option, which will ignore the case of the text when matching and print lines that were substited as a sanity checking procedure.

```
echo 'old old old old new new new' | sed 's/old/new/gp'
```

* One other thing is to switch matches around by containing them in excaped brackets `\(\)` using the `\1`,`\2`, `\3`, and `\4` to refer to the first, second, third and fourth matches, respectively.

```
echo 'one two three four' | sed 's/\(one\)\ \(two\)\ \(three\)\ \(four\)/\4 \3 \2 \1/'
four three two one
```

* We can do this again with with at least one wildcards `+`

```
echo 'one two three four' | sed 's/\(.+\)\ \(.+\)\ \(.+\)\ \(.+\)/\4 \3 \2 \1/'
four three two one
```

* You can also set your particular matching set with `[]`:

```
echo 'one two three four' | sed 's/\([A-z]+\)\ \([A-z]+\)\ \([A-z]+\)\ \([A-z]+\)/\4 \3 \2 \1/'
one two three four
```

#### `awk`

Where `sed` was a text replacer, `awk` is more of a text modifier, and in particular is works with tabular data. It can be used to modify files, manipulate columns, or to convert from one tabular file format to another.

```
awk '/search_pattern/ { action_to_take_on_matches; another_action; }' file_to_parse
```

*  one of the first things to do is pass through a file and print out its contents
    * here we take the `functional_and_taxonomic_table.txt` produced by metapathways.

```
awk '{ print }' HOT_fosmids_small/below_euphotic_200m/results/annotation_table/functional_and_taxonomic_table.txt
```

* we can use the double-slashes command to isolate certain lines, `'/below_euphotic_200m_7271_0/'`, kind of like `grep`:

``` 
below_euphotic_200m_7271_0    302	2	304	below_euphotic_200m_7271	616	-		all	hypothetical protein
```

* now that we have found our particular lines of interest, we can use action braces `{}` to perform a particular function, like print only the columns that we want using the `print` command and the column references `$1`, `$2`, etc, 
    * here the column needs to contain the word `proteo` in an effort to find all the *proteobacteria*

```
awk '/proteo/ {print $1,"\t",$2, "\t", $3;}' HOT_fosmids_small/below_euphotic_200m/results/annotation_table/functional_and_taxonomic_table.txt
```

* note that the whole line can be printed with `$0`

```
awk '/proteo/ {print $0;}' HOT_fosmids_small/below_euphotic_200m/results/annotation_table/functional_and_taxonomic_table.txt
```

* and we can create our own personal file with a custom column order

```
awk '/proteo/ {print $1,"\t",$2, "\t", $3;}' HOT_fosmids_small/below_euphotic_200m/results/annotation_table/functional_and_taxonomic_table.txt
```

* By default the field seperator character `FS` is set to whitespace, but the field character can be specified explicity

```
awk '/proteobacteria/ {FS="\t"; print $1,"\t",$9;}' HOT_fosmids_small/below_euphotic_200m/results/annotation_table/functional_and_taxonomic_table.txt
below_euphotic_200m_7276_0      Gammaproteobacteria
below_euphotic_200m_861_0 	 Gammaproteobacteria
below_euphotic_200m_2785_0 	 Gammaproteobacteria
below_euphotic_200m_3404_0 	 Gammaproteobacteria
below_euphotic_200m_5253_0 	 Gammaproteobacteria
below_euphotic_200m_7506_0 	 Gammaproteobacteria
```

* *Note: It is important in `awk` that you **specify variables with double** (`"`) rather than single quotes (`'`)*

* In fact there are a number of `awk` variables to help with processing the text fields:
    * `FILENAME`: References the current input file.
    * `FS`: The current field separator used to denote each field in a record. By default, this is set to whitespace.
    * `RS`: The record separator used to distinguish separate records in the input file. By default, this is a newline character.
    * `OFS`: The field separator for the outputted data. By default, this is set to whitespace.
    * `ORS`: The record separator for the outputted data. By default, this is a newline character.
    * `NF`: The number of fields in the current record.
    * `NR`: The number of the current record.
    * `FNR`: References the number of the current record relative to the current input file. For instance, if you have two input files, this would tell you the record number of each file instead of as a total.

* For instance, if you specify the `OFS=",", you can quickly turn a tab-delimited file into a custom comma-separated file

```
awk '/proteobacteria/ {FS="\t"; OFS=","; print $1,$9;}' HOT_fosmids_small/below_euphotic_200m/results/annotation_table/functional_and_taxonomic_table.txt
below_euphotic_200m_7276_0,Gammaproteobacteria
below_euphotic_200m_861_0,Gammaproteobacteria
below_euphotic_200m_2785_0,Gammaproteobacteria
below_euphotic_200m_3404_0,Gammaproteobacteria
```

* Note that when this is done, we only need to print the column identifiers rather than exlicity set the separator `print $1,$9;`

* There are also `BEGIN` and `END` code blocks that allow you to optionally specify header and footer for the file.

```
awk 'BEGIN { action; }
/search/ { action; }
END { action; }' input_file
```

* For instance it might be helpful to add an informative header to our custom file

```
awk 'BEGIN {FS="\t"; OFS="\t"; print "ORF_ID","Taxonomy"} /proteobacteria/ { print $1,$9;}' HOT_fosmids_small/below_euphotic_200m/results/annotation_table/functional_and_taxonomic_table.txt
ORF_ID    Taxonomy
below_euphotic_200m_7276_0	Gammaproteobacteria
below_euphotic_200m_861_0	Gammaproteobacteria
below_euphotic_200m_2785_0	Gammaproteobacteria
below_euphotic_200m_3404_0	Gammaproteobacteria
```

* now that we like the structure of our custom file, we are ready to write it out to disk

```
awk 'BEGIN {FS="\t"; OFS="\t"; print "ORF_ID","Taxonomy"} /proteobacteria/ { print $1,$9;}' HOT_fosmids_small/below_euphotic_200m/results/annotation_table/functional_and_taxonomic_table.txt > my_little_tabby.txt
```

* So now the custom file should be read to be read into Excel or R with relatively little additional effort.
* *As a general rule, it is better to use tab characters (`\t`) as delimiters rather than comma characters (`,`) when dealing tables with text fields (like protein annotations), commas in a field will often mess up downstream parsing, an additiona headache we don't really need*

## Unix Shell Scripting

Where the above programs dealt file cleaning and formatting, Unix Shell Scripting really deals with the automation of repetative or simple tasks. In particular, we are going to discuss the `bash` or `b`ourne `a`gain `sh`ell, which is definately the dominant command-line shell in todays unix environment. 

* Most shell scripts involve selecting files with an unix glob `*` and performing an action for each file. This important primative function is setup by creating a `for`-`do`-`done` loop:

```
for file in *fasta
do
    # do some actions
done
```

* As a first example we'll ask the `echo` command to print each filename to the screen, de-referning the filename witht he `$` character

```
for file in *fasta
do
    echo $file
done
```

* since small mistakes when running many commands at once can make a real mess or cause serious damange, **it is often a very good idea to `echo` your loop commands** to inspect them for accuracy before running them for real

* For instance it is very common to rename many files with some kind of suffix

```
for file in *fasta
do
    mv ${file} ${file}.backup
done
```

* This de-references the current file with the `$` or `${}` character and calls the file with the 'move' (`mv`) command to add `.backup` to the name of each file. Especially when appending text to a file the braces `{}` help make the code more clear.

* Furthermore, the `%` character can be used to trim a command form the right-hand-side, usually for changing filenames
    * for instance we will remove the `.backup` suffex we just added to our `.fasta` files
```
for file in *fasta.backup
do
    echo mv $file ${file%.backup}
done
```

## References

Some extra references for more information:

### `grep`

*

### `sed`

* https://www.digitalocean.com/community/tutorials/the-basics-of-using-the-sed-stream-editor-to-manipulate-text-in-linux

### `awk`

* https://www.digitalocean.com/community/tutorials/how-to-use-the-awk-language-to-manipulate-text-in-linux

### `shell scripting`
