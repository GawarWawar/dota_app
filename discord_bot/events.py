import asyncio
from discord.ext import commands
# from starter import send_custom_message, new_event, bot
    
import os
import signal
import sys
import time
from dotenv import load_dotenv
import subprocess

# async def main():
#     load_dotenv()
#     TOKEN = os.getenv('DISCORD_TOKEN')    
#     await bot.login(TOKEN)
    
#     await send_custom_message(None, 778031925315108934, "HI!")
#     await bot.close()
    
# bot.add_listener(main)

# current working directory

async def kill_process(process_to_kill):
    os.killpg(os.getpgid(process_to_kill.pid), signal.SIGTERM) 
    

if __name__ == "__main__":
    print('File name :    ', os.path.basename(__file__))
    print('Directory Name:     ', )
    # process = subprocess.run(['python3', 'discord_bot/starter.py'])
    pro = subprocess.Popen(
        str('python3'+" "+'discord_bot/starter.py'), 
        shell=True,
    ) 

    asyncio.sleep(10)
    kill_process(pro)