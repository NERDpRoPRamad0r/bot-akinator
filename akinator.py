import discord
from discord.ext import commands
from codigo_ai import ai

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='/', intents=intents)

@bot.command()
async def salvar(ctx):
    lista = ctx.message.attachments
    for arquivo in lista:
        nome = arquivo.filename
        await arquivo.save(f"imagens/{nome}")

        arquivo2 = ai("keras_model.h5",
                    "label.txt",
                    f"imagens/{nome}"
                    )

        await ctx.send(f"eu acho que é: {arquivo2}")

        

bot.run("MEU TOKEN")
