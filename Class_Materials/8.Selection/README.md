# Estimating selection in Population

Our last Lecture/Practicum of the class will cover detecting natural selection on populations. Natural selection is a process which has fascinated biologists since Darwin. The core idea behind natural selection is that individuals with traits that increase reproduction or survival (i.e., fitness) of individuals will increase in frequency of populations overtime, thus increasing the fitness of populations. Genetics  enters the picture when answering a preceding question: _how are these traits encoded by the cell and passed on to offspring_?

### How does selection manifest at the level of DNA?
An important clarification to keep in mind is that natural selection acts directly on the trait. Yet,  traits are **encoded** by DNA. As such there is a connection of selection and DNA. Basically, whenever a new mutation arises that produces a benefit in the trait, that mutation will increase in frequency as the  trait itself increases in frequency.

This leads us to an interesting connection with our previous lecture: **how common is natural selection?**, or, from the perspective of DNA, **how common are beneficial mutations?** 

![!DFE](https://upload.wikimedia.org/wikipedia/commons/thumb/f/f9/DFE_in_VSV.png/360px-DFE_in_VSV.png)
In the graph above, A fitness of zero, less than one, one, more than one, respectively, indicates that mutations are lethal, deleterious, neutral, and advantageous. These observations provide us with three interesting insights about evolutionary theory:

1. The neutral theory is not a real reflection of nature -- (Yet, is is a useful null model).
2. Most non-lethal mutations are weakly deleterious, thus people have advocated towards a _Nearly Neutral Theory_.
3. Beneficial mutations are rare.

Based on this observation we can make a prediction: "mutations under selection should be rare within genomes"    

### The time scales of selection: long and short evolutionary times

* We will cover these concepts through a discussion of [Vitti et al.](https://www.annualreviews.org/doi/abs/10.1146/annurev-genet-111212-133526)
* We will close our class discussion with a discussion of [Nielsen et al](https://www.annualreviews.org/doi/abs/10.1146/annurev.genet.39.073003.112420)

## Practicum: Detecting ancient selection with MKT
In their paper, [Rand and Kann](https://academic.oup.com/mbe/article/13/6/735/1023445) collected polymorphism and divergence data from a couple species for the mitochondrial gene ND3. Their results are as follows (each species was polarized relative to an out-group):

| Species 	| FN 	| FS 	| PN 	| PS 	|
|---------	|----	|----	|----	|----	|
| Fly     	| 2  	| 13 	| 1  	| 5  	|
| Human   	| 2  	| 23 	| 11 	| 34 	|
| Mouse   	| 4  	| 31 	| 8  	| 10 	|

Lets translate this data into R:

```
Gene_Matrix <-
matrix(c("FN", "PN", "FS", "PS"),
       nrow = 2,
       dimnames = list(Consequence = c("Fix", "Poly"),
                       Change = c("NSYN", "SYN")))
```
Now lets put some numbers into it:
```
Gene_Matrix <-
matrix(c(4, 8, 31, 10),
       nrow = 2,
       dimnames = list(Consequence = c("Fix", "Poly"),
                       Change = c("NSYN", "SYN")))
```
Run the test
```
fisher.test(Gene_Matrix)
```
## Activity: 

Do Mouse or Human show significant signatures of ancient selection?

## Practicum: Detecting recent selection by uncovering selective sweeps in genomes

The action of recent selection in genomes has the capacity to alter the levels of nucleotide diversity, ![eq ](https://latex.codecogs.com/gif.latex?\large&space;\color{Magenta}\pi), and Tajima's D in populations. What is the difference between the neutral accumulation of mutations (which normally drives ![eq ](https://latex.codecogs.com/gif.latex?\large&space;\color{Magenta}\pi)) and selection? The answer is that selection acts regionally! Lets explore this process

### Explore nucleotide diversity and Tajimas D in a genomes which recently underwent selection:

First, lets copy the vcf file

```
cp /project/biol4585j-yey2sn/Files/Day_8/hardsweep.vcf ./
```

Now lets, estimate pi
```
vcftools --vcf hardsweep.vcf \
--window-pi 50000 \
--window-pi-step 50000 \
--out Calculate_pi_pos_sel
```

Estimate Tajimas'D
```
vcftools --vcf hardsweep.vcf \
--TajimaD 50000 \
--out Calculate_taj_D_pos_sel
```

### Lets graph and discuss the results 


