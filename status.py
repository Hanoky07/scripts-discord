import os 
import time
os.system("clear")

TOKENHERE = "token_da_sua_conta"
APPID = id do app

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

print(f"{bcolors.WARNING}DISCORD STATUS{bcolors.ENDC}")
time.sleep(1.5)
print(f"{bcolors.UNDERLINE}                           {bcolors.ENDC}")
print("")
print(f"{bcolors.OKBLUE}Importando os pacotes{bcolors.ENDC}")
print(f"{bcolors.UNDERLINE}                           {bcolors.ENDC}")
print("")
time.sleep(2.0)
print ("\033[A                             \033[A")
print ("\033[A                             \033[A")
print ("\033[A                             \033[A")
print ("\033[A                             \033[A")
print(f"{bcolors.OKBLUE}completo{bcolors.ENDC}")
print("")

import datetime
import discord
import asyncio
from discord.ext import commands
import threading

presentDate = datetime.datetime.now() 
unix_timestamp = datetime.datetime.timestamp(presentDate)*1000


entercmd = 'na'
prefix = '!!'
client = discord.Client()
name1 = input("Nome da aplicação: ")
print("")
detail1 = input("Detalhes: ")
print("")
state1 = input("Status: ")
print("")
print(f"{bcolors.WARNING}BETA{bcolors.ENDC} Tempo percorrido")
elapsed1 = input("[n para não ativar o tempo decorrido]: ")

imagekey1 = "imagekey1"

bot = commands.Bot(command_prefix=prefix, self_bot=True)


status = bot.change_presence(activity=discord.Activity(application_id=APPID, name=name1, type=discord.ActivityType.playing, state=state1, details=detail1, assets={'large_image_key' : imagekey1, 'large_text' : 'image'}, timestamps={'start' : unix_timestamp}))
status1 = bot.change_presence(activity=discord.Activity(application_id=APPID, name=name1, type=discord.ActivityType.playing, state=state1, details=detail1, assets={'large_image_key' : imagekey1, 'large_text' : 'image'}))

@bot.event 
async def on_ready():
    print(f"{bcolors.UNDERLINE}                           {bcolors.ENDC}")
    print("")
    print(f"Logged in as {bcolors.OKBLUE}{bot.user.name}! {bcolors.ENDC}")
    print(f"{bcolors.WARNING}nunca compartilhe o seu token!")
    time.sleep(1.5)
    print("")
    if elapsed1 == "n" :
    	await status1
    else :
    	await status
    print(f"{bcolors.OKBLUE}status aplicado{bcolors.ENDC}")
    print("")
  
     
async def on_set():
    if elapsed1 == "n" :
    	await status1
    else :
    	await status
    await asyncio.sleep(60)
    client.loop.create_task(on_set())

@bot.command()
async def stop(ctx): 
    if bot.user.id == ctx.message.author.id: 
        print("bot shutdown requested")
        await bot.close()
        time.sleep(3)
       
bot.run(TOKENHERE, bot = False)
