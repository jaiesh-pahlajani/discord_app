from discord.ext import commands
from discord_bot.settings import DISCORD_TOKEN
from modules.message_handling import (
    Hey,
    Google,
    Recent
)
from discord_bot.enums import (
    DoloresReceives
)

client = commands.Bot(command_prefix='')


@client.event
async def on_ready():
    # Dolores is online
    print('Dolores is all set!')


@client.event
async def on_message(command):
    """
        Function to Handle all messages
    """
    try:
        # Extract Message form Command object
        message = command.content.lower()
        message_class = None

        # Assign the message class object based on message
        if message.startswith(DoloresReceives.HEY.value):
            message_class = Hey(message)
        elif message.startswith(DoloresReceives.GOOGLE_SEARCH.value):
            message_class = Google(message)
        elif message.startswith(DoloresReceives.RECENT.value):
            message_class = Recent(message)

        # handle the message
        reply = message_class.handle()

        # reply back
        await command.channel.send(reply)
    except Exception as e:
        print(str(e))


def start_dolores():
    # Start Bot Dolores
    client.run(DISCORD_TOKEN)
