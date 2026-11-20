def mayuscula(palabra):
    resultado = ''
    for i in palabra:
        if i == 's':
            resultado += 'S'
        else:
            resultado += i
    return resultado