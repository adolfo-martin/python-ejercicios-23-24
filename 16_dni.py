# Averigua cómo se calcula la letra del DNI.
# Desarrolla una función que sabiendo un número de DNI y una letra de DNI, 
# nos diga si la letra es correcta o no.

def es_dni_correcto(numero, letra):
    resto = numero % 23

    if resto == 0:
        if letra == 'T':
            return True
        else:
            return False
    elif resto == 1:
        if letra == 'R':
            return True
        else:
            return False
    elif resto == 2:
        if letra == 'W':
            return True
        else:
            return False
    elif resto == 3:
        if letra == 'A':
            return True
        else:
            return False
    elif resto == 4:
        if letra == 'G':
            return True
        else:
            return False
    elif resto == 5:
        if letra == 'M':
            return True
        else:
            return False
    elif resto == 6:
        if letra == 'Y':
            return True
        else:
            return False
    elif resto == 7:
        if letra == 'F':
            return True
        else:
            return False
    elif resto == 8:
        if letra == 'P':
            return True
        else:
            return False
    elif resto == 9:
        if letra == 'D':
            return True
        else:
            return False
    elif resto == 10:
        if letra == 'X':
            return True
        else:
            return False
    elif resto == 11:
        if letra == 'B':
            return True
        else:
            return False
    elif resto == 12:
        if letra == 'N':
            return True
        else:
            return False
    elif resto == 13:
        if letra == 'J':
            return True
        else:
            return False
    elif resto == 14:
        if letra == 'Z':
            return True
        else:
            return False
    elif resto == 15:
        if letra == 'S':
            return True
        else:
            return False
    elif resto == 16:
        if letra == 'Q':
            return True
        else:
            return False
    elif resto == 17:
        if letra == 'V':
            return True
        else:
            return False
    elif resto == 18:
        if letra == 'H':
            return True
        else:
            return False
    elif resto == 19:
        if letra == 'L':
            return True
        else:
            return False
    elif resto == 20:
        if letra == 'C':
            return True
        else:
            return False
    elif resto == 21:
        if letra == 'K':
            return True
        else:
            return False
    elif resto == 22:
        if letra == 'E':
            return True
        else:
            return False
        
print(es_dni_correcto(99999999, 'R'))
print(es_dni_correcto(65004204, 'R'))
print(es_dni_correcto(65004204, 'V'))