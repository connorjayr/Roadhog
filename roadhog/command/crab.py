from discord.ext import commands
from ..util import command

@commands.command()
async def crab(ctx):
    await ctx.send((' ' + command.strip_command(ctx.message.content) + ' ').join(20 * [':crab:']))
