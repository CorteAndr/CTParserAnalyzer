print('¿Qué año deseas investigar?')
año = int(input())
if año % 400 == 0:
    print('año bisiesto')
elif año % 100 == 0:
    print('no año bisiesto')
elif año % 4 == 0:
    print('año bisiesto')
else:
    print('no año bisiesto')