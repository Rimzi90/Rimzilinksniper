#!/usr/bin/env python3
import requests, time, os, re, random
from bs4 import BeautifulSoup

# Colors
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
CYAN = "\033[96m"
RESET = "\033[0m"

# Banner
banner = f"""
{RED} _____ _           _     _       _             
|  __ (_)         | |   (_)     (_)            
| |__) | _ __ ___ | |__  _ _ __  _ _ __   __ _ 
|  ___/ | '__/ _ \\| '_ \\| | '_ \\| | '_ \\ / _` |
| |   | | | | (_) | |_) | | | | | | | | | (_| |
|_|   |_|_|  \\___/|_.__/|_|_| |_|_|_| |_|\\__, |
                                          __/ |
                                         |___/ 
{YELLOW}     WhatsApp & Telegram Group Finder - by RIMZI{RESET}
"""

# Random descriptions
descriptions = [
    "🔥 Active Group - Join Fast!",
    "💬 Daily Discussions & Fun",
    "🔔 24/7 Online Members",
    "🌐 Public Group Open to All",
    "✅ Verified & Active Group"
]

# WhatsApp Group Search
def search_whatsapp(topic):
    print(f"\n{CYAN}Searching WhatsApp groups for:{RESET} {topic}\n")
    headers = {'User-Agent': 'Mozilla/5.0'}
    url = f"https://html.duckduckgo.com/html/?q=site:chat.whatsapp.com+{topic}"
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')
    count = 0

    for a in soup.find_all('a', href=True):
        href = a['href']
        match = re.search(r'uddg=(https?%3A%2F%2Fchat\.whatsapp\.com%2F[^\&]+)', href)
        if match:
            link = match.group(1).replace('%3A', ':').replace('%2F', '/')
            gid = link.split('/')[-1]
            desc = random.choice(descriptions)
            print(f"{YELLOW}╭──────────────[ ✅ SUCCESS ✅ ]──────────────╮")
            print(f"{GREEN} Group Name : {topic.title()} Group")
            print(f" ID         : {gid}")
            print(f" Link       : {link}")
            print(f" Description: {desc}")
            print(f"{YELLOW}╰────────────────────────────────────────────╯{RESET}\n")
            count += 1
            time.sleep(0.2)
    if count == 0:
        print(f"{RED}❌ No groups found.{RESET}")

# Telegram Group Search
def search_telegram(topic):
    print(f"\n{CYAN}Searching Telegram groups for:{RESET} {topic}\n")
    urls = [f"https://t.me/s/{topic}", f"https://t.me/{topic}"]
    found = False
    for url in urls:
        try:
            res = requests.get(url, timeout=5)
            if res.status_code == 200:
                desc = random.choice(descriptions)
                print(f"{YELLOW}╭──────────────[ ✅ SUCCESS ✅ ]──────────────╮")
                print(f"{GREEN} Group Name : {topic.title()} Channel/Group")
                print(f" Link       : {url}")
                print(f" Description: {desc}")
                print(f"{YELLOW}╰────────────────────────────────────────────╯{RESET}\n")
                found = True
                break
        except:
            continue
    if not found:
        print(f"{RED}❌ Group not found on Telegram.{RESET}")

# Main
os.system('clear')
print(banner)
print("\nChoose platform:")
print(" [1] WhatsApp Group Finder")
print(" [2] Telegram Group Finder")
choice = input("\n>> ").strip()

if choice == '1':
    topic = input("\n📘 Enter topic to search (e.g. PUBG, Girls, Crypto): ").strip()
    search_whatsapp(topic)
elif choice == '2':
    topic = input("\n📘 Enter Telegram group name (e.g. CryptoNews, Termux): ").strip()
    search_telegram(topic)
else:
    print(f"{RED}❌ Invalid option. Exiting...{RESET}")
