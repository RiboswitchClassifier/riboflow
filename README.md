# RIBOFLOW - classifying riboswitches with >99% accuracy

[riboflow](https://test.pypi.org/project/riboflow/) is a python package for classifying putative riboswitch sequences into one of 32 classes with > 99% accuracy. It is based on a [tensorflow](https://www.tensorflow.org) deep learning model. ``riboflow`` has been tested using ``Python 3.5.2``. 

Installation
------------

The easiest way to install the package is via ``pip``

    $ pip install riboflow
    
Dependencies:
    
    numpy==1.14.5
    tensorflow==1.8.0   
    keras==2.2.0 
    
A trained ``Bi-directional Recurent Neural Network (RNN) Model`` is integrated into the ``riboflow`` package (and installed automatically with the ``pip``). Note that the source code to generate the ``Bi-directional Recurent Neural Network Model`` is available. The git repository [Riboswitch Classification](https://github.com/RiboswitchClassifier/RiboswitchClassification) could be forked to generate a new model.

Problem Statement
-------------------
Riboswitches are metabolite-sensing mRNAs, for e.g, amino acid or metal ion sensors, that switch conformation upon binding the cognate ligand, thereby exerting control on translation. It would be of interest to classfify the ligand-specificity of riboswitches given their sequence. 

**The prediction problem**:

Given the riboswitch sequence, predict the riboswitch class (as given by the ligand-specificity of the riboswitch).

**Machine learning formulation**:
 - Input: Riboswitch sequence
 - Source dataset: Rfam database (rfam.org)
 - Output: Riboswitch class 
 - Best-performing Classifier: Bi-directional RNN (>99% accuracy)
 - Features used in the best-performing classifier: the full riboswitch sequence

Usage
-------------------

Once `riboflow` is installed, please follow the steps to predict the class of a new riboswitch sequence:

**1. Import the package**:

  - Inside the python shell or in the python file::

        > import riboflow

**2. Construct a list of riboswitch sequences**:

        > # A sequence is a string in alphabet 'ATGC'
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

Riboswitches Accounted For 
------------

    1.  'RF00504 - Glycine Riboswitch'
    2.  'RF01786 - Cyclic di-GMP-II riboswitch'
    3.  'RF01750 - ZMP/ZTP riboswitch'
    4.  'RF00059 - TPP riboswitch (THI element)'
    5.  'RF01057 - S-adenosyl-L-homocysteine riboswitch'
    6.  'RF01725 - SAM-I/IV variant riboswitch'
    7.  'RF00162 - SAM riboswitch (S box leader)'
    8.  'RF00174 - Cobalamin riboswitch'
    9.  'RF01055 - Molybdenum Cofactor riboswitch'
    10. 'RF01727 - SAM/SAH Riboswitch'
    11. 'RF01482 - Abocbl Riboswitch'
    12. 'RF03057 - nhaA-I RNA'
    13. 'RF01734 - Fluroride riboswitch'
    14. 'RF00167 - Purine Riboswitch'
    15. 'RF00234 - glmS glucosamine-6-phosphate activated ribozyme'
    16. 'RF01739 - Glutamine riboswitch'
    17. 'RF03072 - raiA RNA'
    18. 'RF03058 - sul RNA'
    19. 'RF00380 - yKoK leader'
    20. 'RF00168 - Lysine Riboswitch'
    21. 'RF03071 - DUF1646 RNA'
    22. 'RF01689 - Abocbl variant RNA'
    23. 'RF00379 - ydaO/yuaA leader'
    24. 'RF00634 - S-adenosyl methionine (SAM) riboswitch'
    25. 'RF01767 - SMK box translational riboswitch (SAM-III)'
    26. 'RF00080 - yybP-ykoY manganese riboswitch'
    27. 'RF02683 - NiCo riboswitch'
    28. 'RF00442 - Guanidine-I Riboswitch'
    29. 'RF00522 - PreQ1 Riboswitch'
    30. 'RF00050 - FMN Riboswitch'
    31. 'RF01831 - THF riboswitch'
    32. 'RF00521 - SAM riboswitch (alpha-proteobacteria)'
    
Additional information
-----
For more information, please refer to our manuscript below. 

*Premkumar KAR, Bharanikumar R, Palaniappan A.* (2019) Classifying riboswitches with >99% accuracy. **Microorganisms** (to be submitted)

Please cite us if you use our services.

Package Structure
-----

    .
    ├── build                       # Buildout project configuration
    ├── dist                        # Consists of  .whl and .tar package files
    ├── riboflow                    # Package Directory
    │   ├── __init__.py             # main file
    │   ├── rnn_32_model.h5         # Bi-directional Recurent Neural Network Model
    ├── riboflow.egg-info           # Egg information of the project
    ├── LICENSE                     # License
    ├── MANIFEST.in                 # To include the Bi-directional Recurent Neural Network Model within the package
    ├── README.md                   # Package description
    └── setup.py                    # Package metadata

References and acknowledgements for pypi package development
----------

  * http://fouryears.eu/2014/03/19/structure-of-a-python-project/
  * http://www.jeffknupp.com/blog/2013/08/16/open-sourcing-a-python-project-the-right-way/
  * [Bharat Goel](https://github.com/BharatGoel36) provided help in packaging the application. 
  
Authors
----------

  * [Keshav Aditya R.P](https://keshavadityarp.github.io)
    - [Github](https://github.com/KeshavAdityaRP)
    - [LinkedIn](https://www.linkedin.com/in/keshavadityarp/)
  * Ramit Bharanikumar
    - [Github](https://github.com/ramit29)
    - [LinkedIn](https://www.linkedin.com/in/ramit-bharanikumar-12a014114/)
  * Ashok Palaniappan
    - [Senior Assistant Professor](http://www.sastra.edu/staffprofiles/schools/scbt.php?staff_id=C2164)
    - [Github](https://github.com/apalania)
    - [LinkedIn](https://www.linkedin.com/in/ashokpalaniappan/)


Copyright & License
-------------------

Copyright (c) 2019, the Authors. MIT License.

