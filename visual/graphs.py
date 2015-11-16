#file for making graphviz graphs in python

from graphviz import Graph #these are undirected
import sqlite3

#open up the db, pull everything

conn = sqlite3.connect('../db/prot.db')
c = conn.cursor()

c.execute('SELECT * from protein')
proids = {x[0]:x[1] for x in c.fetchall()}

c.execute('SELECT * from tags')
tagids = {x[0]:x[1] for x in c.fetchall()}

c.execute('SELECT * from ptag')
matches = c.fetchall()

graph = Graph('All protein tags', engine='neato')

for key in proids:
    graph.node(proids[key])
for key in tagids:
    graph.node(tagids[key])

for x,y in matches:
    graph.edge(proids[x],tagids[y],len="10.0")

graph.render('tag.gv')

conn.close()
