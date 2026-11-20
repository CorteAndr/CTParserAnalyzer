score = 0
errores = 0
auxiliar = True

while auxiliar:
    print('¿Cuántos bloques has derribado?')
    cantidad = int(input())
    if cantidad == 0:
        errores += 1
    else:
        errores = 0
        if cantidad == 1:
            print('¿Qué número había en tu bloque?')
            puntos = int(input())
            score += puntos
        else:
            score += cantidad

    if score == 50:
        print('¡Ganado!')
        auxiliar = False
    if score > 50:
        score = 25
    if errores == 3:
        print('¡Perdido!')
        auxiliar = False
    print('Puntuación:', score)