import discord
from discord.ext import commands
from datetime import datetime, timezone, timedelta
import os

TOKEN = os.getenv("TOKEN")

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot conectado como {bot.user}")

@bot.event
async def on_member_join(member):
    agora = datetime.now(timezone.utc)
    idade_conta = agora - member.created_at

    if idade_conta < timedelta(days=90):
        try:
            await member.kick(reason="Conta com menos de 3 meses de criação.")
            print(f"{member} foi expulso por conta nova.")
        except Exception as e:
            print(f"Erro ao expulsar: {e}")

bot.run(TOKEN)
