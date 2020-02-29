import discord
import os

client = discord.Client()

id = client.get_guild(681917060011655179)

@client.event
async def on_message(message):
    id = client.get_guild(id)
    channels = ["animal-chatter"]
    valid_users = ["larmoyant#4444"]
    
    if str(message.channel) in channels and str(message.author) in valid_users:
        if message.content.find("!hello") != -1:
            await message.channel.send("*kzzrt* Hi there! Myaubot h-here! *krsh* C-can you hear me?")
if __name__ == '__main__': client.run(os.environ.get('TOKEN'))