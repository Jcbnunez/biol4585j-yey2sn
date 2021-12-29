# Introduction to Phylogenetics using DNA data

## Reconstructing evolutionary history due to common ancestry

Phylogenetics is the study of relationships among the species on the tree of life, a task made possible under the assumption that all current life on earth shares a common ancestor. Other than understanding the evolutionary history of species, in general, phylogenies have multiple specific applications including: understanding the history of populations through time, epidemiology, cancer biology, as well as the evolution of language.   

### For example, the evolutionary rates of the COVID-causing (SARS-CoV-2) virus:
![covid variants evolution](https://scontent.fric1-1.fna.fbcdn.net/v/t39.30808-6/269372108_10159198490925589_1788491593852369443_n.png?_nc_cat=107&ccb=1-5&_nc_sid=9267fe&_nc_ohc=NDDq5TIPsC8AX8iYJvZ&_nc_ht=scontent.fric1-1.fna&oh=00_AT_vFj3j3WEyA3-Iot7An_H21DHTCIWAWv0p9AEE5EG4IQ&oe=61D0D3F7)

### Reading a phylogeny
![basics of trees](https://github.com/Jcbnunez/biol4585j-yey2sn/blob/main/Class_Materials/3.Phylogenies/Figures/trees_basic.2.png?raw=true) 
One of the most important concepts in phylogenetics is to understand what "the trees are telling you". To this end, you should become familiar with the following parts of a phylogenetic tree:

* **The "flow of time"**: The most abstract concept to understand about any phylogenetic tree is the idea that the entire tree in of itself is a statement about evolutionary time. This has tremendous implications for data analysis because, given the right calibration, the "branch distance" between tips and nodes (see below) can be used to calculate divergence times among species.
* **The root**: The root of a tree is represnt a moment in evolutionary history in which all species in the the "tips" shared a common ancestor. Notably, in order to be able to find a the root of a tree, one of our tips must be an out-group. An outgroup is a species which we know shared a common ancestor with the species of interest. for example, chimps and humans.
 In the case that we cannot find an appropriate root, the we will be forced to create and "un-rooted tree" (we will discuss this in class).   
* **The nodes**: Nodes represents times when species, or more precisely lineages, diverge from one another (i.e., when they last shared a common ancestor). 
* **The branches**: Branches represent the lineages that persist through time.
* **The tips**: The tips represent the species that you are using to build your tree. they often consist of in-groups (species that you want to learn about) and out-groups (a species used to "root" your tree).

## Homology and the DNA code
How do we estimate phylogenetic relationships among species? To do this we often compare and contrasts phenotypes or DNA from different species. The most important aspect of this process is to make sure that our comparisons are "fair". To ensure this, we must compare species at **homologous traits**. The term "homology" refer to the idea of comparing similar characters among and between the species of interest. For example, lets say that you want to build a DNA phylogeny with 10 species, but you only have sequences from gene A in 5 species, and of gene B in the other 5. Could you build a phylogeny with these data combined? The answer is **NO**. This would be an unfair comparison -- you either have 10 sequences of A or 10 of B, but no _Frankensteining_ allowed! 

Understanding what is and isn't homologous can often be a contentious debate, but, for this course, we will use straight forward examples: genes from the animal mitochondrial genome -- yes, _the powerhouse of the cell_.

## Findings DNA sequences in NCBI
In today's practicum we will build a species phylogeny using DNA data from the mitochrondrial genome of animals. So, the first question is: "where will we get the data?" .. you should know the answer to this by now! from [NCBI](https://www.ncbi.nlm.nih.gov/)! 

1. Visit NCBI by clicking in the [link](https://www.ncbi.nlm.nih.gov/)
2. Select the nucleotide option on the top ![nucleotide select](https://github.com/Jcbnunez/biol4585j-yey2sn/blob/main/Class_Materials/3.Phylogenies/Figures/nucleotide.png?raw=true)
3. Find your favorite animals with `mitochondrial cytochrome oxidase 1  <<my favorite animal>>`. ![search mito dog](https://github.com/Jcbnunez/biol4585j-yey2sn/blob/main/Class_Materials/3.Phylogenies/Figures/Dog_search.png?raw=true)

### How to navigate the results page?
Notice that your search may result in hundreds of results, some which will be useful and  other a bit less useful. This depends on the need of your project and the target gene you are searching for. 

### What are we looking for in this search?
Generally speaking we are looking for _cytochrome oxidase subunit 1 (COI) gene, partial cds; mitochondrial_ of about **700-900 bp long**.
![Size_search.png](https://github.com/Jcbnunez/biol4585j-yey2sn/blob/main/Class_Materials/3.Phylogenies/Figures/Size_search.png?raw=true)
### How to download DNA data. 
You can save your sequences to a FASTA file using the **send to option**. We will do a demonstration in class.  ![send to](https://github.com/Jcbnunez/biol4585j-yey2sn/blob/main/Class_Materials/3.Phylogenies/Figures/send_to_fasta.png?raw=true)

**Data will download to your home/Downloads folder**

## Aligning sequences 
So you have DNA sequences... good! Now, how do we turn that into a tree?! Remember that to build a good phylogenetic tree we need to ensure that our DNA sequences represent a fair comparison. In DNA terms, this means that our DNA sequences are correctly aligned (or aligned in a homologous fashion). 

![Aligment](https://github.com/Jcbnunez/biol4585j-yey2sn/blob/main/Class_Materials/3.Phylogenies/Figures/seqs_aligned.2.png?raw=true)
Sequence alignment is done through a process of global optimization [Learn more about it here](https://youtu.be/LhpGz5--isw). In brief, alignment optimization is done by evaluating all possible combinations of letters among your sequences and score the number of **matches** , **mismatches**, and **gaps**, assign a score and find the best possible score.

![global aln](https://github.com/Jcbnunez/biol4585j-yey2sn/blob/main/Class_Materials/3.Phylogenies/Figures/global_aligment_plot.png?raw=true)
### Implementing global aligments in MAFFT
 For our particular case, this process will be automated using the program [mafft](https://mafft.cbrc.jp/alignment/software/).

## Logging into Rivanna and moving into our scratch folder
```
cd /scratch/'username'
mkdir phylogenetics_module
cd phylogenetics_module
```

## Making an alignment of homologous sequences
Lets begin by copying a fasta file to our working directory
```
cp /project/biol4585j-yey2sn/Files/Day_3/mitochndrial.sequences.fasta ./
```
Go ahead and take a look at the file
```
head mitochndrial.sequences.fasta
```
### Challenge: can you use grep to find out what species are included in the fasta?

Ok, lets go ahead and build a sequence aligment
```
#first lets tell Rivanna where the program mafft is located:
mafft=/project/biol4585j-yey2sn/software/Mafft/bin/mafft
```
now lets call mafft on our samples

**NOTICE** that you need to type `$mafft` including the `$` and to use mafft
 here we are taking the "mitochndrial.sequences.fasta" file and alining it into a new file "mitochndrial.sequences.aln.fasta" - Ask me why do I need to use the extra `$`!
```
$mafft mitochndrial.sequences.fasta > mitochndrial.sequences.aln.fasta
```
Lets inspect the output file. What differences do you see? 

## Making a tree out of As, Cs, Ts, and Gs. 
How can we build a tree using DNA data? -- especially if DNA only has 4 characters?  The answers lie in our assumptions about the way DNA evolves. Basically, we know two things to be generally true, first, that DNA sequences evolve through time via mutation. Second, we know that way in which DNA evolves can me modeled according to genetic principles. 

OK, so two assumptions are pretty straightforward. Now here is where phylogenetics gets a bit complicated. It turns out that deciding what "genetic principles to apply" to DNA evolution makes a tremendous amount of difference in our analysis. Here are three examples (adapted from [Yang and Rannala 2012](https://www.nature.com/articles/nrg3186.pdf)):
![DNA models](https://github.com/Jcbnunez/biol4585j-yey2sn/blob/main/Class_Materials/3.Phylogenies/Figures/DNA_models.png?raw=true)
Here we have four models used in evolutionary theory:

1. **JC69** (Jukes and Cantor 1969): this is the simplest model of evolution. It basically assumes that all DNA mutations are equally likely and happen at symmetrical rates. 
2. **K80** (Kimura 1980): this is a more realistic model of evolution. We know from classical genetics that DNA bases are either **purines** or **pyrimidines** , and  that the rate at which these mutations occur is different whether you are mutating  purine->purine or pyrimidine->pyrimidine (purine<->pyrimidine).
3. **HKY85**  (Hasegawa-Kishino-Yano, 1985): it is an even more realistic model of evolution. It is based on genetic evidence of the ratio of transitions to trans-versions, as well as empirical knowledge that T <--> C mutations are highly common. 
4. And many many more model, in increasing complexity... 

### So? When do I use JC69, K80, or HKY85?!
The formal answer is complicated and and a bit beyond the scope of this course. But, do not fret! we can find the answer to this question using empirical model fitting with our phylogenetic estimator program [_IQtree_](http://www.iqtree.org/).

Lets give it a try. First lets tell rivanna where IQtree is: 
```
IQtree=/project/biol4585j-yey2sn/software/iqtree/bin/iqtree
```
 
Now lets ask IQtree to do empiral evaluations of various models

```
$IQtree -s mitochndrial.sequences.aln.fasta -m TESTONLY -pre Model_Search
```
In this command the `-s` flag indicated the input fasta file. Also, the `-m TESTONLY ` flag indicates that we want IQtree to run model selection. `-pre Model_Search` simply tells Rivanna to call our output files "Model_Search".

### Lets open the file `Model_Search.log`
**Whats in it?**: if we look at this file we will find that IQtree has taken our data and has tested a large number of models asking the question: "given the data, what model best describes the patterns of DNA evolution observed in the data?" _yeah, IQtree is doing that for you!_
**How does IQtree finds the best model?** The method works by optimizing the likelihood of the tree and model, given the data. This concept is a bit beyond the scope of the class, but for those mathematically minded individuals, you may find an in-depth description of the models and method  in [Kalyaanamoorthy et al 2017](https://www.nature.com/articles/nmeth.4285). 

**Lets chat about the output**

## Lets construct our tree

### Step 1. Choose an out-group
Based on our understanding of the data what organism should be the proper outgroup? **How can we do this?** Lets explore the functionalities of two core databases in evolutionary biology:

1. [**NCBI-BLAST**](https://blast.ncbi.nlm.nih.gov/Blast.cgi) an online program that searches all NIH databases to identify the confidence of a sequence's identity. 
2. [**timetree**](http://www.timetree.org/) a repository used to explore all currently known (i.e., published) phylogenetic relationships among taxa -- based on a combination of both fossil and molecular evidence.

#### Can we replicate the tree from _timetree_ using our data?

### Step 2. Run your analysis!
```
$IQtree -s mitochndrial.sequences.aln.fasta -pre PhyloTree -alrt 1000 -bb 1000 -o <<OUTGROUP>>
```
**What is the `bb` and `alrt` options?** In this analysis these options tell IQtree to do for rapid bootstrapping and rapid resampling. Basically, the way that phylogenetic inference works is that the algorithm constructs 1000 trees with random replacement and then searches for patterns of concordance among all replicates. Ideally no matter what kind of resampling you do, your results should be stable. _We will see what this means shortly..._

## Visualizing our tree
We have completed our analysis of phylogenetic inference and it is contained in within the file **PhyloTree.contree**. How can we visualize this analysis? -- The answer is the _ggtree_ a **Tidyverse** style phylo-package!

### Lets get into R!
```
module load gcc/7.1.0
module load openmpi/3.1.4
module load R/4.1.1

R
```
### Lets load the package ggtree
```
library(ggtree, lib.loc = "/project/biol4585j-yey2sn/R/4.1.1/")
library(tidyverse, lib.loc = "/project/biol4585j-yey2sn/R/4.1.1/")
```

### Step 1. Import the tree data into R
```
tree_file <- "./PhyloTree.contree"
tree <- read.tree(tree_file)
tree <- root(tree, outgroup = "Hoolock_hoolock", resolve.root = TRUE)
```
### Step 2. Graph the base topology of the tree
```
ggtree(tree) -> mytree
ggsave(mytree, file = "mytree.pdf")
```
What are we seeing here?

### Step 3. Lets add tip labels
```
ggtree(tree) +
geom_tiplab()  -> mytree
ggsave(mytree, file = "mytree.pdf")
```
**NOTICE**: we are overwriting the file _"mytree.pdf"_. This is done for simplicity's sake


### Step 4. Lets check the bootstraps
```
ggtree(tree) +
geom_tiplab() +
geom_nodelab(aes(x=branch, label=label), vjust=-.5) + 
geom_treescale(x=0.29, y=0)  -> mytree
ggsave(mytree, file = "mytree.pdf")
```
### Step 5. Lets Visualize the DNA sequences along side the tree
```
DNA_sequence <- "./mitochndrial.sequences.aln.fasta"

msaplot(mytree, 
DNA_sequence, 
window=c(120, 200),
offset = 0.15) -> tree_n_DNA

ggsave(tree_n_DNA, 
file = "mytree_and_DNA.pdf",
width = 12,
height = 6)
```
Lets  take a loot at the data, now in full display!
   
## Activity
Today's coding challenge is to use ggplot to annotate clades in the pylogenetic tree we just made. For simplicity use the object names `mytree`.

The `ggtree` library offer the function `geom_strip()` as a tool to annotate trees. The basic structure of the function is `geom_strip("species_1", "species_2", label="Group Name" )`. Use your knowledge of the ggplot structure, using the `+` operator to add labels for "pongo", "gorilla", and "pan".

### Submit your work to the activities folder in Rivanna as YourName.edges.pdf
