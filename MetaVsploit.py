# -*- coding: utf-8 -*-

# Importing necessary libraries
import os
import time
import sys
import subprocess

# Function to clear the screen based on the operating system
def clear_screen():
    os.system("clear" if os.name == "posix" else "cls")

# Function for slow printing to give a cinematic effect
def slow_print(text, delay=0.02):
    for char in text + '\n':
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)

# Function to log installation activities to a file
def log_activity(text):
    with open("installation_log.txt", "a", encoding="utf-8") as f:
        f.write(text + "\n")

# Function to display the main banner
def display_banner():
    # Install figlet if it's not already installed
    subprocess.run(["pkg", "install", "figlet", "-y"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    os.system("figlet HATAN HACKER")
    print("\033[92m" + "-" * 50)
    slow_print("🔥 Metasploit & Utility Installation Tool 🔥")
    slow_print("👨‍💻 Developer: HATAN HACKER")
    print("-" * 50)

# Function to display a warning and important notes
def display_warning():
    print("\033[91m" + "*" * 40)
    slow_print("⚠️ Note from HATAN HACKER:")
    slow_print("🚫 Do not install external Bash tools.")
    slow_print("✅ Ensure you have good storage and internet.")
    slow_print("🤖 This tool is reliable and tested by HATAN HACKER.")
    print("*" * 40 + "\n")

# Function to display the main menu options
def display_menu():
    print("\033[96m📋 Main Menu:")
    print("1 - Install Metasploit")
    print("2 - Install Additional Tools")
    print("3 - View Installation Log")
    print("4 - Exit\n")

# Function to handle Metasploit installation
def install_metasploit():
    clear_screen()
    slow_print("⏳ Updating packages ...")
    os.system("pkg update -y && pkg upgrade -y")
    os.system("pkg install unstable-repo x11-repo -y")
    slow_print("📦 Installing Metasploit ...")
    os.system("pkg install metasploit -y")
    slow_print("✅ Installation completed successfully!")
    slow_print("🔓 Supervised and developed by: HATAN HACKER")
    log_activity("✅ [Metasploit] Installation completed successfully by HATAN HACKER")
    slow_print("🚀 Launching Metasploit now...")
    os.system("msfconsole")

# Function to handle installation of additional tools
def install_additional_tools():
    tools = {
        "1": ("nmap", "Network scanning tool"),
        "2": ("sqlmap", "Database testing tool"),
        "3": ("hydra", "Password brute-forcing tool"),
        "4": ("wireshark", "Network packet analyzer"),
        "5": ("back", "Back")
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
            log_activity(f"✅ [{tool_name}] Installation completed successfully by HATAN HACKER")
        elif choice == "5":
            break
        else:
            print("\033[91m[!] Invalid option. Please try again.\n")

# Function to display the installation log
def view_log():
    try:
        with open("installation_log.txt", "r", encoding="utf-8") as f:
            print("\n📄 Installation Log:\n")
            print(f.read())
    except FileNotFoundError:
        print("\n⚠️ No log found yet.\n")

# Main function of the program
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
            slow_print("👋 Goodbye with regards from HATAN HACKER!")
            log_activity("👋 User exited the tool - HATAN HACKER")
            sys.exit()
        else:
            print("\033[91m[!] Invalid option. Please choose from 1 to 4.\n")

if __name__ == "__main__":
    main()

# Function to handle installation of additional tools
def install_additional_tools():
    tools = {
        "1": ("nmap", "أداة فحص الشبكات"),
        "2": ("sqlmap", "أداة اختبار قواعد البيانات"),
        "3": ("hydra", "أداة تخمين كلمات المرور"),
        "4": ("wireshark", "تحليل حزم الشبكة"),
        "5": ("back", "الرجوع")
    }

    while True:
        print("\033[95m🔧 اختر الأداة لتثبيتها:\n")
        for num, (name, desc) in tools.items():
            if name != "back":
                print(f"{num} - {name} - {desc}")
            else:
                print(f"{num} - الرجوع إلى القائمة الرئيسية")

        choice = input("\nأدخل رقم الأداة: ").strip()

        if choice in tools and choice != "5":
            tool_name = tools[choice][0]
            slow_print(f"📥 جاري تثبيت {tool_name} ...")
            os.system(f"pkg install {tool_name} -y")
            slow_print(f"✅ تم تثبيت {tool_name} بنجاح!")
            log_activity(f"✅ [{tool_name}] تم التثبيت بنجاح بواسطة HATAN HACKER")
        elif choice == "5":
            break
        else:
            print("\033[91m[!] خيار غير صحيح. حاول مرة أخرى.\n")

# Function to display the installation log
def view_log():
    try:
        with open("installation_log.txt", "r", encoding="utf-8") as f:
            print("\n📄 سجل التثبيت:\n")
            print(f.read())
    except FileNotFoundError:
        print("\n⚠️ لا يوجد سجل حتى الآن.\n")

# Main function of the program
def main():
    clear_screen()
    display_banner()
    display_warning()

    while True:
        display_menu()
        choice = input("\033[97m🔎 أدخل خيارك: ").strip()

        if choice == "1":
            install_metasploit()
        elif choice == "2":
            install_additional_tools()
        elif choice == "3":
            view_log()
        elif choice == "4":
            slow_print("👋 إلى اللقاء مع تحيات HATAN HACKER!")
            log_activity("👋 المستخدم خرج من الأداة - HATAN HACKER")
            sys.exit()
        else:
            print("\033[91m[!] خيار غير صالح. الرجاء اختيار من 1 إلى 4.\n")

if __name__ == "__main__":
    main()        for رقم, (اسم, وصف) in الادوات.items():
            if اسم != "عودة":
                print(f"{رقم} - {اسم} - {وصف}")
            else:
                print(f"{رقم} - الرجوع إلى القائمة الرئيسية")

        خيار = input("\nأدخل رقم الأداة: ").strip()

        if خيار in الادوات and خيار != "5":
            اسم_الأداة = الادوات[خيار][0]
            طباعة_بطيئة(f"📥 جاري تثبيت {اسم_الأداة} ...")
            os.system(f"pkg install {اسم_الأداة} -y")
            طباعة_بطيئة(f"✅ تم تثبيت {اسم_الأداة} بنجاح!")
            سجل(f"✅ [{اسم_الأداة}] تم التثبيت بنجاح بواسطة HATAN HACKER")
        elif خيار == "5":
            break
        else:
            print("\033[91m[!] خيار غير صحيح. حاول مرة أخرى.\n")

def عرض_السجل():
    try:
        with open("سجل_التثبيت.txt", "r", encoding="utf-8") as f:
            print("\n📄 سجل التثبيت:\n")
            print(f.read())
    except FileNotFoundError:
        print("\n⚠️ لا يوجد سجل حتى الآن.\n")

def البرنامج():
    مسح_الشاشة()
    البانر()
    التحذير()

    while True:
        القائمة()
        خيار = input("\033[97m🔎 أدخل خيارك: ").strip()

        if خيار == "1":
            تثبيت_msf()
        elif خيار == "2":
            تثبيت_ادوات_اضافية()
        elif خيار == "3":
            عرض_السجل()
        elif خيار == "4":
            طباعة_بطيئة("👋 إلى اللقاء مع تحيات HATAN HACKER!")
            سجل("👋 المستخدم خرج من الأداة - HATAN HACKER")
            sys.exit()
        else:
            print("\033[91m[!] خيار غير صالح. الرجاء اختيار من 1 إلى 4.\n")

if __name__ == "__main__":
    البرنامج()
