import discord
from discord.ext import commands
import random
import os

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="/", intents=intents)

words = [
    "Sharp", "Sharpi", "Dsharp", "Sharp3", "Sim", "Stim", "Alex", "Simre",
    "Demon", "Cricketer", "Malor", "Sacerdor", "Scotty", "Luna", "Sacer", "Funk",
    "Splinter", "Vicious", "Housni", "Neuro", "Jynx", "OG", "Multi",
    "Joseph", "Rascal", "Fae", "Saad", "MrSmooth" , "Justus" , "Jeax" 
]

@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f"Logged in as {bot.user}")

@bot.tree.command(name="ping")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message("Pong!")

@bot.tree.command(name="genname")
async def genname(interaction: discord.Interaction):
    n_words = random.choice([2, 3])
    name = " ".join(random.choices(words, k=n_words))
    await interaction.response.send_message(name)

bot.run(os.getenv("DISCORD_TOKEN"))



