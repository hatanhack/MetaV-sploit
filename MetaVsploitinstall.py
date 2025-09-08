# MetaVsploitinstall.py
# -*- coding: utf-8 -*-

import os
import sys
import time

# Slow print effect
def slow_print(text, delay=0.03):
    for char in text + '\n':
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)

# Show banner
def show_banner():
    os.system("clear")
    os.system("figlet MetaV-sploit")
    os.system("figlet HATAN HACK")
    print("--------------------------------------------------   🔥 Metasploit & Utility Installation Tool 🔥")
    print("👨‍💻 Developer: HATAN HACKER")
    print("--------------------------------------------------")
    print("⚠️ Note from HATAN HACKER:")
    print("🚫 Do not install external Bash tools.")
    print("✅ Ensure you have enough storage and internet.")
    print("🤖 This tool is reliable and tested by HATAN HACKER.")
    print("****************************************\n")

# Install requirements
def install_requirements():
    slow_print("⏳ Updating system and installing requirements ...")
    os.system("pkg update -y && pkg upgrade -y")
    os.system("pkg install python -y")
    os.system("pkg install figlet -y")
    os.system("pkg install git -y")
    slow_print("✅ Requirements installed successfully.\n")

# Run main tool
def run_tool():
    if os.path.exists("MetaVsploit.py"):
        slow_print("🚀 Launching MetaVsploit tool ...")
        os.system("python MetaVsploit.py")
    else:
        slow_print("❌ MetaVsploit.py not found in this directory.")

if __name__ == "__main__":
    show_banner()
    install_requirements()
    run_tool()
