#display tables

import sqlite3

conn = sqlite3.connect('db/prot.db')
c = conn.cursor()

c.execute('select * from protein')
print '---- protein ----'
print c.fetchall()
print

c.execute('select * from tags')
print '---- tags ----'
print c.fetchall()
print

c.execute('select * from ptag')
print '---- ptags ----'
print c.fetchall()
print

conn.close()
