i = 1
suma = 0
while i <= 6:
    print('Introduce un número')
    numero = int(input())
    if numero == 0:
        break
    else:
        suma += numero
    i += 1
print('La suma total es', suma)