import os
os.system('cls')

equipos = {
    'rm': 'Real Madrid',
    'ba': 'Fútbol Club Barcelona',
    'vg': 'Celta de Vigo',
    'be': 'Real Betis Balompié'
}

print(equipos.get('vg'))
print(equipos['vg'])

print(equipos.get('lo'))
print(equipos['lo'])