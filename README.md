
# 🔥 MetaV-sploit 🔥

أداة **MetaV-sploit** هي سكربت مميز لتثبيت إطار Metasploit وبعض الأدوات المساعدة بسهولة وأمان داخل بيئة **Termux**.  
تم تطويرها بواسطة **HATAN HACKER** 💻

---

## 📌 مميزات الأداة
- تثبيت إطار **Metasploit** بشكل تلقائي في Termux.
- تثبيت أدوات إضافية مثل:
  - **nmap** → أداة فحص الشبكات
  - **sqlmap** → أداة اختبار قواعد البيانات
  - **hydra** → أداة تخمين كلمات المرور
  - **wireshark** → محلل حزم الشبكة
- حفظ سجل التثبيت في ملف `installation_log.txt`.
- واجهة ملونة وسهلة الاستخدام.
- تشغيل Metasploit مباشرة بعد التثبيت.

---

## 📥 خطوات التثبيت

قم بتنفيذ الأوامر التالية داخل **Termux**:

```bash
# 1. تحديث الحزم في Termux
pkg update -y && pkg upgrade -y

# 2. تثبيت المتطلبات الأساسية (Git + Python)
pkg install git -y
pkg install python -y

# 3. تحميل المستودع من GitHub
git clone https://github.com/hatanhack/MetaV-sploit.git

# 4. الدخول إلى مجلد الأداة
cd MetaV-sploit

# 5. تشغيل أداة التثبيت لأول مرة
python MetaVsploitinstall.py


---

▶️ تشغيل الأداة

بعد تثبيت المتطلبات لأول مرة باستخدام MetaVsploitinstall.py
يمكنك تشغيل الأداة مباشرة في أي وقت بالأمر التالي:

python MetaVsploit.py


---

🚀 طريقة الاستخدام

عند تشغيل الأداة (MetaVsploit.py) ستظهر لك القائمة الرئيسية التي تحتوي على:

1. تثبيت Metasploit
يقوم بتحديث النظام، تثبيت المستودعات اللازمة، وتنصيب Metasploit ثم تشغيله مباشرة (msfconsole).


2. تثبيت أدوات إضافية
يمكنك اختيار وتثبيت أدوات مثل:

nmap → فحص الشبكات

sqlmap → اختبار قواعد البيانات

hydra → تخمين كلمات المرور

wireshark → تحليل الحزم



3. عرض سجل التثبيت
يعرض لك جميع الأدوات التي تم تثبيتها (محفوظة داخل ملف installation_log.txt).


4. الخروج
للخروج من الأداة بأمان.




---

👨‍💻 المطور

تم التطوير بكل ❤️ بواسطة HATAN HACKER
