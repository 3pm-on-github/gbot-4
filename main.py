import discord
from discord.ext import commands
from datetime import datetime
from datetime import date
import json
import datetime
import time

bot = commands.Bot('qsdvsqvdgiuodsngvuodsgvobdugtvbqsdfyuqdscbso', intents=discord.Intents.all())
bot.remove_command('help')
privat = open('C:\\Users\\pooki\\OneDrive\\Bureau\\Codes\\GBot 4\\private.json', "r")
jsondata = privat.read()
private = json.loads(jsondata)
nobotsinlogs = False
typeinchannelidthing = False
channelidthing = 0

async def newlogsline(messagethingidk, messageauthor):
    global channelidthing
    channel = discord.guild.Guild.get_channel(messagethingidk.guild, channelidthing)
    global nobotsinlogs
    if not messageauthor == 'GBot 4':
        if nobotsinlogs == True:
            if messagethingidk.author.bot == False:
                todaything = date.today()
                nowthing = datetime.datetime.now()
                againnowthing = nowthing.strftime("%H:%M:%S")
                messagecontent = str(messagethingidk.content)
                encodedmessagecontent = messagecontent.encode("utf-8")
                logs = open('C:\\Users\\pooki\\OneDrive\\Bureau\\Codes\\GBot 4\\logs.txt', "a")
                logs.write(f'{todaything.strftime("%d/%m/%Y")} at {againnowthing}: @{messageauthor} said {encodedmessagecontent} in channel <#{messagethingidk.channel.id}> in {messagethingidk.guild.name}.\n') #type: ignore
                logs.close()
                await channel.send(f'{todaything.strftime("%d/%m/%Y")} at {againnowthing}: @{messageauthor} said {encodedmessagecontent} in channel <#{messagethingidk.channel.id}> in {messagethingidk.guild.name}.')
        elif nobotsinlogs == False:
            todaything = date.today()
            nowthing = datetime.datetime.now()
            againnowthing = nowthing.strftime("%H:%M:%S")
            messagecontent = str(messagethingidk.content)
            encodedmessagecontent = messagecontent.encode("utf-8")
            logs = open('C:\\Users\\pooki\\OneDrive\\Bureau\\Codes\\GBot 4\\logs.txt', "a")
            logs.write(f'{todaything.strftime("%d/%m/%Y")} at {againnowthing}: @{messageauthor} said {encodedmessagecontent} in channel <#{messagethingidk.channel.id}> in {messagethingidk.guild.name}.\n') #type: ignore
            logs.close()
            await channel.send(f'{todaything.strftime("%d/%m/%Y")} at {againnowthing}: @{messageauthor} said {encodedmessagecontent} in channel <#{messagethingidk.channel.id}> in {messagethingidk.guild.name}.')

@bot.event
async def on_message(msg):
    global typeinchannelidthing
    global channelidthing
    await newlogsline(msg, format(msg.author.name))
    if msg.content == 'g4:ping':
        await msg.channel.send('Pong!')
    if msg.content == 'g4:bilt':
        global nobotsinlogs
        if nobotsinlogs == False:
            nobotsinlogs = True
            await msg.channel.send('Bots in logs are now deactivated!')
        elif nobotsinlogs == True:
            nobotsinlogs = False
            await msg.channel.send('Bots in logs are now activated!')
    if msg.content == 'g4:setlogschnlid':
        await msg.channel.send('Please type your channel id.')
        typeinchannelidthing = True
    if typeinchannelidthing == True:
        typeinchannelidthing = False
        channelidthing = msg.content
        await msg.channel.send('Channel id succesfully set.')

bot.run(token=str(private['token']))