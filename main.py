import discord
from discord.ext import commands
from datetime import datetime
from datetime import date
from gbotapilauncheretc import setup
# from music_cog import music_cog
import json
import datetime
import time
import random

bot = commands.Bot('qsdvsqvdgiuodsngvuodsgvobdugtvbqsdfyuqdscbso', intents=discord.Intents.all())
bot.remove_command('help')
privat = open('private.json', "r")
# bot.add_cog(music_cog(bot))
jsondata = privat.read()
private = json.loads(jsondata)
typeinguessthingidk = False
nobotsinlogs = False
typeinchannelidthing = False
whokicktypething = False
kickreasontypething = False
kickpersonid = 0
createimagetype1to9thing = False
sendmessagetoownertypething = False
whobantypething = False
banpersonid = 0
banreasontypething = False
searchgiftypething = False
channelidthing = 1144614402625110126
botthingidklol = open('botthingidklol.txt', "w")
botthingidklol.write(str(bot))
botthingidklol.close()
setup(gbotverthing='0.1.3')

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Game(name='wee wee baguette gachaytb3 the best gbot 4 too'))

async def newlogsline(messagethingidk, messageauthor):
    global channelidthing
    if channelidthing != 0:
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
async def on_ready():
    print('The bot is online!')
    print('------------------')
    if date.today() == '2023-10-15':
        print('Hey! Its haloween event day! You should start the event!')
    elif date.today() == '2023-12-15':
        print('Hey! Its christmas event day! You should start the event!')
    elif date.today() == '2023-10-31':
        print('Hey! Its no longer haloween event day! You should delete the messages!')
    elif date.today() == '2023-12-31':
        print('Hey! Its no longer christmas event day! You should delete the messages!')

@bot.event
async def on_message(msg):
    global sendmessagetoownertypething
    global typeinchannelidthing
    global channelidthing
    global typeinguessthingidk
    global kickpersonid
    global kickreasontypething
    global whokicktypething
    global createimagetype1to9thing
    global whobantypething
    global banreasontypething
    global banpersonid
    global searchgiftypething
    if msg.content == 'g4:ping':
        await msg.channel.send(f'Pong! Bot ping: {round(bot.latency * 1000)}ms.')
    elif msg.content == 'g4:contact':
        await msg.channel.send('What do you want to send to the owner?')
        sendmessagetoownertypething = True
    elif msg.content == 'g4:dice':
        number = random.randint(1, 6)
        await msg.channel.send(f':game_die:{number}')
    elif msg.content == 'g4:hazard':
        await msg.channel.send(f'Please take your time and choose what happens when we get red, orange, yellow, green or blue. You have 30 seconds.')
        time.sleep(30)
        colors = [":red_square:",":orange_square:",":yellow_square:",":green_square:",":blue_square:"]
        number1 = random.randint(0, 4)
        number2 = random.randint(0, 4)
        number3 = random.randint(0, 4)
        number4 = random.randint(0, 4)
        number5 = random.randint(0, 4)
        await msg.channel.send(f'Lets play now!\n1: ||{colors[number1]}||\n2: ||{colors[number2]}||\n3:||{colors[number3]}||\n4: ||{colors[number4]}||\n5: ||{colors[number5]}||')
    elif msg.content == 'g4:guesser':
        await msg.channel.send('Guess a number between 1 and 10 and then type it in the chat.')
        typeinguessthingidk = True
    elif msg.content == 'g4:starthaloweenevent':
        if date.today() == '2023-10-15':
            message = await msg.channel.send("The Halloween event has Started! <:FBFServerHallowenimage:1035263501549187183> React with The Halloween Emoji To Win 2,000 coins! :jack_o_lantern:")
            await message.add_reaction("🎃")
        else:
            await msg.channel.send("The event hasn't started yet! Wait for 2023-10-15.")
    elif msg.content == 'g4:startchristmasevent':
        if date.today() == '2023-12-15':
            message = await msg.channel.send("The Christmas event has Started! <:FBFServerchristmasimage:1155521299179917432> React with The Christmas Tree Emoji To Win 5,000 coins! :christmas_tree:")
            await message.add_reaction("🎄")
        else:
            await msg.channel.send("The event hasn't started yet! Wait for 2023-12-15.")
    elif msg.content == 'g4:finishit':
        letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
        letternumber = random.randint(0, 25)
        await msg.channel.send("I'll send a letter and you gotta finish the word.")
        await msg.channel.send(f'Your letter is: {letters[letternumber]}')
    elif msg.content == 'g4:createimage':
        await msg.channel.send('Create an image with 1 to 9 numbers, example:\n123456789\n123456789\n123456789\nWill give this:\n:red_square::orange_square::yellow_square::green_square::blue_square::purple_square::brown_square::white_large_square::black_large_square:\n:red_square::orange_square::yellow_square::green_square::blue_square::purple_square::brown_square::white_large_square::black_large_square:\n:red_square::orange_square::yellow_square::green_square::blue_square::purple_square::brown_square::white_large_square::black_large_square:')
        createimagetype1to9thing = True
    elif msg.content == 'g4:meme':
        from memeapi import memeApi
        root = memeApi()
        meme = root.getmeme()
        await msg.channel.send(f"*subreddit: {meme['subreddit']}, author: {meme['author']}*\n**{meme['title']}**")
        await msg.channel.send(meme['url'])
    elif msg.content == 'g4:searchgif':
        await msg.channel.send('What do you want to search?')
        searchgiftypething = True
#   elif msg.content == 'g4:yourcommand':
#       await msg.channel.send("your message here")
    elif msg.content == 'g4:help':
        await msg.channel.send('***---Logs commands---***\ng4:bilt: Activates/Deactivates bots in logs.\ng4:setlogschnlid: Sets logs channel id\n***---Other commands---***\ng4:searchgif: search a gif\ng4:meme: Posts a random meme\ng4:ping: What can happen... :thinking:\ng4:help: Shows this message\ng4:ownercmds: owner commands, ask gachaytb3ondc for access.\ng4:contact: contact the owner\n***---Games---***\ng4:dice: roll a dice!\ng4:hazard: Play a game of hazard!\ng4:guesser: Guess a number between 1 and 10 and try to get the same number that the bot guessed!\ng4:finishit: find out yourself...\ng4:createimage: Create a number to emoji image!\n***---Moderation---***\ng4:kick: kicks a person\ng4:ban: bans a person')
    elif msg.content == 'g4:ownercmds':
        if msg.author.id == 932666698438418522:
            await msg.author.send('***---Owner commands---***\ng4:starthaloweenevent: start the haloween event.\ng4:startchristmasevent: start the christmas event.')
        else:
            await msg.channel.send('bro tried to fool me, did u know atleast that the owner can see the logs of every single servers with the bot in it?')
    elif msg.content == 'g4:kick':
        await msg.channel.send('Who do you want to kick? (input user id)')
        whokicktypething = True
    elif msg.content == 'g4:ban':
        await msg.channel.send('Who do you want to ban? (input user id)')
        whobantypething = True
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
    elif createimagetype1to9thing == True:
        currentimage = 'Here is the result:\n'
        emojis = [':red_square:', ':orange_square:', ':yellow_square:', ':green_square:', ':blue_square:', ':purple_square:', ':brown_square:', ':white_large_square:', ':black_large_square:']
        for i in range(len(msg.content)):
            if not msg.author.name == "GBot 4":
                try:
                    val = int(msg.content[i])
                    if val > 0:
                        currentimage = f"{currentimage}{emojis[val - 1]}"
                except:
                    if msg.content[i] == "\n":
                        currentimage = f"{currentimage}\n"
                    else:
                        pass
        createimagetype1to9thing = False
        try:
            await msg.channel.send(str(currentimage))
        except:
            await msg.channel.send('Error: Maybe the bot passed a limit, or is rate limited.')
    elif sendmessagetoownertypething == True:
        if msg.author.name != 'GBot 4':
            sendmessagetoownertypething = False
            messagecontent = str(msg.content)
            encodedmessagecontent = messagecontent.encode("utf-8")
            print(f'Sent by @{msg.author.name}: {encodedmessagecontent} (to contact him: <@{msg.author.id}>)')
            await msg.channel.send('Thanks for letting the owner a message! He will maybe respond.')
    elif searchgiftypething == True:
        searchgiftypething = False
        from memeapi import memeApi
        root = memeApi()
        await msg.channel.send(root.getgif(str(msg.content), 'LIVDSRZULELA', 8))
    elif whokicktypething == True:
        kickpersonid = int(msg.content)
        whokicktypething = False
        await msg.channel.send('And for what reason?')
        kickreasontypething = True
    elif whobantypething == True:
        banpersonid = int(msg.content)
        whobantypething = False
        await msg.channel.send('And for what reason?')
        banreasontypething = True
    elif kickreasontypething == True:
        kickreasontypething = False
        if msg.author.guild_permissions.kick_members:
            try:
                # Attempt to kick the member
                membertokick =  msg.guild.get_member(kickpersonid)
                await membertokick.kick(reason=msg.content)
                await msg.channel.send(f"Succesfully kicked {membertokick.mention} for the reason: '{msg.content}'")
            except:
                await msg.channel.send("Looks like the bot doesn't have permissions to kick persons! If you can, please add the administrator setting to the GBot 4 role.")
        else:
            await msg.channel.send("You don't have permission to kick members.")
    elif banreasontypething == True:
        banreasontypething = False
        if msg.author.guild_permissions.ban_members:
            try:
                # Attempt to kick the member
                membertoban = msg.guild.get_member(banpersonid)
                await membertoban.ban(reason=msg.content)
                await msg.channel.send(f"Succesfully banned {membertoban.mention} for the reason: '{msg.content}'")
            except:
                await msg.channel.send("Looks like the bot doesn't have permissions to ban persons! If you can, please add the administrator setting to the GBot 4 role.")
        else:
            await msg.channel.send("You don't have permission to ban members.")
    elif not channelidthing == 0:
        await newlogsline(msg, format(msg.author.name))

@bot.event
async def on_raw_reaction_add(reaction):
    if reaction.user_id != 1144229461953368214 and reaction.emoji.name == '🎃':
        guild = bot.get_guild(925032109595308072)
        member = guild.get_member(776163922432622603)
        await member.send(f'**Someone reacted to the Halloween event with the emoji! User: <@{reaction.user_id}>**')
        guild2 = bot.get_guild(reaction.guild_id)
        member2 = guild2.get_member(reaction.user_id)
        await member2.send('**You Won 2,000 Coins! of the Halloween Event! They Will be Given Later, Have Fun!**')
    elif reaction.user_id != 1144229461953368214 and reaction.emoji.name == '🎄':
        guild = bot.get_guild(925032109595308072)
        member = guild.get_member(776163922432622603)
        await member.send(f'**Someone reacted to the Christmas event with the emoji! User: <@{reaction.user_id}>**')
        guild2 = bot.get_guild(reaction.guild_id)
        member2 = guild2.get_member(reaction.user_id)
        await member2.send('**You Won 5,000 Coins! of the Christmas Event! They Will be Given Later, Have a Nice Christmas!**')

bot.run(token=str(private['token']))