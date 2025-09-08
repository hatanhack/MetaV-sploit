import os
import time
import sys
import shutil

# Colors
GREEN = "\033[92m"
YELLOW = "\033[93m"
PURPLE = "\033[95m"
CYAN = "\033[96m"
RED = "\033[91m"
WHITE = "\033[97m"
RESET = "\033[0m"

# Clear screen + banner
os.system("clear")
os.system("figlet MSF-Installer")

# Slow print function
def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(5.9 / 100)

# Check if metasploit is already installed
def is_installed():
    return shutil.which("msfconsole") is not None or os.path.isdir(os.path.expanduser("~/metasploit-framework"))

print(YELLOW + "+------------------------------------------------+")
slowprint("|         Install MSF Without Any Errors         |")
print("+------------------------------------------------+" + RESET)

print(PURPLE + '''
[*] Unstable Repo
[*] x11 Repo
[*] Metasploit Framework
''' + RESET)

print(RED + "*********************************************")
slowprint("|                 [!] Note [!]               |")
print("|                                             |")
slowprint("[!] Do NOT install random bash scripts        |")
slowprint("[!] They may cause too many errors            |")
slowprint("[!] This is the best way to install MSF       |")
slowprint("[!] Welcome from HATAN Hacker                 |")
slowprint("[!] MSF requires ~600MB space and data first  |")
print("*********************************************" + RESET)

# Menu
slowprint(CYAN + '''
[01] Install
[02] Run
[03] Update
[04] Exit
''' + RESET)

choice = input(WHITE + "Enter Your Choice : " + RESET)

if choice == "1":
    if is_installed():
        slowprint("[✓] Metasploit is already installed. Skipping installation.")
    else:
        os.system("clear")
        slowprint("[#] Updating packages and preparing repos...")
        os.system("apt update -y && apt upgrade -y")
        os.system("apt install unstable-repo -y")
        os.system("apt install x11-repo -y")
        os.system("apt install metasploit -y")
        # Add shortcut
        with open(os.path.expanduser("~/.bashrc"), "a") as bashrc:
            bashrc.write("\n# Metasploit shortcut\nalias msf='msfconsole'\n")
        slowprint("[✓] Metasploit installed successfully!")
        slowprint("[*] You can now run 'msf' from anywhere.")
        os.system("bash")  # reload shell with new alias

elif choice == "2":
    path = shutil.which("msfconsole")
    if path:
        slowprint(f"[*] Found msfconsole at: {path}")
    else:
        path = os.path.expanduser("~/metasploit-framework/msfconsole")
        if os.path.isfile(path):
            slowprint(f"[*] Found msfconsole at: {path}")
        else:
            slowprint("[✗] Metasploit not found! Please install first.")
            sys.exit()
    slowprint("[*] Launching Metasploit Console ..........")
    os.system(path)

elif choice == "3":
    slowprint("[*] Updating Metasploit and packages ..........")
    os.system("apt update -y && apt upgrade -y")
    os.system("apt install metasploit -y")
    slowprint("[✓] Update Completed")

elif choice == "4":
    slowprint("See You Next Time 👋")
    sys.exit()

else:
    slowprint("Invalid Choice! Please try again.")
