#utility script for adding .fasta protein files to the database

import argparse
import sqlite3
import re

parser = argparse.ArgumentParser(description='Adds .fasta file paths to database')
parser.add_argument('-p','--path',help='.fasta file path')
parser.add_argument('-t','--tags',help='tags to add to database for this fasta file', nargs='+')

args = parser.parse_args()

#open db and write
conn = sqlite3.connect('db/prot.db')
c = conn.cursor()

name = args.path.split('/')
name = (name[len(name)-2] +'_'+name[len(name)-1])[:-6]

t = (name,args.path)

c.execute('SELECT name from protein where name=?', (name,))

if not c.fetchall():
    c.execute('INSERT INTO protein VALUES (NULL,?,?)', t)
else:
    pass #entry is in db

for tag in args.tags:
    c.execute('SELECT name from tags where name=?', (tag,))
    if not c.fetchall():
        c.execute('INSERT INTO tags VALUES (NULL,?)', (tag,))
    else:
        pass #tag is in db

#associated proid with tagid
c.execute('SELECT proid from protein where name=?', (name,))
proid = c.fetchall()[0][0]

for tag in args.tags:
    c.execute('SELECT tagid from tags where name=?', (tag,))
    tagid = c.fetchall()[0][0]

    c.execute('SELECT proid,tagid from ptag where proid=? and tagid=?', (proid, tagid))
    if not c.fetchall():
        c.execute('INSERT INTO ptag VALUES (?,?)', (proid, tagid))
    else:
        pass #id pair has been added

conn.commit()
conn.close()
