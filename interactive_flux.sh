#!/bin/bash
qsub \
-I \
-N interactive_job \
-M thealex@umich.edu \
-m abe \
-A mdatascienceteam_flux \
-q flux \
-l qos=preempt,nodes=4:ppn=16,pmem=4gb,walltime=00:04:00:00 \
-j oe \
-V \
-d "/scratch/mdatascienceteam_flux/thealex/"
