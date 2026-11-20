# Sustituye == (para comparar valores) por
# = (para asignar valores).

def intercambiar(x, y):
    z = y
    y = x
    x = z
    return x, y

x = 3
y = 5
z = (x, y)
print(z)
z = intercambiar(x, y)
print(z)