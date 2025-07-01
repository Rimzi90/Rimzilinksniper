#!/usr/bin/env python3
import os, re, time, random
import requests
from bs4 import BeautifulSoup

# Terminal Colors
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
CYAN = "\033[96m"
RESET = "\033[0m"

# Banner
def show_banner():
    os.system("clear")
    print(f"""{RED}
██╗     ██╗███╗   ██╗██╗  ██╗    ███████╗██╗███╗   ██╗██████╗ ███████╗██████╗ 
██║     ██║████╗  ██║██║ ██╔╝    ██╔════╝██║████╗  ██║██╔══██╗██╔════╝██╔══██╗
██║     ██║██╔██╗ ██║█████╔╝     ███████╗██║██╔██╗ ██║██║  ██║█████╗  ██████╔╝
██║     ██║██║╚██╗██║██╔═██╗     ╚════██║██║██║╚██╗██║██║  ██║██╔══╝  ██╔═══╝ 
███████╗██║██║ ╚████║██║  ██╗    ███████║██║██║ ╚████║██████╔╝███████╗██║     
╚══════╝╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝    ╚══════╝╚═╝╚═╝  ╚═══╝╚═════╝ ╚══════╝╚═╝     
{CYAN}        LINK FINDER - WhatsApp & Telegram Group Finder by RIMZI{RESET}
""")

# Fake descriptions for style
descriptions = [
    "🔥 Active Group - Join Fast!",
    "💬 Daily Discussions & Fun",
    "🔔 24/7 Online Members",
    "🌐 Public Group Open to All",
    "✅ Verified & Active Group"
]

# WhatsApp Finder
def find_whatsapp_groups(topic):
    print(f"\n{CYAN}Searching WhatsApp groups for:{RESET} {topic}\n")
    headers = {'User-Agent': 'Mozilla/5.0'}
    url = f"https://duckduckgo.com/html/?q=site:chat.whatsapp.com+{topic}"
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    links = []
    for a in soup.find_all("a", href=True):
        href = a["href"]
        match = re.search(r'https?://chat\.whatsapp\.com/\S+', href)
        if match and match.group(0) not in links:
            links.append(match.group(0))
        if len(links) >= 10:
            break
    if links:
        for link in links:
            print(f"{YELLOW}╭──────────────[ ✅ SUCCESS ✅ ]──────────────╮")
            print(f"{GREEN} Group Name : {topic.title()} Group")
            print(f" Link       : {link}")
            print(f" Description: {random.choice(descriptions)}")
            print(f"{YELLOW}╰────────────────────────────────────────────╯{RESET}\n")
    else:
        print(f"{RED}❌ No WhatsApp groups found.{RESET}")

# Telegram Finder
def find_telegram_groups(topic):
    print(f"\n{CYAN}Searching Telegram groups for:{RESET} {topic}\n")
    headers = {'User-Agent': 'Mozilla/5.0'}
    url = f"https://duckduckgo.com/html/?q=site:t.me+{topic}+group"
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    links = []
    for a in soup.find_all("a", href=True):
        href = a["href"]
        match = re.search(r'https?://t\.me/\S+', href)
        if match and match.group(0) not in links:
            links.append(match.group(0))
        if len(links) >= 10:
            break
    if links:
        for link in links:
            print(f"{YELLOW}╭──────────────[ ✅ SUCCESS ✅ ]──────────────╮")
            print(f"{GREEN} Group Name : {link.split('/')[-1].title()}")
            print(f" Link       : {link}")
            print(f" Description: {random.choice(descriptions)}")
            print(f"{YELLOW}╰────────────────────────────────────────────╯{RESET}\n")
    else:
        print(f"{RED}❌ No Telegram groups found.{RESET}")

# Main menu
def main():
    while True:
        show_banner()
        print(f"{GREEN}[1]{RESET} WhatsApp Group Finder")
        print(f"{GREEN}[2]{RESET} Telegram Group Finder")
        print(f"{GREEN}[0]{RESET} Exit")
        choice = input(f"\n{BLUE}>> {RESET}").strip()
        if choice == "1":
            topic = input(f"\n📘 Enter topic to search: ").strip()
            find_whatsapp_groups(topic)
        elif choice == "2":
            topic = input(f"\n📘 Enter topic to search: ").strip()
            find_telegram_groups(topic)
        elif choice == "0":
            print(f"{YELLOW}Exiting... Goodbye!{RESET}")
            break
        else:
            print(f"{RED}Invalid choice. Try again.{RESET}")
        input(f"\n{CYAN}🔁 Press Enter to return to main menu...{RESET}")

# Run it
main()#!/usr/bin/env python3
import os, re, time, random
from googlesearch import search

RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
CYAN = "\033[96m"
RESET = "\033[0m"

def show_banner():
    os.system("clear")
    print(f"""{RED}
 _____ _           _     _       _             
|  __ (_)         | |   (_)     (_)            
| |__) | _ __ ___ | |__  _ _ __  _ _ __   __ _ 
|  ___/ | '__/ _ \| '_ \| | '_ \| | '_ \ / _` |
| |   | | | | (_) | |_) | | | | | | | | | (_| |
|_|   |_|_|  \___/|_.__/|_|_| |_|_|_| |_|\__, |
                                          __/ |
                                         |___/ 
{YELLOW}   WhatsApp & Telegram Group Finder - by RIMZI{RESET}
""")

descriptions = [
    "🔥 Active Group - Join Fast!",
    "💬 Daily Discussions & Fun",
    "🔔 24/7 Online Members",
    "🌐 Public Group Open to All",
    "✅ Verified & Active Group"
]

def find_whatsapp_groups(topic):
    print(f"\n{CYAN}Searching WhatsApp groups for:{RESET} {topic}\n")
    query = f"site:chat.whatsapp.com {topic}"
    links = list(search(query, num_results=20))
    count = 0
    for link in links:
        if "chat.whatsapp.com" in link:
            gid = link.split("/")[-1]
            desc = random.choice(descriptions)
            print(f"{YELLOW}╭──────────────[ ✅ SUCCESS ✅ ]──────────────╮")
            print(f"{GREEN} Group Name : {topic.title()} Group")
            print(f" ID         : {gid}")
            print(f" Link       : {link}")
            print(f" Description: {desc}")
            print(f"{YELLOW}╰────────────────────────────────────────────╯{RESET}\n")
            count += 1
            if count >= 10:
                break
            time.sleep(0.3)
    if count == 0:
        print(f"{RED}❌ No groups found.{RESET}")

def find_telegram_groups(topic):
    print(f"\n{CYAN}Searching Telegram groups for:{RESET} {topic}\n")
    query = f"site:t.me {topic}"
    links = list(search(query, num_results=20))
    count = 0
    shown = set()
    for link in links:
        if "t.me/" in link and link not in shown:
            shown.add(link)
            name = link.split("/")[-1].replace("-", " ").title()
            desc = random.choice(descriptions)
            print(f"{YELLOW}╭──────────────[ ✅ SUCCESS ✅ ]──────────────╮")
            print(f"{GREEN} Group Name : {name}")
            print(f" Link       : {link}")
            print(f" Description: {desc}")
            print(f"{YELLOW}╰────────────────────────────────────────────╯{RESET}\n")
            count += 1
            if count >= 10:
                break
            time.sleep(0.3)
    if count == 0:
        print(f"{RED}❌ No Telegram groups found.{RESET}")

def main():
    while True:
        show_banner()
        print(f"{CYAN}Select an option:{RESET}")
        print(f"{GREEN}[1]{RESET} WhatsApp Group Finder")
        print(f"{GREEN}[2]{RESET} Telegram Group Finder")
        print(f"{GREEN}[0]{RESET} Exit")
        choice = input(f"\n{BLUE}>> {RESET}").strip()
        if choice == '1':
            topic = input(f"\n📘 Enter topic to search: ").strip()
            find_whatsapp_groups(topic)
        elif choice == '2':
            topic = input(f"\n📘 Enter topic to search: ").strip()
            find_telegram_groups(topic)
        elif choice == '0':
            print(f"{YELLOW}Exiting... Bye!{RESET}")
            break
        else:
            print(f"{RED}❌ Invalid option. Try again!{RESET}")
        input(f"\n{BLUE}Press Enter to go back to main menu...{RESET}")

main()
