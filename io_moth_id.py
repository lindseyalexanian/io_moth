#!/usr/bin/env python3
# io_moth_id.py

"""This script, meant for teaching, is for printing 
the id of the given fasta file."""

from Bio import SeqIO
import re

infile = "io_moth.fasta"

for record in SeqIO.parse(infile, 'fasta'):
    print(record.id)
