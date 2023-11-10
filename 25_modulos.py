import os
os.system('cls')

modulos = [
    'Sistemas informáticos',
    'Programación',
    'Bases de datos',
    'Inglés técnico',
    'Entornos de desarrollo',
    'Formación y orientación laboral',
    'Empresa e iniciativa emprendedora'
]

print('Los módulos de primero son:')

i = 0
while i < len(modulos):
    print(f'\t{i+1}) {modulos[i]}')
    i += 1

i = 1
for modulo in modulos:
    print(f'\t{i}) {modulo}')
    i += 1

for i in range(0, len(modulos)):
    print(f'\t{i+1}) {modulos[i]}')

for i, modulo in enumerate(modulos):
    print(f'\t{i+1}) {modulo}')
