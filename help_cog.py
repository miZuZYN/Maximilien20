import discord
from discord.ext import commands


class help_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.help_message = """
```
Komennot:
/help - Näyttää kaikki käytettävät komennot.
/p <avainsana> - Etsii YouTube videon ja alkaa toistamaan sitä.
/q - Näyttää jonon.
/skip - Ohittaa sen hetkisen videon.
/clear - Pysäyttää toiston ja tyhjentää jonon.
/leave - Heittää botin vittuun voicesta.
/pause - Pausettaa sen hetkisen videon, tai jatkaa sen toistamista jos se on jo pausella.
/resume - Jatkaa sen hetkisen videon toistamista.
```
"""
        self.text_channel_list = []

    # some debug info so that we know the bot has started
    @commands.Cog.listener()
    async def on_ready(self):
        for guild in self.bot.guilds:
            for channel in guild.text_channels:
                self.text_channel_list.append(channel)

        await self.send_to_all(self.help_message)

    @commands.command(name="help", help="Näyttää kaikki käytössä olevat komennot.")
    async def help(self, ctx):
        await ctx.send(self.help_message)

    async def send_to_all(self, msg):
        for text_channel in self.text_channel_list:
            await text_channel.send(msg)
