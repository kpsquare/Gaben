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
                  'gif',
                    """
;L.    .   ..,,;,;,;;;;;;L;cLjnhK558OGEBbBQQQbGpEOO8pbQQOBbQQgggggg@ggQgQgBQQggggQQgQQBQQQQQBQBQQ
;;;   .   ..::;;;,;,;;;;;,;;rzZKEhEObG8pbbQQgb8ObOGpBbQb8pbpQQgg@ggggQQ8BBB8QQQQQBQQgQQQQBQQQQQQg
;;L,   .   ..,,;;;;;;;;L;;;;;zzZoS5O8b8bEbbQgQGpOB8SOOS5j5nh5ych53SpGOGESOSEoOOO5O8BbQBQQgQgg@@@g
;;;;       .,:,,;,;;;;;;L;LLLLyoESOOp8bO8bbBg83SpGB5ncr;;;;;L:,;,,;,,,;rnnpphnKKS5OOpQgQgg@@@b7  
;;;L,      ..,:,,;,;;;;;;LLrLzcyZhGOEp5hpb8QBOcKEOE5;LLL;L,,;;,:.,:,:;,;;;ro8gQgBQQQQgg@gQZ.   rb
;;;;r:      ::,.,:,,L;L;L;;;;,;;;;;;j3oy3KOGBn;yOO8pSz7LFryjL;zKGE88BBgg@@@B8EB@@BQg@QG;   .ng@@@
;;;;;L.    ..:::.::,;;,;;;,:....   .:,;;;Ljhn;,yhBQ@ggbGzZ3Lnb88OpG88BBQggg@gg3yKppF.   ,8@@g@gQB
;;;;;;L     .:::,:. ....,.. ..,:,,;,:...;;c;:,LzSb@@@g@bp7.jSKSKF;. .  ;. ,,;;yc;oE.:Lb@@@@QQBQBQ
;;;;;LL.     :,,,,.      .,LFhOb8BQQO8h3z7;;..,L,;;;FOphByhy,;:. .;;.  ;:;FZEbBQ8QBQQ@ggQQQgBBbQB
;;;;;,,:.     .:,;,.....;LFjKZ5SShjLF7zrL;. c.  ,r7KBB8LLr8S7;;;;LcLcrjSQg@@@gQ8bpbbbQgQgQQQQBbbB
;;;;;: ......    :::.. ;,;;;::..   y.:       . .ZbE8Q@@g.,y38BhjyyFZZES8p8pB8bbQbbQQQQQQQQQQBQbbb
;;;;L.    . . :.      :,          .zLcr;;;:... :yKEbQQ@@B.p5,3bOOSGhOOOSOGppbQgBBQgQQQQBQQQQQbb8B
;;;;;;      ...,::..  ,c   ..,,;;zyn3oZnc;.... ,;ypbQQg@gg;Go3ZohOEO5OOO8b8ObQBBQQBQQQQQQQBQBB8bp
;;;;;;;.    ...:::,,;:.K;.,,;Lz7yyyzyrrLL;;....;;jbBgggg@@@8ggbhEhhK5ZEGOSKySGb8bbBbQQgQgQQQQbQBB
;;;;;;;r;.   ....:,;;;:;OF.:,;;LrrLr;L;L;;::::;;;GBgggggggg@@@ggbbOOEEhhoh5OObbBBQQQQQQgQQQQQQQQB
;;;;;;;;LL;.......:,;;r;;hG7L;L;rLLLc;r;;,,,;;;,;nbQgggQgggg@g@QQ8B88p8O8OBbbbBBQQgggQgQQQQQQBQQQ
;;;;;;;;;;;r:  ...:;,;;;;;75hKFyzyFzLc;;;L;L;;;;;yGbQgQgQgQgggQQOo3ESSG8O8pb8QBQBgQgQgQgBQBQBQBQB
;;;;;;;;;;;;L.. ..::;:;;L;L;LcjyZyZFyzFzzL;,,;;,rjEpQQgQQBgQQBBBQ5r;;LFnK5OOb8bbQBQQgggQQBQBQQQQQ
;;;;;;;;;;;;;;...:.::;,;;LLyZShGGESEKKjz;,..:;;;;ZSbQgQQQQQQ8bbQQQn;,::;;7ySEppbbBQgQQBQQQbQQQQQQ
;,;;;;;;;;;;;;,...:.::;,;;zF535oEo5jycL,.  :;,;,;yppQQgQgQQQQQgggQ8GGy;::,;roS8p88QQQQQBBBQ8QQQBQ
,;;;;;;;;;;;;;;,.:...::;;L7zj5K5K5ZyrL,.   L;;;;;ch8bQggQgQgggQbObBQBbEj;;:;;ynEE88BBQBQBQQBBQQQB
;;;;;;;;;;;;;;L;..:...::;;z7jZ5noK5Zz;;.  :;;;;;zFS8BQgg@QgBbOEnOQgQgBBpOycLL;c7yKGO88BbQBQBQBQQQ
,;,;,;;;;;;;;;;;.......,,LLz7Z333oKEnz;;:;,,:::;LKSp8QggggBbQQQQbQQgQQ8b8b53nc7KK3opOBBQBQBQbBBQB
;,;,;;;;;;;;;;;;: :.,.::;;LLyy5ZKKh5oFF;;;;;;.. .;ynhObBBZ3SOpBbQQQQQbB8bBQ8QE3KO88ObBQQQBQB8BQQg
,;;;,;,;;;,;;;;L, ..::..:;;rFZZo3ESh3ncrLL;;;;.....,;znhz;zny5O8bQQQBQQQBQQgB8ozy55nhQBQBQBQbBBQQ
;,;,;;;,;;;;;;;;L...::...:;;cLjZ5oSo53F;;;;,;,;;;;LLyyh5SS5nEOBbgg@@@@@@@Q8Sy7y7y;;LSBQbQBQQQbQBQ
,;,;;;;;;;;;,;;;;; ..:....,;;zjSo5KoZ5jL;;;;;;;L;zFE8BQQBQBb88p8OGo3jz;;;73EKno8EF;38QQQBQQQQB8BB
;,;;;;;,;,;;;,;;;;. ..:...,,;rno3j3ZKjzL;;;;;;r7jn35G5Oh5KKjZL; ,...::LhQggggbbO5y5GBBQQQQQBQBQbQ
,;,;;;;;;;;;;;;;;L,........,;FFLLnjjynFL,,,;;L;;;;::   ..  ,LjnKGBQgg@@@gQQQQQBbhoEbBQBQBQBBBQBQB
;,;,;,;,;;;;;;;;;;L. ...:...;zS;LnonK3KL;:.         .:;cjcFZpbQg@ggggQgQQbQQQQQbbG88BBQBQBBbQbBbB
,;,;,;,;,;;;,;;;;;;;. ...,. :7nZzohpGOE5y;,;::...:;y5pO888O88BBQQQQQBQQQbQbQQQQQBB8B8bpB8BBB8Q8b8
;,;,;,;,;,;;;;;;;;;;; ...:;. :LjyrSObpGhSzL;L;;;,.,;FjooEhOE5KEG8bQBQQQQQBBQQQgQQBQbb8b88bQ888Bp8
,;,;,;,;,;;;,;,;;;;;;,  ..:;. .Lz77SpbpOZF7c;L;,...:,LcnzLLKn3n5OBBQBQQgBQBBbQQgQQBQ8b8QbBBB8b8bO
;,,,;,;;;,;,;;;,;;;;;;:   .,;. .;;LyhhphS7Lr7LL;;,,:;;jK5zyKOEGS88bBQBBbb8BbQBQBQQQQQbbbb8bbbp8p8
,;,;,;,;,;,;,;,;,;;;;;L.   .:;.  ,;7y35Go5;Lc7L7;L;Lco5Go53EEShOG88bO8OppbbQbBQQBQQQbBbB8B8b888b8
;,;,;,;,;,;,;,;;;;;,;;;;.   ..,.. .,LLFzyyF;rLrcyzyz3nKojFF7yjKoEObGESpO88QBQQQBQQQBBbBbBbb88Ob8b
,;,;,;,;,;,;,;,;;;,;,;,;;. .   ... .:::;;L;rcz;nZ33on7;;;LLnKSSpG8p88b8BbQBQQQBQBQBB8bpb8b88Ob8b8
;,;,;,;,;,;,;,;,;,;;;,;;L;. .   ........:,;;rLcz3h5rL;;;Fzo5OS8Ep8bpBBBBQBQBQBBbB8b8b8bpbO88b8B8b
,,,;,;,,,;,;,;,;,;;;,;,;;;;. . . ..... . .:;;L;LLycL;LLynSSOEEhO8B8bbQBQBQQQBQ8bppO88b8b8b8B88pb8
,,,,;,;,;,;,;,;,;,;,;,;,;;;;. ... . ..... ..,,;;;;cL;;7nhZOEEEpO8bB8BbQQQQQbQb8EpO88bO8p88B8b88p8
:,:,,;,;,;,,,;,;,;,;,;,;,;;c;  ... . ....  ..,,;;;;L;LLyjoEOhSOpObOb8BbQbBbbpphGO8pB8b8pb8bbp8O8O
                   """]
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
        response = "".join(random.choices(responses, weights = [10, 10, 15, 15, 10, 10, 3, 2, 10, 2], k = 1))
        if response == 'gif':
            ctx = await client.get_context(message)
            embed=discord.Embed()
            gifs = ['https://media1.giphy.com/media/AcbborW0z5XW0/giphy.gif','https://i.pinimg.com/originals/34/44/46/344446e9a10e64452e95d6fb18c44457.jpg']
            gif = "".join(random.choices(gifs, weights = [10, 10], k = 1))
            embed.set_image(url=gif)
            await ctx.send(embed=embed)
        elif len(response) > 1000:
            gabenLocation = "./gaben.txt"
            if not os.path.exists(gabenLocation) or os.path.getsize(gabenLocation) ==  0:
                with open("gaben.txt", "w") as text_file:
                    text_file.write(response)

            ctx = await client.get_context(message)
            with open("gaben.txt", "rb") as file:
                await ctx.send(file=discord.File(file, "result.txt"))
        else:
            await message.reply(f'{response}', mention_author=False)

token = os.environ.get('api_key')
client.run(token)
