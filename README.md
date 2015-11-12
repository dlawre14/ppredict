# Protein Function Prediction

### Introduction
***
A package for determining protein function from a given amino acid sequence. This package requires BioPython for some of its scripts.

### Dependencies
***
This package runs on Python 2.7.x and requires the following libraries to work:

* [Cython](https://github.com/cython/cython)
* [Numpy](https://github.com/numpy/numpy)
* [BioPython](https://github.com/biopython/biopython)
* [Kivy](https://github.com/kivy/kivy)

Note: most of these can be acquried with `pip`

Additionally you will need a version of [Jellyfish](https://github.com/gmarcais/Jellyfish) if using kmer/ngram style analysis.

You will need [Blast+](https://blast.ncbi.nlm.nih.gov/Blast.cgi?PAGE_TYPE=BlastDocs&DOC_TYPE=Download) if doing alignment based analysis.

### Protein Families in training set
***
The following is the current library of proteins used in our training set, it follows the format

* **Family**
  * **Organism member protein**

***

* Hemoglobin (subunit beta)
  * Homo sapiencs (Human)
  * Canis lupus (Wolf/Dog)
  * Felis catus (Domestic Cat)
  * Mus musculus (House Mouse)
  * Sus scrofa (Pig)
  * Oryctolagus cuniculus (European Rabbit)
* IGFBP1 (insulin-like growth factor-binding)
  * Homo sapiencs (Human)
  * Canis lupus (Wolf/Dog)
  * Felis catus (Domestic Cat)
  * Mus musculus (House Mouse)
  * Sus scrofa (Pig)
  * Oryctolagus cuniculus (European Rabbit)

Note: additional training data may be specified at runtime

### Database
***
This program comes with a predefined `sqlite3` database that can be found in `db/pro.db` This database is used to associate all .fasta protein files with different tags.

For easiest viewing, please run `dbdisp.py` which will print out the database in list readable format.

The database contains the following structure:

Table name | Column names
---------- | ------------
protein    | proid (primary key, auto increment), name, path
tags       | tagid (primary key, auto increment), name
ptag       | proid, tagid

Writing to this database is facilitated by `dbapp.py` which can be run by:

`python dbapp.py -p <fastafilepath> -t <space delimited tags>`

For easier writing we also include 'dirapp.py' which takes an entire directory of fasta files and writes them all, it is run by:

`python dirapp.py -p <directory> -t <space delimited tags>`

Please note that all append `.py` files will only make writes that are novel, this means that `dirapp.py` is safe to use on a directory it is already run on. For this reason, we recommend only accessing the database through these .py files

If you wish to make a fresh database file this can be done using `db/makedb.py`

### Clustering
***
Lorem ipsum

### Neural Net
***
Lorem ipsum
