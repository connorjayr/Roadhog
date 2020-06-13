import discord
from discord.ext import commands

@commands.command()
async def gg_ears(ctx):
    voice = ctx.author.voice
    if voice is None or voice.channel is None:
        return await ctx.send(':warning: You must be connected to a voice channel to execute this command.')
        
    if ctx.voice_client is None:
        await voice.channel.connect()
    else:
        ctx.voice_client.stop()

    def after(err):
        if err is None:
            ctx.bot.loop.create_task(ctx.voice_client.disconnect())

    source = discord.FFmpegPCMAudio('/home/connor/workspace/roadhog/roadhog/assets/gg_ears.mp3')
    ctx.voice_client.play(source, after=after)
