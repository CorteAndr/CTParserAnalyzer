import unittest
import parser
from computational_thinking import ProgElement

class TestLayer1(unittest.TestCase):

    def test_hola_cortesmente(self):
        structures = parser.get_structures("examples/hola_cortesmente.py")
        self.assertDictEqual(structures,
                             {
                                 ProgElement.SEQUENCE: {2},
                                 ProgElement.VARIABLES: {4},
                                 ProgElement.EXPRESSIONS: {4},
                                 ProgElement.INPUT: {4},
                                 ProgElement.OUTPUT: {2, 6, 7}
                             })

    def test_area(self):
        structures = parser.get_structures("examples/area.py")
        self.assertDictEqual(structures,
                             {
                                 ProgElement.SEQUENCE: {1},
                                 ProgElement.VARIABLES: {2,4,5},
                                 ProgElement.DATA_TYPES: {2,4},
                                 ProgElement.EXPRESSIONS: {2,4,5},
                                 ProgElement.INPUT: {2,4},
                                 ProgElement.OUTPUT: {1,3,6}
                             })

    def test_ano_bisiesto(self):
        structures = parser.get_structures("examples/ano_bisiesto.py")
        self.assertDictEqual(structures,
                             {
                                 ProgElement.SEQUENCE: {1},
                                 ProgElement.SELECTION: {3,5,7},
                                 ProgElement.VARIABLES: {2},
                                 ProgElement.DATA_TYPES: {2},
                                 ProgElement.EXPRESSIONS: {2},
                                 ProgElement.INPUT: {2},
                                 ProgElement.OUTPUT: {1,4,6,8,10}
                             })
        
    def test_estaciones(self):
        structures = parser.get_structures("examples/estaciones.py")
        self.assertDictEqual(structures,
                             {
                                 ProgElement.SEQUENCE: {1},
                                 ProgElement.SELECTION: {5,6,19,23,27},
                                 ProgElement.VARIABLES: {2,4},
                                 ProgElement.DATA_TYPES: {2,4},
                                 ProgElement.EXPRESSIONS: {2,4},
                                 ProgElement.INPUT: {2, 4},
                                 ProgElement.OUTPUT: {1, 3, 22, 26, 30, 32, 34, 36}
                             })

    def test_suma_total(self):
        structures = parser.get_structures("examples/suma_total.py")
        self.assertDictEqual(structures,
                             {
                                 ProgElement.SEQUENCE: {1, 5},
                                 ProgElement.ITERATION: {4},
                                 ProgElement.VARIABLES: {1, 2, 6, 7},
                                 ProgElement.DATA_TYPES: {6},
                                 ProgElement.EXPRESSIONS: {1,2,6,7},
                                 ProgElement.INPUT: {6},
                                 ProgElement.OUTPUT: {5,9}
                             })

    def test_triangulo_de_astericos(self):
        structures = parser.get_structures("examples/trianglo_de_astericos.py")
        self.assertDictEqual(structures,
                             {
                                 ProgElement.SEQUENCE: {2},
                                 ProgElement.ITERATION: {1,2},
                                 ProgElement.VARIABLES: {1,2},
                                 ProgElement.OUTPUT: {3,4},
                             }
        )

    def test_factoial(self):
        structures = parser.get_structures("examples/factorial.py")
        self.assertDictEqual(structures,
                             {
                                 ProgElement.SEQUENCE: {2},
                                 ProgElement.ITERATION: {3},
                                 ProgElement.VARIABLES: {2,3,4},
                                 ProgElement.EXPRESSIONS: {2,4},
                                 ProgElement.FUNCTIONS_PROCEDURES: {1},
                                 ProgElement.PARAMETERS_RETURNS: {1,5}
                             })
    def test_longitud_de_una_cadena(self):
        structures = parser.get_structures("examples/longitud.py")
        self.assertDictEqual(structures,
                             {
                                 ProgElement.SEQUENCE: {2},
                                 ProgElement.SELECTION: {3},
                                 ProgElement.VARIABLES: {2},
                                 ProgElement.EXPRESSIONS: {2},
                                 ProgElement.FUNCTIONS_PROCEDURES: {1},
                                 ProgElement.PARAMETERS_RETURNS: {1,5},
                                 ProgElement.OUTPUT: {4}
                             })
    def test_estadisticas(self):
        structures = parser.get_structures("examples/estadisticas.py")
        self.assertDictEqual(structures,
                             {
                                 ProgElement.SEQUENCE: {1, 14},
                                 ProgElement.SELECTION: {2, 8},
                                 ProgElement.VARIABLES: {15, 17, 19, 21, 23, 24, 25, 26},
                                 ProgElement.DATA_TYPES: {15, 17, 19, 21, 23},
                                 ProgElement.EXPRESSIONS: {15, 17, 19, 21, 23, 24, 25, 26},
                                 ProgElement.DATA_STRUCTS: {27},
                                 ProgElement.FUNCTIONS_PROCEDURES: {1, 7, 13},
                                 ProgElement.PARAMETERS_RETURNS: {1,3,5,7,9,11,27},
                                 ProgElement.FUNCTION_CALL: {24, 25},
                                 ProgElement.INPUT: {15, 17, 19, 21, 23},
                                 ProgElement.OUTPUT: {14, 16, 18, 20, 22}
                             })

    def test_errores_logicos_en_el_cambio(self):
        structures = parser.get_structures("examples/calcular_cambio.py")
        self.assertDictEqual(structures,
                             {
                                 ProgElement.SEQUENCE: {2},
                                 ProgElement.SELECTION: {2,6,10,13},
                                 ProgElement.VARIABLES: {5, 8, 9, 12},
                                 ProgElement.EXPRESSIONS: {5, 8, 9, 12},
                                 ProgElement.FUNCTIONS_PROCEDURES: {1},
                                 ProgElement.PARAMETERS_RETURNS: {1, 15},
                                 ProgElement.OUTPUT: {3, 7, 11, 14}
                             })

    def test_longitud_de_un_numero(self):
        structures = parser.get_structures("examples/calcular_longitud.py")
        self.assertDictEqual(structures, 
                             {
                                 ProgElement.SEQUENCE: {3,7},
                                 ProgElement.ITERATION: {6},
                                 ProgElement.VARIABLES: {3,5,7,8},
                                 ProgElement.EXPRESSIONS: {3,5,7,8},
                                 ProgElement.FUNCTIONS_PROCEDURES: {1},
                                 ProgElement.PARAMETERS_RETURNS: {1,9}
                             })
        
    def test_estudiante_en_clase(self):
        structures = parser.get_structures("examples/estudiante_en_clase.py")
        self.assertDictEqual(structures, 
                             {
                                ProgElement.SEQUENCE: {2},
                                ProgElement.SELECTION: {4},
                                ProgElement.ITERATION: {3},
                                ProgElement.VARIABLES: {2,3},
                                ProgElement.FUNCTIONS_PROCEDURES: {1},
                                ProgElement.PARAMETERS_RETURNS: {1,5,6},
                                ProgElement.INPUT: {2}
                             })

if __name__ == '__main__':
    unittest.main()