import discord
from dotenv import load_dotenv
from discord.ext import commands
from discord.ext.commands import CommandNotFound

import os


def get_prefix(bot, message):
    """A callable Prefix for our bot. This could be edited to allow per server prefixes."""

    # Notice how you can use spaces in prefixes. Try to keep them simple though.
    prefixes = ["!"]

    # Check to see if we are outside of a guild. e.g DM's etc.
    if not message.guild:
        # Only allow ? to be used in DMs
        return '?'

    # If we are in a guild, we allow for the user to mention us or use any of the prefixes in our list.
    return commands.when_mentioned_or(*prefixes)(bot, message)


class DiscordBot(commands.Bot):
    def __init__(self, command_prefix, description):
        super(DiscordBot, self).__init__(command_prefix=command_prefix,
                                         description=description)

    async def on_ready(self):
        print(f'\n\nLogged in as: {bot.user.name} - {bot.user.id}\nVersion: {discord.__version__}\n')
        print("Successfully logged in and booted...!")

    async def on_command_error(self, ctx, error):
        if isinstance(error, CommandNotFound):
            return ctx.send("your command is crap. don't know what to do")
        raise error


if __name__ == "__main__":
    load_dotenv()
    token = os.getenv('DISCORD_TOKEN')
    initial_extensions = ['music']
    bot = DiscordBot(command_prefix=get_prefix, description='BenjaminBot')
    for extension in initial_extensions:
        bot.load_extension(extension)
    bot.run(token, bot=True, reconnect=True)
