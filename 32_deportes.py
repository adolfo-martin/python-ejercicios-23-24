import os
os.system('cls')

deportes = ['futbol', 'baloncesto', 'esgrima', 'natacion', 'ciclismo', 'hockey', 'equitacion', 'tiro con arco', 'pesca', 'ajedrez']

deporte = deportes[2]
deportes[2]= deportes[7]
deportes[7] = deporte

print(deportes)
print(deportes.sort())