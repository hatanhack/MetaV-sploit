# MetaVsploit.py
# -*- coding: utf-8 -*-

import os
import time
import sys
import subprocess

# Clear screen
def clear_screen():
    os.system("clear" if os.name == "posix" else "cls")

# Slow print effect
def slow_print(text, delay=0.02):
    for char in text + '\n':
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)

# Log installation
def log_activity(text):
    with open("installation_log.txt", "a", encoding="utf-8") as f:
        f.write(text + "\n")

# Banner
def display_banner():
    subprocess.run(["pkg", "install", "figlet", "-y"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    os.system("figlet HATAN HACKER")
    print("\033[92m" + "-" * 50)
    slow_print("🔥 Metasploit & Utility Installation Tool 🔥")
    slow_print("👨‍💻 Developer: HATAN HACKER")
    print("-" * 50)

# Warning
def display_warning():
    print("\033[91m" + "*" * 40)
    slow_print("⚠️ Note from HATAN HACKER:")
    slow_print("🚫 Do not install external Bash tools.")
    slow_print("✅ Ensure you have enough storage and internet.")
    slow_print("🤖 This tool is reliable and tested by HATAN HACKER.")
    print("*" * 40 + "\n")

# Menu
def display_menu():
    print("\033[96m📋 Main Menu:")
    print("1 - Install Metasploit")
    print("2 - Install Additional Tools")
    print("3 - View Installation Log")
    print("4 - Exit\n")

# Install Metasploit
def install_metasploit():
    clear_screen()
    slow_print("⏳ Updating packages ...")
    os.system("pkg update -y && pkg upgrade -y")
    os.system("pkg install unstable-repo x11-repo -y")
    slow_print("📦 Installing Metasploit ...")
    os.system("pkg install metasploit -y")
    slow_print("✅ Installation completed successfully!")
    slow_print("🔓 Developed by: HATAN HACKER")
    log_activity("✅ [Metasploit] Installation completed successfully")
    slow_print("🚀 Launching Metasploit now...")
    os.system("msfconsole")

# Install extra tools
def install_additional_tools():
    tools = {
        "1": ("nmap", "Network scanning tool"),
        "2": ("sqlmap", "Database testing tool"),
        "3": ("hydra", "Password brute-forcing tool"),
        "4": ("wireshark", "Network packet analyzer"),
        "5": ("back", "Return to main menu")
    }

    while True:
        print("\033[95m🔧 Choose a tool to install:\n")
        for num, (name, desc) in tools.items():
            if name != "back":
                print(f"{num} - {name} - {desc}")
            else:
                print(f"{num} - Back to Main Menu")

        choice = input("\nEnter the tool number: ").strip()

        if choice in tools and choice != "5":
            tool_name = tools[choice][0]
            slow_print(f"📥 Installing {tool_name} ...")
            os.system(f"pkg install {tool_name} -y")
            slow_print(f"✅ {tool_name} installed successfully!")
            log_activity(f"✅ [{tool_name}] Installation completed successfully")
        elif choice == "5":
            break
        else:
            print("\033[91m[!] Invalid option. Please try again.\n")

# View log
def view_log():
    try:
        with open("installation_log.txt", "r", encoding="utf-8") as f:
            print("\n📄 Installation Log:\n")
            print(f.read())
    except FileNotFoundError:
        print("\n⚠️ No log found yet.\n")

# Main program
def main():
    clear_screen()
    display_banner()
    display_warning()

    while True:
        display_menu()
        choice = input("\033[97m🔎 Enter your choice: ").strip()

        if choice == "1":
            install_metasploit()
        elif choice == "2":
            install_additional_tools()
        elif choice == "3":
            view_log()
        elif choice == "4":
            slow_print("👋 Goodbye from HATAN HACKER!")
            log_activity("👋 User exited the tool")
            sys.exit()
        else:
            print("\033[91m[!] Invalid option. Please choose from 1 to 4.\n")

if __name__ == "__main__":
    main()
