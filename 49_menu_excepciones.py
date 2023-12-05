import os, sys
os.system('cls')


contactos = [
    { 'nombre': 'Antonio', 'apellidos': 'Pérez',  'edad': 58,  'telefono': 666111111 },
    { 'nombre': 'Ramiro', 'apellidos': 'Sánchez',  'edad': 25,  'telefono': 666222222 },
    { 'nombre': 'Cristina', 'apellidos': 'Martínez',  'edad': 37,  'telefono': 666333333 },
    { 'nombre': 'Juan', 'apellidos': 'Giménez',  'edad': 21,  'telefono': 666444444 },
    { 'nombre': 'Sonia', 'apellidos': 'Fernández',  'edad': 71,  'telefono': 666555555 },
]


def mostrar_menu_y_pedir_opcion():
    while True:
        print('--------------- AGENDA --------------')
        print('1) Crear contacto.')
        print('2) Opción 2')
        print('3) Opción 3')
        print('4) Opción 4')
        print('5) Salir')

        opcion = input('Introduce una opción: ')

        match opcion:
            case '1':
                crear_contacto()
            case '2':
                pass
            case '3':
                pass
            case '4':
                pass
            case '5':
                sys.exit()
            case _:
                print('Introduce una opción correcta.\n')


def crear_contacto():
    nombre = input('Dime tu nombre: ')
    apellidos = input('Dime tus apellidos: ')
    edad = pedir_edad()
    telefono = pedir_telefono()
    insertar_contacto_en_agenda(nombre, apellidos, edad, telefono)


def insertar_contacto_en_agenda(nombre, apellidos, edad, telefono):
    nuevo_contacto = {
        'nombre' : nombre,
        'apellidos': apellidos,
        'edad': edad,
        'telefono': telefono
    }

    for contacto in contactos:
        if contacto['telefono'] == nuevo_contacto['telefono']:
            # print('Ya existe un usuario con ese teléfono.')
            raise Exception('Ya existe un usuario con ese teléfono.')

    contactos.append(nuevo_contacto)




def pedir_edad():
    while True:
        try:
            edad = int(input('Dime tu edad: '))
            if edad < 0 or edad > 120:
                print('La edad introducida no es correcta.')
                continue
            break
        except Exception as error:
            print('No has introducido un número para la edad.\n')
            continue

    return edad

def pedir_telefono():
    while True:
        try:
            telefono = int(input('Dime tu teléfono: '))
            if telefono < 600000000 or telefono > 999999999:
                print('El teléfono introducido no es correcto.')
                continue
            break
        except Exception as error:
            print('No has introducido un número para el teléfono.\n')
            continue

    return telefono


mostrar_menu_y_pedir_opcion()