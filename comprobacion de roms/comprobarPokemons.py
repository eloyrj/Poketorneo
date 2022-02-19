
from cProfile import label
from math import fabs
import mmap
import sys
from tkinter import *
from tkinter import filedialog


from matplotlib.pyplot import title


rutaLog =""
rutaLectura =""
nPokemons = 6

def abrirLog():
    archivo = filedialog.askopenfilename()
    global rutaLog
    rutaLog = archivo
    
def abrirEquipo():
    archivo = filedialog.askopenfilename()
    global rutaLectura 
    rutaLectura= archivo

def cargarDiccionario(ruta):
    with open(ruta, 'r') as archivo:
        separador = ':'
        data = {}
        
        for linea in archivo:
            value, key = linea.split(separador)
            data[key.strip()] = value.strip()

    return data

def cargarDiccionarios():
    return  cargarDiccionario('archivos/diccionario.txt'),cargarDiccionario('archivos/naturaleza.txt') , cargarDiccionario('archivos/habilidades.txt')

def compruebaMT(ataque):
    f2 = open(rutaLog,"r",encoding='utf-8')
    lines = f2.readlines()[2504:2595]
    for line in lines:
        
        mt = line.split(" ")[0]
        if(line.find(ataque)>0):
            return True, mt
        
    return False,mt

def generarArchivoConData():

    PokemonAparece = False
    ataquesCorrectos = False
    naturalezaCorrecta = False
    HabilidadCorrecta = False
    
    
    f1 = open(rutaLectura)
    salida = open("salida.txt","w",encoding="utf-8")

    f2 = open(rutaLog,"r",encoding='utf-8')
    with f2 as myfile:
        total_lines = sum(1 for line in myfile)
    f2.close()

    repetidas = 0
    encontrado = False
    bajo = 0
    alto = 10
    for p in range(nPokemons):
        #-------------------------------------------------------------------------------------------------------------------------
        f1 = open(rutaLectura)
        pala = f1.readlines()[bajo:alto]
        sete = pala[0].split(" ")
        if len(sete)>3:
            pokemon = sete[1][1:(len(sete[1])-1)]
        else:
            pokemon = sete[0]
            
        evoluciones = []
        with open("archivos/evolucionesOrden.txt", 'r') as archivo:
        
            for linea in archivo:
                if linea.find(pokemon)>=0:
                    value= linea.split(":")
                    for i in range(len(value)):
                        if i != (len(value)-1):
                            evoluciones += [value[i]]
        
        nivel = pala[2].split(" ")[1]
        nivel = int(nivel)
        if nivel <= 50:
            nivelValido = True
        else:
            nivelValido = False
            nivellb.config(text="El Pokemon "+ pokemon +" es Nivel: "+str(nivel))
        
    
                        


        pokemon = pokemon.upper()
        habilidadapoyo  = pala[1].split(" ")[1:len(pala[1].split(" ")[1:])-1]
        habilidadIngles = ""
        for j in habilidadapoyo:
            if j != habilidadapoyo[len(habilidadapoyo)-1]:
                habilidadIngles = habilidadIngles+j+" "
            else:
                habilidadIngles = habilidadIngles+j
            
        habilidad = diccionarioHabilidades.get(habilidadIngles.upper())

        naturalezaIngles = pala[4].split(" ")[0]
        naturaleza = diccionarioNaturaleza.get(naturalezaIngles)
        
        if pala[5].split(" ")[0].strip() == "IVs:":
            longi = 10
        else:
            longi = 9
        
       

        ataque1apoyo = pala[(longi-4)].split(" ")[1:len(pala[(longi-4)].split(" "))-2]
        ataque1Ingles = ""
        for i in ataque1apoyo:
            if i != ataque1apoyo[len(ataque1apoyo)-1]:
                ataque1Ingles = ataque1Ingles+i+" "
            else:
                ataque1Ingles = ataque1Ingles+i
        ataque1 = diccionarioAtaques.get(ataque1Ingles)

        ataque2apoyo = pala[(longi-3)].split(" ")[1:len(pala[(longi-3)].split(" "))-2]
        ataque2Ingles = ""
        for i in ataque2apoyo:
            if i != ataque2apoyo[len(ataque2apoyo)-1]:
                ataque2Ingles = ataque2Ingles+i+" "
            else:
                ataque2Ingles = ataque2Ingles+i
        ataque2 = diccionarioAtaques.get(ataque2Ingles)

        ataque3apoyo = pala[(longi-2)].split(" ")[1:len(pala[(longi-2)].split(" "))-2]
        ataque3Ingles = ""
        for i in ataque3apoyo:
            if i != ataque3apoyo[len(ataque3apoyo)-1]:
                ataque3Ingles = ataque3Ingles+i+" "
            else:
                ataque3Ingles = ataque3Ingles+i
        ataque3 = diccionarioAtaques.get(ataque3Ingles)

        ataque4apoyo = pala[(longi-1)].split(" ")[1:len(pala[(longi-1)].split(" "))-2]
        ataque4Ingles = ""
        for i in ataque4apoyo:
            if i != ataque4apoyo[len(ataque4apoyo)-1]:
                ataque4Ingles = ataque4Ingles+i+" "
            else:
                ataque4Ingles = ataque4Ingles+i
        ataque4 = diccionarioAtaques.get(ataque4Ingles)
        
       
        
        lbs[p].config(text=naturaleza)
            
        PosicionTexto = -1
        NumeroLinea = 0
        #------------------------------------------------------------------------------------------
        PokemonAparece = False
        ataquesCorrectos = False
        naturalezaCorrecta = False
        HabilidadCorrecta = False
        ataque1Correctos = False
        ataque2Correctos = False
        ataque3Correctos = False
        ataque4Correctos = False
        
        
        for h in evoluciones:
            pokemon = h.upper()
            
            f2 = open(rutaLog,"r",encoding='utf-8')
            
            lines = f2.readlines()[1944:2501]
            encontrado= False
        
            for line in lines:
                
                NumeroLinea = NumeroLinea + 1
                PosicionTexto = line.find(pokemon)
                if PosicionTexto >= 0:
                    encontrado =True
                    s =  "hay un " + pokemon + " en la linea "+ str(NumeroLinea)
                    salida.write(s)
                    salida.write(" --> ")
                    salida.write(line)
                    PokemonAparece = True
                
            f2.close()
            if(encontrado):

                f2 = open(rutaLog,"r",encoding='utf-8')
                lines = f2.readlines()[520:1012]
                for line in lines:
                    NumeroLinea = NumeroLinea + 1
                    PosicionTexto = line.find(pokemon)
                    if PosicionTexto >= 0:
                        s =  "Tiene los ataques "
                        salida.write(s)
                        salida.write(" --> ")
                        salida.write(line)
                        
                        
                        if line.find(ataque1)>=0: 
                            ataque1Correctos = True
                        
                            
                        if line.find(ataque2)>=0 : 
                            ataque2Correctos = True
                        
                            
                        if line.find(ataque3)>=0: 
                            ataque3Correctos = True
                        
                            
                        if  line.find(ataque4)>=0:
                            ataque4Correctos = True
                        
                            
                        if ataque1Correctos and ataque2Correctos and ataque3Correctos and ataque3Correctos and ataque4Correctos :
                            print("los ataques estan bien "+ pokemon)
                            ataquesCorrectos = True
                            
                f2.close()


                f2 = open(rutaLog,"r",encoding="utf-8")
                lines = f2.readlines()[3:495]
                for line in lines:       
                    NumeroLinea = NumeroLinea + 1
                    PosicionTexto = line.find(pokemon)
                    if PosicionTexto >= 0:                
                        s =  "Tiene las Stats a nivel 50 "
                        salida.write(s)
                        salida.write(" --> ")
                        salida.write(line)    
                        if(habilidad == None):
                            print("habilidad no encontrada")
                            return False
                        
                        if habilidad ==   line.split("|")[9].upper().strip() or habilidad == line.split("|")[10].upper().strip():
                            print( "la habilidad es correcta")
                            HabilidadCorrecta = True
                        
                            
                salida.write( '\n' )
                f2.close()
                if(HabilidadCorrecta and ataquesCorrectos and PokemonAparece and nivelValido):
                    break
            
        else:
            s =  "No se ha encontado a ningun "+pokemon
            salida.write(s)
            salida.write( '\n' )
            salida.write( '\n' )
        
        if not ataquesCorrectos:
            
            if compruebaMT(ataque1)[0] and not ataque1Correctos:
                ataque1Correctos = True
                mtslb[p].config(text=compruebaMT(ataque1)[1])
                
            if compruebaMT(ataque2)[0] and not ataque2Correctos:
                ataque2Correctos = True 
            mtslb[p].config(text=compruebaMT(ataque2)[1])
            
            if compruebaMT(ataque3)[0] and not ataque3Correctos:
                ataque3Correctos = True
                mtslb[p].config(text=compruebaMT(ataque3)[1])
            
            if compruebaMT(ataque4)[0]:
                ataque4Correctos = True
                mtslb[p].config(text=compruebaMT(ataque4)[1])
            
            if ataque1Correctos and ataque2Correctos and ataque3Correctos and ataque3Correctos and ataque4Correctos :
                print("los ataques estan bien "+ pokemon)
                ataquesCorrectos = True
            
            
        
        bajo = bajo + longi+1
        alto = alto + longi+1
        if (not HabilidadCorrecta or not ataquesCorrectos or not PokemonAparece or not nivelValido):
            lb1.config(text="El Equipo NO Es Valido")
            print(False)
            return False
        
                
        

    print("El archivo se ha generado correctamente.")
    lb1.config(text="El Equipo Es Valido")
    return True




c = cargarDiccionarios()
diccionarioAtaques=c[0]
diccionarioNaturaleza=c[1]
diccionarioHabilidades=c[2]



interfaz = Tk()
interfaz.title("Comprobacin De Roms")
interfaz.resizable(True, True)
interfaz.geometry('800x500')


lb1 = Label(interfaz,text="")
lb1.grid(column=1,row=2)
nivellb = Label(interfaz,text="")
nivellb.grid(column=2,row=0)

btn=Button(interfaz, text='Seleccion de Log',command=abrirLog,).grid(column=0,row=0)

btn1=Button(interfaz, text='Seleccion de Equipo',command=abrirEquipo).grid(column=1,row=0)
btn2=Button(interfaz, text='Comprobar Equipo ',command=generarArchivoConData).grid(column=0,row=2)

lb2 = Label(interfaz,text="Naturaleza Pokemon 1:")
lb3 = Label(interfaz,text="Naturaleza Pokemon 2:")
lb4 = Label(interfaz,text="Naturaleza Pokemon 3:")
lb5 = Label(interfaz,text="Naturaleza Pokemon 4:")
lb6 = Label(interfaz,text="Naturaleza Pokemon 5:")
lb7 = Label(interfaz,text="Naturaleza Pokemon 6:")
lb8 = Label(interfaz,text="Naturaleza Pokemon 7:")
lb9 = Label(interfaz,text="Naturaleza Pokemon 8:")
lb2.grid(column=0,row=3)
lb3.grid(column=0,row=4)
lb4.grid(column=0,row=5)
lb5.grid(column=0,row=6)
lb6.grid(column=0,row=7)
lb7.grid(column=0,row=8)
lb8.grid(column=0,row=9)
lb9.grid(column=0,row=10)

lb10 = Label(interfaz,text=" ")
lb11 = Label(interfaz,text=" ")
lb12 = Label(interfaz,text=" ")
lb13 = Label(interfaz,text=" ")
lb14 = Label(interfaz,text=" ")
lb15 = Label(interfaz,text=" ")
lb16 = Label(interfaz,text=" ")
lb17 = Label(interfaz,text=" ")
lb10.grid(column=1,row=3)
lb11.grid(column=1,row=4)
lb12.grid(column=1,row=5)
lb13.grid(column=1,row=6)
lb14.grid(column=1,row=7)
lb15.grid(column=1,row=8)
lb16.grid(column=1,row=9)
lb17.grid(column=1,row=10)
lbs = [lb10,lb11,lb12,lb13,lb14,lb15,lb16,lb17]

lb18 = Label(interfaz,text="MT Pokemon 1:")
lb19 = Label(interfaz,text="MT Pokemon 2:")
lb20 = Label(interfaz,text="MT Pokemon 3:")
lb21 = Label(interfaz,text="MT Pokemon 4:")
lb22 = Label(interfaz,text="MT Pokemon 5:")
lb23 = Label(interfaz,text="MT Pokemon 6:")
lb24 = Label(interfaz,text="MT Pokemon 7:")
lb25 = Label(interfaz,text="MT Pokemon 8:")
lb18.grid(column=2,row=3)
lb19.grid(column=2,row=4)
lb20.grid(column=2,row=5)
lb21.grid(column=2,row=6)
lb22.grid(column=2,row=7)
lb23.grid(column=2,row=8)
lb24.grid(column=2,row=9)
lb25.grid(column=2,row=10)
lb26 = Label(interfaz,text=" ")
lb27 = Label(interfaz,text=" ")
lb28 = Label(interfaz,text=" ")
lb29 = Label(interfaz,text=" ")
lb30 = Label(interfaz,text=" ")
lb31 = Label(interfaz,text=" ")
lb32 = Label(interfaz,text=" ")
lb33 = Label(interfaz,text=" ")
lb26.grid(column=3,row=3)
lb27.grid(column=3,row=4)
lb28.grid(column=3,row=5)
lb29.grid(column=3,row=6)
lb30.grid(column=3,row=7)
lb31.grid(column=3,row=8)
lb32.grid(column=3,row=9)
lb33.grid(column=3,row=10)
mtslb = [lb26,lb27,lb28,lb29,lb30,lb31,lb32,lb33]

interfaz.mainloop()



