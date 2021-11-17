import discord
import os
from discord.ext import commands
import random
import re
from fuzzywuzzy import fuzz

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print('logged in')
    
@client.listen('on_message')
async def gaben_listen(message):
    responses =  ['EIIIII GABEN',
                  'GABEEEEEEN',
                  'MmmmMMm GABEEEEEN',
                  '<:gaben:703198078836015154>',
                  'GAAABEEN <:gaben:703198078836015154>',
                  'GABEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEN',
                  'prysnat <:suspect:589057771933138945>' 
                  ]
    streamables = re.compile('[g|G]+[a|A]+[b|B]+[e|E]+[n|N]+')
    
    messageContent=message.content.lower()
    gaben = "gaben"

    Token_Sort_Ratio = fuzz.token_sort_ratio(gaben,messageContent)
    Token_Set_Ratio = fuzz.token_set_ratio(gaben,messageContent)
    similar = ((Token_Sort_Ratio + Token_Set_Ratio) / 2)
    
    match = streamables.search(messageContent)


    if message.author == client.user:
        return
    
    if match or similar > 60:
        await message.reply(f'{random.choice(responses)}', mention_author=False)

token = os.environ.get('api_key')        
client.run(token)
