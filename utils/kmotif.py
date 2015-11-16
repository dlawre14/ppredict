#Finds the most common kmer between two proteins

import argparse
import subprocess
import os #for cleanup

from operator import itemgetter

parser = argparse.ArgumentParser(description='most common kmer')
parser.add_argument('-q','--query',help='query .fasta file')
parser.add_argument('-s','--subject',help='subject .fasta file')
parser.add_argument('-k','--kmerlen',help='length of kmers')

args = parser.parse_args()
