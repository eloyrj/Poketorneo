import mmap
import enchant
d = enchant.Dict("en_US")

salida = open("evolucionesOrden.txt","w",encoding="utf-8")




f2 = open("evoluciones.txt","r",encoding='utf-8')
    
lines = f2.readlines()
encontrado= False
contador  = 1 
l = ""
for line in lines:
    
    data = line.split(" ")
    print(data)
    
    if data[0] == "\\\n":
        l = l+"\n"
        salida.write(l)
        contador = 0
        l=""
    elif data[0]=="\n":
        None
    else:
        l = l + data[2] 
        l = l +":"

    contador= contador +1