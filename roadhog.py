import discord
from discord.ext import commands as cmd

import command.crab as crab

class Roadhog(cmd.Bot):
    commands = [crab.crab]

    def __init__(self):
        cmd.Bot.__init__(self, command_prefix='!')

        for command in Roadhog.commands:
            self.add_command(command)

        print('Roadhog has landed his hook')

roadhog = Roadhog()
# TODO: use .env to retrieve bot token
roadhog.run()
