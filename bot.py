import discord
from discord.ext import commands

client = commands.bot(command_prefix = '$')

@client.event
async def on_ready():
print('Bot is ready.')

client.run('OTQ3MDEzNDE5Nzc5ODg3MTE2.YhnE-Q.gZ_8htObgsmocVu8-GAq9_VfEws')
