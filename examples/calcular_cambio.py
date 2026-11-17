def calcular_cambio(precio, importe):
    if importe < precio:
        print('Pago insuficiente')
    else:
        moneda_cinco = (importe - precio) // 5
        if moneda_cinco > 0:
            print('Paga', moneda_cinco, 'moneda(s) de 5 Bs')
        cambio = (importe - precio) % 5
        moneda_dos = cambio // 2
        if moneda_dos > 0:
            print('Paga', moneda_dos, 'moneda(s) de 2 Bs')
        moneda_uno = cambio % 2
        if moneda_uno > 0:
            print('Paga', moneda_uno, 'moneda(s) de 1 Bs')
    return importe - precio