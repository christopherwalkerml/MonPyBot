# bot.py
from CommandHandler import commandHandler

import discord

client = discord.Client()

@client.event
async def on_ready():
    print("MonPyBot has booted up!")

@client.event
async def on_message(message):
    await commandHandler(message)

client.run("Njc1MjI5ODEyMDIwODcxMjA4.Xj1VVg.NyZ3fUTGxDbnuonR3Ug6wbdpF4Y")