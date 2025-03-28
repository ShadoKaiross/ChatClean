import discord
from discord.ext import commands
import os

TOKEN = os.getenv("TOKEN")  # Bot token'ını Replit'ten alıyoruz
intents = discord.Intents.default()
intents.messages = True  # Mesajları okuma izni
intents.guilds = True  # Sunucuları izleme izni
intents.message_content = True  # Mesaj içeriğini okuma izni

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptı!')

@bot.command()
async def temizle(ctx, channel_name: str):
    channel = discord.utils.get(ctx.guild.text_channels, name=channel_name)

    if not channel:
        await ctx.send(f"{channel_name} adlı kanal bulunamadı!")
        return

    await ctx.send(f"{channel_name} adlı kanal temizleniyor...")
    
    await channel.purge()

    await ctx.send(f"{channel_name} adlı kanal başarıyla temizlendi!")

bot.run(TOKEN)
