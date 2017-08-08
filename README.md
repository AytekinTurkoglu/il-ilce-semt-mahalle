## Ptt İl, ilçe, semt, mahalle Veritabanı

Öncelikle güncel <b>xlsx</b> datasını http://postakodu.ptt.gov.tr/ bu adresten indirin.

#### Python 3.6.0 Kurulum
- https://www.python.org/downloads/ bu adresten <b>Python 3.6.0</b> sürümünü indirin. Kurulum dosyasını çalıştırdığınızda açılan sayfada alt kısımda path yoluna ekle kısmına tick atıp öyle kurulum yapın.
 
 
#### MySQL Veritabanı Ayarları
- Bir veritabanı oluşturup içine <b>data/</b> dizini altındaki <b>sablon.sql</b> dosyasını aktarın.
- <b>src/ptt-pk/</b> dizini altındaki <b>fetch.py</b> dosyasını açın. <b>Connection</b> kısmını ve <b>data/</b> dizini altındaki <b>xlsx</b> dosyasının ismini doğru şekilde ayarlayın.
 
#### Console Ayarları
- Komut istemini (Çalıştır > cmd) açın.
- Buradan indirdiğiniz dosyaları nereye çıkardıysanız cmd üzerinde o dizine gidin. 
- <b>Örn:</b> Dosyaları masaüstüne indirdiyseniz şuna benzer bir komut girin: <b>cd dosya_yolu</b>

```
 cd C:\Users\Semih\Desktop\il-ilce-semt-mahalle-master
```

- Gerekli paketleri yüklemek için : 

```
python setup.py install
```

- Aktarma işlemini başlatmak için : 

```
python src/ptt-pk/fetch.py
```

#### Dipnot

-  Sonu <b>Aktarilmis.sql</b> ile biten dosyalardan istediğiniz birini veritabanı oluşturup aktarabilirsiniz.

##### Aktardıktan sonra aşağıdaki sql komutlarını çalıştır:

```
update iller set il_adi = replace(il_adi, 'i̇', 'i');
update ilceler set ilce_adi = replace(ilce_adi, 'i̇', 'i');
update semtler set semt_adi = replace(semt_adi, 'i̇', 'i');
update mahalleler set mahalle_adi = replace(mahalle_adi, 'i̇', 'i');
```

##### Bu sql komutlarını i harfini düzeltmek için yapıyoruz.