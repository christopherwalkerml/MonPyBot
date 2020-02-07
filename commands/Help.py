import discord

async def helpCommand(message):
    embed = discord.Embed(title="MonPyBot", description="Darkolythe's Test Bot. List of commands are:", color=0x308ef7)
    embed.add_field(name="Gets an amount of pictures from prnt.sc", value="!getpic <prnt scr url> <amount>", inline=False)
    embed.add_field(name="Shows this text block", value="!help", inline=False)
    await message.channel.send(embed=embed)