import discord
from discord.ext import commands

class NotifDiscord:
    def __init__(self, token, channel):
        self.token = token
        self.channel = channel

    
    def notif(self,message):
        intents = discord.Intents.default()
        bot = commands.Bot(command_prefix="!", intents=intents)
        @bot.event
        async def on_ready():
            print(f"Connecté en tant que {bot.user}")
            channel = bot.get_channel(self.channel)
            if channel:
                await channel.send(message)
            else:
                print("Channel introuvable")
            await bot.close()  # Arrête le bot après avoir envoyé le message

        # Lance le bot
        bot.run(self.token)