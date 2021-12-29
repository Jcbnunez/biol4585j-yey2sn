# Fundamentals of genome assembly

## What are genomes?
Genomes are the blue print for all life on earth. They are made up of protein-coding genes, non-coding-regulatory sequences, and unknown-purpose sequences (often called "junk DNA", but this is a misnomer). As biologist information contain in genomes is a treasure trove about how are phenotype encoded and passed on from one generation to another, about the origin of disease, and about how natural selection shapes form and function in the wild.

![wiki genome](https://github.com/Jcbnunez/biol4585j-yey2sn/blob/main/Class_Materials/4.Genome_assembly/figures/genome_comp.png?raw=true)

An important element to know is that genomes contain a lot of evolutionary information. Because of the way that genetic transmission works, genomes contain information, not just about the individuals themselves, but also about: their parents, their grandparents, their great grandparents, their ancestors in general, and even about the species of origin! This is why genome assembly and analysis (a.k.a. _genomics_) is such an exciting field at the forefront of biology! 

## What is genome assembly from DNA reads
Genome assembly is the process of using DNA sequencing reads (short or long) in order to reconstruct a genome to the level of chromosomes. Or at least that is the dream! The reality is a bit more complex.  Here is a review with some additional information for [optional reading](https://www.nature.com/articles/nmeth.1935). For a video introduction to genome assembly check [here](https://www.youtube.com/watch?v=5wvGapmA5zM).

![the genomics dreams vs reality](https://media.springernature.com/relative-r300-703_m1050/springer-static/image/art%3A10.1038%2Fnmeth.1935/MediaObjects/41592_2012_Article_BFnmeth1935_Figa_HTML.jpg?as=webp)

Here is an example of a work pipeline adapted from [Baker  2012](https://www.nature.com/articles/nmeth.1935):

![Genome assembly](https://media.springernature.com/relative-r300-703_m1050/springer-static/image/art%3A10.1038%2Fnmeth.1935/MediaObjects/41592_2012_Article_BFnmeth1935_Figb_HTML.jpg)

## Assess the quality of the starting material (GIGO)
Our capacity to build genome assemblies is directly tied to the quality of the starting material. In this case reads. As such, before we dive into the details of genome assembly we need to become familiar with DNA reads. Lets take a look at the reads we will use today `raw_R1.fastq`

```
@read_name-24960/1
AATGTTGTCACTTGGATTCAAATGACATTTTAAATCTAATTATTCATGAATCGAACTAGTACGAAATGCAATGAGCATCTT
+
5??A9?BBBDDDBEDDBFF+FGHHIIHHHEIHIIHIIAHDHIIHIG#IIHIFHHHFGIII*IHHHIHFIIHGICIHHIHFF
```
We can learn more about quality encoding [here](https://support.illumina.com/help/BaseSpace_OLH_009008/Content/Source/Informatics/BS/QualityScoreEncoding_swBS.htm#)

## Logging into Rivanna and moving into our scratch folder
```
cd /scratch/'username'
mkdir genome_assmb_module
cd genome_assmb_module
```

Now, lets take a look for ourselves: 
```
cp /project/biol4585j-yey2sn/Files/Day_4/Fasta_files/raw_R1.fastq ./
```
Use head to visualize the first couple lines:
```
head raw_R1.fastq
```

### Do a quality assesment with FastQC
FastQC is an integrated module designed to do a comprhensive quality control assessment of your reads
```
module load fastqc
fastqc raw_R1.fastq
```
Lets go over the results toghther

# Core concepts in genome assembly

## 1. Shotgun sequencing (Coverage and Redundancy)
Recall from our reading of Shendure et al., when we sequence DNA, we often use a "shotgun" approach where the genome is amplified and randomly sampled. 

![genome asmb](https://github.com/Jcbnunez/biol4585j-yey2sn/blob/main/Class_Materials/4.Genome_assembly/figures/genomasmb.2.png?raw=true)
**Coverage**: A very important concept in genome assembly is _coverage_, the number of times a particular section of the genome was sampled during sequencing. Ideally we would like **all** the genome to be sampled **multiple times**.  
![cvg](https://github.com/Jcbnunez/biol4585j-yey2sn/blob/main/Class_Materials/4.Genome_assembly/figures/Cover.2.png?raw=true)
**Notice that this is never this simple!** To successfully assembly a genome we need high amounts of coverage

## Assembly strategies depend on the lenght of the base reads

### Short Reads (100-150 bps)

* Produced by Illumina instruments
* Short but highly accurate reads
* Cannot resolve repetitive regions
* Can produce a very very high amount of Data (need supercomputer to analyze)

### Long Reads (5000 - 25000 bps)

* Produced by PacBio machines
* Can be very long but often less accurate reads
* Can be used to revolve repeats, but often lead to the discovery of "false mutations"
* Need supercomputer for error-correction

## Assembly of long reads uses "OLC" (Overlap-Layout-Consensus )
Uses a three step approach to assembly.

![OLC](https://github.com/Jcbnunez/biol4585j-yey2sn/blob/main/Class_Materials/4.Genome_assembly/figures/OLC.png?raw=true)

## Assembly of short reads uses _de Bruijn_ graphs
While the concept of OLC is pretty intuitive, it only really works with long reads. When reads become too short the total number of potential overlaps explodes exponentially and the assembly becomes computationally untrackable.   

To solve this issue, computational biologist adopted a new strategy for assembly. Break up the reads into _"k-mers"_ and build  _de Bruijn_ graphs.

Then, we can construct a graph using the K-mers:
![kmers](https://github.com/Jcbnunez/biol4585j-yey2sn/blob/main/Class_Materials/4.Genome_assembly/figures/debrjn.png?raw=true)
Using this approach the, supercomputers can "approximate" OLC graphs. But there are some caveats:
![paths](https://github.com/Jcbnunez/biol4585j-yey2sn/blob/main/Class_Materials/4.Genome_assembly/figures/solving_paths.png?raw=true)

Final "contigs" are built from contiguous paths:
![paths final](https://github.com/Jcbnunez/biol4585j-yey2sn/blob/main/Class_Materials/4.Genome_assembly/figures/debruj_final.png?raw=true)
# Testing the impact of _K_ selection in assembly
Lets dive into some coding. As a class, we will collectively assess the impact of k-mer size on genome assembly. Each group in the class will be assigned a k-mer size. We will implement the algorithm and we will discuss our findings. 

```
module load sparseassembler

K=? # <----- declare here the k-mer value you have been given

SparseAssembler k $K GS 100000 f raw_R1.fastq
```
## Activity
You can load files into R using the `fread` function in the package `datatable`

```
module load gcc/7.1.0
module load openmpi/3.1.4
module load R/4.1.1
R
```
In R:
```
library(data.table, lib.loc = "/project/biol4585j-yey2sn/R/4.1.1/")
library(tidyverse, lib.loc = "/project/biol4585j-yey2sn/R/4.1.1/")
```
Now lets use the function `fread` to load in the file `CovHist.txt`, a file generated as part of the `SparseAssembler` command.
```
my_data <- fread("./CovHist.txt")
```
#you can modify the names of your data table using the following commands
```
#change name of 1st column
names(my_data)[1] = "kmer_count"

#change name of 2nd column
names(my_data)[2] = "frequency"
```
Now for the challenge. Let's visualize this data. in the ggplot/tidyverse you can use the option  `geom_bar(stat="identity")` to plot a bar graph plot. The challenge is to do a bar plot, that has ,on the x-axis the "kmer_count" and on the y-axis "frequency". Make sure that the color of the bars is blue.
