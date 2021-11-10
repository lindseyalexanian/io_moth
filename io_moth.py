#!/usr/bin/env python3
# io_moth.py

"""This script is for teaching a young biology enthusiast and student about
the basics of Biopython. This prints the sequence record of the genome
of the io moth (automeris io), the organism requested by the student. It also
transcribes and translates the DNA."""


from Bio.Seq import Seq
import re
from Bio import SeqIO


# open sesame
with open("io_moth.fasta") as infile:
    for record in SeqIO.parse(infile, "fasta"):
        print(record)
        dna = (record.seq)
        # transcription!
        rna = dna.transcribe()
        # only groups of 3!
        orf = re.search('AUG([AUGC]{3})+?(UAA|UAG|UGA)', str(rna)).group()
        # change from string to BioSeq, else translation will fail
        seq_orf = Seq(orf)
        protein = seq_orf.translate()
        # some formatting
        print('\n')
        # print protein sequence!
        print("The protein sequence is: ", protein)


