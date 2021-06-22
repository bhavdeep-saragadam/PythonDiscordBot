import discord
from discord.ext import commands



client = commands.Bot(command_prefix="")

@client.event

async def on_ready():
        print('Bot Is Ready')

@client.command()
async def hello(ctx):
    await ctx.send("Sup")
@client.command()
async def hi(ctx):
    await ctx.send("Sup")


client.run('ODU2NzU3MjI2MjgyOTQyNDk0.YNFrWA.W2ADTmyXTJOkP90RGFK3LXxVec8')