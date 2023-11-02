print('\n'*5)

texto1 = "Hola"
texto2 = "Pepe"
texto3 = 'Python'

# Primera forma de concatenar
print('Mi mensaje es: ' + texto1 + ', soy ' + texto2 + '. Me gusta ' + texto3 + ".")

# Segunda forma: f-string
lenguaje = 'Python'
calificacion = 10

print(f'Mi mensaje es: {lenguaje} se merece un {calificacion + 1}.')

# Tercera forma
print("Mi mensaje es: %s se merece un %d" % (lenguaje, calificacion))

# Cuarta forma
print('Mi mensaje es: {0} se merece un {1}'.format(lenguaje, calificacion))