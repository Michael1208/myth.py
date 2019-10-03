import discord 
import os
import asyncio
import time
from discord.ext import commands, tasks
from itertools import cycle

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():        
    await bot.change_presence(status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.watching, name="Watching Over DBH | !ping"))
    print("Mythical Python has started!")
    
@bot.command()
async def ping(ctx):
    start = time.monotonic()
    embed = discord.Embed(title="Mythical Python's Ping!", color=0x0084FD)
    embed.add_field(name="latency", value="{} ms".format(int(ctx.bot.latency*1000)))
    await ctx.send(embed=embed)
    
@bot.command()
async def slap(ctx):
    await ctx.send(f"**{ctx.author.display_name just slapped {Target.mention}!
    return
    
bot.run('NjIyMDYxODA4NDI5MDM5NjI3.XXudrw.FbMEm0MZjCbgT9RgEGSxqkCgkMc')
