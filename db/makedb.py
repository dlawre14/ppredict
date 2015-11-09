#should be called once
import sqlite3

conn = sqlite3.connect('prot.db')
c = conn.cursor()

c.execute('CREATE TABLE protein (proid integer primary key, name VARCHAR(200), path VARCHAR(200))')
c.execute('CREATE TABLE tags (tagid integer primary key, name VARCHAR(200))')
c.execute('CREATE TABLE ptag (proid,tagid)')

conn.commit()
conn.close()
