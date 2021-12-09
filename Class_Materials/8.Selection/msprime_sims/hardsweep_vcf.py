import numpy as np
import msprime
import IPython
from IPython.display import SVG
import os
import math
import sys

#set working directory. same as setwd() except it doesn't like ~/
os.chdir("./")

#write vcf with given pre-determined scenario

#set up variables
popA_size = 15_000 #population size individuals are drawn from, held constant
sample_num=100 #individuals sampled for writing vcf
mu=2.1e-9 #mutation rate
rr=0.50e-7 #recombination rate
L=1e6 #length of genome
pl=2 #ploidy
sel=0.20 #selection coefficient of allele
dt=1e-6 #dt is the small increment of time for stepping through the sweep phase of the model. a good rule of thumb is for this to be approximately 1/40N or smaller.

#write demography. for a more complex example, see below
demography = msprime.Demography()
demography.add_population(name="A", initial_size=popA_size)

'''
more complex example demography with 3 populations splitting at time time_split in the past
demography = msprime.Demography()
demography.add_population(name="A", initial_size=popA_size)
demography.add_population(name="B", initial_size=popB_size)
demography.add_population(name="C", initial_size=popC_size)
demography.add_population_split(time=time_split, derived=["A", "B"], ancestral="C") #this makes A and B cleave off from C at a predetermined timepoint

#choose sample size
sample_set_1 = msprime.SampleSet(sample_pop1, population= "A", ploidy=2)
sample_set_2 = msprime.SampleSet(sample_pop2, population= "B", ploidy=2)
samples=[sample_set_1,sample_set_2]

see https://tskit.dev/msprime/docs/stable/demography.html for more details and choices
'''

#set up sweep model
#originally from API tutorial: https://tskit.dev/msprime/docs/stable/ancestry.html#selective-sweeps
sweep_model = msprime.SweepGenicSelection(
    position=L / 2,  # middle of chrom
    start_frequency=1.0 / (2 * popA_size),
    end_frequency=1.0 - (1.0 / (2 * popA_size)),
    s=sel,
    dt=dt,
)

#choose sample size
sample = [msprime.SampleSet(sample_num, population= "A", ploidy=pl)] #randomly samples from population "A"

#simulate demographic history
ts = msprime.sim_ancestry(samples=sample, 
                          demography=demography, 
                          sequence_length=L, 
                          recombination_rate=rr, 
                          model=[sweep_model, msprime.StandardCoalescent()], # aka hudson, which incorporates recombination. see https://tskit.dev/msprime/docs/stable/ancestry.html for more
                          ploidy=pl)
                          
#simulate random mutations 
mts = msprime.sim_mutations(ts, rate=mu)

#writes vcf to working directory
with open("./hardsweep.vcf", "w") as vcf_file:
                      mts.write_vcf(vcf_file)