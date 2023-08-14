import os

import discord

from llm import getResponse
from keep_alive import keep_alive

DISCORD_TOKEN = os.environ['DISCORD_TOKEN']

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
  print(f'We have logged in as {client.user}')


@client.event
async def on_message(message):
  if message.author == client.user:
    return

  call = '$llm '
  if message.content.startswith(call):
    response = getResponse(message.content.split(call)[1])
    await message.channel.send(response.content)


keep_alive()
client.run(DISCORD_TOKEN)
