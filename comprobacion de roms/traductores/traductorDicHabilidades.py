import mmap
import enchant
d = enchant.Dict("en_US")

salida = open("habilidades.txt","w",encoding="utf-8")




f2 = open("habilidadesTocho.txt","r",encoding='utf-8')
    
lines = f2.readlines()
encontrado= False
contador  = 1 
l = ""
for line in lines:
    if contador == 1:
        data = line.split(" ")[1:]
        data[len(data)-1] = data[len(data)-1][:(len(data[len(data)-1])-1)]
        
        for i in data:
            if i!=data[len(data)-1]:
                l = l + i.upper() + " "
            else:
                l = l + i.upper() 
        
        
        
        
    elif contador == 2:
        l = l +":"
        data = line.split(" ")[:3]
        
        for i in data:
            if d.check(i) and i.upper()!="EVITA" and i.upper()!="LA" and i.upper()!="SI" and i.upper()!="COMO" and i.upper()!="AL" and i.upper()!="A" and i.upper()!="LOS" and i.upper()!="NO" and i.upper()!="SOLO" and i.upper()!="LAS" and i.upper()!="SE":
                if i!=data[len(data)-1]:
                    l = l + i.upper() + " "
                else:
                    l = l + i.upper() 
             
        l = l+"\n"
        salida.write(l)
        contador = 0
        l=""

    contador= contador +1