import argparse
from Bio import SeqIO

def kmers(seqpath,length):
    seq = SeqIO.read(seqpath,'fasta').seq

    kmers = {}
    for i in range(len(seq) - length):
        kmers[seq[i:i+length]] = kmers.get(seq[i:i+length],0) + 1

    return kmers

def dump(kmers):
    #dumps a dictionary of kmers
    for key in kmers:
        print key + '\t' + str(kmers[key])

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='generate protein kmers')
    parser.add_argument('-f','--file',help='fasta file to process')
    parser.add_argument('-n','--klen',help='length of kmers')

    args = parser.parse_args()

    dump(kmers(args.file, int(args.klen)))
