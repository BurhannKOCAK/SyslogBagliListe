import os  # Dosya işlemleri için gerekli kütüphane


# Bağlı liste düğüm sınıfı
class GunlukDugum:
    def __init__(self, mesaj):
        """Bağlı liste düğümü oluşturur. Her düğüm bir günlük (log) mesajı saklar."""
        self.mesaj = mesaj  # Günlük mesajını saklar
        self.sonraki = None  # Sonraki düğüme işaretçi (başlangıçta None)


# Bağlı liste sınıfı
class GunlukBagliListe:
    def __init__(self):
        """Bağlı listeyi başlatır."""
        self.bas = None  # Listenin başlangıç noktası

    def gunluk_ekle(self, mesaj):
        """Yeni bir günlük kaydı ekler (Bağlı listenin başına ekleme yapar)."""
        yeni_dugum = GunlukDugum(mesaj)  # Yeni düğüm oluştur
        yeni_dugum.sonraki = self.bas  # Yeni düğümün 'sonraki' değerini önceki başa bağla
        self.bas = yeni_dugum  # Yeni düğüm artık listenin başı olur

    def gunlukleri_yazdir(self):
        """Bağlı listedeki tüm günlük kayıtlarını ekrana yazdırır."""
        mevcut = self.bas  # Bağlı listenin başından başla
        while mevcut:  # Listenin sonuna gelene kadar devam et
            print(mevcut.mesaj)  # Günlük mesajını yazdır
            mevcut = mevcut.sonraki  # Bir sonraki düğüme geç

    def gunlukleri_temizle(self):
        """Bağlı listeyi temizler (Bellekteki referansları kaldırır)."""
        self.bas = None  # Liste başını None yaparak tüm düğümleri temizlemiş oluruz


# Syslog dosyasından belirli sayıda satır okuma fonksiyonu
def syslog_oku(dosya_yolu, satir_sayisi=10):
    """Belirtilen syslog dosyasından son N satırı okur."""
    if not os.path.exists(dosya_yolu):  # Dosya mevcut mu kontrol et
        print("Günlük dosyası bulunamadı.")
        return []

    with open(dosya_yolu, "r") as dosya:  # Dosyayı okuma modunda aç
        satirlar = dosya.readlines()  # Tüm satırları oku

    return satirlar[-satir_sayisi:]  # Son 'satir_sayisi' kadar satırı alıp döndür


# Ana çalışma fonksiyonu
def ana():
    """Bağlı liste kullanarak syslog verilerini işleten ana fonksiyon."""
    syslog_yolu = "/var/log/syslog"  # Ubuntu için varsayılan syslog yolu
    gunluk_listesi = GunlukBagliListe()  # Bağlı liste nesnesi oluştur

    gunlukler = syslog_oku(syslog_yolu, 5)  # Syslog dosyasından son 5 satırı oku
    for gunluk in gunlukler:
        gunluk_listesi.gunluk_ekle(gunluk.strip())  # Her günlük satırını bağlı listeye ekle

    print("=== Syslog Kayıtları ===")
    gunluk_listesi.gunlukleri_yazdir()  # Günlükleri ekrana yazdır

    gunluk_listesi.gunlukleri_temizle()  # Belleği temizle


# Script doğrudan çalıştırıldığında ana() fonksiyonunu çağır
if __name__ == "__main__":
    ana()
