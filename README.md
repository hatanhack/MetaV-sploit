# 🔥 MetaV-sploit 🔥

أداة **MetaV-sploit** هي سكربت مميز لتثبيت إطار Metasploit والأدوات المساعدة بشكل آمن وسهل عبر بيئة Termux.  
تم تطويرها بواسطة **HATAN HACKER** 💻

---

## 📌 مميزات الأداة
- تثبيت Metasploit تلقائيًا في Termux.
- تثبيت أدوات إضافية مثل:
  - nmap (فحص الشبكات)
  - sqlmap (اختبار قواعد البيانات)
  - hydra (تخمين كلمات المرور)
  - wireshark (تحليل الشبكات)
- حفظ سجل التثبيت في ملف `سجل_التثبيت.txt`.
- واجهة ملونة وسهلة الاستخدام.
- تشغيل Metasploit مباشرة بعد التثبيت.

---

## 📥 تثبيت الأداة

```bash
# تثبيت المتطلبات
pkg update -y && pkg upgrade -y
pkg install git -y
pkg install python -y

# تحميل المستودع
git clone https://github.com/hatanhack/MetaV-sploit.git

# دخول المجلد
cd MetaV-sploit

# تشغيل أداة التثبيت
python MetaVsploitinstall.py


---

🚀 طريقة الاستخدام

بعد تشغيل السكربت، ستظهر لك واجهة رئيسية فيها:

1. تثبيت Metasploit
يقوم بتثبيت إطار Metasploit وتشغيله مباشرة.


2. تثبيت أدوات إضافية
مثل (nmap – sqlmap – hydra – wireshark).


3. عرض سجل التثبيت
لعرض الأدوات المثبتة عبر الأداة.


4. الخروج
لإنهاء البرنامج.




---

📂 ملفات المشروع

MetaVsploitinstall.py → لتثبيت المتطلبات وتشغيل الأداة الأساسية.

MetaVsploit.py → الأداة الأساسية التي تدير التثبيت والتشغيل.

سجل_التثبيت.txt → يتم إنشاؤه تلقائيًا لحفظ كل عمليات التثبيت.



---

⚠️ ملاحظات

الأداة مخصصة للاستخدام في Termux فقط.

تأكد من وجود اتصال إنترنت جيد ومساحة كافية.

الأداة موثوقة ومجربة من قبل HATAN HACKER.



---

👨‍💻 المطور

الاسم: HATAN HACKER

GitHub: MetaV-sploit
