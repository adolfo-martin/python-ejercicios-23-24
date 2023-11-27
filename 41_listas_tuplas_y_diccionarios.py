import os
os.system('cls')

# LISTAS: son mutables
marcas_de_coches = [ 'Seat', 'Mercedes', 'Renault', 'Fiat', 'Volkswagen', 'Citroen', 'Tesla', 'Ford', 'Ferrari' ]
marcas_de_coches.append('Porsche')
marcas_de_coches.append('Audi')
el_volkswagen = marcas_de_coches[4]

# TUPLAS: no son mutables, son algo propio de Python
marcas_de_coches_como_tupla = ( 'Seat', 'Mercedes', 'Renault', 'Fiat', 'Volkswagen', 'Citroen', 'Tesla', 'Ford', 'Ferrari' )

# DICCIONARIOS: son mutables, se llama en otros lenguajes 'arrays asociativos'. Tienen clave y valor
marcas_de_coches_como_diccionario = { 
    'se': 'Seat', 
    'ci': 'Citroen', 
    'me': 'Mercedes', 
    'fi': 'Fiat', 
    'vo': 'Volkswagen', 
    'te': 'Tesla', 
    'fo': 'Ford', 
    'fe': 'Ferrari',
    're': 'Renault', 
}

el_volkswagen = marcas_de_coches_como_diccionario['vo']
print(el_volkswagen)

print()
for i in marcas_de_coches_como_diccionario:
    print(f'El vehículo con clave "{i}" es "{marcas_de_coches_como_diccionario[i]}"')