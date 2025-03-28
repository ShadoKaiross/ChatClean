import discord
from discord.ext import commands
import os
from flask import Flask
import threading

app = Flask(__name__)

# Web sayfası: Bu, sunucunun çalışıp çalıştığını test edebilmek için basit bir sayfa.
@app.route('/')
def home():
    return "Bot Çalışıyor!"

# Flask'ı çalıştıran fonksiyon
def run():
    app.run(host="0.0.0.0", port=5000)

# Flask sunucusunu ayrı bir thread'de çalıştır
threading.Thread(target=run).start()

# Bot kodunu buraya ekle, yani botunun geri kalan kısmı buradan devam eder.
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

# Bot komutları ve diğer bot kodları buraya gelecek
@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yapıldı!')

bot.run('YOUR_BOT_TOKEN')  # Burada botunun tokenını yazmalısın


# GitHub secrets'tan bot token'ını al
TOKEN = os.getenv('DISCORD_TOKEN')  # GitHub secrets kısmına eklediğin TOKEN ismiyle
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
