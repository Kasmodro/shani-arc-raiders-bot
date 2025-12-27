import os
import asyncio
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Eingeloggt als {bot.user}")
    print("Lösche globale Commands...")
    bot.tree.clear_commands(guild=None)
    await bot.tree.sync()
    print("Globale Commands gelöscht.")
    
    for guild in bot.guilds:
        print(f"Lösche Commands für Guild: {guild.name} ({guild.id})")
        bot.tree.clear_commands(guild=guild)
        await bot.tree.sync(guild=guild)
        print(f"Commands für {guild.name} gelöscht.")
        
    print("\nAlle Commands wurden bereinigt. Starte den normalen Bot nun neu, um die Commands (nur Guild-basiert) wieder zu registrieren.")
    await bot.close()

if __name__ == "__main__":
    if not TOKEN:
        print("Fehler: DISCORD_TOKEN nicht in .env gefunden.")
    else:
        asyncio.run(bot.start(TOKEN))
