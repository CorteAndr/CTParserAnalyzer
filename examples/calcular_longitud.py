def calcular_longitud(n):
    # cada número tiene al menos un dígito
    contador = 1
    # verifica si hay más dígitos
    n //= 10
    while n != 0:
        n //= 10
        contador += 1
    return contador