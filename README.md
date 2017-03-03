## Ptt İl, ilçe, semt, mahalle Veritabanı

Öncelikle güncel <b>xlsx</b> datasını <a href="http://postakodu.ptt.gov.tr/" target="_blank">http://postakodu.ptt.gov.tr/</a> bu adresten indirin.

#### Python 3.6.0 Kurulum
 - <a href="https://www.python.org/downloads/" target="_blank">https://www.python.org/downloads/</a> bu adresten <b>Python 3.6.0</b> sürümünü indirin. Kurulum dosyasını çalıştırdığınızda açılan sayfada alt kısımda path yoluna ekle kısmına tick atıp öyle kurulum yapın.
 
 
#### MySQL Veritabanı Ayarları
 - Bir veritabanı oluşturup içine <b>sablon.sql</b> dosyasını aktarın.
 - <b>src/ptt-pk/</b> dizini altındaki <b>fetch.py</b> dosyasını açın. <b>Connection</b> kısmını ve <b>data/</b> dizini altındaki <b>xlsx</b> dosyasının ismini doğru şekilde ayarlayın.
 
#### Console Ayarları
 - Komut istemini (Çalıştır > cmd) açın.
 - Buradan indirdiğiniz dosyaları nereye çıkardıysanız cmd üzerinde o dizine gidin. 
 - <b>Örn:</b> Dosyaları masaüstüne indirdiyseniz şuna benzer bir komut girin: <b>cd dosya_yolu</b>
 - <b>cd C:\Users\Semih\Desktop\il-ilce-semt-mahalle-master</b>
 - Daha sonra şu komutu girin: <b>python setup.py install</b>
 - Son olarak aktarma işlemini başlatacağımız komutu giriyoruz: <b>python src/ptt-pk/fetch.py</b>