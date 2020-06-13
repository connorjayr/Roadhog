import discord
from discord.ext import commands as cmd

import roadhog.command.crab as crab
import roadhog.command.gg_ears as gg_ears
import roadhog.command.stfu as stfu

class Roadhog(cmd.Bot):
    commands = [
        crab.crab,
        stfu.stfu,
        gg_ears.gg_ears,
    ]

    def __init__(self):
        cmd.Bot.__init__(self, command_prefix='!')

        for command in Roadhog.commands:
            self.add_command(command)

        print('Roadhog has landed his hook')
