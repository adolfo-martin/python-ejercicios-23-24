import os
os.system('cls')

def convertir_celsius_a_kelvin(celsius):
    kelvin = celsius + 273.15
    return kelvin

def convertir_kelvin_a_celsius(kelvin):
    celsius = kelvin - 273.15
    return celsius


while True:
    print('\n MENÚ')
    print('  1) Convertir celsius a kelvin')
    print('  2) Convertir kelvin a celsius')
    print('  7) Salir')

    opcion = int(input('Introduce la opción de conversión: '))
    if opcion == 1:
        celsius = int(input('Dime los grados celsius: '))
        kelvin = convertir_celsius_a_kelvin(celsius)
        print(f'{celsius} grados celsius son {kelvin} grados kelvin')
    elif opcion == 2:
        kelvin = int(input('Dime los grados kelvin: '))
        celsius = convertir_kelvin_a_celsius(kelvin)
        print(f'{kelvin} grados kelvin son {celsius} grados celsius')
    elif opcion == 7:
        break