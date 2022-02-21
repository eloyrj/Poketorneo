
from cProfile import label
from math import fabs
from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
import os
print(os.path.abspath(os.getcwd()))
rutaGeneral = os.path.abspath(os.getcwd())

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
    with open( ruta, 'r',encoding='utf-8') as archivo:
        separador = ':'
        data = {}
        
        for linea in archivo:
            value, key = linea.split(separador)
            data[key.strip()] = value.strip()

    return data

def cargarDiccionarios():
    return  cargarDiccionario(rutaGeneral + "/diccionario.txt"),cargarDiccionario(rutaGeneral + "/naturaleza.txt"),cargarDiccionario(rutaGeneral +"/habilidades.txt")

def compruebaMT(ataque):
    f2 = open(rutaLog,"r",encoding='utf-8')
    lines = f2.readlines()[2504:2595]
    for line in lines:
        
        mt = line.split(" ")[0]
        if(line.find(ataque)>0):
            return True, mt
        
    return False,mt

def generarArchivoConData():
    nivellb.config(text=" ")
    lb1.config(text=" ")
    PokemonAparece = False
    ataquesCorrectos = False
    naturalezaCorrecta = False
    HabilidadCorrecta = False
    
    
    f1 = open(rutaLectura)
    salida = open(rutaGeneral + "/salida.txt","w",encoding="utf-8")

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
        with open(rutaGeneral + "/evolucionesOrden.txt", 'r') as archivo:
        
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
interfaz.resizable(False, False)
interfaz.geometry('800x500')

bg = ImageTk.PhotoImage( Image.open("fondo.jpeg")) 
label1 = Label( interfaz, image = bg) 
label1.place(x = 0, y = 0, relwidth = 1, relheight = 1)

lb1 = Label(interfaz,text=" ",bg='#546e91',fg='white',font=("Century gothic", 13))
lb1.place(width=300,height=33, x=267,y=41)

nivellb = Label(interfaz,text=" ",bg='#546e91',fg='white',font=("Century gothic", 13))
nivellb.place(width=300,height=33, x=355,y=0)

imbutton = ImageTk.PhotoImage( Image.open("btnLog.png")) 
btn=Button(interfaz, text='Seleccion de Log',image=imbutton,command=abrirLog)
btn.place(width=162,height=35, x=0,y=0)

imbutton1 = ImageTk.PhotoImage( Image.open("btnEqui.png")) 
btn1=Button(interfaz, text='Seleccion de Equipo',image=imbutton1,command=abrirEquipo)
btn1.place(width=188,height=35, x=165,y=0)

imbutton2 = ImageTk.PhotoImage( Image.open("btnCom.png")) 
btn2=Button(interfaz, text='Comprobar Equipo ',image=imbutton2,command=generarArchivoConData)
btn2.place(width=195,height=35, x=72,y=41)

lb10 = Label(interfaz,text="  ",bg='#546e91',fg='white',font=("Century gothic", 13))
lb11 = Label(interfaz,text="  ",bg='#546e91',fg='white',font=("Century gothic", 13))
lb12 = Label(interfaz,text="  ",bg='#546e91',fg='white',font=("Century gothic", 13))
lb13 = Label(interfaz,text="  ",bg='#546e91',fg='white',font=("Century gothic", 13))
lb14 = Label(interfaz,text="  ",bg='#546e91',fg='white',font=("Century gothic", 13))
lb15 = Label(interfaz,text="  ",bg='#546e91',fg='white',font=("Century gothic", 13))
lb16 = Label(interfaz,text="  ",bg='#546e91',fg='white',font=("Century gothic", 13))
lb17 = Label(interfaz,text="  ",bg='#546e91',fg='white',font=("Century gothic", 13))
lb10.place(width=100,height=20, x=160,y=132)
lb11.place(width=100,height=20, x=160,y=156)
lb12.place(width=100,height=20, x=160,y=180)
lb13.place(width=100,height=20, x=160,y=204)
lb14.place(width=100,height=20, x=160,y=228)
lb15.place(width=100,height=20, x=160,y=252)
lb16.place(width=100,height=20, x=160,y=276)
lb17.place(width=100,height=20, x=160,y=300)
lbs = [lb10,lb11,lb12,lb13,lb14,lb15,lb16,lb17]


lb26 = Label(interfaz,text="  ",bg='#546e91',fg='white',font=("Century gothic", 13))
lb27 = Label(interfaz,text="  ",bg='#546e91',fg='white',font=("Century gothic", 13))
lb28 = Label(interfaz,text="  ",bg='#546e91',fg='white',font=("Century gothic", 13))
lb29 = Label(interfaz,text="  ",bg='#546e91',fg='white',font=("Century gothic", 13))
lb30 = Label(interfaz,text="  ",bg='#546e91',fg='white',font=("Century gothic", 13))
lb31 = Label(interfaz,text="  ",bg='#546e91',fg='white',font=("Century gothic", 13))
lb32 = Label(interfaz,text="  ",bg='#546e91',fg='white',font=("Century gothic", 13))
lb33 = Label(interfaz,text="  ",bg='#546e91',fg='white',font=("Century gothic", 13))
lb26.place(width=100,height=20, x=520,y=132)
lb27.place(width=100,height=20, x=520,y=156)
lb28.place(width=100,height=20, x=520,y=180)
lb29.place(width=100,height=20, x=520,y=204)
lb30.place(width=100,height=20, x=520,y=228)
lb31.place(width=100,height=20, x=520,y=252)
lb32.place(width=100,height=20, x=520,y=276)
lb33.place(width=100,height=20, x=520,y=300)
mtslb = [lb26,lb27,lb28,lb29,lb30,lb31,lb32,lb33]



interfaz.mainloop()



