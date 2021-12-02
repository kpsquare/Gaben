import aiohttp
import discord
import os
from discord.ext import commands
import random
import re
from fuzzywuzzy import fuzz

client = commands.Bot(command_prefix = '.')

# Maika ti sheiba GABEEEEEEEEEEEEEEEEEN EIIIIIIIIII x (GABEN PEDERAS) = TRUE 
# GABEN / 0 = 42
# if GABEN or NEWELL > 1750 kg
#    return my lost mmr
#    await dota patch da mi preebesh geroq pak GABEEEEEEEEN



@client.event
async def on_ready():
    print('logged in')
    
@client.listen('on_message')
async def gaben_listen(message):
    responses =  ['**EIIIII GABEN**',
                  '**GABEEEEEEN**',
                  '**MmmmMMm GABEEEEEN**',
                  '<:gaben:703198078836015154>',
                  '**GAAABEEN <:gaben:703198078836015154>**',
                  '**prysnat <:suspect:589057771933138945>**',
                  '||<:EDU:588721771373658123><:gaben:703198078836015154><:EDU:588721771373658123><:TOPKEK:588721771310743572>||',
                  '||<:gaben:703198078836015154> FREE MMR <:gaben:703198078836015154>||',
                  'gif'
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
        response = "".join(random.choices(responses, weights = [10, 10, 15, 15, 10, 10, 3, 2, 10], k = 1))
        if response == 'gif':
            ctx = await client.get_context(message)
            embed=discord.Embed()
            embed.set_image(url='https://media1.giphy.com/media/AcbborW0z5XW0/giphy.gif')
            await ctx.send(embed=embed)
        else:
        await message.reply(f'{response}', mention_author=False)

token = os.environ.get('api_key')        
client.run(token)
