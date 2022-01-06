# Scoring mutations in DNA data
Mutations are the raw material of evolution. These arise in genomes as "errors" in DNA replication and, while a proportion of them have negative impacts on individuals, most are "effectively neutral", and others are even beneficial! Evolutionary novelty and adaptation are facilitated by mutations. As biologists we are interested in discovering where mutations occur in the genomes of individuals living in populations.

## Discovering mutations in DNA reads

Last class we learned the basic principles of genome assembly. Today, we will learn how we can use a reference genome to discover mutations segregating in populations. 

![mutations](https://github.com/Jcbnunez/biol4585j-yey2sn/blob/main/Class_Materials/5.SNP_calling/figs/mutations.1.png?raw=true)
Figure adapted from: Schlötterer et al 2014

A traditional experimental pipeline would look like this:

1. Identify populations or samples of interests (e.g., different adaptations, cancer cells, etc)
2. Sequence DNA from organisms of interest
3. Map the DNA sequences from organisms agains a reference genome
4. Compare the DNA reads vs the reference sequence to look for mutated loci

## Step 1. load the appropriate programs and obtain data
### Load programs in rivanna
```
module load gcc/9.2.0
module load bwa/0.7.17
module load samtools
module load picard
module load bcftools

#define qualimap program
qualimap=/project/biol4585j-yey2sn/software/qualimap_v2.2.1/qualimap
```
### Copy data
Lets discuss what this data contains
```
cp /project/biol4585j-yey2sn/Files/Day_5/reads_day3.fastq ./

cp /project/biol4585j-yey2sn/Files/Day_5/reference_sequence.fasta ./
```
### Running blast to find the identity of an unknown sequence (Demonstration only)
1. In order to identify unknown sequences start by visiting https://blast.ncbi.nlm.nih.gov/Blast.cgi 
2. Select "Nucleotide BLAST" we will discuss the other algorithms briefly
3. Upload or copy/paste sequence

Lets discuss the results

## Step 2. Index the reference genome
Indexing the reference genome is one of the most important steps required to map reads onto a reference genome.
```
bwa index reference_sequence.fasta
```
## Step 3. Map reads to the reference genome
```
bwa mem -M reference_sequence.fasta reads_day3.fastq > my_Alignment.sam
```
This step creates a SAM file. A type of file which contain the search and map information for your reads and genome. Lets check what's in a [SAM File](https://en.wikipedia.org/wiki/SAM_(file_format)).

## Step 4. Remove un-mapped reads 

In the next step we are going to filter our alignment.  Using 2 important tools in the program samtools `-q` (quality) and `-f -F` (filtering flags).

1. Understand PHRED quality: https://en.wikipedia.org/wiki/Phred_quality_score 
2. Understand SAM F/f flags: https://broadinstitute.github.io/picard/explain-flags.html 

```
# reformat to Bam
samtools view -b -q 20 -F 0x0004  my_Alignment.sam >  my_Alignment.flt.bam
```
## Step 5. Sort the BAM file
This step is needed for downstream analysis. Here the file is sorted according to genome coordinates. 
```
# Sort with picard
java -jar $EBROOTPICARD/picard.jar SortSam I=my_Alignment.flt.bam O=my_Alignment.flt.srt.bam SO=coordinate VALIDATION_STRINGENCY=SILENT
```

## Step 6. Remove duplicated (redundant) reads
This is done in order to avoid false positives which may emerge during sequencing
```
# Remove duplicates with picard
java -jar $EBROOTPICARD/picard.jar MarkDuplicates I=my_Alignment.flt.srt.bam O=my_Alignment.flt.srt.rmdp.bam  M=dupstat.txt VALIDATION_STRINGENCY=SILENT REMOVE_DUPLICATES=true
```
## Step 7. Index the BAM file
This is another necessary step for downstream analyses
```
# index
samtools index my_Alignment.flt.srt.rmdp.bam
```
## Step 8. Check final quality of the mapping file
```
# Quality Check
$qualimap bamqc -bam my_Alignment.flt.srt.rmdp.bam  -outdir ./Qualimap_myAln 
```
Lets look over these quality reports

## Step 9. from mapped reads to mutations
For our final step, we are going to use a mutation discovery algorithm to find the mutations along the genome

```
bcftools mpileup -Ou -f reference_sequence.fasta -A my_Alignment.flt.srt.rmdp.bam | bcftools call -c -v > Mutation_Discovery.vcf
```

## Challenge
Your challenge today is a two parter:

First, to reproduce the graphs **mapping_quality_across_reference** and **coverage_across_reference**. You will find the raw data for these here:

```
library(data.table, lib.loc = "/project/biol4585j-yey2sn/R/4.1.1/")

cove <- fread("./Qualimap_myAln/raw_data_qualimapReport/coverage_across_reference.txt")
qual <- fread("./Qualimap_myAln/raw_data_qualimapReport/mapping_quality_across_reference.txt")

names(cove)[1] = "position"
names(qual)[1] = "position"
names(qual)[2] = "quality"

```
In both of these files the first column is always the genomic position and the second column is always is either the coverage or the quality score, respectively. 

### For the graph, I want to see, two line graphs, one showing on the y-axis the coverage, and the other one the quality. In both cases, the x-axis should be genomic position.

Second, please show whether there is a correlation 
