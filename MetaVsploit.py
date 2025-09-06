import os
import time
import sys

def مسح_الشاشة():
    os.system("clear" if os.name == "posix" else "cls")

def طباعة_بطيئة(النص, تأخير=0.02):
    for حرف in النص + '\n':
        sys.stdout.write(حرف)
        sys.stdout.flush()
        time.sleep(تأخير)

def سجل(نص):
    with open("سجل_التثبيت.txt", "a", encoding="utf-8") as f:
        f.write(نص + "\n")

def البانر():
    os.system("pkg install figlet -y > /dev/null 2>&1")
    os.system("figlet HATAN HACKER")
    print("\033[92m" + "-" * 50)
    طباعة_بطيئة("🔥 أداة تثبيت Metasploit والأدوات المساعدة 🔥")
    طباعة_بطيئة("👨‍💻 المطور: HATAN HACKER")
    print("-" * 50)

def التحذير():
    print("\033[91m" + "*" * 40)
    طباعة_بطيئة("⚠️  ملاحظة من HATAN HACKER:")
    طباعة_بطيئة("🚫 لا تقم بتثبيت أدوات Bash خارجية.")
    طباعة_بطيئة("✅ تأكد من وجود مساحة وإنترنت جيد.")
    طباعة_بطيئة("🤖 الأداة موثوقة ومجربة من قبل HATAN HACKER.")
    print("*" * 40 + "\n")

def القائمة():
    print("\033[96m📋 القائمة الرئيسية:")
    print("1 - تثبيت Metasploit")
    print("2 - تثبيت أدوات إضافية")
    print("3 - عرض سجل التثبيت")
    print("4 - الخروج\n")

def تثبيت_msf():
    مسح_الشاشة()
    طباعة_بطيئة("⏳ جاري تحديث الحزم ...")
    os.system("pkg update -y && pkg upgrade -y")
    os.system("pkg install unstable-repo x11-repo -y")
    طباعة_بطيئة("📦 جاري تثبيت Metasploit ...")
    os.system("pkg install metasploit -y")
    طباعة_بطيئة("✅ تم التثبيت بنجاح!")
    طباعة_بطيئة("🔓 بإشراف وتطوير: HATAN HACKER")
    سجل("✅ [Metasploit] تم التثبيت بنجاح بواسطة HATAN HACKER")
    طباعة_بطيئة("🚀 سيتم تشغيل Metasploit الآن...")
    os.system("msfconsole")

def تثبيت_ادوات_اضافية():
    الادوات = {
        "1": ("nmap", "أداة فحص الشبكات"),
        "2": ("sqlmap", "أداة اختبار قواعد البيانات"),
        "3": ("hydra", "أداة تخمين كلمات المرور"),
        "4": ("wireshark", "تحليل حزم الشبكة"),
        "5": ("عودة", "")
    }

    while True:
        print("\033[95m🔧 اختر الأداة لتثبيتها:\n")
        for رقم, (اسم, وصف) in الادوات.items():
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