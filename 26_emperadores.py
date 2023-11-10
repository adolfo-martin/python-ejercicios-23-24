import os
os.system('cls')

emperadores = [
    'Augusto', 
    'Tiberio', 
    'Calígula', 
    'Claudio', 
    'Nerón', 
    'Galba', 
    'Otón', 
    'Vitelio', 
    'Vespasiano', 
    'Tito', 
    'Domiciano',
]

print('EMPERADORES DE ROMA')

for i, emperador in enumerate(emperadores):
    if i == 0:
        print(f'{i+1}) {emperador} fue el primer emperador.')
    elif i == len(emperadores)-1:
        print(f'{i+1}) {emperador} fue el último emperador.')
    else:
        print(f'{i+1}) {emperador} sucedió a {emperadores[i-1]}.')
