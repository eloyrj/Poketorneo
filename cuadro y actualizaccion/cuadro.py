from ast import Try


from pyglet import font
from cProfile import label
from glob import glob
import json
from math import fabs
from tkinter import *
from tkinter import filedialog
import traceback
from xml.etree.ElementPath import ops
from PIL import ImageTk, Image
import os
from cupshelpers import Printer
from matplotlib.pyplot import text
import openpyxl
import random
from os import remove

font.add_file('/home/corte/.local/share/fonts/Unknown Vendor/OpenType/Hogfish DEMO/Hogfish_Regular.ttf')
fonte = font.load('Hogfish Demo',11,bold=False,italic=False )

print(os.path.abspath(os.getcwd()))
rutaGeneral = os.path.abspath(os.getcwd())

rutaExcel =""

participantes = []


def abrirExcel():
    archivo = filedialog.askopenfilename()
    global rutaExcel
    rutaExcel = archivo
    leerRandomizar()
    
def leerRandomizar():
    global c
    global photo
    
    c.create_text(100, 280, text='tkinter canvas', fill='green')
    c.create_image(0, 0, image=photo, anchor=NW)
    
    global lbs
    excel_document = openpyxl.load_workbook(rutaExcel)
    sheet = excel_document['Respuestas de formulario 1']
    global participantes
    counter = 2
    participantes = []
    for i in range(20):
        valor ='E'+str(counter)
        participantes += [sheet[valor].value]
        counter+=1
    random.shuffle(participantes)
    for i in range(20):
        c.create_text(lbs[i][0],lbs[i][1],text=participantes[i],font="HogfishDEMO")
    
    print(participantes)
    
def ponerJugadores():
    
    
    global lbs
    global participantes
    for i in range(20):
        c.create_text(lbs[i][0],lbs[i][1],text=participantes[i],font='HogfishDEMO')
    
    
    


interfaz = Tk()
interfaz.title("Sorteo Cuadro")
interfaz.resizable(False, False)
interfaz.geometry('1920x1080')


im = Image.open("cuadro.png")
im = im.resize((1920,1080),1)
interfaz.tk.call('wm', 'iconphoto', interfaz._w, ImageTk.PhotoImage(file="logo.png"))


c = Canvas(width=1920, height=1080, bg='white')
c.pack(expand=YES, fill=BOTH)
photo=ImageTk.PhotoImage(im)
c.create_text(100, 280, text='tkinter canvas', fill='green')
c.create_image(0, 0, image=photo, anchor=NW)
btn=Button(interfaz, text='Seleccion de Log',command=abrirExcel)
btn.place(width=162,height=35, x=0,y=0)

lbs =[
(144,258),
(144,318),
(362,365),
(362,424),
(362,483),
(362,601),
(362,660),
(362,717),
(144,761),
(144,818),

(1769,258),
(1769,318),
(1551,365),
(1551,424),
(1551,483),
(1551,601),
(1551,660),
(1551,712),
(1769,761),
(1769,818),
]



try:
    with open('data.json') as file:
    
        participantes = json.load(file)
        print(participantes)
        ponerJugadores()
        remove('data.json')
        
except:
    print("no se pudo cargar el log")
   
        

    

    

interfaz.mainloop()

with open('data.json', 'w') as file:
    json.dump(participantes,file)

