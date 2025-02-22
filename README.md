# Bağlı Liste Kullanarak Syslog Okuyucu

## Açıklama
Bu Python betiği, sistem günlük dosyalarını (**syslog**) okur ve **tek yönlü bağlı liste** kullanarak son N günlük kaydını saklar. Bağlı liste, Python'un yerleşik listelerini kullanmadan günlük girişlerini dinamik olarak yönetmek için kullanılır ve temel veri yapıları kavramlarını gösterir.

## Özellikler
- `/var/log/syslog` dosyasını okur.
- Günlükleri **bağlı liste** içinde saklar.
- Günlükleri **ters sırayla** (en son eklenen ilk olarak) ekrana yazdırır.
- İşlem tamamlandıktan sonra bağlı listeyi bellekten temizler.

## Gereksinimler
- Python 3.x
- Ubuntu veya Linux tabanlı bir işletim sistemi (**syslog** dosyasına erişmek için)
- Syslog dosyasını okumak için yeterli izinler (**sudo** gerekebilir)

## Kullanım
- Betik, `/var/log/syslog` dosyasından **son 5 satırı** okur.
- Bunları **tek yönlü bağlı listeye** ekler.
- Günlükleri ekrana yazdırır.
- Belleği temizler.

## Kod Genel Bakışı
### Sınıflar
1. **GunlukDugum**: Bağlı listedeki her düğümü temsil eder.
2. **GunlukBagliListe**: Tek yönlü bağlı listeyi uygular:
   - `gunluk_ekle(mesaj)`: Günlük girişini listeye ekler.
   - `gunlukleri_yazdir()`: Tüm günlükleri ekrana yazdırır.
   - `gunlukleri_temizle()`: Listeyi temizler.

### Fonksiyonlar
- **syslog_oku(dosya_yolu, satir_sayisi)**: Syslog dosyasından son `N` satırı okur.
- **ana()**: Günlükleri okuma, saklama, gösterme ve temizleme işlemlerini yönetir.


## Notlar
- **/var/log/syslog** dosyasını okumak için **root yetkileri** gerekebilir.
- Başka günlük dosyalarını okumak için `syslog_oku()` fonksiyonunu değiştirebilirsiniz.





