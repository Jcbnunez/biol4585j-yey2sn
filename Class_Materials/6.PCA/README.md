# Principal component analysis in Genomics

## What is PCA
Often in genetics we are interested in learning about the differences between individuals or populations. To achieve this, we normally measure different variables such as phenotypes or genotypes (e.g., abundance of mutations).  When we have only a couple of measurements, for example one, two, or three mutations, we can investigate differences using "traditional" (univariate or bivariate) statistical approaches. However, when we have many many variables this becomes a problem. To solve this issue we must become familar with the term "dimentionality reduction" and with a widely used method known as the principal component analysis (PCA).

### Lets watch a quick review of PCA: [Link to Josh Starmer 5 min Review](https://www.youtube.com/watch?v=HMOI_lkzW08)

## PCAs with genetic data
In today's lecture and practicum we will learn how to build PCAs using two sources of data: genotypes (using VCFs) and allele frequencies (using population files)

# Building PCAs with genotype data (individuals)

## Understanding the input data
As inputs we will use VCF files. The types of files which we generated in our last class. Lets take a moment to recall the type of data contained in VCF files.

### Loading VCF data into R
```
library(vcfR, lib.loc = "/project/biol4585j-yey2sn/R/4.0/")
library(FactoMineR, lib.loc = "/project/biol4585j-yey2sn/R/4.0/")
library(tidyverse, lib.loc = "/project/biol4585j-yey2sn/R/4.0/")
library(data.table, lib.loc = "/project/biol4585j-yey2sn/R/4.0/")

#read the vcf file
read.vcfR("/project/biol4585j-yey2sn/Files/Day_6/DGRP2_freeze2.2L.flt.thin.recode.vcf") -> input_vcf

# transform the vcf input into R data
my_genind <- vcfR2genind(input_vcf)

#Extract genotype data
my_genind@tab %>%
as.data.frame -> vcf_table

#Do an additional filtering step (this is related to the way that R load the data) 
vct_table[,grep(".0", names(vct_table))] -> vcf_table_flt
```
Lets take a look at the output.
```
vcf_table_flt[1:20,1:10]
```
## Generate a PCA object
```
PCA(vcf_table_flt, 
	graph = FALSE,
	scale.unit = F,
	ncp=5 ) -> pca_fig
```

## Plot the graph
```
pca_fig$ind$coord %>%
as.data.frame %>%
ggplot(aes(
x=Dim.1,
y=Dim.2
)) +
geom_point() -> pca_gg_figure

ggsave(pca_gg_figure, file = "pca_gg_figure.pdf")
```
## Lets add some metadata
```
inversion_info = fread("/project/biol4585j-yey2sn/Files/Day_6/inversion.info.txt")
```
Lets explore what this data means

## Lets merge datasets with the "join" commands

```
pca_fig$ind$coord %>%
as.data.frame %>%
mutate(DGRP_line = rownames(.)) %>%
left_join(inversion_info) -> 
pca_fig_with_inv
```
Does inversion status project onto our PCA?
```
pca_fig_with_inv %>%
ggplot(aes(
x=Dim.1,
y=Dim.2,
col = In_2L_t
)) +
geom_point() -> pca_gg_figure_col

ggsave(pca_gg_figure_col, file = "pca_gg_figure_col.pdf")
```

## Visualize the PCA projections given inversion
Box plots
```
pca_fig_with_inv %>%
ggplot(aes(
x=In_2L_t,
y=Dim.1
)) +
geom_boxplot() -> box_plot

ggsave(box_plot, file = "box_plot.pdf")
```
Violin plots
```
pca_fig_with_inv %>%
ggplot(aes(
x=In_2L_t,
y=Dim.1
)) +
geom_violin() -> violin_plot

ggsave(violin_plot, file = "violin_plot.pdf")
```

## Is there a statically significant effect of inversion on Dimension 1?
We can use linear regression and ANOVA to test this hypothesis.

[Linear Regression Review](https://youtu.be/nk2CQITm_eo)
[ANOVA Review](https://www.youtube.com/watch?v=NF5_btOaCig)
```
lm_model <- lm(Dim.1 ~ In_2L_t, data = pca_fig_with_inv)
anova(lm_model)
```
What can we  conclude from this analysis?

# PCA with allele frequencies (populations)
Instead of genotypes, we can use allele frequencies to build our PCAs. Allele frequencies are the the proportion of the genotype counts in populations. For example if there are 50 copies of an allele in a population of 100 diploid individuals the allele frequency is 25%. **Why?!** Because diploids have 2 chromosomes per individual so there are 200 possible chromosomes an allele can inhabit, and since we observe 50, then the allele frequency is:
 
$$50/(100*2) = 50/200 = 25\%$$

Building a PCA from allele frequencies is not that different from the genotype version, we just need to mind the **input data**.

## Input allele frequencies
```
allele_freqs <- load
```
Lest examine this file
```
allele_freqs[1:10,1:10]
```
What is different from the genotype version?

## Build the PCA
```
PCA(allele_freqs, 
	graph = FALSE,
	scale.unit = F,
	ncp=5 ) -> pca_fig_pool
```

## Plot the PCA
```
pca_fig_pool$ind$coord %>%
as.data.frame %>%
ggplot(aes(
x=Dim.1,
y=Dim.2
)) +
geom_point() -> pca_gg_figure_pool

ggsave(pca_gg_figure_pool, file = "pca_gg_figure_pool.pdf")
```
What patterns emerge in the PCA?

# Activity
The data we used to build the allele frequency PCA was collected in various seasons (spring, fall) across various years. We can incorporate this information into our PCA object using the techniques we learned above

```
metadata_allele_freqs <- fread("/project/biol4585j-yey2sn/Files/Day_6/allele_freq_metadata.txt")

pca_fig_pool$ind$coord %>%
as.data.frame %>%
mutate(sampleId = rownames(.)) %>%  ##** see note
left_join(metadata_allele_freqs) -> 
pca_gg_figure_pool_with_meta

##Note --> We have to call it "sampleId" so that both objects have a common column
```

Using linear models and ANOVAs, can you determine if either year, or, season play a role in PCA signals of Dimensions 1 and 2? Provide your answer in the Collab portal.

