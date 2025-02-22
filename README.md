Syslog Kayıtlarını Bağlı Liste ile Yönetme

Bu proje, Linux syslog günlüklerini okumak ve bağlı liste (linked list) veri yapısı ile yönetmek için geliştirilmiştir. Python kullanılarak sistem günlükleri işlenir ve terminalde görüntülenir.

📌 Proje Özellikleri

✅ Linux syslog dosyasını okur (/var/log/syslog)
✅ Bağlı liste veri yapısını kullanarak günlükleri saklar
✅ Günlükleri ekrana yazdırır
✅ Belleği temizler

🚀 Kurulum ve Çalıştırma

1️⃣ Depoyu Kopyalayın

git clone https://github.com/kullaniciadi/syslog-linked-list.git
cd syslog-linked-list

2️⃣ Python Gereksinimi

Bu proje Python 3 kullanılarak geliştirilmiştir. Python’un yüklü olduğundan emin olun:

python3 --version

3️⃣ Script'i Çalıştırın

Root yetkisi ile çalıştırmalısınız, çünkü syslog dosyalarına erişim kısıtlıdır:

sudo python3 script.py

📜 Kod Açıklaması

Bağlı Liste Yapısı:

GunlukDugum: Tek yönlü bağlı listenin düğümünü temsil eder.

GunlukBagliListe: Bağlı listeyi yönetir (ekleme, yazdırma, temizleme).

Ana Fonksiyonlar:

syslog_oku(dosya_yolu, satir_sayisi): Syslog dosyasından son N satırı okur.

gunluk_ekle(mesaj): Yeni bir günlük ekler.

gunlukleri_yazdir(): Günlükleri terminalde gösterir.

gunlukleri_temizle(): Bağlı listeyi sıfırlar.
