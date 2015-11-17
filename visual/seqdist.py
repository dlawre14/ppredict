#use blast to generate a graph of sequences and distances

import sqlite3
import graphviz

from Bio.Blast import NCBIXML
from Bio.Blast.Applications import NcbiblastpCommandline

import StringIO

def seqdist(seq1,seq2):
    cline = NcbiblastpCommandline(query=seq1, subject=seq2, outfmt=5, evalue=100000000)
    out,err = cline()
    result = NCBIXML.read(StringIO.StringIO(out))

    if len(result.alignments) == 0:
        return -1

    return result.alignments[0].hsps[0].expect

graph = graphviz.Graph('Distance between all sequences', engine='neato')

conn = sqlite3.connect('db/prot.db')
c = conn.cursor()

c.execute('SELECT * FROM protein')
records = c.fetchall()

dist = {}
paths = {}

for record in records:
    graph.node(record[1])
    dist[record[1]] = {}
    paths[record[1]] = record[2]

for key in dist:
    for record in records:
        #print 'Comparing ' + key + ' and ' + record[1]
        #print 'Distance is: ' + str(seqdist(paths[key],paths[record[1]]))
        dist[key][record[1]] = seqdist(paths[key],paths[record[1]])

for key in dist:
    val = 100
    closest = None
    for k in dist[key]:
        if dist[key][k] > 0 and dist[key][k] < val:
            val = dist[key][k]
            closest = k
    val = int(max(10,min(val*150,30)))
    print 'Adding edge from ' + key + ' to ' + k + ' with length ' + str(val)
    graph.edge(key,k,len=str(val),label=str(val)) #TODO: figure out why nothing is drawing in

graph.render('dist.gv')
