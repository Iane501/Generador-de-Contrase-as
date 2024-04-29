import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.group()
async def cool(ctx):
    """Says if a user is cool.

    In reality this just checks if a subcommand is being invoked.
    """
    if ctx.invoked_subcommand is None:
        await ctx.send(f'No, {ctx.subcommand_passed} no es cool...')


@cool.command(name='bot')
async def _bot(ctx):
    """Is the bot cool?"""
    await ctx.send('Si, el bot es cool!')

@bot.command()
async def guardar_y_enviar(ctx,*,texto):
    canal_id="1234357971455311893"

    canal_destino= bot.get_channel(int(canal_id))

    if canal_destino is None:
        await ctx.send("El canal no existe")
        return
    await canal_destino.send(texto)
    await ctx.send("¡Mensaje enviado!")

bot.run("MTIyOTU5ODE3Mzg1MzM4NDcyNQ.GYOpzF.tneK8YBEqXOERTT-B5snaTLzaRj5_lJB1l9SFk")
