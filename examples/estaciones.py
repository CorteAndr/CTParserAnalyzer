print('¿Qué mes es?')
mes = int(input()) 
print('¿Qué día es?')
dia = int(input())
if mes > 0 and mes < 13:
    if (dia > 0 and
        ((mes == 1 and dia < 32) or
        (mes == 2 and dia < 29) or
        (mes == 3 and dia < 32) or
        (mes == 4 and dia < 31) or
        (mes == 5 and dia < 32) or
        (mes == 6 and dia < 31) or
        (mes == 7 and dia < 32) or
        (mes == 8 and dia < 32) or
        (mes == 9 and dia < 31) or
        (mes == 10 and dia < 32) or
        (mes == 11 and dia < 31) or
        (mes == 12 and dia < 32))):
            if ((mes == 3 and dia >= 21) or
                (mes > 3 and mes < 6) or
                (mes == 6 and dia < 21)):
                print('primavera')
            elif ((mes == 6 and dia >= 21) or
                  (mes > 6 and mes < 9) or
                  (mes == 9 and dia < 21)):
                print('verano')
            elif ((mes == 9 and dia >= 21) or
                  (mes > 9 and mes < 12) or
                  (mes == 12 and dia < 21)):
                print('otoño')
            else:
                print('invierno')
    else:
        print('Este mes no existe.')
else:
    print('Este día no existe.')