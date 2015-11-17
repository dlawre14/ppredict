#simple aa count classifier

from Bio import SeqIO
import sqlite3
import argparse

from math import log

def aafreq(seqpath):
    seq = str(SeqIO.read(seqpath, 'fasta').seq)
    freq = {}

    total = 20 #since we're going to smooth
    for aa in seq:
        freq[aa.lower()] = freq.get(aa.lower(),0) + 1
        total += 1

    allaa = "ACDEFGHIKLMNPQRSTVWY".lower()
    for aa in allaa:
        freq[aa] = float(freq.get(aa,1)) / total

    return freq

def kl(p,q): #Kullback-Leibler Divergence
    return sum(p[x] + log(p[x]/q[x]) for x in p)

def jsd(p,q): #Jensen-Shannon Divergence of two probability distributions
  #TODO: fix
  avg = {x:((p[x] + q[x])/2) for x in p}
  return (kl(p,avg) + kl(q,avg))/2

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Classify target protein using relative amino acid frequency')
    parser.add_argument('-q','--query',help='the query fasta path')

    args = parser.parse_args()

    conn = sqlite3.connect('db/prot.db')
    c = conn.cursor()

    c.execute('SELECT * FROM protein')
    proteins = c.fetchall()

    ppaths = {}
    for entry in proteins:
        ppaths[entry[0]] = entry[2] #key by id

    aafrequency = {}
    for key in ppaths:
        aafrequency[key] = aafreq(ppaths[key])

    queryfreq = aafreq(args.query)

    for key in aafrequency:
        print jsd(aafrequency[key],queryfreq)
