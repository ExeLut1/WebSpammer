import discord_webhook
from discord_webhook import DiscordEmbed, DiscordWebhook
import string
import random
import time
import requests
import colorama
import json
from colorama import Fore

colorama.init()

print("""

░██╗░░░░░░░██╗███████╗██████╗░██╗░░██╗░█████╗░░█████╗░██╗░░██╗░ ██████╗██████╗░░█████╗░███╗░░░███╗███╗░░░███╗███████╗██████╗░
░██║░░██╗░░██║██╔════╝██╔══██╗██║░░██║██╔══██╗██╔══██╗██║░██╔╝ ██╔════╝██╔══██╗██╔══██╗████╗░████║████╗░████║██╔════╝██╔══██╗
░╚██╗████╗██╔╝█████╗░░██████╦╝███████║██║░░██║██║░░██║█████═╝░ ╚█████╗░██████╔╝███████║██╔████╔██║██╔████╔██║█████╗░░██████╔╝
░░████╔═████║░██╔══╝░░██╔══██╗██╔══██║██║░░██║██║░░██║██╔═██╗░░ ╚═══██╗██╔═══╝░██╔══██║██║╚██╔╝██║██║╚██╔╝██║██╔══╝░░██╔══██╗
░░╚██╔╝░╚██╔╝░███████╗██████╦╝██║░░██║╚█████╔╝╚█████╔╝██║░╚██╗ ██████╔╝██║░░░░░██║░░██║██║░╚═╝░██║██║░╚═╝░██║███████╗██║░░██║
░░░╚═╝░░░╚═╝░░╚══════╝╚═════╝░╚═╝░░╚═╝░╚════╝░░╚════╝░╚═╝░░╚═╝ ╚═════╝░╚═╝░░░░░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═╝░░░░░╚═╝╚══════╝╚═╝░░╚═╝
Made by : Wizzly
""")

def webhkspammer():
    webhook = input(Fore.YELLOW + "[>] Webhook Url Input: ")
    message = input(Fore.GREEN + "[>] Text Untuk Spam: ")
    delay = float(input(Fore.RED + "[>] Masukkan Leg Spam (Contoh : 0.5)"))

    while True:
        print(Fore.CYAN + "Mengirim --> " + message)
        print(Fore.RESET + " ")
        try:
            time.sleep(delay)
            _data = requests.post(webhook, json={'content': message})

            if _data.status_code == 204:
                print(Fore.CYAN + "Terkirim --> " + message)
        except:
            print("Sesuatu Terjadi! / Mungkin Webhook Rusak -> " + webhook)
            time.sleep(5)
            exit()

x = 5
while x == 5:
    webhkspammer()