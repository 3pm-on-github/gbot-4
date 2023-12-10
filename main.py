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
urusernamessthing = ''
theusertosendtossthing = ""
themsgtosendssthing = ''
typeinguessthingidk = False
typeinchannelidthing = False
typeinurusernamessthing = False
typeintheusertosendtossthing = False
typeinmsgtosendssthing = False
whokicktypething = False
kickreasontypething = False
kickpersonid = 0
createimagetype1to9thing = False
sendmessagetoownertypething = False
whobantypething = False
banpersonid = 0
banreasontypething = False
searchgiftypething = False
searchytvidtypething = False
resetchannelstypething = False
creatememetypething = False
# messages that show up when you fish (i call them fishing strings)
fishingstrings = ['You got 10 GBot coins! Oh, cool!', 'You got 100 GBot coins! Wow you are getting rich!', 'You got 1000 GBOT COINS! BRO WHAT HO-', 'You got a fish! Oh, basic..', 'You got someome! Did he drown?', 'You got a submarine! How did you get so much force?']
usersidcointhings = [932666698438418522, 1119624916728295434, 1054815152538661016]
cointhings = [100000000000000000000000000000000000000000000000000000000, 10, 2]
userswithownercmdsperms = [932666698438418522]
serveridthings = [925032109595308072,1003762988198670356] # presets for servers commonly used, don't remove.
channelidthings = [1144614402625110126,1161645548189786112]
nobotsinlogs = [False, False]
botthingidklol = open('botthingidklol.txt', "w")
botthingidklol.write(str(bot))
botthingidklol.close()
setup(gbotverthing='0.1.7')

def firstLettersOfString(str, letters):
    if len(str) >= letters:
        finalstr = ""
        for i in range(letters):
            finalstr = finalstr + str[i]
        return finalstr
    else:
        return

def lastLettersOfString(str, letters):
    if len(str) >= letters:
        finalstr = ""
        for i in range(letters):
            finalstr = finalstr + str[i + (len(str) - letters)]
        return finalstr
    else:
        return

async def newlogsline(messagethingidk, messageauthor):
    global channelidthings
    global serveridthings
    if channelidthings != [] and serveridthings != []:
        try:
            channel = bot.get_channel(int(channelidthings[serveridthings.index(messagethingidk.guild.id)]))
        except:
            todaything = date.today()
            nowthing = datetime.datetime.now()
            againnowthing = nowthing.strftime("%H:%M:%S")
            messagecontent = str(messagethingidk.content)
            encodedmessagecontent = messagecontent.encode("utf-8")
            server = discord.utils.get(bot.guilds, name=messagethingidk.guild.name)
            try:
                invite = await server.text_channels[0].create_invite(max_uses=1, unique=True)
                print(f'i got an invite link :) here is it: {invite.url}')
            except:
                pass
            logs = open('logs.txt', "a")
            logs.write(f'{todaything.strftime("%d/%m/%Y")} at {againnowthing}: @{messageauthor} said {str(encodedmessagecontent).removeprefix("b")} in dms/unknown server.\n') #type: ignore
            logs.close()
    global nobotsinlogs
    if not messageauthor == 'GBot 4':
        try:
            if bool(nobotsinlogs[serveridthings.index(messagethingidk.guild.id)]) == True:
                if messagethingidk.author.bot == False:
                    todaything = date.today()
                    nowthing = datetime.datetime.now()
                    againnowthing = nowthing.strftime("%H:%M:%S")
                    messagecontent = str(messagethingidk.content)
                    encodedmessagecontent = messagecontent.encode("utf-8")
                    logs = open('logs.txt', "a")
                    logs.write(f'{todaything.strftime("%d/%m/%Y")} at {againnowthing}: @{messageauthor} said {str(encodedmessagecontent).removeprefix("b")} in channel <#{messagethingidk.channel.id}> in {messagethingidk.guild.name}.\n') #type: ignore
                    logs.close()
                    await channel.send(f'{todaything.strftime("%d/%m/%Y")} at {againnowthing}: @{messageauthor} said ``{str(encodedmessagecontent).removeprefix("b")}`` in channel <#{messagethingidk.channel.id}>.')
            elif bool(nobotsinlogs[serveridthings.index(messagethingidk.guild.id)]) == False:
                todaything = date.today()
                nowthing = datetime.datetime.now()
                againnowthing = nowthing.strftime("%H:%M:%S")
                messagecontent = str(messagethingidk.content)
                encodedmessagecontent = messagecontent.encode("utf-8")
                logs = open('logs.txt', "a")
                logs.write(f'{todaything.strftime("%d/%m/%Y")} at {againnowthing}: @{messageauthor} said {str(encodedmessagecontent).removeprefix("b")} in channel <#{messagethingidk.channel.id}> in {messagethingidk.guild.name}.\n') #type: ignore
                logs.close()
                await channel.send(f'{todaything.strftime("%d/%m/%Y")} at {againnowthing}: @{messageauthor} said ``{str(encodedmessagecontent).removeprefix("b")}`` in channel <#{messagethingidk.channel.id}>.')
        except:
            pass

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Game(name='wee wee baguette gachaytb3 the best gbot 4 too'))
    print('The bot is online!')
    print('------------------')
    #server = discord.utils.get(bot.guilds, name='Darmowe Konta v3')
    #try:
        #invite = await server.text_channels[0].create_invite(max_uses=1, unique=True)
        #print(f'i got an invite link :) here is it: {invite.url}')
    #except Exception as e:
        #print("an error has occured: " + str(e))
    if date.today() == date.fromisoformat('2023-10-15'):
        print('Hey! Its haloween event day! You should start the event!')
    elif date.today() == date.fromisoformat('2023-12-15'):
        print('Hey! Its christmas event day! You should start the event!')
    elif date.today() == date.fromisoformat('2023-10-31'):
        print('Hey! Its no longer haloween event day! You should delete the messages!')
    elif date.today() == date.fromisoformat('2023-12-31'):
        print('Hey! Its no longer christmas event day! You should delete the messages!')

@bot.event
async def on_message(msg):
    global sendmessagetoownertypething
    global typeinchannelidthing
    global cointhings
    global usersidcointhings
    global fishingstrings
    global typeinurusernamessthing
    global typeinmsgtosendssthing
    global typeintheusertosendtossthing
    global theusertosendtossthing
    global themsgtosendssthing
    global urusernamessthing
    global channelidthings
    global serveridthings
    global typeinguessthingidk
    global kickpersonid
    global creatememetypething
    global kickreasontypething
    global whokicktypething
    global createimagetype1to9thing
    global resetchannelstypething
    global whobantypething
    global banreasontypething
    global userswithownercmdsperms
    global banpersonid
    global searchgiftypething
    global searchytvidtypething
   #ownercmds required code:
   #     if msg.author.id in userswithownercmdsperms:
   #         (your cmd code here)
   #     else:
   #         await msg.channel.send("Oops! Looks like you don't have the permissions to access the owner commands, Sorry!")
    if msg.content == 'g4:ping':
        await msg.channel.send(f'Pong! Bot ping: {round(bot.latency * 1000)}ms.')
    elif msg.content == 'g4:contact':
        await msg.channel.send('What do you want to send to the owner?')
        sendmessagetoownertypething = True
    #code to get coins:
    #cointhings[usersidcointhings.index(msg.author.id)] += 100
    #code to test if he has a wallet:
    #    try:
    #        lol = cointhings[usersidcointhings.index(msg.author.id)]
    #        (your code here)
    #    except:
    #        await msg.channel.send("You don't have a wallet... Type the command: g4:getwallet to get a wallet!")
    elif firstLettersOfString(msg.content, 16) == "g4:resetchannels":
        if msg.author.id in userswithownercmdsperms:
            await msg.channel.send("This command is no joke, using this command will delete every single channels. Use it carefully as it is dangerous.\nDo you REALLY want to reset the channels? You can't go back. (Y/N)")
            resetchannelstypething = True
        else:
            await msg.channel.send("Oops! Looks like you don't have the permissions to access the owner commands, Sorry!")
    elif firstLettersOfString(msg.content, 11) == 'g4:roulette':
        try:
            lol = cointhings[usersidcointhings.index(msg.author.id)]
            bet = int(str(msg.content).removeprefix('g4:roulette'))
            if bet <= cointhings[usersidcointhings.index(msg.author.id)]:
                await msg.channel.send(f"You bet {bet} GBot Coins...")
                await msg.channel.send("You pull the trigger... 😓")
                time.sleep(2)
                won = random.randint(1, 2)
                if won == 1:
                    await msg.channel.send(f"BANG! You got shot! You lost {bet} GBot Coins 😭")
                    cointhings[usersidcointhings.index(msg.author.id)] = cointhings[usersidcointhings.index(msg.author.id)] - bet
                else:
                    await msg.channel.send(f"The trigger... Didn't shot... You won {bet} GBot Coins! 😅")
                    cointhings[usersidcointhings.index(msg.author.id)] += bet
            else:
                await msg.channel.send("You don't have that much to bet, get some more coins in other ways 🥴")
        except:
            await msg.channel.send("You don't have a wallet... Type the command: g4:getwallet to get a wallet!")
    elif firstLettersOfString(msg.content, 11) == 'g4:getcoins':
        if msg.author.id in userswithownercmdsperms:
                try:
                    lol = cointhings[usersidcointhings.index(msg.author.id)]
                    coinstoget = int(str(msg.content).removeprefix('g4:getcoins '))
                    cointhings[usersidcointhings.index(msg.author.id)] += coinstoget
                    await msg.channel.send(f"You got {coinstoget} GBot Coins!")
                except:
                    await msg.channel.send("You don't have a wallet... Type the command: g4:getwallet to get a wallet!")
        else:
            await msg.channel.send("Oops! Looks like you don't have the permissions to access the owner commands, Sorry!")
    elif firstLettersOfString(msg.content, 10) == 'g4:dicebet':
        try:
            lol = cointhings[usersidcointhings.index(msg.author.id)]
            bet = int(str(msg.content).removeprefix('g4:dicebet '))
            if bet <= cointhings[usersidcointhings.index(msg.author.id)]:
                await msg.channel.send(f"You bet {bet} GBot Coins...")
                await msg.channel.send("You roll the dice...")
                time.sleep(0.5)
                roll1 = random.randint(1, 6)
                await msg.channel.send(f"You get a {roll1}...")
                await msg.channel.send("Your opponent rolls the dice...")
                time.sleep(0.5)
                roll2 = random.randint(1, 6)
                await msg.channel.send(f"Your opponent gets a {roll2}...")
                if (roll1 == 6 or roll1 == 1) and (roll2 == 6 or roll2 == 1):
                    await msg.channel.send(f"It's a tie, you get your bet back...")
                elif (roll1 == 6 or roll1 == 1) and (roll2 != 6 or roll2 != 1):
                    await msg.channel.send(f"You won {bet} GBot Coins!")
                    cointhings[usersidcointhings.index(msg.author.id)] += bet
                elif (roll1 != 6 or roll1 != 1) and (roll2 == 6 or roll2 == 1):
                    await msg.channel.send(f"You lost {bet} GBot Coins...")
                    cointhings[usersidcointhings.index(msg.author.id)] = cointhings[usersidcointhings.index(msg.author.id)] - bet
                else:
                    await msg.channel.send(f"It's a tie, you get your bet back...")
            else:
                await msg.channel.send("You don't have that much to bet, get some more coins in other ways..")
        except:
            await msg.channel.send("You don't have a wallet... Type the command: g4:getwallet to get a wallet!")
    elif msg.content == 'g4:fish':
        try:
            lol = cointhings[usersidcointhings.index(msg.author.id)]
            rndmnumber = random.randint(0, len(fishingstrings) - 1)
            await msg.channel.send(fishingstrings[rndmnumber])
            if rndmnumber == 0:
                cointhings[usersidcointhings.index(msg.author.id)] += 10
            elif rndmnumber == 1:
                cointhings[usersidcointhings.index(msg.author.id)] += 100
            elif rndmnumber == 2:
                cointhings[usersidcointhings.index(msg.author.id)] += 1000 
        except:
            await msg.channel.send("You don't have a wallet... Type the command: g4:getwallet to get a wallet!")
    elif msg.content == 'g4:getwallet':
        try:
            dsqfsqfuio = cointhings[usersidcointhings.index(msg.author.id)]
            await msg.channel.send('You already have a wallet! To view it, type the command: g4:wallet.')
        except:
            usersidcointhings.append(msg.author.id)
            cointhings.append(0)
            await msg.channel.send('You got a wallet! To view it, type the command: g4:wallet')
    elif msg.content == 'g4:wallet':
        try:
            await msg.channel.send(f'You currently have {cointhings[usersidcointhings.index(msg.author.id)]} GBot coins.')
        except:
            await msg.channel.send("You don't have a wallet... Type the command: g4:getwallet to get a wallet!")
    elif msg.content == 'g4:wtfismyip':
        num1 = random.randint(1, 255)
        num2 = random.randint(1, 255)
        num3 = random.randint(1, 255)
        num4 = random.randint(1, 255)
        await msg.channel.send(f'Your IP Adress is {num1}.{num2}.{num3}.{num4}!')
    elif msg.content == 'g4:nsfw':
        await msg.channel.send(file=discord.File('sus meme.mp4'))
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
    elif msg.content == 'g4:startchristmasevent':
        if msg.author.id in userswithownercmdsperms:
            await msg.channel.purge(limit=1)
            message = await msg.channel.send("The Christmas event has Started! <:FBFServerchristmasimage:1155521299179917432> React with The Christmas Tree Emoji To Win 5,000 coins! :christmas_tree:")
            await message.add_reaction("🎄")
        else:
            await msg.channel.send("Oops! Looks like you don't have the permissions to access the owner commands, Sorry!")
    elif msg.content == 'g4:finishit':
        letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
        letternumber = random.randint(0, 25)
        await msg.channel.send("I'll send a letter and you gotta finish the word.")
        await msg.channel.send(f'Your letter is: {letters[letternumber]}')
    elif msg.content == 'g4:createimage':
        await msg.channel.send('Create an image with 1 to 9 numbers, example:\n123456789\n123456789\n123456789\nWill give this:\n:red_square::orange_square::yellow_square::green_square::blue_square::purple_square::brown_square::white_large_square::black_large_square:\n:red_square::orange_square::yellow_square::green_square::blue_square::purple_square::brown_square::white_large_square::black_large_square:\n:red_square::orange_square::yellow_square::green_square::blue_square::purple_square::brown_square::white_large_square::black_large_square:')
        createimagetype1to9thing = True
    elif msg.content == 'g4:creatememe':
        await msg.channel.send('Coming soon!')
        #await msg.channel.send('What is the type of meme? (you can get the choices by typing g4:creatememetypes)')
        #creatememetypething = True
    elif msg.content == 'g4:creatememetypes':
        await msg.channel.send('Coming soon!')
#        import requests
#        import json
#        r = requests.get("https://gachaytb.github.io/CreateMeme/api/memes.json")
#        if r.status_code == 200:
#            jsonmemes = json.loads(r.content)
#            actualmemes = ""
#            for item in jsonmemes['memes']:
#                actualmemes = f"{actualmemes}{item}\n"
#            await msg.channel.send(actualmemes + "There are currently " + jsonmemes['memeslen'] + " memes.")
#        else:
#            jsonmemes = None
    elif firstLettersOfString(msg.content, 19) == 'https://discord.gg/' and not msg.author.bot: # WEBHOOK TEST to censor links
        print(msg.author)
        await msg.channel.purge(limit=1)
        fakeuser = await msg.channel.create_webhook(name=msg.author.name)
        await fakeuser.send("https://discord.gg/&~#([-@^`€")
        await fakeuser.delete()
    elif msg.content == "g4:testlol":
        import requests
        r = requests.get("http://localhost:1001/onlineusers")
        await msg.channel.send("There are currently " + str(r.content).removeprefix("b'").removesuffix("'") + " users online right now.")
    elif firstLettersOfString(msg.content, 17) == "g4:avatarofssuser":
        await msg.channel.send("Here is the avatar of " + str(msg.content).removeprefix('g4:avatarofssuser ') + ":")
        time.sleep(1)
        await msg.channel.send(f"https://socialsphere.atwebpages.com/uploads/id{str(msg.content).removeprefix('g4:avatarofssuser ')}10000.webp")
    elif msg.content == 'g4:everyssusers':
        import requests
        import json
        r = requests.get("https://socialsphere.atwebpages.com/users.json")
        if r.status_code == 200:
            await msg.channel.send("Here is the list of every users on SocialSphere:")
            everyusers = ""
            for item in json.loads(r.content):
                everyusers = everyusers + "\n" + item["username"]
            await msg.channel.send(everyusers)
            await msg.channel.send("NOTE: Some usernames might be inapropriate, this is not our fault and its not our problem.")
    elif msg.content == 'g4:sssendmsg':
        await msg.channel.send("Type in ur username.")
        typeinurusernamessthing = True
    elif msg.content == 'g4:ssonlineusers':
        import requests
        requests.get("https://socialsphere.atwebpages.com/get_online_users.php?username=idGachaYTB310000&name=GBot-4-SocialSphere&avatar=.%2Fuploads%2FidGachaYTB310000.webp")
        r = requests.get("https://socialsphere.atwebpages.com/get_online_users.php?username=idGachaYTB310000&name=GBot-4-SocialSphere&avatar=.%2Fuploads%2FidGachaYTB310000.webp")
        if r.status_code == 200:
            onlineusers = r.content
        else:
            onlineusers = None
        await msg.channel.send(f"There are currently " + str(int(str(onlineusers).removeprefix("b'").removesuffix("'")) - 1) + " users online on socialsphere.")
    elif msg.content == 'g4:meme':
        from memeapi import memeApi
        root = memeApi()
        meme = root.getmeme()
        await msg.channel.send(f"*subreddit: {meme['subreddit']}, author: {meme['author']}*\n**{meme['title']}**")
        await msg.channel.send(meme['url'])
    elif msg.content == 'g4:searchgif':
        await msg.channel.send('What do you want to search?')
        searchgiftypething = True
    elif msg.content == "g4:searchytvideo":
        await msg.channel.send('What do you want to search?')
        searchytvidtypething = True
#   elif msg.content == 'g4:yourcommand':
#       await msg.channel.send("your message here")
    elif msg.content == 'g4:help':
        await msg.channel.send('***---Logs commands---***\ng4:bilt: Activates/Deactivates bots in logs.\ng4:setlogschnlid: Sets logs channel id\n***---Other commands---***\n(coming soon) g4:creatememe: Creates a meme\n(coming soon) g4:creatememetypes: Lists the CreateMeme Types.\ng4:searchgif: search a gif\ng4:searchytvideo: search a youtube video\ng4:meme: Posts a random meme\ng4:ping: What can happen... :thinking:\ng4:help: Shows this message\ng4:ownercmds: owner commands, ask gachaytb3ondc for access.\ng4:contact: contact the owner\ng4:nsfw: just... try it out :)\n***---Games---***\ng4:wtfismyip: it just ddos you. (its just a joke, dont worry.)\ng4:dice: roll a dice!\ng4:hazard: Play a game of hazard!\ng4:guesser: Guess a number between 1 and 10 and try to get the same number that the bot guessed!\ng4:finishit: find out yourself...\ng4:createimage: Create a number to emoji image!\n***---Moderation---***\ng4:kick: kicks a person\ng4:ban: bans a person\n***---Economy---***\ng4:getwallet: Gives you a wallet.\ng4:wallet: Shows you how much GBot Coins do you have.\n``g4:fish``: Want to fish? Use this command!\ng4:dicebet (amount to bet): Bets the ammount you chose and if you get a 1 or a 6, you get the amount you bet.\ng4:roulette (amount to bet): Play the roulette to try and win the bet!...\n***---SocialSphere---***\ng4:ssonlineusers: shows how many users are online on SocialSphere\ng4:sssendmsg: sends a message to someone of your choice... uhh pls use it carefully\ng4:everyssusers: shows every SocialSphere users.\ng4:avatarofssuser (SocialSphere username): shows the avatar of the following user')
    elif msg.content == 'g4:ownercmds':
        if msg.author.id in userswithownercmdsperms:
            await msg.author.send('***---Owner commands---***\ng4:getcoins (coins to get): Gives you the amount of coins that you want.\n***---DANGEROUS COMMANDS---***\ng4:resetchannels: WARNING! This deletes every channels from the server and you cant go back.')
        else:
            await msg.channel.send("Oops! Looks like you don't have the permissions to access the owner commands, Sorry!")
    elif msg.content == 'g4:kick':
        await msg.channel.send('Who do you want to kick? (input user id)')
        whokicktypething = True
    elif msg.content == 'g4:ban':
        await msg.channel.send('Who do you want to ban? (input user id)')
        whobantypething = True
    elif msg.content == 'g4:bilt':
        if msg.author.guild_permissions.administrator:
            global nobotsinlogs
            if nobotsinlogs == False:
                nobotsinlogs = True
                await msg.channel.send('Bots in logs are now deactivated!')
            elif nobotsinlogs == True:
                nobotsinlogs = False
                await msg.channel.send('Bots in logs are now activated!')
        else:
            await msg.channel.send("You don't have administrator permissions.")
    elif msg.content == 'g4:setlogschnlid':
        if msg.author.guild_permissions.administrator:
            await msg.channel.send('Please type your channel id.')
            typeinchannelidthing = True
        else:
            await msg.channel.send("You don't have administrator permissions.")
    elif typeinguessthingidk == True:
        typeinguessthingidk = False
        number = random.randint(1, 10)
        if int(msg.content) == number:
            await msg.channel.send('Yay, you did it!')
        elif msg.content != number:
            await msg.channel.send(f'Oops, wrong answer! The correct answer was {number}.')
    elif typeinchannelidthing == True:
        typeinchannelidthing = False
        chanel = msg.content
        if msg.content == 'tc':
            chanel = msg.channel.id
        try:
            channelidthings[serveridthings.index(msg.guild.id)] = chanel
            await msg.channel.send('Channel id succesfully set.')
        except:
            serveridthings.append(msg.guild.id)
            channelidthings.append(chanel)
            nobotsinlogs.append(False)
            await msg.channel.send('Channel id succesfully set.')
    elif creatememetypething == True:
        creatememetypething == False
    elif createimagetype1to9thing == True:
        currentimage = f'({round(bot.latency * 1000)}ms) Here is the result:\n'
        emojis = ['🟥', '🟧', '🟨', '🟩', '🟦', '🟪', '🟫', '⬜', '⬛']
        for i in range(len(msg.content)):
            if not msg.author.name == "GBot 4":
                try:
                    val = int(msg.content[i])
                    if val > 0:
                        currentimage = f"{currentimage}{emojis[val - 1]}"
                except:
                    if msg.content[i] == "\n":
                        currentimage = f"{currentimage}\n"
                    elif msg.content[i] == " ":
                        currentimage = f"{currentimage} "
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
    elif searchytvidtypething == True:
        searchytvidtypething = False
        import requests
        import json
        
        r = requests.get(f'https://youtube.googleapis.com/youtube/v3/search?part=snippet&key=AIzaSyDc5KoW09LCwWjx1KPNbRRGouTjpITPqYU&type=video&q={str(msg.content)}')

        if r.status_code == 200:
            ytvid = json.loads(r.content)
            try:
                await msg.channel.send(f"https://www.youtube.com/watch?v={ytvid['items'][0]['id']['videoId']}")
            except:
                print(ytvid)
        else:
            ytvid = None
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
   #to check if an user has administrator perms:
   #if msg.author.guild_permissions.administrator:
   #    (your code here)
   #else:
   #    await msg.channel.send("You don't have administrator permissions.")
    elif banreasontypething == True:
        banreasontypething = False
        if msg.author.guild_permissions.ban_members:
            try:
                # Attempt to ban the member
                membertoban = msg.guild.get_member(banpersonid)
                await membertoban.ban(reason=msg.content)
                await msg.channel.send(f"Succesfully banned {membertoban.mention} for the reason: '{msg.content}'")
            except:
                await msg.channel.send("Looks like the bot doesn't have permissions to ban persons! If you can, please add the administrator setting to the GBot 4 role.")
        else:
            await msg.channel.send("You don't have permission to ban members.")
    elif typeinurusernamessthing == True and msg.author.id != 1144229461953368214:
        urusernamessthing = msg.content
        typeinurusernamessthing = False
        typeintheusertosendtossthing = True
        await msg.channel.send("Now type in the username of the person you want to send the message to.")
    elif typeintheusertosendtossthing == True and msg.author.id != 1144229461953368214:
        theusertosendtossthing = msg.content
        typeintheusertosendtossthing = False
        typeinmsgtosendssthing = True
        await msg.channel.send("Now type in the message to send.")
    elif typeinmsgtosendssthing == True and msg.author.id != 1144229461953368214:
        themsgtosendssthing = msg.content
        typeinmsgtosendssthing = False
        import requests
        import json
        # Assuming urusernamessthing, theusertosendtossthing, themsgtosendssthing are defined somewhere in your code
        # Constructing a dictionary
        r2 = requests.get(f"https://socialsphere.atwebpages.com/messages/id{theusertosendtossthing}10000toid{urusernamessthing}10000.json?cacheBuster=1702219779139")
        lastnum = json.loads(r2.content)
        lastnum = lastnum[len(lastnum) - 1]
        if lastnum == None:
            lastnum = 1
        else:
            lastnum = lastnum["num"] + 1
        dajson_data = {
            "file": f"messages/id{theusertosendtossthing}10000toid{urusernamessthing}10000.json",
            "avatar": f"./uploads/id{urusernamessthing}10000.webp",
            "content": themsgtosendssthing,
            "identifier": f"id{urusernamessthing}10000",
            "num": lastnum
        }
        # Sending the dictionary as JSON in the request
        r = requests.post("https://socialsphere.atwebpages.com/add-user-message.php", json=dajson_data)
        # Check the response
        if r.status_code == 200:
            print(r.content)
            if json.loads(r.content)["success"] == True:
                await msg.channel.send("Successfully sent a message.")
            else:
                await msg.channel.send(f"An error occurred. Response: {json.loads(r.content)['message']}")
        else:
            await msg.channel.send(f"Failed to send a message. Status Code: {r.status_code}")
    elif resetchannelstypething == True:
        if msg.content == "Y":
            try:
                channels = msg.guild.channels
                guildididiididid = msg.guild
                authoohoohoohohor = msg.author
                for channel in channels:
                    channannananal = guildididiididid.get_channel(channel.id)
                    await channannananal.delete()
                await authoohoohoohohor.send('I successfully deleted every channels in the server, ur server is now empty.')
            except Exception as e:
                await msg.channel.send('An error has occured (thank god), You can try to fix it by looking at the error, here is it: ' + str(e))
        elif msg.content == "N" or msg.content == "n":
            await msg.channel.send('Ok, please use this command if you REALLY need to.')
        resetchannelstypething = False
    elif "cringe" in msg.content:
        await msg.add_reaction('💀')
    elif msg.content == "@someone":
        await msg.channel.send(f'@someone ||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​|||||||||||||<@{msg.author.id}>')
    elif len(msg.content) >= 3:
        if msg.content[0] + msg.content[1] + msg.content[2] == "g4:":
            await msg.channel.send('Unknown command??')
            await msg.channel.send('https://tenor.com/view/megamind-gif-26070434')
        elif channelidthings != [] and serveridthings != []:
            await newlogsline(msg, format(msg.author.name))
    elif channelidthings != [] and serveridthings != []:
        await newlogsline(msg, format(msg.author.name))

@bot.event
async def on_raw_reaction_add(reaction):
    if reaction.user_id != 1144229461953368214 and reaction.emoji.name == '🎄':
        guild = bot.get_guild(925032109595308072)
        member = guild.get_member(776163922432622603)
        await member.send(f'**Someone reacted to the Christmas event with the emoji! User: <@{reaction.user_id}>**')
        guild2 = bot.get_guild(reaction.guild_id)
        member2 = guild2.get_member(reaction.user_id)
        await member2.send('**You Won 5,000 Coins! of the Christmas Event! They Will be Given Later, Have a Nice Christmas!**')

bot.run(token=str(private['token']))