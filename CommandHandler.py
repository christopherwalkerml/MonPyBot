from commands.Help import helpCommand
from commands.GetPic import getPicCommand

async def commandHandler(message):
    if message.content.startswith('!'):
        msgs = message.content.split()
        if msgs[0] == "!help":
            await helpCommand(message)
        elif msgs[0] == "!getpic":
            await getPicCommand(message)
