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
        await message.channel.send('tony es un pancho barbaro')

client.run('ODc5NDg3NzI1NTUwNTkyMDQy.YSQcxQ.Dm_SRAd88mBzW_pstUpEDpcFWFM')