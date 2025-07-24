import discord
from discord.ext import commands
from discord import app_commands
import os
from discord.ext import tasks
import datetime
from datetime import datetime, timezone
import comandos_bot

TOKEN = "MTM4NTgwMTg      xNzk2Mjg0NDE4MA.GvZrri.hr_07aYx7wFLGGXJKIw0o2SX7ZgNCXaHsNX3s8"
# TOKEN = os.getenv("DISCORD_TOKEN")
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", case_insensitive=True, intents=intents,help_command=None)

# todo: Cargar comandos externos desde comandos.py
comandos_bot.setup(bot)
# CANAL_ID = 138579038013331pytohn8827  # ! Reemplaza con tu canal real

# @tasks.loop(seconds=10)
# async def enviar_cada_30_dias():
#     canal = bot.get_channel(CANAL_ID)
#     if canal:
#         fecha = datetime.now(timezone.utc).strftime("%d/%m/%Y")
#         await canal.send(f"📅 ¡Han pasado 30 días! ({fecha}) Este es un recordatorio automático.")
#     else:
#         print(f"❌ No se encontró el canal con ID {CANAL_ID}")
# @enviar_cada_30_dias.before_loop
# async def antes_de_empezar():
#     await bot.wait_until_ready()
@bot.event
async def on_ready():
    print(f"✅ Bot listo como {bot.user}")
    # enviar_cada_30_dias.start()
    try:
        synced = await bot.tree.sync()
        print(f"✅ Comandos slash sincronizados ({len(synced)})")
    except Exception as e:
        print(f"❌ Error al sincronizar comandos slash: {e}")

bot.run(TOKEN)
