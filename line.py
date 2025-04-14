import math

def ecuacion(m, b, x):
    resultado = m * x + b
    return resultado

def line():
    a = float(input())
    b = float(input())
    x1 = float(input())
    x2 = float(input())
    print('Ingrese el coeficiente A:', a)
    print('Ingrese el coeficiente B:', b)
    print('Ingrese el coeficiente X1:', x1)
    print('Ingrese el coeficiente X2:', x2)
    print('El coeficiente A de su ecuación de la recta es:', a)
    print('El coeficiente B de su ecuación de la recta es:', b)
    print('El coeficiente X1 de su ecuación de la recta es:', x1)
    print('El coeficiente X2 de su ecuación de la recta es:', x2)
    print('')
    print('Para la siguiente ecuación:')
    print('\tY =', a, 'X +', b)
    print('')
    print('Dados los siguientes puntos:')
    punto1 = x1, ecuacion(2.3, -4, x1)
    print('\tP1', (punto1))
    punto2 = x2, ecuacion(2.3, -4, x2)
    print('\tP2', (punto2))
    print('')
    print('La distancia entre ellos es: ', math.dist(punto1, punto2))
line()
