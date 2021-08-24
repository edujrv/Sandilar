#Imports
import discord
import os
import random
from Horario import *
#Fin imports

#python3 -m pip install -U discord.py  SI SE ROMPE USAR ESE COMANDO PARA IMPORTAR PACKETES DISCORD
client = discord.Client()

#Funciones
def recordatorio_constructor(frase):
    frase = frase.replace("$nh ","").split(";")
    frase = frase.split(";")
    
    
    '''
    dia = frase[0]
    mes = frase[1]              (opcional) -> Mes actual
    ano = frase[2]            (opcional) -> Año actual
    hora = frase[3]            (opcional)  -> No importa 
    minuto = frase[4]         (opcional) -> No importa 
    materia/curso = frase[5]  (opcional) -> No importa 
    descripcion = frase[6]
    '''
    return frase

def bardeo():
    file = open("insultos.txt")

    contenido = file.readlines()

    palabras = []

    for line in contenido:
        palabras.append(line.replace('\n',''))

    return palabras[random.randint(0,len(palabras)-1)]
#Fin funciones

#Activacion
@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))
#Fin activacion

#Eventos
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    mensaje = message.content.split(" ")
    if (mensaje[0] == "$tony"):
        await message.channel.send('tony pancho barbaro')

    if (mensaje[0] == "$hater"):
        await message.channel.send('Segun paginas oficiales como Wikipedia y resultados analiticos de laboratorios de investigacion a nivel mundial, esta comprobado que '+message.mentions[0].mention+' es el mas hater')
    
    if (mensaje[0] == "$klan"):
        await message.channel.send('Esto es una pelota, esto es un pelotudo!!')
        await message.channel.send('https://i.ytimg.com/vi/4fEm0agWpXA/maxresdefault.jpg')
        await message.channel.send('https://img.redbull.com/images/c_fill,g_auto,w_860,h_1229/q_auto,f_auto/redbullcom/2020/11/5/xn1jqonq5eepwycucuxw/klan')

    if (mensaje[0] == "$ricto"):
        await message.channel.send('Lo siento homie')

    if (mensaje[0] == "$autobardear"):
        await message.channel.send(message.author.mention + ' es un un uachin')

    if (mensaje[0] == "$strike"):
	    await message.channel.send('Que te pasa Strike?')
        
    if (mensaje[0] == "$bardear"):
        await message.channel.send(message.mentions[0].mention + " sos un " + bardeo())
    
    if (mensaje[0] == "$nh"):
        recordatorio_constructor(message.content)
          # $nh '"Descripcion"' '"Materia o Curso"'(opcional) 'Año-Mes-Día-Hora-Minutos' 
        frase = message.content.replace("$nh ","")
        frase = frase.split(";")
        dia = frase[0]
        mes = frase[1]
        ano = frase[2]
        hora = frase[3]
        minuto = frase[4]
        materia = frase[5]
        descripcion = frase[6]
        
        #await message.channel.send(desc[1]," ",desc[2])
        await message.channel.send(dia + "/" + mes + "/" + ano + " - " + hora + ":" + minuto + " - " + materia + " - " + descripcion)
        
        #           dia     mes     ano     hora     materia     actividad
        #   $nh     05;     08;     2021;   15:00;  auditoria;   curso

        cond_descripcion = False
        descripcion = ""
        for i in mensaje:
            if i == ' " ' and cond_descripcion == False:
                cond_descripcion = True
                continue
            if i == ' " ' and cond_descripcion == True:
                cond_descripcion = True
                break
            if cond_descripcion:
                descripcion += i
        print(descripcion)
                

        #await message.channel.send('https://i.imgur.com/TrTObBQ.jpg')
#Fin eventos

client.run(os.getenv('TOKEN'))




