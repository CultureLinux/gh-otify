import discord
from discord.ext import commands

class NotifDiscord:
    def __init__(self, token, channel):
        self.token = token
        self.channel = channel

    
    def notif(self,projet,tags):
        intents = discord.Intents.default()
        bot = commands.Bot(command_prefix="!", intents=intents)
        @bot.event
        async def on_ready():
            print(f"Connecté en tant que {bot.user}")
            channel = bot.get_channel(self.channel)
            if channel:

                for tag in tags:
                    embed = discord.Embed(
                        title=f"**{projet}**",  # Titre en gras
                        description=f"> Un nouveau tag *{tag}* vient d'apparaitre !\n",
                        color=discord.Color.green()  # Couleur de l'embed
                    )
                    
                    embed.add_field(name="Retrouvez les changes ici", value=f"[Github](https://github.com/{projet}/releases/tag/{tag}).", inline=False)

                    await channel.send(embed=embed)
            else:
                print("Channel introuvable")
            await bot.close()  # Arrête le bot après avoir envoyé le message

        # Lance le bot
        bot.run(self.token)