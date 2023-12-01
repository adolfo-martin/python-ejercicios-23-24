datos_poblacionales_ciudades_grandes = [
    ['Cáceres',   17001,  185294, 3162876],
    ['La Coruña', 42001,  719458, 2371974],
    ['Barcelona',  3001, 2492654, 3258453],
    ['Murcia',    30001,  727432, 2836493],
    ['Madrid',     7001, 4036721, 3347365],
    ['Córdoba',   24001,  269351, 2637296],
]

datos_fiscales_ciudades_grandes = [
    ['Murcia',    180665738952],
    ['La Coruña', 192377313536],
    ['Córdoba',    63818409834],
    ['Cáceres',    42153829118],
    ['Madrid',   1326131472757],
    ['Barcelona', 765581286290],
]

datos_poblacionales_ciudades_pequenias = [
    ['Lorca',        30801,  94528, 76628],
    ['Villagarcía',  42032,  72863, 47197],
    ['Badalona',      3043, 324624, 25841],
    ['Huercalovera', 23043,  32236, 43647],
    ['Carabancel',    7321, 436528, 34364],
    ['Torremolinos', 21032,  29734, 23732],
]

datos_fiscales_ciudades_pequenias = [
    ['Torremolinos', 7098784362],
    ['Carabancel',   133933774848],
    ['Villagarcía',  19634538336],
    ['Badalona',     96716851440],
    ['Huercalovera', 7036119484],
    ['Lorca',        21380153984],
]


def juntar_datos_poblacionales_y_fiscales(datos_poblacionales, datos_fiscales):
    datos_unidos = []

    for dato_pob in datos_poblacionales:
        for dato_fis in datos_fiscales:
            if dato_pob[0] == dato_fis[0]:
                nuevo_dato = [dato_pob[0], dato_pob[1], dato_pob[2], dato_pob[3], dato_fis[1]]
                datos_unidos.append(nuevo_dato)
                break

    return datos_unidos


def juntar_todos_los_datos(datos_poblacionales_ciudades_grandes, datos_fiscales_ciudades_grandes, datos_poblacionales_ciudades_pequenias, datos_fiscales_ciudades_pequenias):
    datos = []
    datos_grandes = juntar_datos_poblacionales_y_fiscales(datos_poblacionales_ciudades_grandes, datos_fiscales_ciudades_grandes)
    datos_pequenias = juntar_datos_poblacionales_y_fiscales(datos_poblacionales_ciudades_pequenias, datos_fiscales_ciudades_pequenias)

    for dato in datos_grandes:
        datos.append(dato)

    for dato in datos_pequenias:
        datos.append(dato)

    return datos


print(juntar_todos_los_datos(datos_poblacionales_ciudades_grandes, datos_fiscales_ciudades_grandes, datos_poblacionales_ciudades_pequenias, datos_fiscales_ciudades_pequenias))