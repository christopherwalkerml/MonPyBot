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
            return False
        urlstr = addString(urlstr, 1)
    await message.channel.send("Next url: " + urlstr)
    return True

async def getPicCommand(message):
    msgs = message.content.split()
    if len(msgs) == 3:
        try:
            int(msgs[2])
            await message.channel.send("Fetching pictures...")
            if not await getPics(message, msgs[1], int(msgs[2])):
                await message.channel.send("ex: !getpic qytxtv 5")
        except TypeError:
            await message.channel.send("Invalid syntax: !getpic <prnt scr url> <integer>")
    else:
        await message.channel.send("Invalid syntax: !getpic <prnt scr url> <amount>")
        await message.channel.send("ex: !getpic qytxtv 5")