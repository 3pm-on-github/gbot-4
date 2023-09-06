# Welcome to the gbot api launcher! You don't have to setup the gbot api by launching this script, the main.py script will do it for you.

from gbotapi import gbotapi
from numpy.core.defchararray import isnumeric
from _xxsubinterpreters import ChannelID
bot = None
loop = False
root = None
gbotver = None

def setup(gbotverthing):
    botthingidklol = open('botthingidklol.txt', "r")
    bot = botthingidklol.read()
    gbotver = gbotverthing
    startapi()

def startapi():
    variablelol = input('do you want to turn on the api')
    if variablelol == 'yes':
        root = gbotapi(botthing=bot, gbotverthing=gbotver)
        loop = True
        askcommand()
    elif variablelol == 'no':
        print('ok bye')

def askcommand():
    command = input('Ready')
    if "sendmsg" in command:
        error = False
        guildid = input('Please input the guild id.') # is this bot designed to be a giant backdoor?
        channelid = input('Please input the channel id.')
        messagething = input('Please input the message you want to send.')
        if messagething == '':
            print('sendmsg: ERROR 1: Message empty.')
            error = True
        try:
            test_s = str(messagething)
        except:
            print("sendmsg: ERROR 2: Message isn't a string.")
            error = True
        
        if (not isnumeric(channelid)):
            print("sendmsg: ERROR 3: input: \n\""+channelid+"\"\n could not be recognised as a Channel ID.")
            error = True
            if "," in channelid:
                print("Perhaps, why did you put a comma?")
        
        if (not isnumeric(guildid)):
            print("sendmsg: ERROR 4: input: \n\""+guildid+"\"\n could not be recognised as a Server ID.")
            error = True
            if "," in guildid:
                print("Perhaps, why did you put a comma?")
        
        if error == False:
            root.sendMessage(channel=channelid, guild=guildid, message=messagething)
        if loop == True:
            askcommand()
    elif command == 'apiver':
        print(root.apiver())
        if loop == True:
            askcommand()
    elif command == 'gbotver':
        print(root.gbotver())
        if loop == True:
            askcommand()