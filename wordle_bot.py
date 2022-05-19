import random
import discord
from discord.ext import commands

link = 'https://discord.com/api/oauth2/authorize?client_id=968880340032700466&permissions=8&scope=bot'
TOKEN = ''
with open('./data/Token.txt') as f: 
    TOKEN = f.readline().strip()

client = discord.Client()
#bot = commands.Bot(command_prefix="-")

nijer = ['CLOTH','DREAM','SWING','HEART','WRATH','SHEEP','NIGGA','NANDI','BLACK']
good = ['Alcon','Aught','Hella','Ought','Thame','There','Thine','Thine','Where','Which','Whose','Whoso','Yours','Admit','Adopt','Agree','Allow','Alter','Apply','Argue','Arise','Avoid','Begin','Blame','Break','Bring','Build','Burst','Carry','Catch','Cause','Check','Claim','Clean','Clear','Climb','Close','Count','Cover','Cross','Dance','Doubt','Drink','Drive','Enjoy','Enter','Exist','Fight','Focus','Force','Guess','Imply','Issue','Judge','Laugh','Learn','Leave','Let’s','Limit','Marry','Match','Occur','Offer','Order','Phone','Place','Point','Press','Prove','Raise','Reach','Refer','Relax','Serve','Shall','Share','Shift','Shoot','Sleep','Solve','Sound','Speak','Spend','Split','Stand','Start','State','Stick','Study','Teach','Thank','Think','Throw','Touch','Train','Treat','Trust','Visit','Voice','Waste','Watch','Worry','Would','Write','Above','Acute','Alive','Alone','Angry','Aware','Awful','Basic','Black','Blind','Brave','Brief','Broad','Brown','Cheap','Chief','Civil','Clean','Clear','Close','Crazy','Daily','Dirty','Early','Empty','Equal','Exact','Extra','Faint','False','Fifth','Final','First','Fresh','Front','Funny','Giant','Grand','Great','Green','Gross','Happy','Harsh','Heavy','Human','Ideal','Inner','Joint','Large','Legal','Level','Light','Local','Loose','Lucky','Magic','Major','Minor','Moral','Naked','Nasty','Naval','Other','Outer','Plain','Prime','Prior','Proud','Quick','Quiet','Rapid','Ready','Right','Roman','Rough','Round','Royal','Rural','Sharp','Sheer','Short','Silly','Sixth','Small','Smart','Solid','Sorry','Spare','Steep','Still','Super','Sweet','Thick','Third','Tight','Total','Tough','Upper','Upset','Urban','Usual','Vague','Valid','Vital','White','Whole','Wrong','Young','Afore','After','Bothe','Other','Since','Slash','Until','Where','While','Aback','Abaft','Aboon','About','Above','Accel','Adown','Afoot','Afore','Afoul','After','Again','Agape','Agogo','Agone','Ahead','Ahull','Alife','Alike','Aline','Aloft','Alone','Along','Aloof','Aloud','Amiss','Amply','Amuck','Apace','Apart','Aptly','Arear','Aside','Askew','Awful','Badly','Bally','Below','Canny','Cheap','Clean','Clear','Coyly','Daily','Dimly','Dirty','Ditto','Drily','Dryly','Dully','Early','Extra','False','Fatly','Feyly','First','Fitly','Forte','Forth','Fresh','Fully','Funny','Gaily','Gayly','Godly','Great','Haply','Heavy','Hella','Hence','Hotly','Icily','Infra','Intl.','Jildi','Jolly','Laxly','Lento','Light','Lowly','Madly','Maybe','Never','Newly','Nobly','Oddly','Often','Other','Ought','Party','Piano','Plain','Plonk','Plumb','Prior','Queer','Quick','Quite','Ramen','Rapid','Redly','Right','Rough','Round','Sadly','Secus','Selly','Sharp','Sheer','Shily','Short','Shyly','Silly','Since','Sleek','Slyly','Small','So-So','Sound','Spang','Srsly','Stark','Still','Stone','Stour','Super','Tally','Tanto','There','Thick','Tight','Today','Tomoz','Truly','Twice','Under','Utter','Verry','Wanly','Wetly','Where','Wrong','Wryly','Abaft','Aboon','About','Above','Adown','Afore','After','Along','Aloof','Among','Below','Circa','Cross','Furth','Minus','Neath','Round','Since','Spite','Under','Until','Aargh','Adieu','Adios','Alack','Aloha','Avast','Bakaw','Basta','Begad','Bless','Blige','Brava','Bravo','Bring','Chook','Damme','Dildo','Ditto','Frick','Fudge','Golly','Gratz','Hallo','Hasta','Havoc','Hella','Hello','Howay','Howdy','Hullo','Huzza','Jesus','Kapow','Loose','Lordy','Marry','Mercy','Night','Plonk','Psych','Quite','Salve','Skoal','Sniff','Sooey','There','Thiam','Thwap','Tough','Twirp','Viola','Vivat','Wacko','Wahey','Whist','Wilma','Wirra','Woops','Wowie','Yecch','Yeeha','Yeesh','Yowch','Zowie','Abuse','Adult','Agent','Anger','Apple','Award','Basis','Beach','Birth','Block','Blood','Board','Brain','Bread','Break','Brown','Buyer','Cause','Chain','Chair','Chest','Chief','Child','China','Claim','Class','Clock','Coach','Coast','Court','Cover','Cream','Crime','Cross','Crowd','Crown','Cycle','Dance','Death','Depth','Doubt','Draft','Drama','Dream','Dress','Drink','Drive','Earth','Enemy','Entry','Error','Event','Faith','Fault','Field','Fight','Final','Floor','Focus','Force','Frame','Frank','Front','Fruit','Glass','Grant','Grass','Green','Group','Guide','Heart','Henry','Horse','Hotel','House','Image','Index','Input','Issue','Japan','Jones','Judge','Knife','Laura','Layer','Level','Lewis','Light','Limit','Lunch','Major','March','Match','Metal','Model','Money','Month','Motor','Mouth','Music','Night','Noise','North','Novel','Nurse','Offer','Order','Other','Owner','Panel','Paper','Party','Peace','Peter','Phase','Phone','Piece','Pilot','Pitch','Place','Plane','Plant','Plate','Point','Pound','Power','Press','Price','Pride','Prize','Proof','Queen','Radio','Range','Ratio','Reply','Right','River','Round','Route','Rugby','Scale','Scene','Scope','Score','Sense','Shape','Share','Sheep','Sheet','Shift','Shirt','Shock','Sight','Simon','Skill','Sleep','Smile','Smith','Smoke','Sound','South','Space','Speed','Spite','Sport','Squad','Staff','Stage','Start','State','Steam','Steel','Stock','Stone','Store','Study','Stuff','Style','Sugar','Table','Taste','Terry','Theme','Thing','Title','Total','Touch','Tower','Track','Trade','Train','Trend','Trial','Trust','Truth','Uncle','Union','Unity','Value','Video','Visit','Voice','Waste','Watch','Water','While','White','Whole','Woman','World','Youth']
words = nijer+good


@client.event    
async def on_ready():
    print("Client LOG in User : {0.user}".format(client))

@client.event
async def on_message(message):
    #await ctx.channel.send("Sorry for the inconvenience, but the feature will be up and running when your niggas get paid")
    
    username = str(message.author).split("#")[0]
    msg = str(message.content)
    channel = str(message.channel.name)

    if message.author == client.user:
        #await message.channel.send(f'Tu fir aa gaya')
        return
    
    # if msg.lower().find('chd')!=-1:
    #     await message.channel.send(f'Bachaoooo {username}!!!!')
    #     return

    # if msg.lower().find('date')!=-1:
    #     await message.channel.send(f'Akbar Dhyat E Jete Chai Vai')
    #     return
    
    # if msg.lower().find('society')!=-1:
    #     await message.channel.send(f'Introducing...\nAvi, MAN OF ZE SOZIETY !!!')
    #     return
    
    # if msg.lower().find('female')!=-1 or msg.lower().find('girl')!=-1:
    #     await message.channel.send(f'No Bitches ?')
    #     return

    # if msg.lower().find('youtu')!=-1:
    #     await message.channel.send(f'UThoob Kaun dekhta hai bhai, dena hai to PornHub Link de')
    #     return

    if(msg=="-wordle"):
        await message.channel.send("Welcome to the Wordle Challenge : "+(str(message.author).split("#")[0]))
        # await message.channel.send("Can you prove your Nigerian Identity ?")
        # await message.channel.send("Shit goes like the Normal Wordle :")
        await message.channel.send("Rules are same as Normal Wordle :")
        #Choose a secret word
        secret = random.choice(words).upper()
        i = 0
        flag = True
        while i < 6:
            if flag:
                # await message.channel.send('Word Bol Bsdk ! Round : ' + str(i+1))
                await message.channel.send('Choose your Wordle ! Round : ' + str(i+1))
            flag = True
            worde = await client.wait_for("message")
            word = worde.content.upper()
            # print("WORD : "+word)
            if worde.channel!=message.channel :
                # await message.channel.send("Galat Channel "+(str(worde.author).split("#")[0])+" ?")
                flag = False
                continue
            if(worde.author != message.author):
                # await message.channel.send("Kaun Hai Be Tu Imposter "+(str(worde.author).split("#")[0])+" ?")
                await message.channel.send("You're not playing the game "+(str(worde.author).split("#")[0])+" ?")
                continue
            if(word=="-QUIT"):
                # await message.channel.send("Fuck Off You Spinless Pussy "+(str(message.author).split("#")[0]))
                await message.channel.send("Guess the Wordle was that hard to make you quit "+(str(message.author).split("#")[0]))
                return
            if invalid(word):
                # await message.channel.send("Invalid Word Format, You Microscopic Brain Cell Haver")
                await message.channel.send("Invalid Word Format !")
                flag = False
                continue
            if word==secret:
                # await message.channel.send("Congrats on having a Brain : "+str(i+1)+"/6")
                await message.channel.send("Congrats on solving the Wordle : "+str(i+1)+"/6")
                result = wordify(secret,word)
                await message.channel.send(result[0])
                await message.channel.send(result[1])
                return
            else:
                result = wordify(secret,word)
                await message.channel.send(result[0])
                await message.channel.send(result[1])
                i+=1
        
        # await message.channel.send("Can't even guess a simple word you fkn RTX")
        await message.channel.send("So Close, Better Luck Next Time !")
        await message.channel.send("Wordle was :")
        result = wordify(secret,secret)
        await message.channel.send(result[0])

def invalid(word):
    # print("INVALID CHECK :")
    if len(word)!=5:
        return True
    for i in word:
        # print(i)
        if i<'A' or i>'Z':
            return True
    return False

def wordify(sec,word):
    result = ["",""]
    black = ':red_square:'
    green = ':green_square:'
    yellow = ':yellow_square:'

    secret = sec
    for i in range(5):
        result[0]+=':regional_indicator_'+word[i].lower()+':'
        if secret[i]==word[i]:
            result[1] += green
            secret = secret[:i] + '*' + secret[i + 1:]
            #secret[i]='*'
        else:
            y = False
            for j in range(5):
                if secret[j]==word[i] and word[j]!=secret[j]:
                    y = True
                    secret = secret[:i] + '*' + secret[i + 1:]
                    #secret[j]='*'
                    break
            if y:
                result[1] += yellow
            else:
                result[1] += black

    return result

client.run(TOKEN)

#print(wordify('PETIS','SAAAS'))