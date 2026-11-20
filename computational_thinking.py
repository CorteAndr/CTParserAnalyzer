from enum import Enum
from collections import defaultdict
import typing

class ProgElement(Enum):
    SEQUENCE = 1
    SELECTION = 2
    ITERATION = 3
    VARIABLES = 4
    DATA_TYPES = 5
    EXPRESSIONS = 6
    DATA_STRUCTS = 7
    FUNCTIONS_PROCEDURES = 8
    PARAMETERS_RETURNS = 9
    RECURSION = 10
    FUNCTION_CALL = 11
    INPUT = 12
    OUTPUT = 13
    TESTING = 14
    DEBUGGING = 15

class CTElement(Enum):
    ABSTRACTION = 1,
    DECOMPOSITION = 2,
    PATTERN_RECOGNITION = 3,
    EVALUATION = 4



CT_TO_PROG_MAP = {
    CTElement.ABSTRACTION: (ProgElement.VARIABLES, ProgElement.DATA_TYPES, ProgElement.EXPRESSIONS, ProgElement.PARAMETERS_RETURNS),
    CTElement.DECOMPOSITION: (ProgElement.FUNCTIONS_PROCEDURES, ProgElement.SELECTION),
    CTElement.PATTERN_RECOGNITION: (ProgElement.ITERATION, ProgElement.RECURSION, ProgElement.FUNCTION_CALL),
    CTElement.EVALUATION: {ProgElement.TESTING, ProgElement.DEBUGGING}
}

def analyze_structures(structs : typing.Dict):
    ct_elements = defaultdict(set)
    for ct_el in CT_TO_PROG_MAP:
        for prog_el in CT_TO_PROG_MAP[ct_el]:
            ct_elements[ct_el].update(structs[prog_el])
    return ct_elements

def analyze_ast(ast_tree):
    pass
