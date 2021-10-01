#Imports
import discord
from discord.ext import commands
import music
import os
import Eventos
#Fin imports
#python3 -m pip install -U discord.py  SI SE ROMPE USAR ESE COMANDO PARA IMPORTAR PACKETES DISCORD

#keep alive
from keep_alive import keep_alive




client = discord.Client()


#Activacion
@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))



#Fin activacion

keep_alive()

Eventos.evento(client)
client.run(os.getenv('TOKEN'))