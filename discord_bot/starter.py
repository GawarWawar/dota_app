# bot.py
import os

import discord
from discord.ext import commands, tasks
from discord import client
import builtins
import sys
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(
    "!",
    intents = discord.Intents.all()
)

@bot.event
async def on_ready():

    for guild in bot.guilds:
        print(
            f'{bot.user} is connected to the following guild:\n'
            f'{guild.name}(id: {guild.id})\n'
        )
        channels = "\n -".join(f"{channel.name}, {channel.id}" for channel in guild.channels)
        members = '\n - '.join([member.name for member in guild.members])
        with open("random_file.txt", "w") as f:
            f.write(f'Guild Channels:\n - {channels}')
            f.write(f'Guild Members:\n - {members}')
            
        send_message.start() 
        # sys.exit()


@tasks.loop(seconds=10)
async def send_message():
    channel = bot.get_channel(778031925315108934)  # Replace with your channel ID
    print("channel:", channel)
    if channel:
        await channel.send(f"This is a message sent every {10} seconds")

@bot.command()
async def send_custom_message(ctx, message):
    guild = bot.get_guild(523494625303068712)
    channel = guild.get_channel(778031925315108934)
    await channel.send(message)
    await ctx.channel.send(message)

bot.listen()
async def new_event ():
    print("Here!")
    desired_channel_name = "welcome"
    print(bot.is_ready())

    for guild in bot.guilds:
        for channel in guild.channels:
            print(channel.name)
            if channel.name == desired_channel_name: 
                channel.send("HI!")


# if __name__ == "__main__":
bot.run(TOKEN)
