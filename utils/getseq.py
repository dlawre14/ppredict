#Accepts an accession number, returns a protein sequence

from Bio import SeqIO
from Bio import Entrez
from Bio.Blast import NCBIWWW,NCBIXML
import argparse
from time import sleep

parser = argparse.ArgumentParser(description='Get aa sequence from accession number')
parser.add_argument('-an', '--accession', help='the accession number for the sequence')
parser.add_argument('-o', '--output', help='the outputdirectory')
parser.add_argument('-l', '--orglist', help='organism list')
args = parser.parse_args()

#Get original sequence
Entrez.email = 'dlawre14@slu.edu'

handle = Entrez.efetch(db="protein", id=args.accession, retmode='xml')
records = Entrez.read(handle)

name = records[0]['GBSeq_organism'].lower().replace(' ','_')

with open(args.output+name+'.fasta', 'w') as f:
  f.write('>gi|' + args.accession + '|' + records[0]['GBSeq_definition'] + '\n' + records[0]['GBSeq_sequence'])

#Run blast on organism list to find orthologs
query = args.output+name+'.fasta'
seq = SeqIO.read(query,'fasta')

with open(args.orglist, 'r') as f:
    for line in f:
        line = line.rstrip('\n')
        result = NCBIWWW.qblast('blastp', 'nr', seq.seq, entrez_query=line+'[Organism]')
        records = NCBIXML.parse(result)

        accno = None
        for record in records:
            accno = record.alignments[0].accession

        handle = Entrez.efetch(db='protein', id=accno, retmode='xml')
        records = Entrez.read(handle)

        print 'Writing to: ' + '/'.join(query.split('/')[0:-1]) + '/' + line.lower().replace(' ','_') + '.fasta'

        with open('/'.join(query.split('/')[0:-1]) + '/' + line.lower().replace(' ','_') + '.fasta', 'w') as o:
            o.write('>gi|' + accno + '|' + records[0]['GBSeq_definition'] + '\n' + records[0]['GBSeq_sequence'])
