#KusaSH

Eğlence amaçlı yapılmış bir UNZBK Group ürünüdür.

~ ❗​Kurulması/Güncellenmesi Gereken Paketler❗​ ~
python3
python3-venv
git

~ ❗​ASIL KURULUM❗​ ~

git clone https://github.com/kusapi/kusash.git
cd kusash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 main.py

~ ❗​Kullanım❗​ ~
< v0.1 için! >
try -p Merhaba Dünya
try -e echo Hello
try -pkg install git
try --kusafetch
try --whoami
try --help

💀 KusaShell v0.1 Bug Listesi
🔴 Boş input crash → ENTER basınca cmd[0] → IndexError
🔴 Eksik komut crash → try yazınca cmd[1] → IndexError
🟡 -p parametresiz kullanım → hata vermiyor, saçma boş çıktı
💀 -e komutu tehlikeli → kullanıcı istediği terminal komutunu çalıştırır
🔴 -pkg eksik parametre crash → cmd[2] yoksa patlar
🟡 -pkg install paketsiz → apt install -y saçma komut
🔴 apt bağımlılığı → apt yoksa shell düzgün çalışmaz
🟡 Gereksiz import → from sys import platform kullanılmıyor
🟡 exec değişken adı kötü → Python keyword override ediliyor
🔴 Ctrl+C / Ctrl+D crash → shell düzgün kapanmıyor
🟡 Prompt basit → profesyonel görünmüyor
🟡 --kusafetch zayıf çıktı → düz ve çirkin tuple basıyor

❗​v0.2'de bu bütün bug'lar fixlenecektir❗​
