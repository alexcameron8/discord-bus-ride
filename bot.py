# bot.py
import os
import discord
from dotenv import load_dotenv
import "ride_the_bus_game.py"

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()


@client.event
async def on_ready():
    client.isPlaying = False
    guild = discord.utils.find(lambda g: g.name == GUILD, client.guilds)
    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("~ride"):
        if client.isPlaying:
            await message.channel.send(f"Already a game in progress (started by {client.player})!")
        else:
            # enter game loop
            client.isPlaying = True
            client.player = message.author
            client.game = ride_the_bus_game()

            f = discord.File(open(".gitignore"))

            await message.channel.send(f"Its time to play {client.player}", files=[f])

            f.close()

            # options
            reactions = ["🔴", "⚫", "♦️",
                         "♠️", "♣️", "❤️",
                         "⬆️", "⬇️", "📥", "📤"]

            def check(reaction, user):
                # need to have the available options
                return user == client.player and reaction in reactions

            while client.isPlaying:
                msg = await message.channel.send(f"Black or red")

                await msg.add_reaction("🔴")
                await msg.add_reaction("⚫")

                try:
                    await message.channel.send("You have 60 seconds to react with your answer")
                    reaction, user = await client.wait_for("reaction_add", timeout=60, check=check)

                    # check make sure game still going
                    if client.isPlaying:
                        client.game.black_or_red(reaction == "🔴")

                except:
                    client.isPlaying = False
                    await message.channel.send("Too slow game ended!")

    elif client.isPlaying and message.author == client.player and message.content.startswith("~quit"):
        client.isPlaying = False
        await message.channel.send("He's done")
    elif message.content.startswith("~help"):
        await message.channel.send("TODO: help here")

client.run(TOKEN)
