# https://www.bbvaassetmanagement.com/es/actualidad/como-se-calculan-los-intereses-y-la-cuota-cuando-pedimos-un-credito-hipotecario-el-sistema-de-amortizacion-frances/

import os
os.system('cls')

def calcular_cuota_mensual(capital, meses, interes):
    interes = interes / 100
    cuota = capital * ( (1 + interes)**meses * interes / ((1 + interes)**meses - 1) )
    return cuota / 12


def calcular_interes_mensual(capital_pendiente, interes):
    interes = interes / 100
    intereses = interes * capital_pendiente
    return intereses / 12


print(calcular_interes_mensual(150000, 4.828))

# cuota = calcular_cuota_mensual(150000, 30, 4.828)
# print(cuota)