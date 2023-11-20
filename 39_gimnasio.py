import os
os.system('cls')

clientes_gimnasio = [
    ['Juan', 'M', 182, 92],
    ['Alicia', 'F', 157, 52],
    ['Manuel', 'M', 171, 75],
    ['Sonia', 'F', 152, 51],
    ['Jimena', 'F', 165, 64],
    ['Carlos', 'M', 169, 67],
    ['Sara', 'F', 163, 54]
]

print('Longitud lista externa:', len(clientes_gimnasio))
print('Toda Alicia:', clientes_gimnasio[1])
print('El nombre Alicia', clientes_gimnasio[1][0])

clientes_gimnasio.append(['Antonio', 'M', 185, 87])

cliente_nueve = []
# cliente_nueve[0] = 'Mónica'
# cliente_nueve[1] = 'F'
# cliente_nueve[2] = '156'
# cliente_nueve[3] = '60'
cliente_nueve.insert(0, 'Mónica')
cliente_nueve.insert(1, 'F')
cliente_nueve.insert(2, 156)
cliente_nueve.insert(3, 60)
print(cliente_nueve)
clientes_gimnasio.append(cliente_nueve)

