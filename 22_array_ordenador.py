import os
os.system('cls')

componentes_von_newmann = [
    'procesador',
    'memoria principal',
    'memoria secundaria',
    'dispositivos de entrada/salida'
]

print('Los elementos que forman la arquitectura Von Newmann son:')
# print('\t1) ', componentes_von_newmann[0])
# print('\t2) ', componentes_von_newmann[1])
# print('\t3) ', componentes_von_newmann[2])
# print('\t4) ', componentes_von_newmann[3])

i = 0
while i < len(componentes_von_newmann):
    print(f'\t{i+1}) {componentes_von_newmann[i]}')
    i += 1