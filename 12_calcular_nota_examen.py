import os

os.system('cls')

# cada pregunta se valora entre 0 y 10
# pregunta_1 = 5

# pregunta_2 = 8

# pregunta_3 = 10

# pregunta_4 = 5


def calcular_nota(pr_1, pr_2, pr_3, pr_4):
    po_1 = 3
    po_2 = 1
    po_3 = 2
    po_4 = 4
    nota = (pr_1 * po_1) / 10 + (pr_2 * po_2) / 10 + (pr_3 * po_3) / 10 + (pr_4 * po_4) / 10 
    return nota

# calificacion = calcular_nota(pregunta_1, pregunta_2, pregunta_3, pregunta_4)

calificacion = calcular_nota(10, 10, 10, 10)
print(calificacion)

calificacion = calcular_nota(0, 0, 0, 0)
print(calificacion)

calificacion = calcular_nota(5, 5, 5, 5)
print(calificacion)

calificacion = calcular_nota(5, 8, 10, 5)
print(calificacion)