def contenido_archivo(nombre_archivo):
    with open(nombre_archivo, 'r') as archivo:
        return archivo.read()