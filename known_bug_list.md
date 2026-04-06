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



🟡 --kusafetch zayıf çıktı → düz ve çirkin tuple basıyor
