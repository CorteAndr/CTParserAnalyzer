def hallar_min(x, y):
    if (x > y):
        return y
    else:
        return x

def hallar_max(x, y):
    if (x > y):
        return x
    else:
        return y

def hallar_estadisticas():
    print('¿Cuál es el número 1?')
    x1 = int(input())
    print('¿Cuál es el número 2?')
    x2 = int(input())
    print('¿Cuál es el número 3?')
    x3 = int(input())
    print('¿Cuál es el número 4?')
    x4 = int(input())
    print('¿Cuál es el número 5?')
    x5 = int(input())
    mi = hallar_min(hallar_min(hallar_min(x1,x2), hallar_min(x3,x4)),x5)
    ma = hallar_max(hallar_max(hallar_max(x1,x2), hallar_max(x3,x4)),x5)
    ge = (x1 + x2 + x3 + x4 + x5) / 5
    return ge, mi, ma