# RIBOFLOW

This is [riboflow](https://test.pypi.org/project/riboflow/), a python package for the classification of putative riboswitch sequences into one of 24 classes with > 99% accuracy. It is based on a [tensorflow](https://www.tensorflow.org) deep learning model. ``riboflow`` has been tested using ``Python 3.5.2``.

Installation
------------

The easiest way to install the package is via ``pip``::

    $ pip install -i https://test.pypi.org/simple/ riboflow==0.13.dev0
    
Dependencies:
    
    numpy==1.14.5
    tensorflow==1.8.0   
    keras==2.2.0 
    
A trained ``Bi-directional Recurent Neural Network Model`` is integrated into the ``riboflow`` package (and installed automatically with the ``pip installation``). 

Note that the source code to generate the ``Bi-directional Recurent Neural Network Model`` is available. The git repository [Riboswitch Classification](https://github.com/RiboswitchClassifier/RiboswitchClassification) can be forked to generate a new model.

Usage
-------------------

Once you have successfully installed `riboflow` using `pip install riboflow`, please follow the steps to predict the class of a new riboswitch sequence:

**1. Import the package**:

  - Inside the python shell or in your python file::

        > import riboflow

**2. Construct an array of riboswitch sequences**:

        > # Input Sequence
        > sequences = [
            "TTTTTTTTGCAGGGGTGGCTTTAGGGCCTGAGAAGATACCCATTGAACCTGACCTGGCTAAAACCAGGGTAGGGAATTGCAGAAATGTCCTCATT",
            "CTCTTATCCAGAGCGGTAGAGGGACTGGCCCTTTGAAGCCCAGCAACCTACACTTTTTGTTGTAAGGTGCTAACCTGAGCAGGAGAAATCCTGACCGATGAGAG",
            "CCACGATAAAGGTAAACCCTGAGTGATCAGGGGGCGCAAAGTGTAGGATCTCAGCTCAAGTCATCTCCAGATAAGAAATATCAGAAAGATAGCCTTACTGCCGAA"
          ]

**3a. Predict the class for each riboswitch sequence**:

        > # Predict the most probable riboswitch class of each sequence
        > riboflow.predict(sequences, "predict_class")
        
**3b. Predict a vector of class probabilities for each riboswitch sequence**:

        > # Predict probabilty of each riboswitch class associated with each sequence 
        > riboflow.predict(sequences, "predict_prob")

Package Structure
-----

    .
    ├── build                       # Buildout project configuration
    ├── dist                        # Consists of  .whl and .tar package files
    ├── riboflow                    # Package Directory
    │   ├── __init__.py             # main file
    │   ├── rnn_24_model.h5         # Bi-directional Recurent Neural Network Model
    ├── riboflow.egg-info           # Egg information of the project
    ├── LICENSE                     # License
    ├── MANIFEST.in                 # To include the Bi-directional Recurent Neural Network Model within the package
    ├── README.md                   # Package description
    └── setup.py                    # Package metadata


References for pypi package development
----------

  * PyPI Page: http://pypi.python.org/pypi/python_boilerplate_template
  * Github: https://github.com/konstantint/python-boilerplate-template
  * Cookiecutter version: https://github.com/konstantint/cookiecutter-python-boilerplate
  * Blog post: http://fouryears.eu/2014/03/19/structure-of-a-python-project/
  * Useful reading
     - http://www.jeffknupp.com/blog/2013/08/16/open-sourcing-a-python-project-the-right-way/
  * Related projects: `[1] <https://pypi.python.org/pypi/modern-package-template>`_, `[2] <https://pypi.python.org/pypi/python-package-template/>`_, `[3] <https://github.com/vital-fadeev/python-package-template>`_.
  
Acknowledgement
----------

  * We thank [Barath Goel](https://github.com/BharatGoel36) for helping us package the application. 
  
Authors
----------

  * [Keshav Aditya R.P](https://keshavadityarp.github.io)
    - [Github](https://github.com/KeshavAdityaRP)
    - [LinkedIn](https://www.linkedin.com/in/keshavadityarp/)
  * Ramit Bharanikumar
    - [Github](https://github.com/ramit29)
    - [LinkedIn](https://www.linkedin.com/in/ramit-bharanikumar-12a014114/)
   * [Ashok Palaniappan](http://www.sastra.edu/staffprofiles/schools/scbt.php?staff_id=C2164)
    - [Github](https://github.com/apalania)
    - [LinkedIn](https://www.linkedin.com/in/ashokpalaniappan/)


Copyright & License
-------------------

Copyright (c) 2019, `riboflow`. MIT License.

