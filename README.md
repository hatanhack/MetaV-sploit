# 🔥 MetaV-sploit 🔥

**MetaV-sploit** هي أداة بسيطة لتثبيت إطار **Metasploit Framework** وبعض الأدوات المساعدة بسهولة وأمان داخل بيئة **Termux**.  
تم تطويرها بواسطة **HATAN HACKER** 💻  

---

## ✨ مميزات الأداة
- تثبيت إطار **Metasploit Framework** بشكل تلقائي في Termux.
- إمكانية تثبيت أدوات إضافية مثل:
  - **nmap** → أداة لفحص الشبكات.
  - **sqlmap** → أداة لاختبار قواعد البيانات واكتشاف الثغرات.
  - **hydra** → أداة لتخمين كلمات المرور (Brute Force).
  - **wireshark** → أداة لتحليل الحزم الشبكية.
- حفظ سجل التثبيت لسهولة المراجعة لاحقًا.

---

## 📖 ما هو Metasploit؟
إطار **Metasploit** هو منصة مفتوحة المصدر لاختبار الاختراق، تم تطويرها أول مرة بواسطة **H. D. Moore** سنة 2003.  
يُستخدم Metasploit في:
- اختبار الاختراق (Penetration Testing).  
- تطوير تواقيع أنظمة كشف التسلل (IDS/IPS).  
- البحث وتطوير الثغرات (Exploit Research).  

---

## ⚙️ خطوات التثبيت (في Termux)

```bash
# تحديث وترقية الحزم
apt update -y && apt upgrade -y

# تثبيت أداة git
pkg install git -y

# نسخ المستودع من GitHub
git clone https://github.com/hatanhack/MetaV-sploit.git

# الدخول إلى مجلد الأداة
cd MetaV-sploit

# تشغيل ملف التثبيت (لتثبيت المتطلبات)
python MetaVsploitinstall.py

# تشغيل الأداة
python MetaVsploit.py
