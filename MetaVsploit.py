import os
import time
import sys

print("\033[92m ")
os.system("clear")
os.system("figlet MSFInstall")

def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(5.9 / 100)

print("\033[93m+------------------------------------------------+")
slowprint("|         Install MSF Without No Errors          |")
print("+------------------------------------------------+")
print('''\033[95m

[*] Unstable Repo
[*] x11 Repo
[*] Metasploit Framework''')
print("\033[91m                      ")
print("*********************************************")
slowprint("|               [!] Note [!]                |")
print("|                                           |")
slowprint("[!] Do Not Install Any Bash tool or script  |")
slowprint("[!] If You Install Bash Script              |")
slowprint("[!] You Face Too Many Errors                |")
slowprint("[!] This is best way to Install MSF         |")
slowprint("[!] If you got error then                   |")
slowprint("[!] contact: HATAN Hackr                    |")
slowprint("[!] Msf Needs ~600MB Space and Data first   |")
print("*********************************************")

slowprint('''\033[96m
[01] Install
[02] Run
[03] Update
[04] Exit ''')
print("       ")
z = input("\033[97mEnter Your Choice : ")

# Detect msfconsole path
msf_path = os.path.expanduser("~/metasploit-framework/msfconsole")
msf_update = os.path.expanduser("~/metasploit-framework/msfupdate")

if z == "1":
    os.system("clear")
    slowprint("[#] Collecting Data................................")
    slowprint("[#] Installing ....................................")
    os.system("apt update && apt upgrade -y")
    os.system("figlet Repo Installing")
    os.system("apt install unstable-repo -y")
    os.system("apt install x11-repo -y")
    os.system("figlet Complete")
    os.system("figlet MSF Installing")

    if os.path.exists(msf_path):
        slowprint("[✓] metasploit-framework already installed. Skipping reinstall.")
    else:
        os.system("chmod +x metasploit.sh")
        os.system("./metasploit.sh")

    # إضافة المسار للـ PATH عشان تقدر تستعمل msfconsole من أي مكان
    bashrc = os.path.expanduser("~/.bashrc")
    with open(bashrc, "a") as f:
        f.write(f"\nexport PATH=$PATH:$HOME/metasploit-framework\n")
    os.system("source ~/.bashrc")

    os.system("figlet MSF Install")
    slowprint("[*] Starting Metasploit Framework Console..............")
    os.system(msf_path)

elif z == "2":
    slowprint("[*] Launching Metasploit Console ..........")
    if os.path.exists(msf_path):
        os.system(msf_path)
    else:
        slowprint("[✗] Metasploit is not installed! Please choose option 1 first.")

elif z == "3":
    slowprint("[*] Updating Metasploit and packages ..........")
    os.system("apt update && apt upgrade -y")
    if os.path.exists(msf_update):
        os.system(msf_update)
    else:
        os.system(f"{msf_path} -x 'msfupdate; exit'")
    slowprint("[✓] Update Completed")

elif z == "4":
    slowprint("\033[93mSee You Next Time")
    sys.exit()

else:
    slowprint("\033[91mInvalid Choice! Please try again.")
