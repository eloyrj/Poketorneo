import mmap
f1 = open("comprobacion de roms\prueba.bas")
salida = open("salida.txt","w",encoding="utf-8")

f2 = open("comprobacion de roms\TRAMPA.gba.log","r",encoding='utf-8')
with f2 as myfile:
    total_lines = sum(1 for line in myfile)
f2.close()

repetidas = 0
pala = f1.readline()
sete = pala.split(" ")
encontrado = False
for palabra in sete:

    PosicionTexto = -1
    NumeroLinea = 0

    f2 = open("comprobacion de roms\TRAMPA.gba.log","r",encoding='utf-8')
    
    lines = f2.readlines()[1682:total_lines]
    encontrado= False
    for line in lines:
        
        NumeroLinea = NumeroLinea + 1
        PosicionTexto = line.find(palabra)
        if PosicionTexto >= 0:
            encontrado =True
            s =  "hay un " + palabra + " en la linea "+ str(NumeroLinea)
            salida.write(s)
            salida.write(" --> ")
            salida.write(line)
    f2.close()
    if(encontrado):

        f2 = open("comprobacion de roms\TRAMPA.gba.log","r",encoding='utf-8')
        lines = f2.readlines()[412:797]
        for line in lines:
            NumeroLinea = NumeroLinea + 1
            PosicionTexto = line.find(palabra)
            if PosicionTexto >= 0:
                s =  "Tiene los ataques "
                salida.write(s)
                salida.write(" --> ")
                salida.write(line)
        f2.close()


        f2 = open("comprobacion de roms\TRAMPA.gba.log","r",encoding="utf-8")
        lines = f2.readlines()[3:388]
        for line in lines:       
            NumeroLinea = NumeroLinea + 1
            PosicionTexto = line.find(palabra)
            if PosicionTexto >= 0:                
                s =  "Tiene las Stats a nivel 50 "
                salida.write(s)
                salida.write(" --> ")
                salida.write(line)       
        salida.write( '\n' )
        f2.close()
    else:
        s =  "No se ha encontado a ningun "+palabra
        salida.write(s)
        salida.write( '\n' )
        salida.write( '\n' )

print("El archivo se ha generado correctamente.")