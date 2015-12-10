#take a list of proteins and accession numbers and run getseq on each

import os
import subprocess
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser('Automated sequence fetch pipeline')
    parser.add_argument('-f','--file',help='file of proteins to fetch')
    args = parser.parse_args()

    with open(args.file,'r') as f:
        for line in f:
            line = line.rstrip('\n').split()

            try:
                os.mkdir('proteins/'+line[0])
            except OSError as e:
                print 'Directory ' + 'proteins/'+line[0] + ' already exists.'
                print 'Was this program run partially...?'

            print 'Fetching ' + str(line) + ' ...'
            out = 'proteins/'+line[0]

            subprocess.call(['python','utils/getseq.py','-an',line[1],'-o',out,'-l','orglist.txt'])

    print 'All proteins fecthed'
