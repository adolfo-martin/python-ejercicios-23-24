# contador = 1

# while contador <= 10:
#     print(contador)
#     contador += 1

# print('FIN 🏁')

contador = 1

while True:
    print(contador)
    contador += 1
    
    if contador <= 10:
        continue
    else:
        break

    print('Aquí no puede llegar porque lo impiden las líneas 16 y 18')

print('FIN 🏁')