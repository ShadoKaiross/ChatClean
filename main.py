import discord
from discord.ext import commands
import os
from flask import Flask
import threading

app = Flask(__name__)

@app.route('/')
def index():
    return "Bot is running!"

def run_flask():
    app.run(host='0.0.0.0', port=8080)

def run_bot():
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

if __name__ == '__main__':
    # Flask web server'ını başlatmak için bir thread başlatıyoruz
    threading.Thread(target=run_flask).start()
    
    # Botu başlatıyoruz
    run_bot()
