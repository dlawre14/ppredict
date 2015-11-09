#append an entire directory of fasta files to database with shared tags

import argparse
import subprocess
import os

parser = argparse.ArgumentParser(description='Adds .fasta files to database from a directory')
parser.add_argument('-p','--path',help='directory path')
parser.add_argument('-t','--tags',help='tags to add to database for fasta files in path', nargs='+')

args = parser.parse_args()

for name in os.listdir(args.path):
    subprocess.call(['python', 'dbapp.py', '-p', args.path.rstrip('/') + '/' + name, '-t'] + args.tags) #to be safe whether / is on the end or not
