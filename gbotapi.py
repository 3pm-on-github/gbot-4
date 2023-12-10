# Welcome to the gbot-4 api! Here we can make actions for gbot with just an command or other things!
bot = None
apiver =  '0.0.2'
gbotver = None

class gbotapi:
    def __init__(self, botthing, gbotverthing):
        global bot
        global gbotver
        bot = botthing
        gbotver = gbotverthing

    async def sendMessage(self, channel, message):
        await channel.send(str(message))
    
    def apiver(self):
        global apiver
        return apiver
    
    def gbotver(self):
        global gbotver
        return gbotver