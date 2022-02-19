import mmap
salida = open("diccionario.txt","w",encoding="utf-8")


f2 = open("t.txt","r",encoding='utf-8')
with f2 as myfile:
    total_lines = sum(1 for line in myfile)
f2.close()

f2 = open("t.txt","r",encoding='utf-8')
    
lines = f2.readlines()
encontrado= False
contador  = 1 
l = ""
for line in lines:
    if contador == 1:
        data = line.split(" ")
        
        for d in range(len(data)):
            if d!= len(data)-1:
                if (d+1) == len(data)-1:
                    l = l + data[d+1][:(len(data[d+1])-1)]

                else:
                    l = l + data[d+1]+ " "
        
    elif contador == 2:
        data = line.split(" ")
        
        l=l+ ":"
        for d in  range(len(data)-4):
            if d == range(len(data)-4):
                l = l + data[d]
            else:
                l = l + data[d]+ " "
             
        l = l+"\n"
    elif contador == 4:
        salida.write(l)
        contador = 0
        l=""

    contador= contador +1
    






