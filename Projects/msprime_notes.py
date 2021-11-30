#This is a basic demographic model in msPrime

#module load anaconda/2020.11-py3.8
#source activate msprime_env

import numpy as np
import msprime
import IPython
from IPython.display import SVG
import os
import math
import sys
import allel

#setting current working directory
os.chdir("./")

#write vcf with given pre-determined scenario

#set up variables
mu=2.8e-8 #mutation rate
seq_len=500000

#var = argv[1]
var = str('Neutral_100k')

#write demography
demography = msprime.Demography.island_model([10000]*5,0.5)
#demography.set_migration_rate(source=0, dest=1, rate=0.3)
#demography.set_migration_rate(source=1, dest=2, rate=0.8)

ts = msprime.sim_ancestry(
    samples={0: 100, 1: 100, 2: 100, 3: 100, 4: 100},
    demography=demography,
    ploidy=2,
    random_seed=12345,
    sequence_length=seq_len)
    

ts

#simulate random mutations during history
mts = msprime.sim_mutations(ts, rate=mu)

#writes vcf
with open("%s.vcf" % var, "w") as vcf_file:
                      mts.write_vcf(vcf_file)
                      
