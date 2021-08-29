#Imports
import discord
import os
import Eventos
#Fin imports

#python3 -m pip install -U discord.py  SI SE ROMPE USAR ESE COMANDO PARA IMPORTAR PACKETES DISCORD
client = discord.Client()


#Activacion
@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))
#Fin activacion

Eventos.evento(client)
client.run(os.getenv('TOKEN'))