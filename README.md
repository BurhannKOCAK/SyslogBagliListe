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

## Kurulum
1. Depoyu klonlayın veya betiği indirin:
   ```sh
   git clone https://github.com/your-repo/syslog_reader.git
   cd syslog_reader
   ```
2. Python'un yüklü olduğundan emin olun:
   ```sh
   python3 --version
   ```
3. Betiği çalıştırın:
   ```sh
   python3 syslog_reader.py
   ```
   Eğer izin hatası alırsanız, şu komutu deneyin:
   ```sh
   sudo python3 syslog_reader.py
   ```

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

## Örnek Çıktı
```
=== Syslog Kayıtları ===
Feb 22 10:15:43 systemd[1]: Starting Cleanup...
Feb 22 10:15:42 kernel: [  243.540000] Network connection established
Feb 22 10:15:40 CRON[1234]: (root) CMD (/usr/bin/update)
Feb 22 10:15:39 systemd[1]: Stopping User Manager for UID 1000...
Feb 22 10:15:37 kernel: [  242.500000] USB device connected
```

## Notlar
- **/var/log/syslog** dosyasını okumak için **root yetkileri** gerekebilir.
- Başka günlük dosyalarını okumak için `syslog_oku()` fonksiyonunu değiştirebilirsiniz.

## Lisans
Bu proje açık kaynaklıdır ve MIT Lisansı altında sunulmaktadır.



