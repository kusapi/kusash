# Known Bugs List


💀 Kusash v0.1 Bug Listesi



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


🐛 KuSaSH Known Bugs (v0.2)

1️⃣ Ctrl-C ve Ctrl-D Kapanmaları

Açıklama: Shell’den çıkarken bazen hatalı kapanabiliyor veya traceback veriyor.

2️⃣ Empty Input Hataları

Açıklama: try -e veya network --ping gibi parametreler boş bırakılırsa shell bazen IndexError veriyor.

3️⃣ Network --ping Invalid Input

Açıklama: IP adresi veya ping sayısı boş veya geçersiz girildiğinde shell bazen düzgün hata vermiyor.

4️⃣ Network --scan Display Issue

Açıklama: Çok fazla Wi-Fi ağında çıktı kayabilir veya terminal formatting bozulabilir.

5️⃣ -pkg Edge Cases

Açıklama: Paket adı veya paket yöneticisi yanlış girilirse shell bazen eksik hata mesajı veriyor.

6️⃣ --kusafetch Compatibility

Açıklama: Sistemler arası (Windows/Linux/WSL) neofetch komutu çalışmayabilir.



🟡 --kusafetch zayıf çıktı → düz ve çirkin tuple basıyo
