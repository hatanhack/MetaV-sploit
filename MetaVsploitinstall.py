import os
import sys

# Colors
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
PURPLE = "\033[95m"
RESET = "\033[0m"

# Clear screen
os.system("clear")

# Banner
os.system("figlet MetaVsploit")

print(CYAN + "==========================================" + RESET)
print(GREEN + "       🔥 Welcome to MetaVsploit 🔥       " + RESET)
print(CYAN + "==========================================" + RESET)
print(PURPLE + "          Developed by: HATAN Hacker      " + RESET)

# Install required packages
os.system("pkg install figlet -y")
os.system("pkg install python -y")  # Python3 instead of Python2

print(GREEN + "\n[✔] Installation complete!" + RESET)
print(YELLOW + "👉 Now run the tool with: " + RESET + "python MetaVsploit.py")
