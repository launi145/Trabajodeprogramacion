import csv

def leer_datos_csv(nombre_archivo):
    lista_datos = []

    # Abre el archivo CSV en modo lectura
    with open(nombre_archivo, 'r') as datos:
        # Crea un objeto lector de CSV
        lector_csv = csv.reader(datos)
        encabezado = next(lector_csv)
        lista_datos.append(encabezado)

        for fila in lector_csv:
            lista_datos.append(fila)

    return lista_datos


nombre_archivo = 'datos.csv'
datos = leer_datos_csv(nombre_archivo)
for fila in datos:
    print(fila) 



def listodict(datos):
    lista_diccionarios = []

    for linea in datos:
        valores = linea.split('\t')
        provincia = valores[0]
        latitud = valores[1]
        longitud = valores[2]

        diccionario = {provincia: (latitud, longitud)}
        lista_diccionarios.append(diccionario)

    return lista_diccionarios

datos = [
    'Buenos Aires\t-34.6037\t-58.3816',
    'CABA\t-34.6158\t-58.4333',
    'Catamarca\t-28.4696\t-65.7795',
    'Chaco\t-26.6021\t-59.3087',
    'Chubut\t-43.6848\t-68.2714',
    'Córdoba\t-31.4167\t-64.1833',
    'Corrientes\t-27.4692\t-58.8309',
    'Entre Ríos\t-31.7642\t-60.5247',
    'Formosa\t-26.1844\t-58.1759',
    'Jujuy\t-24.1858\t-65.2995',
    'La Pampa\t-36.6167\t-64.2833',
    'La Rioja\t-29.4131\t-66.8558',
    'Mendoza\t-32.8908\t-68.8272',
    'Misiones\t-27.3621\t-55.9007',
    'Neuquén\t-38.9516\t-68.0591',
    'Río Negro\t-40.8135\t-62.9967',
    'Salta\t-24.7829\t-65.4232',
    'San Juan\t-31.5375\t-68.5364',
    'San Luis\t-33.3335\t-66.3499',
    'Santa Cruz\t-51.6236\t-69.2169',
    'Santa Fe\t-31.6333\t-60.7',
    'Santiago del Estero\t-27.784\t-64.2665',
    'Tierra del Fuego\t-54.8019\t-68.302',
    'Tucumán\t-26.808\t-65.2176'
]

lista_diccionarios = listodict(datos)

# Imprimir la lista de diccionarios
for diccionario in lista_diccionarios:
    print(diccionario)