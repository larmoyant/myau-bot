import discord

id = client.get_guild(681917060011655179)


client = discord.Client()


@client.event
async def on_message(message):
    id = client.get_guild(id)
    channels = ["animal-chatter"]
    valid_users = ["larmoyant#4444"]

    if str(message.channel) in channels and str(message.author) in valid_users:
        if message.content.find("!hello") != -1:
            await message.channel.send("*kzzrt* Hi there! Myaubot h-here! *krsh* C-can you hear me?") 
        elif message.content == "!users":
            await message.channel.send(f"""# of Members: {id.member_count}""")

client.run(NjgyMzgwMTA4NDQ2Njk1NDU1.XlnnDw.nc3JsqwMIKvm0X9zx9QKJINg82w)