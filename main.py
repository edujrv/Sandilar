import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
        
    if message.content.startswith('$tony'):
        await message.channel.send('tony pancho barbaro')
    
    if message.content.startswith('$klan'):
        await message.channel.send('y no escucha perro para tu cucha')

    if message.content.startswith('$ricto'):
        await message.channel.send('Lo siento homie')

    if message.content.startswith('$autobardear'):
        await message.channel.send(message.author.mention + ' es un un uachin')


client.run(os.getenv('TOKEN'))




