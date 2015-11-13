#clustering algorithm for protein classification, uses kmers for classifying

from cluster import cluster

class kmercluster(cluster):

    def __init__(self):
        cluster.__init__(self)

    def calljf(self, seq1, seq2, jfpath, kmersize):
      #call jellyfish on seq1 and seq2 then compare their kmers
      pass
