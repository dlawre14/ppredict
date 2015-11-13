#generic cluster class

import sqlite3

class cluster:

    def __init__(self):
        self.data = None

    def train(self):
        #read in proteins to data as a dict of proid : path
        self.data = {}

        conn = sqlite3.connect('db/prot.db')
        c = conn.cursor()
        c.execute('SELECT * FROM protein')

        proteins = c.fetchall()

        conn.close()

        self.data = {x[0]:x[2] for x in proteins} #keyed by proid
