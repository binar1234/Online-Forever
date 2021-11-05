import discord, os, keep_alive, asyncio, datetime, requests

from discord.ext import tasks, commands

client = commands.Bot(
  command_prefix=':',
  self_bot=True
)

async def on_ready():
    client.remove_command('help')
    await client.change_presence(status=discord.Status.online, activity=discord.Game("TESTING"))

keep_alive.keep_alive()
client.run(os.getenv("ODI4MDA4Mzg3NzQzOTczMzg3.YVRfCA.ml0ur8kP9u9pIhdzumeMsQHo2X0"), bot=False)
