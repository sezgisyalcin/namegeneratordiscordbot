import random
import discord
from discord import app_commands
from discord.ext import commands

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

WORDS = [
    "Sharp", "Sharpi", "Dsharp", "Sharp3", "Sim", "Stim", "Simrey", "Simre",
    "Demon", "Cricketer", "Malof", "Shard", "Scotty", "Luna", "Sacer", "Funk",
    "Splinter", "Vicious", "Moroccan", "Neuro", "Jynx", "Energetic", "Multi",
    "Joseph", "Rascal", "Fae"
]

def generate_name():
    length = random.choice([2, 3])
    parts = random.sample(WORDS, length)
    return " ".join(parts)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")
    await bot.tree.sync()
    print("Commands synced.")

@bot.tree.command(name="ping", description="Test the bot's responsiveness")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message("Pong! 🏓")

@bot.tree.command(name="genname", description="Generate a random name - Combinations where Piica mixes up our names")
async def genname(interaction: discord.Interaction):
    name = generate_name()
    await interaction.response.send_message(f"✨ Your generated name: **{name}**")

bot.run("MTQwMzcyNDU4Njg1MTUwNDIyOA.Gw4OBV.NJXdgsoYbqZNzZjtmDhrG4oWEP1UKPXTKbNGik")
