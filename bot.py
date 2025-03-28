import discord
from discord.ext import commands
import os


# GitHub secrets'tan bot token'ını al
TOKEN = os.getenv('TOKEN')  # GitHub secrets kısmına eklediğin TOKEN ismiyle
intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
intents.message_content = True  # Mesaj içeriğini okuma izni

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptı!')

# !temizle komutu
@bot.command()
async def temizle(ctx, channel_name: str):
    # Kanal adı ile kanalı bulma
    channel = discord.utils.get(ctx.guild.text_channels, name=channel_name)

    if not channel:
        await ctx.send(f"{channel_name} adlı kanal bulunamadı!")
        return

    # Kanalın geçmişindeki tüm mesajları silme
    await ctx.send(f"{channel_name} adlı kanal temizleniyor...")

    # Mesajları temizleme işlemi
    await channel.purge()

    # Temizleme işlemi tamamlandıktan sonra bilgilendirme
    await ctx.send(f"{channel_name} adlı kanal başarıyla temizlendi!")

bot.run(TOKEN)
