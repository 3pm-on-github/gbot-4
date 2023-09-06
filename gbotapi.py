# Welcome to the gbot-4 api! Here we can make actions for gbot with just an command or other things!
bot = None
apiver =  '0.0.1'
gbotver = None

class gbotapi:
    def __init__(self, botthing, gbotverthing):
        bot = botthing
        gbotver = gbotverthing

    async def sendMessage(self, channel, guild, message):
        await channel.send(str(message))
    
    def apiver(self):
        return apiver
    
    def gbotver(self):
        return gbotver