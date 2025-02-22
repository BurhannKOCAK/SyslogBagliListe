# Syslog Reader with Linked List
Bu Python scripti, bir sistemin log dosyasındaki en son günlük kayıtlarını okur, bağlı liste (linked list) yapısında saklar ve ekrana yazdırır. Ardından listeyi temizler.

## Proje Özeti
* Amaç:
Syslog dosyasından son günlük kayıtlarını okuma, bağlı liste yapısında saklama ve yazdırma.

Kullanılan Yöntem:
Bağlı liste yapısı (Linked List) kullanılarak log kayıtları yönetilir ve işlenir.

Kriterler:

Bağlı Liste Yapısı: Log kayıtları bağlı listeye eklenir ve sırasıyla ekrana yazdırılır.
Dosya Okuma: Syslog dosyasından son N satır okunur (varsayılan olarak 10 satır).
Bellek Temizliği: Kullanılmayan veriler ve bağlantılar temizlenir.
Kullanılan Teknolojiler
Python: Proje Python dilinde yazılmıştır.
os: Dosya işlemleri için kullanılmıştır.
Kurulum
Python yüklü olduğundan emin olun. Python'u buradan indirebilirsiniz.

Repo'yu klonlayın veya dosyaları bir klasöre indirin.

bash
Copy
Edit
git clone https://github.com/username/repository.git
Gerekli Python modüllerini yükleyin (eğer herhangi bir modül eksikse):

bash
Copy
Edit
pip install -r requirements.txt
Kullanım
Projeyi çalıştırın ve syslog dosyasından günlük kayıtlarını okuyun:

bash
Copy
Edit
python syslog_reader.py
Kodu özelleştirmek isterseniz, syslog_oku fonksiyonunun satir_sayisi parametresini değiştirerek okunan satır sayısını ayarlayabilirsiniz.

python
Copy
Edit
gunlukler = syslog_oku(syslog_yolu, 10)  # Son 10 satırı oku
Kod Açıklamaları
1. GunlukDugum Sınıfı
Bu sınıf, bağlı listedeki her bir günlük kaydını temsil eder.
Her düğüm bir günlük mesajı (mesaj) ve bir işaretçi (sonraki) içerir.
2. GunlukBagliListe Sınıfı
Bağlı listeyi yönetir ve günlükleri ekler, yazdırır ve temizler.
gunluk_ekle: Yeni bir günlük kaydını listenin başına ekler.
gunlukleri_yazdir: Listeyi ekrana yazdırır.
gunlukleri_temizle: Belleği temizler.
3. syslog_oku Fonksiyonu
Syslog dosyasından belirli sayıda satırı okur ve döndürür.
4. ana Fonksiyonu
Ana program işlevi olarak günlükleri okur, listeye ekler ve yazdırır.
