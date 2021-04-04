#Import packages
import numpy as np
import Bio
from Bio import SeqIO


#FASTA file
#FASTA sequence for PSPa protein: Trial 1
#display directionality and genetic context (neighbors) of this gene

for seq_record in SeqIO.parse("pspa_sequence_trial1.fasta", "fasta"):
    print(seq_record.id)
    print(repr(seq_record.seq))
    print(len(seq_record))
