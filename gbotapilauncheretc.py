# Welcome to the gbot api launcher! You don't have to setup the gbot api by launching this script, the main.py script will do it for you.

from gbotapi import gbotapi
loop = False
bot = None
root = None
gbotver = None

def setup(gbotverthing, bott):
    global gbotver
    global bot
    bot = bott
    gbotver = gbotverthing

def askcommand():
    command = input('Ready')
    if "sendmsg" in command:
        error = False
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
        
        try:
            test_i1 = int(channelid)
        except:
            print("sendmsg: ERROR 3: input: \n"+channelid+"\n could not be recognised as a Channel ID.")
            error = True
            if "," in channelid:
                print("Perhaps, why did you put a comma?")
        
        if error == False:
            root.sendMessage(channel=channelid, message=messagething)
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

def startapi():
    global loop
    global root
    global bot
    variablelol = input('do you want to turn on the api')
    if variablelol == 'yes':
        root = gbotapi(botthing=bot, gbotverthing=gbotver)
        loop = True
        askcommand()
    elif variablelol == 'no':
        print('ok bye')

#startapi()