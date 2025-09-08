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
slowprint("|         Install MSF Without Any Errors         |")
print("+------------------------------------------------+")
print('''\033[95m

[*] Unstable Repo
[*] x11 Repo
[*] Metasploit Framework''')
print("\033[91m                      ")
print("*********************************************")
slowprint("|                 [!] Note [!]               |")
print("|                                            |")
slowprint("[!] Do not install random bash scripts       |")
slowprint("[!] Installing wrong scripts may cause errors|")
slowprint("[!] This is the safest way to install MSF    |")
slowprint("[!] Welcome from HATAN Hacker                |")
slowprint("[!] MSF requires ~600MB space and internet   |")
print("*********************************************")

slowprint('''\033[96m
[01] Install
[02] Exit ''')
print("       ")
z = input("\033[97mEnter Your Choice : ")

if z == "1":
    os.system("clear")
    slowprint("[#] Collecting Data................................")
    slowprint("[#] Installing ....................................")
    os.system("apt update -y && apt upgrade -y")
    os.system("figlet Repo Installing")
    os.system("apt install unstable-repo -y")
    os.system("apt install x11-repo -y")
    os.system("figlet Complete")
    os.system("figlet MSF Installing")

    # Fixed installation (using official script)
    os.system("pkg install wget -y")
    os.system("wget https://raw.githubusercontent.com/gushmazuko/metasploit_in_termux/master/metasploit.sh -O metasploit.sh")
    os.system("chmod +x metasploit.sh")
    os.system("./metasploit.sh")

    os.system("figlet MSF Install")
    slowprint("[*] Starting Metasploit Framework Console..............")
    os.system("msfconsole")

elif z == "2":
    slowprint("\033[93mSee You Next Time")
    sys.exit()
