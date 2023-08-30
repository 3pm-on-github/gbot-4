import discord
from discord.ext import commands
from datetime import datetime
from datetime import date
import json
import datetime
import time
import random

bot = commands.Bot('qsdvsqvdgiuodsngvuodsgvobdugtvbqsdfyuqdscbso', intents=discord.Intents.all())
bot.remove_command('help')
privat = open('C:\\Users\\pooki\\OneDrive\\Bureau\\Codes\\GBot 4\\private.json', "r")
jsondata = privat.read()
private = json.loads(jsondata)
typeinguessthingidk = False
nobotsinlogs = False
typeinchannelidthing = False
channelidthing = 0

async def newlogsline(messagethingidk, messageauthor):
    global channelidthing
    channel = bot.get_channel(channelidthing)
    global nobotsinlogs
    if not messageauthor == 'GBot 4':
        if nobotsinlogs == True:
            if messagethingidk.author.bot == False:
                todaything = date.today()
                nowthing = datetime.datetime.now()
                againnowthing = nowthing.strftime("%H:%M:%S")
                messagecontent = str(messagethingidk.content)
                encodedmessagecontent = messagecontent.encode("utf-8")
                logs = open('logs.txt', "a")
                logs.write(f'{todaything.strftime("%d/%m/%Y")} at {againnowthing}: @{messageauthor} said {encodedmessagecontent} in channel <#{messagethingidk.channel.id}> in {messagethingidk.guild.name}.\n') #type: ignore
                logs.close()
                await channel.send(f'{todaything.strftime("%d/%m/%Y")} at {againnowthing}: @{messageauthor} said ``{encodedmessagecontent}`` in channel <#{messagethingidk.channel.id}> in {messagethingidk.guild.name}.')
        elif nobotsinlogs == False:
            todaything = date.today()
            nowthing = datetime.datetime.now()
            againnowthing = nowthing.strftime("%H:%M:%S")
            messagecontent = str(messagethingidk.content)
            encodedmessagecontent = messagecontent.encode("utf-8")
            logs = open('logs.txt', "a")
            logs.write(f'{todaything.strftime("%d/%m/%Y")} at {againnowthing}: @{messageauthor} said {encodedmessagecontent} in channel <#{messagethingidk.channel.id}> in {messagethingidk.guild.name}.\n') #type: ignore
            logs.close()
            await channel.send(f'{todaything.strftime("%d/%m/%Y")} at {againnowthing}: @{messageauthor} said ``{encodedmessagecontent}`` in channel <#{messagethingidk.channel.id}> in {messagethingidk.guild.name}.')

@bot.event
async def on_message(msg):
    global typeinchannelidthing
    global channelidthing
    global typeinguessthingidk
    if msg.content == 'g4:ping':
        await msg.channel.send('Pong!')
    elif msg.content == 'g4:dice':
        number = random.randint(1, 6)
        await msg.channel.send(f':game_die:{number}')
    elif msg.content == 'g4:hazard':
        await msg.channel.send(f'Please take your time and choose what happens when we get red, orange, yellow, green or blue. You have 30 seconds.')
        time.sleep(30)
        colors = [":red_square:",":orange_square:",":yellow_square:",":green_square:",":blue_square:"]
        number1 = random.randint(1, 5)
        number2 = random.randint(1, 5)
        number3 = random.randint(1, 5)
        number4 = random.randint(1, 5)
        number5 = random.randint(1, 5)
        await msg.channel.send(f'Lets play now!\n1: ||{colors[number1]}||\n2: ||{colors[number2]}||\n3:||{colors[number3]}||\n4: ||{colors[number4]}||\n5: ||{colors[number5]}||')
    elif msg.content == 'g4:guesser':
        await msg.channel.send('Guess a number between 1 and 10 and then type it in the chat.')
        typeinguessthingidk = True
    elif msg.content == 'g4:help':
        await msg.channel.send('***---Logs commands---***\ng4:bilt: Activates/Deactivates bots in logs.\ng4:setlogschnlid: Sets logs channel id\n***---Other commands---***\ng4:ping: What can happen... :thinking:\ng4:help: Shows this message\ng4:ownercmds: owner commands, ask gachaytb3ondc for access.\n***---Games---***\ng4:dice: roll a dice!\ng4:hazard: Play a game of hazard!\ng4:guesser: Guess a number between 1 and 10 and try to get the same number that the bot guessed!')
    elif msg.content == 'g4:ownercmds':
        if msg.author.id == 932666698438418522:
            await msg.author.send('***---Owner commands---***\nComing soon!')
        else:
            await msg.channel.send('bro tried to fool me, did u know atleast that the owner can see the logs of every single servers with the bot in it?')
    elif msg.content == 'g4:bilt':
        global nobotsinlogs
        if nobotsinlogs == False:
            nobotsinlogs = True
            await msg.channel.send('Bots in logs are now deactivated!')
        elif nobotsinlogs == True:
            nobotsinlogs = False
            await msg.channel.send('Bots in logs are now activated!')
    elif msg.content == 'g4:setlogschnlid':
        await msg.channel.send('Please type your channel id.')
        typeinchannelidthing = True
    elif typeinguessthingidk == True:
        typeinguessthingidk = False
        number = random.randint(1, 10)
        if int(msg.content) == number:
            await msg.channel.send('Yay, you did it!')
        elif msg.content != number:
            await msg.channel.send(f'Oops, wrong answer! The correct answer was {number}.')
    elif typeinchannelidthing == True:
        typeinchannelidthing = False
        channelidthing = int(msg.content)
        await msg.channel.send('Channel id succesfully set.')
    elif not channelidthing == 0:
        await newlogsline(msg, format(msg.author.name))

bot.run(token=str(private['token']))