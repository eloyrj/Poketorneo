

with open('pDic.txt', 'r') as archivo:
    separador = ':'
    data = {}
    
    for linea in archivo:
        value, key = linea.split(separador)
        data[key.strip()] = value.strip()

    print(data)