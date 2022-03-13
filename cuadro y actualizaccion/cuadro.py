from cProfile import label
from math import fabs
from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
import os
from matplotlib.pyplot import text
import openpyxl
import random

print(os.path.abspath(os.getcwd()))
rutaGeneral = os.path.abspath(os.getcwd())

rutaExcel =""
lbs = []


def abrirExcel():
    archivo = filedialog.askopenfilename()
    global rutaExcel
    rutaExcel = archivo
    leerRandomizar()
    
def leerRandomizar():
    global lbs
    excel_document = openpyxl.load_workbook(rutaExcel)
    sheet = excel_document['Respuestas de formulario 1']
    participantes = []
    counter = 2
    for i in range(64):
        valor ='E'+str(counter)
        participantes += [sheet[valor].value]
        counter+=1
    random.shuffle(participantes)
    for i in range(64):
        lbs[i].config(text=participantes[i])
    
    print(participantes)
    


interfaz = Tk()
interfaz.title("Comprobacin De Roms")
interfaz.resizable(False, False)
interfaz.geometry('800x610')

bg = ImageTk.PhotoImage( Image.open("tabla.jpg")) 
label1 = Label( interfaz, image = bg) 
label1.place(x = 0, y = 0, relwidth = 1, relheight = 1, )

btn=Button(interfaz, text='Seleccion de Log',command=abrirExcel)
btn.place(width=162,height=35, x=0,y=0)

factorSuma = 16.5
altura = 64
for i in range(32):
    
    lbs += [Label(interfaz,text="  ")]
    lbs[i].place(width=60,height=11, x=37,y=altura)
    if i == 15:
        altura += factorSuma +5;
    else:
        altura += factorSuma ;

factorSuma = 16.5
altura = 64

for i in range(32,64):
    
    lbs += [Label(interfaz,text="  ")]
    lbs[i].place(width=60,height=11, x=703,y=altura)
    if i == 47:
        altura += factorSuma +5;
    else:
        altura += factorSuma ;
    

interfaz.mainloop()

