# # A discord bot to control a minecraft server using chat

import discord
from mcrcon import MCRcon
import os

# Set RCON_PASSWORD and DISCORD_TOKEN as environment variables to prevent evil

# RCON should be run on a local network since passwords
# are sent in plaintext over the web
RCON_SERVER = os.getenv('RCON_SERVER')
RCON_PASSWORD = os.getenv('RCON_PASSWORD')
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')

if RCON_PASSWORD == "":
    raise ValueError("RCON_PASSWORD has not been set in as an environment variable")

if DISCORD_TOKEN == "":
    raise ValueError("DISCORD_TOKEN has not been set in as an environment variable")

if RCON_SERVER == "":
    raise ValueError("RCON_SERVER has not been set in as an environment variable")

# Create discord client
client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('//'):

        if message.content == "//" or message.content == "//help":
            await message.channel.send("""
            Help for Archecord
            Run any Minecraft command as normal using '//' as a prefix, instead of the standard single slash.
            You cannot run '/op', '/deop', '/kill', '/stop' or '/give' here.
            """)
            return

        if "//op" in message.content:
            await message.channel.send("Cannot use that command here")
            return

        if "//deop" in message.content:
            await message.channel.send("Cannot use that command here")
            return

        if "//stop" in message.content:
            await message.channel.send("Cannot use that command here")
            return

        if "//kill" in message.content:
            await message.channel.send("Cannot use that command here")
            return

        if "//give" in message.content:
            await message.channel.send("Cannot use that command here")
            return

        COMMAND = message.content.replace("//", "/", 1)
        print(COMMAND)
        with MCRcon(RCON_SERVER, RCON_PASSWORD) as mcr:
            resp = mcr.command(COMMAND)
            print(resp)
            await message.channel.send(resp)

client.run(DISCORD_TOKEN)