#entry point for all protein programs

import argparse
from clustering.kmercluster import kmercluster
from clustering.blastcluster import blastcluster

#Function here

if __name__ == '__main__':
  parser = argparse.ArgumentParser(description='Protein function predictor')
  parser.add_argument('-v', '--visual', action='store_true', help='display visual network with kivy')
  parser.add_argument('-jf', '--jellyfish', help='path to jellyfish exectuable if not in path', default='jellyfish')
  parser.add_argument('-kmer', help='length of kmers to form if clustering')
  parser.add_argument('-m', '--mode', help='mode of analysis, options: kmercluster, blastcluster, kmernetwork, blastnetwork')
  parser.add_argument('-q', '--query', help='query fasta file for classification')

  args = parser.parse_args()

  if args.mode == 'kmercluster':
      print 'Beginning clustering algorithm by kmers...'
      clust = kmercluster()
      clust.train()
  elif args.mode == 'blastcluster':
      print 'Beginning clustering algorithm using blast...'
      clust = blastcluster()
      clust.train()
      print clust.classify(args.query)
