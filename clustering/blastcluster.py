#clustering using blast alignment

from cluster import cluster
from Bio.Blast import NCBIXML
from Bio.Blast.Applications import NcbiblastpCommandline

import StringIO
import sqlite3

class blastcluster(cluster):

  def __init__(self):
    cluster.__init__(self)

  def classify(self, query):
      tags = []

      bestscore = 10000000
      bestid = -1
      for key in self.data:
          score = self.callblast(query, self.data[key])
          if score < bestscore:
              score = bestscore
              bestid = key

      conn = sqlite3.connect('db/prot.db')
      c = conn.cursor()
      c.execute('SELECT * FROM ptag WHERE proid=?',(bestid,))

      for pair in c.fetchall():
          c.execute('SELECT name FROM tags WHERE tagid=?',(pair[1],))
          tags.append(c.fetchall()[0][0])

      conn.close()
      return tags

  def callblast(self, seq1, seq2):
      #seq1, seq2 should be fasta file paths
      #we make evalue huge incase sequences are very far apart

      #TODO: consider changing to check if alignments are in e-value range and return trivial
      #worst case if not
      
      cline = NcbiblastpCommandline(query=seq1, subject=seq2, outfmt=5, evalue=100000000)
      out,err = cline()
      result = NCBIXML.read(StringIO.StringIO(out))

      return result.alignments[0].hsps[0].score
