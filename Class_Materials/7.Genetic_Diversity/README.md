# Calculating Genetic Diversity in Populations

Genetic diversity is a fundamental concept in evolutionary genomics. Genetic diversity is represents the amount of genetic variation contained within population. Generally speaking, high levels of genetic diversity is considered to be beneficial for species because it may allow for rapid adaptation to take place.  Conversely, low levels of genetic diversity are often associated with "bad evolutionary outcomes" such as inbreeding depression or population collapse. Today, we will learn how to estimate various estimators of genetic diversity using genomic data.

## Assumptions of neutrality and nucleotide diversity
One thing is to measure genetic diversity. Something entirely different is to assess whether any give amount of genetic variation seen in a species or population is "expected" vs. "unusually high" or "unusually low". To this end it is key to understand what are the expectations at play. 

### The neutral and coalescent theories build null models in evolution
Introduced by Motoo Kimura, Tomokho Otha, Jack Lester King and Thomas H. Jukes in the late 1960s and 1970s, the **The neutral theory of molecular evolution** creates a theoretical framework positing that most mutations that arise in genome are _effectively neutral_. While this may sounds a bit trivial to us today, the idea ran counter to the dominant idea of the day that all mutations always experience some form of natural selection, either positive (_selected for_) or negative (_selected against_). Instead, the theory argues that while positive and negatively selected mutations do occur, they are rare, and most mutations _do **effectively** nothing_ to phenotypes. While today we have a more nuanced understanding of the concept of neutrality and _neutral mutations_ in general, the general ideas of the neutral theory, combined with other important theories such as **coalescent theory** (a theory describing how lineages converge in time)  provide a very useful null model in evolutionary biology.

### What is nucleotide diversity?
Under the core assumptions of the neutral and coalescent theories, all species will naturally enter neutral mutations at a rate (![eq ](https://latex.codecogs.com/gif.latex?\large&space;\color{Magenta}\mu)). Where ![eq ](https://latex.codecogs.com/gif.latex?\large&space;\color{Magenta}\mu) is the mutation rate of a given species. In addition to this, the rate at which this mutations accumulate in populations is also a function of how many individuals reproduce in the population (the _effective population size_, or ![eq ](https://latex.codecogs.com/gif.latex?\large&space;\color{Magenta}N_e)). Based on these two parameters we can infer what is the expected amount of neutral genetic variation that should accumulate within a population of a given species. Mathematically, we can express this as:

![eq 1 ](https://latex.codecogs.com/gif.latex?\large&space;\color{Magenta}\theta=4N_e\mu) 


It turns out, that it is very difficult to accurately estimate ![eq ](https://latex.codecogs.com/gif.latex?\large&space;\color{Magenta}\mu) and ![eq ](https://latex.codecogs.com/gif.latex?\large&space;\color{Magenta}N_e) for any given species. Instead, what we can do is to calculate an estimator of ![eq ](https://latex.codecogs.com/gif.latex?\large&space;\color{Magenta}\theta). One of the most widely used estimations of theta is **Nucleotide diversity**, or![eq ](https://latex.codecogs.com/gif.latex?\large&space;\color{Magenta}\pi).  Unlike ![eq ](https://latex.codecogs.com/gif.latex?\large&space;\color{Magenta}\theta) which requires knowledge of population-level or species-level parameters, ![eq ](https://latex.codecogs.com/gif.latex?\large&space;\color{Magenta}\pi) can be estimated directly from DNA data as:

![eq ](https://latex.codecogs.com/gif.latex?\large&space;\color{Magenta}\pi=\frac{n}{n-1}\sum_{ij}x_ix_j\pi_{ij}) 

Do not fret! That long formula is just the mathematical notation of saying, more or less, ![eq ](https://latex.codecogs.com/gif.latex?\large&space;\color{Magenta}\pi) "compare all pairwise differences among genetic loci". In practice, ![eq ](https://latex.codecogs.com/gif.latex?\large&space;\color{Magenta}\pi) is an estimator bound between 0 and 1 that is estimated by comparing genomic loci across multiple individuals in a population or species. Accordingly, ![eq ](https://latex.codecogs.com/gif.latex?\large&space;\color{Magenta}\pi) indicates that all individuals have the same nucleotide at that position and this genetic variation is low. ![eq ](https://latex.codecogs.com/gif.latex?\large&space;\color{Magenta}\pi) indicates that genetic variation at that given position is very high. It is important to know that ![eq ](https://latex.codecogs.com/gif.latex?\large&space;\color{Magenta}\pi) can be estimated per site, per genomic window, or per entire genome. Most interestingly, the levels of diversity also vary across the tree of life. Lets explore this briefly by [discussing Romiguier et al](https://doi.org/10.1038/nature13685)

## Estimating ![eq ](https://latex.codecogs.com/gif.latex?\large&space;\color{Magenta}\pi) in populations
Now, as I promised at the beginning of the class, we are not going to do any paper math, instead we are going to learn how to ask the computer to do these calculations for us. 

### Obtaining the data for this practicum
```
cp /project/biol4585j-yey2sn/Files/Day_6/DGRP2_freeze2.2L.flt.thin.recode.vcf ./
```

### Loading the required programs 
```
module load vcftools
```
Check out the manual at: https://vcftools.github.io/man_latest.html

### Run vcftools on the data to estimate ![eq ](https://latex.codecogs.com/gif.latex?\large&space;\color{Magenta}\pi)
```
#run vcftools to estimate pi
vcftools --vcf DGRP2_freeze2.2L.flt.thin.recode.vcf \
--window-pi 50000 \
--window-pi-step 50000 \
--out Calculate_pi
```

Lets look over the results

## Departures from neutrality and Tajima's D

It is important to realize that ![eq ](https://latex.codecogs.com/gif.latex?\large&space;\color{Magenta}\pi) is what we call a descriptive summary statistic. This is, a value that summarizes some aspect of genetic variation in populations. However, this is just a _description_ of the population and we have not performed a statistical test to determine whether our observe values of ![eq ](https://latex.codecogs.com/gif.latex?\large&space;\color{Magenta}\pi) are higher or lower than the null expectation.  In order to make such a test, we need to introduce a new _test_ statistic called Tajima's $D$. 

### Tajima's D
The basis of this test is to compare two different estimators of ![eq ](https://latex.codecogs.com/gif.latex?\large&space;\color{Magenta}\theta), one of the is ![eq ](https://latex.codecogs.com/gif.latex?\large&space;\color{Magenta}\pi) a summary statistic which, as we just learned, measures genetic variation (mostly common mutation). The other is an estimator of ![eq ](https://latex.codecogs.com/gif.latex?\large&space;\color{Magenta}\theta) which is very sensitive to rare mutations (we wont dive much deeper into the math of $D$ due to time constrains). The test produces values near 0, greater than 0, and less than 0. Each of these have a different interpretation. 

| Value of D 	| Driver                                           	| Neutral Interpretation                         	|
|--------------	|--------------------------------------------------	|------------------------------------------------	|
| D = 0      	| Observed variation similar to expected variation 	| Population evolving as per the null            	|
| D < 0      	| Rare alleles abundant                            	| population expansion after a recent bottleneck 	|
| D > 0      	| Rare alleles scarce                              	| sudden population contraction                  	|

Lets chat about this estimator

### Run vcftools on the data to estimate D
```
vcftools --vcf DGRP2_freeze2.2L.flt.thin.recode.vcf \
--TajimaD 50000 \
--out Calculate_D
```
Lets look over the results


## Activity << 30 points >>: Plot ![eq ](https://latex.codecogs.com/gif.latex?\large&space;\color{Magenta}\pi) and D in R 

Upload to R the two outputs from Pi and Taj. D. -- Once uploaded join the two datasets into one single datatset, using the left_join() function. You will have to create a shared column like this:

```
library(tidyverse, ...add correct lib.loc)
library(data.table, ...add correct lib.loc)

taj <- fread("Calculate_D.Tajima.D")
taj %>% mutate(POS = BIN_START) -> taj_share
pi <- fread("Calculate_pi.windowed.pi")
pi %>% mutate(POS = BIN_START-1) -> pi_share

left_join(taj_share[,c("POS","TajimaD")], pi_share[,c("POS","PI")], by = "POS") -> join_pi_taj

```

### Upload a document to Collab with the following Information. Include your name and the name of your partners. All margins must be 0.5 inches. ALL GRAPHS must be clearly labeled.

1. Is there a correlation between these two variables? you can test correlations in R using the function cor.test(). Is the correlation statistically significant? Report estimates and p-values. [3 pts]

3. What are the mean values for pi and Tajima's D [3 pts]

4. Include two histogram, one for pi and another D (optional: you could test advanced skills by plotting them as a joint object!) [3 pts]. 

5. Plots for pi and D using the outputs of the analyses above. The x-axis should be the the nucleotide position and the y-axis should be statistic itself. Choose the appropiate *geom_* art to accomplish this task? (consult your partner for this). [6 pts]

6. Mutate a new variable to your dataset (call it "D_win") using the "case_when()" function which creates two categories of genomic window: a.when D <0, or b.when D >0. Using your knowledge of data summarization, report the mean and standard deviation values of pi, as a function of these two categories of Taj. D. [6 pts]

7. Lastly, report the results of a test of whether the mean pi between these two categories of Taj D are statistically different from each other. [9 pts]
