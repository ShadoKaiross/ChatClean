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
    app.run(host='0.0.0.0', port=1234)

def run_bot():  
    TOKEN = os.getenv('TOKEN')  # GitHub secrets'tan bot token'ını al
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
    @commands.has_role(1354170988870369342)  # Rol ismini buraya yazın
    async def temizle(ctx, channel_name: str):
        # Kanal adı ile kanalı bulma
        channel = discord.utils.get(ctx.guild.text_channels, name=channel_name)
    
        if not channel:
            await ctx.send(f"{channel_name} adlı kanal bulunamadı!")
            return
    
        # Kanalın geçmişindeki mesajları silme
        await ctx.send(f"{channel_name} adlı kanal temizleniyor...")
    
        # 300 mesajı silmek için döngü ile purge işlemi
        limit = 300  # Her seferinde silmek istediğiniz mesaj sayısı
        while True:
            deleted = await channel.purge(limit=100)  # Bir seferde maksimum 100 siler
            if len(deleted) < 100:  # Eğer 100'den az mesaj silindiyse, işlem tamamlanır
                break
            limit -= 100  # Silinen mesajları düşür
            if limit <= 0:  # Hedeflenen mesaj sayısına ulaşıldıysa dur
                break
    
        # Temizleme işlemi tamamlandıktan sonra bilgilendirme
        await ctx.send(f"{channel_name} adlı kanal başarıyla temizlendi!")

    bot.run(TOKEN)
    
if __name__ == '__main__':
    # Flask web server'ını başlatmak için bir thread başlatıyoruz
    threading.Thread(target=run_flask).start()

    # Botu başlatıyoruz
    run_bot()    
