import numpy as np


def calcula_bhaskara(valor_a, valor_b, valor_c):
    if valor_a == 0:
        raise ArithmeticError("Valor de 'a' não pode ser '0'.")

    delta = ((valor_b ** 2) - 4 * valor_a * valor_c)
    if delta < 0:
        raise ArithmeticError("Raiz negativa, fora dos números reais")

    eixo_x1 = round((-valor_b + (delta ** 0.5)) / (2 * valor_a))
    eixo_x2 = round((-valor_b - (delta ** 0.5)) / (2 * valor_a))

    array_x = np.linspace(eixo_x1, eixo_x2)
    eixo_y = (valor_a*(array_x ** 2))-(valor_b*array_x)+valor_c

    return eixo_x1, eixo_x2, array_x, eixo_y
