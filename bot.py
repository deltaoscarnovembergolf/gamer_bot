# bot.py
import os

import time


import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

@client.event
async def on_ready():
	guild_count = 0

	print(f"{client.user} is connected to the following guilds:\n")
	
	for guild in client.guilds:
		guild_count += 1

		print( 
			f"- {guild.name} (id: {guild.id})")

#			f'{guild.name}(id: {guild.id})')

	print(f"gamer bot is in {str(guild_count)} guilds")

@client.event
async def on_message(message):
	prefix = "$"
	new_prefix = ""

	img1 = "https://i.imgur.com/nuMETTo.png"
	img2 = "https://i.imgur.com/xXA413h.png"
	img3 = "https://i.imgur.com/WmkWxvB.png"

	if message.content == prefix + "gamer":
		await message.channel.send(f"{img1}\n{img2}\n{img3}")

	elif message.content == prefix + "owner":
		await message.channel.send(discord.Member.display_name)

	elif message.content == prefix + "carl":
		await message.channel.send("<:Carl:787817526665936906>")

	elif message.content == prefix + "eg":
		await message.channel.send("<:egg_cat:768894731219763290>")

	elif message.content == prefix + "bock":
		await message.channel.send("note bock")

	elif message.content == prefix + "ban everyone":
		await message.channel.send("everyone has been banned")
		await message.channel.send(":moyai:")

	elif message.content == "gamer bot is all powerful":
		await message.channel.send("you dont even know my true form :moyai:")

	elif message.content == prefix + "ban me mr bot":
		await message.channel.send("aight")
		await message.channel.send("band :moyai:")

#		each message is separated by an uncomfortable pause
#		as vsauce demonstrates here

	elif message.content == prefix + "vsauce":
		await message.channel.send("oh, hi! heh,")
		time.sleep(1.7)
		await message.channel.send("i didn't see you come in.")
		time.sleep(2)
		await message.channel.send("do you feel this... connection we have? heh,")
		time.sleep(2.5)
		await message.channel.send("i've been feeling it all day... \*heavy breathing\*")
		time.sleep(2.5)
		await message.channel.send("i know!")
		time.sleep(2.5)
		await message.channel.send("...are you thinking what i'm thinking?")
		time.sleep(2.5)
		await message.channel.send("\*giggles\* no, no you say it first!")
		time.sleep(2.5)
		await message.channel.send("you- ok, i'll say it,")
		time.sleep(2.5)
		await message.channel.send("**6,606.48.**")
		time.sleep(2.5)
		await message.channel.send("_ᴅɪᴠɪᴅᴇᴅ ʙʏ 2!_")
		time.sleep(2.5)
		await message.channel.send("\*silent kisses\*")

		




#	elif message.content == prefix + "command":
#		await message.channel.send("

#	elif message.content == prefix + "command":
#		await message.channel.send("




client.run(TOKEN)
