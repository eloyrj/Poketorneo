from email.mime.image import MIMEImage

import random
import openpyxl
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders, message
import os

rutaGeneral = os.path.abspath(os.getcwd())


        
        


def cargarDiccionario(ruta):
    with open( ruta, 'r',encoding='utf-8') as archivo:
        separador = ' '
        data = {}
        for linea in archivo:
            key,value = linea.split(separador)
            data[key.strip()] = value.strip()

    return data

def leerCorreos():
    correos = []
    nombres=[]
    excel_document = openpyxl.load_workbook("prueba.xlsx")
    sheet = excel_document['Respuestas de formulario 1']
    counter = 2
    for i in range(64):
        valor ='B'+str(counter)
        if(sheet[valor].value != None):
            correos += [sheet[valor].value]
            valor ='E'+str(counter)
            nombres += [sheet[valor].value]
        counter+=1
    
    
    return correos,nombres
    
def envioDeCorreos():
    salida = open(rutaGeneral + "/salida.txt","w",encoding="utf-8")
    
    remitente = 'cortecerito@gmail.com'
    asunto = 'Poketorneo: Envio de Rom'
    
    
    
    # Establecemos los atributos del mensaje
    correos = leerCorreos()
    roms = cargarDiccionario("roms.txt")
    
    
    
    
    for i in range(0,len(correos[0])):
        mensaje = MIMEMultipart()
        mensaje['From'] = remitente
        mensaje['To'] = correos[0][i]
        mensaje['Subject'] = asunto
        file = open("logoLue.jpg", "rb")
        attach_image = MIMEImage(file.read(),_subtype="jpeg")
    
        html = """\
        <html>
        <head></head>
        <body>
            <p>Hola, Somos tus amigos de Poketorneo<br><br>
            Esta es tu rom para el torneo recuerda que no la puedes cambiar sin nuestra supervision.<br>
            Esta es tu <a href=""" +roms.get(str(i))+""">Rom</a>.<br>
            <br>
            ¡Hazte con Todos!
            <br>
            Un Saludo, <a href="https://poketorneo.site/">Poketorneo</a>
            <br>
            <br>
            
            
            <a href="https://linktr.ee/L.U.E">LUE</a>

            </p>
        </body>
        </html>
        """
        hola = MIMEText(html , 'HTML')

        mensaje.attach(hola)
        
        sesion_smtp = smtplib.SMTP('smtp.gmail.com', 587)
        sesion_smtp.starttls()
        sesion_smtp.login('liga.universitaria.espanola@gmail.com','iqccgzkxbnpttlas')
        texto = mensaje.as_string()
        sesion_smtp.sendmail(remitente, correos[0][i], texto)
        
        
        salida.write("Se ha enviado la rom ")
        salida.write(str(i))
        salida.write(" al jugador ")
        salida.write(str(correos[1][i]))
        salida.write(" con correo ")
        salida.write(correos[0][i])
        salida.write(" y se encuentra en el link ")
        salida.write(roms.get(str(i)))
        salida.write("\n")

    sesion_smtp.quit()
    salida.close()    
    
    

e = leerCorreos()
print (e[0])
print(e[1])
envioDeCorreos()