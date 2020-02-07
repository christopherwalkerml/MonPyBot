# bot.py
import discord
import urllib.request as urllib2

def getValidUrl(urlstr):
    url = "https://prnt.sc/" + urlstr
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2226.0 Safari/537.36'}
    req = urllib2.Request(url=url, headers=headers)

    resp = urllib2.urlopen(req, timeout=3) #check if redirect

    return resp.geturl() == url

def addString(string, index):
    lst = [c for c in string]
    if index == 6:
        return "000000"
    elif lst[-index] == '9':
        lst[-index] = 'a'
    elif lst[-index] == 'z':
        lst = [c for c in addString(''.join(lst), index + 1)]
        lst[-index] = '0'
    else:
        lst[-index] = chr(ord(lst[-index]) + 1)
    return ''.join(lst)

async def getPics(message, urlstr, amt):
    for i in range(min(amt, 10)):
        if getValidUrl(urlstr):
            await message.channel.send("https://prnt.sc/" + urlstr)
        else:
            await message.channel.send("No pictures.")
            return
        urlstr = addString(urlstr, 1)
    await message.channel.send("Next url: " + urlstr)

client = discord.Client()

@client.event
async def on_ready():
    print("MonPyBot has booted up!")

@client.event
async def on_message(message):
    if message.content.startswith('!'):
        msgs = message.content.split()
        if msgs[0] == "!help":
            embed = discord.Embed(title="MonPyBot", description="Darkolythe's Test Bot. List of commands are:", color=0x308ef7)
            embed.add_field(name="Gets an amount of pictures from prnt.sc", value="!getpic <prnt scr url> <amount>", inline=False)
            embed.add_field(name="Shows this text block", value="!help", inline=False)
            await message.channel.send(embed=embed)
        elif msgs[0] == "!getpic":
            if len(msgs) == 3:
                try:
                    int(msgs[2])
                    await message.channel.send("Fetching pictures...")
                    await getPics(message, msgs[1], int(msgs[2]))
                except TypeError:
                    await message.channel.send("Invalid syntax: !getpic <prnt scr url> <integer>")
            else:
                await message.channel.send("Invalid syntax: !getpic <prnt scr url> <amount>")
                await message.channel.send("ex: !getpic qytxtv 5")

client.run("Njc1MjI5ODEyMDIwODcxMjA4.Xj0TkA.CXBfdb2nQ0agSNgP3RfmZq9WiDk")