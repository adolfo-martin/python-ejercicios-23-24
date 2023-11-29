import os
os.system('cls')

ingredientes = [
    {'nombre': 'Base de pizza', 'cantidad': 1, 'precio': 0.90},
    {'nombre': 'Salsa de tomate', 'cantidad': 1 , 'precio': 0.25},
    {'nombre': 'Jamón de york', 'cantidad': 2, 'precio': 0.40},
    {'nombre': 'Queso rallado', 'cantidad': 2, 'precio': 0.20},
    {'nombre': 'Aceitunas', 'cantidad': 1, 'precio': 0.25},
    {'nombre': 'Salami', 'cantidad': 1, 'precio': 0.45},
    {'nombre': 'Orégano', 'cantidad': 1, 'precio': 0.10},
    {'nombre': 'Alcaparras', 'cantidad': 1, 'precio': 0.15},
]


IVA_EXENTO = 0
IVA_SUPERREDUCIDO = 4
IVA_REDUCIDO = 10
IVA_NORMAL = 21


def calcular_base_imponible(ingredientes):
    base_imponible = 0
    for ingrediente in ingredientes:
        base_imponible += ingrediente['cantidad'] * ingrediente['precio']

    return base_imponible


print(calcular_base_imponible(ingredientes))


def calcular_precio_total(ingredientes, iva):
    base_imponible = calcular_base_imponible(ingredientes)
    precio_total = base_imponible + base_imponible * (iva / 100)
    return precio_total

def imprimir_ticket(ingredientes):
    for ingrediente in ingredientes:
        print(f'{ingrediente["nombre"]:20s} {ingrediente["cantidad"]:2} {ingrediente["precio"]:6.2f}' )

imprimir_ticket(ingredientes)