# Computational Thinking parser
## Parser.py
`get_structures` takes in the path to a python file after which using the `ast` package it generates and walks through the AST tree of the program and maps nodes to Programming Elements such as Selection, Iterations, etc.

Tested using a starting test set where the programs are shown in [examples](/examples/) which can be executed using the following command: `python3 -m unittest tests/test_layer1.py -v` in the root directory