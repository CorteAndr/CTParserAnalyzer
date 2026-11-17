def estudiante_en_clase(nombre_archivo, nombre):
    with open(nombre_archivo, 'r') as archivo:
        for linea in archivo:
            if nombre == linea.strip():
                return True
    return False