

with open('diccionario.txt', 'r',encoding="utf-8") as archivo:
    separador = ':'
    data = {}

    for linea in archivo:
        value, key = linea.split(separador)
        data[key.strip()] = value.strip()

    print(data)