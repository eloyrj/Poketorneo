rutaLectura = "prueba.bas"

def cargarDiccionario(ruta):
    with open(ruta, 'r') as archivo:
        separador = ':'
        data = {}
        
        for linea in archivo:
            value, key = linea.split(separador)
            data[key.strip()] = value.strip()

    return data

def cargarDiccionarios():
    return  cargarDiccionario('diccionario.txt'),cargarDiccionario('naturaleza.txt') , cargarDiccionario('habilidades.txt')

c = cargarDiccionarios()
diccionarioAtaques=c[0]
diccionarioNaturaleza=c[1]
diccionarioHabilidades=c[2]

f1 = open(rutaLectura)
pala = f1.readlines()[0:10]
sete = pala[0].split(" ")
pokemon = sete[1][1:(len(sete[1])-1)].upper()
print(pokemon)


habilidadapoyo  = pala[1].split(" ")[1:len(pala[1].split(" ")[1:])-1]
habilidadIngles = ""
for j in habilidadapoyo:
    if j != habilidadapoyo[len(habilidadapoyo)-1]:
        habilidadIngles = habilidadIngles+j+" "
    else:
        habilidadIngles = habilidadIngles+j
    
habilidad = diccionarioHabilidades.get(habilidadIngles.upper())

print(habilidad)

naturalezaIngles = pala[4].split(" ")[0]
naturaleza = diccionarioNaturaleza.get(naturalezaIngles)
print(naturaleza)


ataque1apoyo = pala[6].split(" ")[1:len(pala[6].split(" "))-2]
ataque1Ingles = ""
for i in ataque1apoyo:
    if i != ataque1apoyo[len(ataque1apoyo)-1]:
        ataque1Ingles = ataque1Ingles+i+" "
    else:
        ataque1Ingles = ataque1Ingles+i
ataque1 = diccionarioAtaques.get(ataque1Ingles)
print(ataque1)


ataque2apoyo = pala[7].split(" ")[1:len(pala[7].split(" "))-2]
ataque2Ingles = ""
for i in ataque2apoyo:
    if i != ataque2apoyo[len(ataque2apoyo)-1]:
        ataque2Ingles = ataque2Ingles+i+" "
    else:
        ataque2Ingles = ataque2Ingles+i
ataque2 = diccionarioAtaques.get(ataque2Ingles)
print(ataque2)

ataque3apoyo = pala[8].split(" ")[1:len(pala[8].split(" "))-2]
ataque3Ingles = ""
for i in ataque3apoyo:
    if i != ataque3apoyo[len(ataque3apoyo)-1]:
        ataque3Ingles = ataque3Ingles+i+" "
    else:
        ataque3Ingles = ataque3Ingles+i
ataque3 = diccionarioAtaques.get(ataque3Ingles)
print(ataque3)

ataque4apoyo = pala[9].split(" ")[1:len(pala[9].split(" "))-2]
ataque4Ingles = ""
for i in ataque4apoyo:
    if i != ataque4apoyo[len(ataque4apoyo)-1]:
        ataque4Ingles = ataque4Ingles+i+" "
    else:
        ataque4Ingles = ataque4Ingles+i
ataque4 = diccionarioAtaques.get(ataque4Ingles)
print(ataque4)

