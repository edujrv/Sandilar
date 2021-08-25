#Imports
import discord
import os
import random
from Anotacion import *
from datetime import datetime
#Fin imports

#python3 -m pip install -U discord.py  SI SE ROMPE USAR ESE COMANDO PARA IMPORTAR PACKETES DISCORD
client = discord.Client()

#Funciones
def recordatorio_constructor(frase):
    frase = frase.replace("$na ","").split(";")
#    frase = frase.split(";")
    frase_final = ["?","?","?","?","?","?","?"]

    fecha = frase[0].split("/")
    desc = frase[-1]
    hora = ["?","?"]
    materia = "?"

    if(len(fecha) == 1):
        fecha.append(str(datetime.now().month))
        fecha.append(str(datetime.now().year))
    elif(len(fecha) == 2):
        fecha.append(str(datetime.now().year))


    if (len(frase) == 3):                 #Puede ser hora o materia
        frase_aux = frase[1].split(":")
        if(frase_aux[0].isnumeric()):       #Se trata de una hora
            hora[0] = frase_aux[0]
            if(len(frase_aux) == 1):        #Solo hora  
                hora[1] = "00"
            else:                           #hora y minuto
                hora[1] = frase_aux[1]
        else:                               #Es la materia
            materia = frase[1]
    
    if(len(frase) == 4):
        frase_aux = frase[1].split(":")
        hora[0] = frase_aux[0]
        if(len(frase_aux) == 1):        #Solo hora  
            hora[1] = "00"
        else:                           #hora y minuto
            hora[1] = frase_aux[1]
        materia = frase[2]
                                    
    frase_final[0] = fecha[0]
    frase_final[1] = fecha[1]
    frase_final[2] = fecha[2]

    frase_final[3] = hora[0]
    frase_final[4] = hora[1]

    frase_final[5] = materia.lower()

    frase_final[6] = desc.lower()

    print(frase_final)
    

    
    '''
    dia = frase[0]
    mes = frase[1]              (opcional) -> Mes actual
    ano = frase[2]            (opcional) -> Año actual
    hora = frase[3]            (opcional)  -> No importa 
    minuto = frase[4]         (opcional) -> No importa 
    materia/curso = frase[5]  (opcional) -> No importa 
    descripcion = frase[6]
    '''
    return frase_final

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
        await message.channel.send('tony es un bot y pancho barbaro')
        await message.channel.send('https://media.discordapp.net/attachments/698233666601484379/880130562956853258/unknown.png')

    if (mensaje[0] == "$hater"):
        await message.channel.send('Segun paginas oficiales como Wikipedia y resultados analiticos de laboratorios de investigacion a nivel mundial, esta comprobado que '+message.mentions[0].mention+' es el mas hater')
    
    if (mensaje[0] == "$klan"):
        await message.channel.send('Esto es una pelota, esto es un pelotudo!!')
        await message.channel.send('https://i.ytimg.com/vi/4fEm0agWpXA/maxresdefault.jpg')

    if (mensaje[0] == "$ricto"):
        await message.channel.send('Lo siento homie')

    if (mensaje[0] == "$autobardear"):
        await message.channel.send(message.author.mention + ' es un un uachin')

    if (mensaje[0] == "$horario"):
	    await message.channel.send('https://media.discordapp.net/attachments/821355545838485535/877535911309635624/unknown.png')

    if(mensaje[0] == "$sandi"):
      await message.channel.send('Este soy yo, bonito no?')
      await message.channel.send('https://cdn5.dibujos.net/dibujos/pintados/201627/trozo-de-sandia-comida-frutas-10712724.jpg')

    if(mensaje[0] == "$help"):
      await message.channel.send('Te voy a dar una ayudita, puedes usarme con: \n```▁ ▂ ▄ ▅ ▆ ▇ █ 𝕃𝕀𝕊𝕋𝔸 𝔻𝔼 ℂ𝕆𝕄𝔸ℕ𝔻𝕆𝕊 █ ▇ ▆ ▅ ▄ ▂ ▁\n$tony\n$hater\n$klan ♥\n$ricto\n$autobardear\n$horario\n$sandi\n$celebrar\n$bardear\n$na```')

    if(mensaje[0] == "$celebrar"):
      await message.channel.send('¡¡A CELEBRAR!!')
      await message.channel.send('https://i.pinimg.com/originals/c9/ae/85/c9ae85b4431228f0d59e2ab9e4515378.gif')
        
    if (mensaje[0] == "$bardear"):
        await message.channel.send(message.mentions[0].mention + " sos un " + bardeo())
    
    if (mensaje[0] == "$na"):
        frase = recordatorio_constructor(message.content)
          # $nh '"Descripcion"' '"Materia o Curso"'(opcional) 'Año-Mes-Día-Hora-Minutos' 
        
        #frase = message.content.replace("$nh ","")
        #frase = frase.split(";")
        dia = frase[0]
        mes = frase[1]
        ano = frase[2]
        hora = frase[3]
        minuto = frase[4]
        materia = frase[5]
        descripcion = frase[6]
    
        print("\n\n\n")
        print(frase)

        agendado = dia + "/" + mes + "/" + ano + " - "
        if( not hora == '?'):
            agendado += hora
        if(not minuto == '?'):
            agendado += ":"+minuto + " - "
        if(not materia == '?'):
            agendado += materia + " - "
        agendado += descripcion

        
        print(agendado)

        await message.channel.send(agendado)
        
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




