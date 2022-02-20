
import openpyxl
import random

excel_document = openpyxl.load_workbook('torneo randomlock.xlsx')

sheet = excel_document['Respuestas de formulario 1']

valores = [sheet['M69'].value,sheet['M70'].value,sheet['M71'].value,sheet['M72'].value,sheet['M73'].value,sheet['M74'].value]
random.shuffle(valores)


sheet['D71'].value= valores[0]
sheet['D74'].value= valores[1]
sheet['D75'].value= valores[2]
sheet['D78'].value= valores[3]
sheet['D79'].value= valores[4]
sheet['D82'].value= valores[5]

excel_document.save('m.xlsx')

