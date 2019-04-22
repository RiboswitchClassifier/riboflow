# RIBOFLOW - classifying riboswitches with >99% accuracy

[riboflow](https://test.pypi.org/project/riboflow/) is a python package for classifying putative riboswitch sequences into one of 24 classes with > 99% accuracy. It is based on a [tensorflow](https://www.tensorflow.org) deep learning model. ``riboflow`` has been tested using ``Python 3.5.2``. 

Installation
------------

The easiest way to install the package is via ``pip``::

    $ pip install -i https://test.pypi.org/simple/riboflow==0.13.dev0
    
Dependencies:
    
    numpy==1.14.5
    tensorflow==1.8.0   
    keras==2.2.0 
    
A trained ``Bi-directional Recurent Neural Network Model`` is integrated into the ``riboflow`` package (and installed automatically with the ``pip``). Note that the source code to generate the ``Bi-directional Recurent Neural Network Model`` is available. The git repository [Riboswitch Classification](https://github.com/RiboswitchClassifier/RiboswitchClassification) could be forked to generate a new model.

Riboswitches Accounted For 
------------

    1.  'RF00050 - Flavin Mononucleotide Riboswitch',
    2.  'RF00059 - Thiamine pyrophosphate riboswitch',
    3.  'RF00162 - SAM - 1 Riboswitch',
    4.  'RF00167 - Purine Riboswitch',
    5.  'RF00168 - Lysine Riboswitch',
    6.  'RF00174 - Cobalamin riboswitch',
    7.  'RF00234 - Glucosamine-6-phosphate riboswitch',
    8.  'RF00380 - Ykok riboswitch(Magnesium sensing riboswitch)',
    9.  'RF00504 - Glycine riboswitch',
    10. 'RF00521 - SAM - 2 Riboswitch',
    11. 'RF00522 - pre-queosine riboswitch1',
    12. 'RF00634 - SAM - 4 Riboswitch',
    13. 'RF01051 - Cyclic di-GMP-I riboswitches',
    14. 'RF01054 - pre-queosine riboswitch2',
    15. 'RF01055 - Molybdenum Co-factor riboswitch',
    16. 'RF01057 - SAH Riboswitch',
    17. 'RF01725 - SAM -1 -4 Variant riboswitch',
    18. 'RF01726 - SAM - 2 Long loop riboswitch',
    19. 'RF01727 - SAM-SAH Riboswitch',
    20. 'RF01734 - Fluoride Riboswitch',
    21. 'RF01739 - Glutamine riboswitch',
    22. 'RF01763 - Guanidine - 3 Riboswitch',
    23. 'RF01767 - SAM - 3 Riboswitch',
    24. 'RF02683 - NiCo riboswitch(sense Nickel or Cobalt)'

Usage
-------------------

Once `riboflow` is successfully installed, please follow the steps to predict the class of a new riboswitch sequence:

**1. Import the package**:

  - Inside the python shell or in the python file::

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


Additional information
-----
For more information, please refer to our manuscript below. 

*Premkumar KAR, Bharanikumar R, Palaniappan A.* (2019) Classifying riboswitches with >99% accuracy. **Microorganisms** (submitted)

Please cite us if you use our services.

References for pypi package development
----------

  * PyPI Page: http://pypi.python.org/pypi/python_boilerplate_template
  * Github: https://github.com/konstantint/python-boilerplate-template
  * Cookiecutter version: https://github.com/konstantint/cookiecutter-python-boilerplate
  * Blog post: http://fouryears.eu/2014/03/19/structure-of-a-python-project/
  * Useful reading
     - http://www.jeffknupp.com/blog/2013/08/16/open-sourcing-a-python-project-the-right-way/
  * Related projects: `[1] <https://pypi.python.org/pypi/modern-package-template>`, `[2] <https://pypi.python.org/pypi/python-package-template/>`, `[3] <https://github.com/vital-fadeev/python-package-template>`.
  
  * _We thank [Barath Goel](https://github.com/BharatGoel36) for helping us package the application._ 
  
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

