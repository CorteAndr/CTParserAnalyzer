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
                                 ProgElement.SEQUENCE: {2, 5},
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

    def test_7_nombres(self):
        structures = parser.get_structures("examples/7_nombres.py")
        self.assertDictEqual(structures,
                             {
                                 ProgElement.SEQUENCE: {1, 5},
                                 ProgElement.ITERATION: {4},
                                 ProgElement.VARIABLES: {2, 3, 6},
                                 ProgElement.EXPRESSIONS: {2, 3, 6},
                                 ProgElement.INPUT: {2},
                                 ProgElement.OUTPUT: {1, 5}
                             })

    def test_suma_de_6(self):
        structures = parser.get_structures("examples/suma_de_6.py")
        self.assertDictEqual(structures,
                             {
                                 ProgElement.SEQUENCE: {1, 4},
                                 ProgElement.SELECTION: {6},
                                 ProgElement.ITERATION: {3},
                                 ProgElement.VARIABLES: {1, 2, 5, 9, 10},
                                 ProgElement.DATA_TYPES: {5},
                                 ProgElement.EXPRESSIONS: {1, 2, 5, 9, 10},
                                 ProgElement.INPUT: {5},
                                 ProgElement.OUTPUT: {4, 11}
                             })

    def test_mayuscula(self):
        structures = parser.get_structures("examples/mayuscula.py")
        self.assertDictEqual(structures,
                             {
                                 ProgElement.SEQUENCE: {2},
                                 ProgElement.SELECTION: {4},
                                 ProgElement.ITERATION: {3},
                                 ProgElement.VARIABLES: {2,3,5,7},
                                 ProgElement.EXPRESSIONS: {2, 5, 7},
                                 ProgElement.FUNCTIONS_PROCEDURES: {1},
                                 ProgElement.PARAMETERS_RETURNS: {1, 8}
                             })

    def test_intercambiar(self):
        structures = parser.get_structures("examples/intercambiar.py")
        self.assertDictEqual(structures,
                             {
                                 ProgElement.SEQUENCE: {4, 5},
                                 ProgElement.VARIABLES: {5,6,7,10,11,12,14},
                                 ProgElement.EXPRESSIONS: {5,6,7,10,11,12,14},
                                 ProgElement.DATA_STRUCTS: {8, 12},
                                 ProgElement.FUNCTIONS_PROCEDURES: {4},
                                 ProgElement.PARAMETERS_RETURNS: {4, 8},
                                 ProgElement.FUNCTION_CALL: {14},
                                 ProgElement.OUTPUT: {13, 15}
                             })

    def test_juego_en_ka_feria(self):
        structures = parser.get_structures("examples/juego_en_la_feria.py")
        print(structures)
        self.assertDictEqual(structures,
                             {
                                 ProgElement.SEQUENCE: {1, 6, 11, 13, 20, 25},
                                 ProgElement.SELECTION: {8, 12, 19, 22, 24},
                                 ProgElement.ITERATION: {5},
                                 ProgElement.VARIABLES: {1,2,3,7,9,11,14,15,17,21,23,26},
                                 ProgElement.DATA_TYPES: {7, 14},
                                 ProgElement.EXPRESSIONS: {1,2,3,7,9,11,14,15,17,21,23,26},
                                 ProgElement.INPUT: {7, 14},
                                 ProgElement.OUTPUT: {6, 13, 20, 25, 27}
                             })
    def test_leer_el_contenido_de_un_archivo(self):
        structures = parser.get_structures("examples/leer_el_contenido_de_un_archivo.py")
        self.assertDictEqual(structures,
                            {
                                ProgElement.VARIABLES: {2},
                                ProgElement.FUNCTIONS_PROCEDURES: {1},
                                ProgElement.PARAMETERS_RETURNS: {1, 3},
                                ProgElement.INPUT: {2, 3}
                            })
    def test_trampolin_mejorado(self):
        structures = parser.get_structures("examples/trampolin_mejorado.py")
        self.assertDictEqual(structures,
                             {
                                 ProgElement.VARIABLES: {1},
                                 ProgElement.OUTPUT: {1, 2}
                             })

if __name__ == '__main__':
    unittest.main()