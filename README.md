# Protein Function Prediction
***

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

Additionally you will need a version of [Jellyfish](https://github.com/gmarcais/Jellyfish)

### Protein Families in training set
***
The following is the current library of proteins used in our training set, it follows the format

* Family
  * Organism member protein

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

### Clustering
***
Lorem ipsum

### Neural Net
***
Lorem ipsum
