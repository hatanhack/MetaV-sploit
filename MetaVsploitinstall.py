# هذا السكربت يقوم بتثبيت المتطلبات الضرورية ثم تشغيل الأداة الأساسية

import os
import sys
import time

def طباعة_بطيئة(النص, تأخير=0.03):
    for حرف in النص + '\n':
        sys.stdout.write(حرف)
        sys.stdout.flush()
        time.sleep(تأخير)

# تثبيت المتطلبات الأساسية لأداة MetaVsploit
def تثبيت_المتطلبات():
    طباعة_بطيئة("⏳ جاري تحديث النظام وتثبيت المتطلبات ...")
    os.system("pkg update -y && pkg upgrade -y")
    os.system("pkg install python -y")
    os.system("pkg install figlet -y")
    os.system("pkg install git -y")
    طباعة_بطيئة("✅ تم التثبيت بنجاح.\n")

# تشغيل ملف الأداة الرئيسي
def تشغيل_الأداة():
    if os.path.exists("MetaVsploit.py"):
        طباعة_بطيئة("🚀 جاري تشغيل أداة MetaVsploit ...")
        os.system("python MetaVsploit.py")
    else:
        طباعة_بطيئة("❌ لم يتم العثور على ملف MetaVsploit.py في هذا المجلد.")

if __name__ == "__main__":
    تثبيت_المتطلبات()
    تشغيل_الأداة()