import os
import sys
import time
import shutil
import subprocess

# Colors
GREEN = "\033[92m"
YELLOW = "\033[93m"
PURPLE = "\033[95m"
CYAN = "\033[96m"
RED = "\033[91m"
WHITE = "\033[97m"
RESET = "\033[0m"

# Clear + Banner
os.system("clear")
os.system("figlet MetaV-sploit")

def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(5.9 / 100)

# Check if package installed
def is_package_installed(pkg_name):
    try:
        subprocess.run(
            ["dpkg", "-s", pkg_name],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            check=True
        )
        return True
    except subprocess.CalledProcessError:
        return False

# Check if msfconsole installed
def is_msf_installed():
    return shutil.which("msfconsole") is not None or os.path.isfile(
        os.path.expanduser("~/metasploit-framework/msfconsole")
    )

# --- Auto-check & auto-install ---
if not is_msf_installed():
    slowprint("[!] Metasploit not found, starting auto-install...")
    os.system("apt update -y && apt upgrade -y")
    if not is_package_installed("unstable-repo"):
        os.system("apt install unstable-repo -y")
    if not is_package_installed("x11-repo"):
        os.system("apt install x11-repo -y")
    os.system("apt install metasploit -y")
    slowprint("[✓] Metasploit installed successfully!")

# --- Menu ---
print(YELLOW + "+------------------------------------------------+")
slowprint("|         MetaV-sploit by HATAN HACKER           |")
print("+------------------------------------------------+" + RESET)

slowprint(CYAN + '''
[01] Run
[02] Update
[03] Exit
''' + RESET)

choice = input(WHITE + "Enter Your Choice : " + RESET)

if choice == "1":
    path = shutil.which("msfconsole") or os.path.expanduser("~/metasploit-framework/msfconsole")
    if os.path.isfile(path) or path:
        slowprint("[*] Launching Metasploit Console...")
        os.system(path)
    else:
        slowprint("[✗] Metasploit not found. Please reinstall.")

elif choice == "2":
    slowprint("[*] Updating system and Metasploit...")
    os.system("apt update -y && apt upgrade -y")
    os.system("apt install metasploit -y")
    slowprint("[✓] Update Completed")

elif choice == "3":
    slowprint("See You Next Time 👋")
    sys.exit()

else:
    slowprint("Invalid Choice! Please try again.")
