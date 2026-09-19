import json
import os

# Complete Flashcard database builder for Tarih (12 Topics x 10 Flashcards = 120 Flashcards)
tarih_flashcard_database = {
  "topic-tarih-ilk-turk-devletleri": [
    {"card_number": 1, "title": "Asya Hun Devleti Kurucusu", "body": "Tarihte bilinen ilk Türk devletidir. Kurucusu Teoman, en parlak dönemi ise mete Han dönemidir."},
    {"card_number": 2, "title": "Mete Han ve Onlu Sistem", "body": "Mete Han M.Ö. 209 yılında ilk düzenli Türk ordusunu kurmuş ve Onlu Sistemi getirmiştir (Kara Kuvvetlerinin kuruluşu kabul edilir)."},
    {"card_number": 3, "title": "Kavimler Göçü Sonuçları", "body": "Balamir önderliğinde başlayan göçle Roma İkiğe ayrılmış, Feodalite (Derebeylik) doğmuş ve İlk Çağ kapanıp Orta Çağ başlamıştır."},
    {"card_number": 4, "title": "Yerleşik Hayata Geçen İlk Türkler", "body": "Uygurlar, Maniheizm dinini kabul ederek yerleşik hayata geçen, ilk Türk şehrini (Ordu-Balık) ve matbaayı kullanan ilk Türk devletidir."},
    {"card_number": 5, "title": "Göktürkler (Kök Türkler)", "body": "Tarihte 'Türk' adını ilk kez resmi devlet adı olarak kullanan devlettir. Bumin Kağan tarafından kurulmuştur."},
    {"card_number": 6, "title": "Orhun Abideleri Özelliği", "body": "II. Göktürk (Kutluk) döneminde dikilen ilk Türkçe yazılı belgelerdir. Bilge Kağan, Kül Tigin ve Vezir Tonyukuk adına dikilmiştir."},
    {"card_number": 7, "title": "İslamiyeti Kabul Eden İlk Türk Boyu", "body": "Karluklar, 751 Talas Savaşı'nda Müslüman Arapların yanında yer alarak İslamiyet'i kabul eden ilk Türk boyu olmuştur."},
    {"card_number": 8, "title": "Museviliği Kabul Eden İlk Türkler", "body": "Hazarlar, Musevilik dinini benimseyen tek Türk devletidir. Ticaret yolları sayesinde Hazar Barış Çağı'nı (Pax Hazarica) yaşatmışlardır."},
    {"card_number": 9, "title": "İstiklal Simgesi Töre ve Kut", "body": "Kut, hükümdara yönetme yetkisinin Tanrı tarafından verildiğine inanılmasıdır. Töre ise yazısız hukuk kurallarıdır."},
    {"card_number": 10, "title": "Kurultay (Toy / Keneş)", "body": "Siyasi, askeri ve ekonomik kararların alındığı devlet meclisidir. Kağan olmadığında eşi Hatun da toplantılara katılabilir."}
  ],
  "topic-tarih-turk-islam": [
    {"card_number": 1, "title": "İlk Müslüman Türk Devleti", "body": "Orta Asya'da kurulan ilk Müslüman Türk devleti Karahanlılar'dır (Satuk Buğra Han dönemi). Doğu Avrupa'da ise İtil Bulgar Devleti'dir."},
    {"card_number": 2, "title": "Divan-ı Lügati't-Türk", "body": "Kaşgarlı Mahmut tarafından Araplara Türkçe öğretmek amacıyla yazılan ilk Türkçe sözlüktür (İçinde ilk Türk dünyası haritası bulunur)."},
    {"card_number": 3, "title": "Kutadgu Bilig (Mutluluk Veren Bilgi)", "body": "Yusuf Has Hacip tarafından Tabgaç Buğra Han'a sunulan ilk İslami Türk eseridir; siyasetname niteliğindedir."},
    {"card_number": 4, "title": "Gazneli Mahmud Unvanı", "body": "Hindistan'a 17 sefer düzenleyerek İslamiyet'i yayan ve tarihte 'Sultan' unvanını kullanan ilk Türk hükümdarı Gazneli Mahmud'dur."},
    {"card_number": 5, "title": "Dandanakan Savaşı (1040)", "body": "Büyük Selçuklu Devleti ile Gazneliler arasında yapılmış, Büyük Selçuklu resmen kurulurken Gazneliler yıkılış sürecine girmiştir."},
    {"card_number": 6, "title": "Malazgirt Savaşı (1071)", "body": "Sultan Alparslan'ın Bizans'ı mağlup ettiği, Anadolu'nun kapılarını Türklere açan ve 'Yurt Açan Savaş' olarak bilinen tarihi zaferdir."},
    {"card_number": 7, "title": "Miryokefalon Savaşı (1176)", "body": "II. Kılıç Arslan döneminde Bizans mağlup edilmiş, Anadolu'nun Türk yurdu olduğu kesinleşmiş ('Yurt Tutan Savaş') ve Bizans savunmaya geçmiştir."},
    {"card_number": 8, "title": "Anadolu'daki İlk Türk Medresesi", "body": "Danişmentliler tarafından Tokat Niksar'da kurulan Yağıbasan Medresesi, Anadolu'da yapılan ilk Türk medresesidir."},
    {"card_number": 9, "title": "Nizamiye Medreseleri", "body": "Büyük Selçuklu Veziri Nizamülmülk tarafından Bağdat'ta kurulan, dünyanın ilk üniversitesi kabul edilen medresedir."},
    {"card_number": 10, "title": "Kösedağ Savaşı (1243)", "body": "Anadolu Selçuklu Devleti'nin Moğollara (İlhanlılar) yenildiği ve Anadolu'da İkinci Beylikler Dönemi'nin başladığı yıkılış savaşıdır."}
  ],
  "topic-tarih-osmanli-kurulus-yukselme": [
    {"card_number": 1, "title": "Osmanlı'nın Kurucusu ve İlk Başkent", "body": "Osmanlı Devleti 1299'da Osman Bey tarafından Söğüt ve Domaniç merkezli kurulmuştur. İlk fethedilen önemli merkez Karacahisar'dır."},
    {"card_number": 2, "title": "Koyunhisar (Bafeus) Savaşı (1302)", "body": "Osman Bey döneminde Bizans ile yapılan ilk resmi savaştır ve galibiyetle sonuçlanmıştır."},
    {"card_number": 3, "title": "İlk Osmanlı Parası ve Vergi", "body": "Bakır para (Mangır) Osman Bey döneminde basılmış, ilk vergi (Bac vergisi) yine bu dönemde konulmuştur."},
    {"card_number": 4, "title": "Bursa'nın Fethi ve İskan Politikası", "body": "Orhan Bey Bursa'yı fethederek başkent yapmıştır. İskan politikası ile Balkanlar'a Göçebe Türkmenler yerleştirilmiştir."},
    {"card_number": 5, "title": "İlk Düzenli Ordu (Yaya ve Müsellem)", "body": "Orhan Bey döneminde kurulmuştur. Ayrıca ilk Osmanlı donanması Karesioğulları Beyliği'nin katılmasıyla elde edilmiştir."},
    {"card_number": 6, "title": "I. Kosova Savaşı (1389)", "body": "I. Murat döneminde Haçlılara karşı kazanılan zaferdir. İlk kez top kullanılmış, I. Murat savaş alanında şehit düşen tek padişahtır."},
    {"card_number": 7, "title": "Ankara Savaşı (1402) ve Fetret Dönemi", "body": "Yıldırım Bayezid ile Timur arasında yapılmış, Osmanlı yenilmiş ve 11 yıl süren iç karışıklık (Fetret Dönemi) başlamıştır."},
    {"card_number": 8, "title": "İstanbul'un Fethi (1453)", "body": "II. Mehmet (Fatih) tarafından fethedilmiş, Bizans yıkılmış, Orta Çağ kapanıp Yeni Çağ başlamış, Fatih 'Fatih' unvanını almıştır."},
    {"card_number": 9, "title": "Preveze Deniz Zaferi (1538)", "body": "Barbaros Hayrettin Paşa komutasındaki Osmanlı donanmasının Haçlı donanmasını mağlup ettiği ve Akdeniz'in Türk gölü haline geldiği zaferdir."},
    {"card_number": 10, "title": "İlk Osmanlı Halifesi Yavuz Sultan Selim", "body": "1517 Mısır Seferi (Rizdaniye Savaşı) ile Memlük Devleti'ne son verilmiş, kutsal emanetler İstanbul'a getirilmiş ve Halifelik Osmanlı'ya geçmiştir."}
  ],
  "topic-tarih-osmanli-duraklama-gerileme": [
    {"card_number": 1, "title": "Duraklama Dönemi İç Nedenleri", "body": "Merkezi yönetimin bozulması, beşik ulemalığı (alimin oğlu alimdir), yeniçeri isyanları ve tımar sisteminin bozulmasıdır."},
    {"card_number": 2, "title": "Ferhat Paşa Antlaşması (1590)", "body": "Iran ile imzalanmış olup Osmanlı Devleti'nin DOĞUDA EN GENİŞ SINIRLARA ulaştığı antlaşmadır."},
    {"card_number": 3, "title": "Bucaş Antlaşması (1672)", "body": "Lehistan ile imzalanmış olup Osmanlı Devleti'nin BATI'DA EN GENİŞ SINIRLARA ulaştığı antlaşmadır."},
    {"card_number": 4, "title": "Karlofça Antlaşması (1699)", "body": "Osmanlı'nın Batı'da ilk kez büyük miktarda toprak kaybettiği ve Gerileme Dönemi'ne girdiği tarihi antlaşmadır."},
    {"card_number": 5, "title": "Zitvatorok Antlaşması (1606)", "body": "Avusturya kralı protokolde Osmanlı padişahına denk sayılmış, Osmanlı'nın Kanuni dönemindeki diplomatik üstünlüğü sona ermiştir."},
    {"card_number": 6, "title": "Genç Osman (II. Osman) Islahatı", "body": "Yeniçeri Ocağı'nı kaldırmayı planlayan ilk padişahtır. Yedikule zindanlarında Yeniçeriler tarafından şehit edilmiştir."},
    {"card_number": 7, "title": "Lale Devri (1718-1730)", "body": "Passarofça Antlaşması ile başlayıp Patrona Halil İsyanı ile biten, Batı'nın üstünlüğünün kabul edildiği barış ve zevk dönemidir."},
    {"card_number": 8, "title": "İlk Özel Türk Matbaası", "body": "Lale Devri'nde İbrahim Müteferrika ve Sait Efendi tarafından kurulmuştur. Basılan ilk eser Vankulu Lügati'dir."},
    {"card_number": 9, "title": "Küçük Kaynarca Antlaşması (1774)", "body": "Kırım bağımsız olmuş (ilk kez halkı Müslüman toprak kaybı), Rusya'ya kapitülasyon verilmiş ve Rusya Karadeniz'e inmiştir."},
    {"card_number": 10, "title": "Nizam-ı Cedid Ordusu", "body": "III. Selim tarafından Batı tarzında kurulan ilk düzenli ordudur. İrad-ı Cedid adında yeni bir hazine ile finanse edilmiştir."}
  ],
  "topic-tarih-osmanli-dagilma-islahat": [
    {"card_number": 1, "title": "Sened-i İttifak (1808)", "body": "II. Mahmut ile Ayanlar arasında imzalanmıştır. Padişahın yetkileri ilk kez kısıtlanmış ve anayasal sürecin ilk adımı kabul edilmiştir."},
    {"card_number": 2, "title": "Vaka-i Hayriye (1826)", "body": "II. Mahmut tarafından Yeniçeri Ocağı'nın kaldırılması olayıdır. Yerine Asakir-i Mansure-i Muhammediye ordusu kurulmuştur."},
    {"card_number": 3, "title": "Tanzimat Fermanı (1839)", "body": "Mustafa Reşit Paşa tarafından Gülhane Parkı'nda okunmuştur. Hukukun üstünlüğü ilkesi kabul edilmiş ve kanun önünde eşitlik getirilmiştir."},
    {"card_number": 4, "title": "Islahat Fermanı (1856)", "body": "Parrıs Antlaşması öncesi gayrimüslimlere ekstra din, vicdan ve mülkiyet hakları tanıyan fermandır."},
    {"card_number": 5, "title": "I. Meşrutiyet ve Kanun-i Esasi (1876)", "body": "II. Abdülhamit döneminde ilan edilmiştir. Kanun-i Esasi Türk tarihinin İLK ANAYASASI'dır; Meclis-i Mebusan açılmıştır."},
    {"card_number": 6, "title": "31 Mart Vakası (1909)", "body": "Türk tarihinde rejim değişikliğine karşı çıkan ilk isyandır. İsyanı Hareket Ordusu bastırmış, Kurmay Başkanı Mustafa Kemal olmuştur."},
    {"card_number": 7, "title": "Trablusgarp Savaşı (1911-1912)", "body": "İtalya'ya karşı yapılan savaştır. Mustafa Kemal Derne ve Tobruk'ta tüccar (Gazeteci Şerif) kılığında yerel halkı örgütlemiştir."},
    {"card_number": 8, "title": "Uşi Antlaşması (1912)", "body": "Trablusgarp Savaşı sonrası imzalanmış, Osmanlı Kuzey Afrika'daki SON TOPRAĞINI kaybetmiş, 12 Ada geçici olarak İtalya'ya verilmiştir."},
    {"card_number": 9, "title": "Balkan Savaşları (1912-1913)", "body": "I. Balkan'da Karadağ, Yunanistan, Sırbistan ve Bulgaristan saldırmıştır. Midye-Enez hattının batısı kaybedilmiş, Arnavutluk bağımsız olmuştur."},
    {"card_number": 10, "title": "Bab-ı Ali Baskını (1913)", "body": "I. Balkan Savaşı yenilgisi üzerine İttihat ve Terakki'nin hükümet darbesiyle yönetimi tamamen ele geçirdiği olaydır."}
  ],
  "topic-tarih-osmanli-kultur-medeniyet": [
    {"card_number": 1, "title": "Divan-ı Hümayun ve Baş meclis", "body": "Orhan Bey kurmuş, II. Mahmut kaldırmıştır. Fatih'ten itibaren Sadrazam başkanlık etmeye başlamıştır."},
    {"card_number": 2, "title": "Seyfiye (Kılıç Ehli)", "body": "Yönetim ve askerlik sınıfıdır. Sadrazam, Kubbealtı vezirleri, Kaptan-ı Derya, Yeniçeri Ağası bu sınıftadır."},
    {"card_number": 3, "title": "İlmiye (İlim Ehli)", "body": "Adalet, din ve eğitim sınıfıdır. Şeyhülislam, Kazasker, Kadı ve Müderrisler bu sınıftadır (Sadrazam olamazlar)."},
    {"card_number": 4, "title": "Kalemiye (Kalem Ehli)", "body": "Bürokrasi ve diplomasi sınıfıdır. Nişancı, Defterdar ve Reisülküttab bu sınıftadır."},
    {"card_number": 5, "title": "Kazasker (Kadıasker) Görevi", "body": "Divanda adalet ve eğitim işlerinden sorumludur. Kadı ve Müderris tayinlerini yapar (Türk ve Müslüman olma şartı vardır)."},
    {"card_number": 6, "title": "Nişancı ve Reisülküttab", "body": "Nişancı padişahın tuğrasını çeker, tımar kayıtlarını (Tahrir defteri) tutar. Reisülküttab ise dış işlerden sorumlu bakandır."},
    {"card_number": 7, "title": "Devşirme Sistemi ve Enderun", "body": "Hristiyan çocukların eğitilerek asker (Kapıkulu) veya devlet adamı (Enderun mektebi) yapıldığı sistemdir."},
    {"card_number": 8, "title": "Tımar (Dirlik) Sistemi", "body": "Toprak gelirine göre asker (Cebelü) yetiştirme sistemidir. Devlet cebinden para çıkmadan hazineden yük almadan ordu besler."},
    {"card_number": 9, "title": "Lonca Teşkilatı (Ahilik)", "body": "Esnaf ve zanaatkarlar örgütüdür. Fiyat belirleme (Narh koyma), ürün kalitesi denetimi ve ustalık belgesi verir."},
    {"card_number": 10, "title": "Millet Sistemi Kuralı", "body": "Osmanlı'da toplum ırkına göre değil, DİN VE MEZHEP esasına göre sınıflandırılmıştır."}
  ],
  "topic-tarih-kurtulus-hazirlik": [
    {"card_number": 1, "title": "Mustafa Kemal'in Samsun'a Çıkışı", "body": "19 Mayıs 1919'da 9. Ordu Müfettişi olarak Bandırma vapurula Samsun'a çıkmış ve Milli Mücadele'yi fiilen başlatmıştır."},
    {"card_number": 2, "title": "Amasya Genelgesi (22 Haziran 1919)", "body": "Milli Mücadele'nin gerekçesi, amacı ve yöntemi ilk kez açıklanmıştır: 'Milletin bağımsızlığını yine milletin azim ve kararı kurtaracaktır.'"},
    {"card_number": 3, "title": "Mustafa Kemal'in Askerlikten İstifası", "body": "Amasya Genelgesi sonrası, Erzurum Kongresi öncesinde (7-8 Temmuz 1919) tüm askeri ve resmi görevlerinden istifa etmiştir ('Sine-i millete döndüm')."},
    {"card_number": 4, "title": "Erzurum Kongresi (23 Temmuz 1919)", "body": "Toplanış bakımından bölgesel, kararları bakımından MİLLİ bir kongredir. İlk kez Mebusan Meclisi'nin açılması ve Manda kabul edilemez kararı alınmıştır."},
    {"card_number": 5, "title": "Sivas Kongresi (4-11 Eylül 1919)", "body": "Hem toplanış hem kararları bakımından MİLLİDİR. Tüm cemiyetler 'Anadolu ve Rumeli Müdafaa-i Hukuk Cemiyeti' adı altında birleştirilmiştir."},
    {"card_number": 6, "title": "Temsil Heyeti'nin İlk Yürütme Yetkisi", "body": "Sivas Kongresi'nde Ali Fuat Paşa'nın Batı Cephesi Komutanlığı'na atanması Temsil Heyeti'nin ilk yürütme yetkisi kullanımıdır."},
    {"card_number": 7, "title": "Amasya Görüşmeleri (Ekim 1919)", "body": "İstanbul Hükümeti (Salih Paşa) ile Temsil Heyeti (Mustafa Kemal) arasında yapılmış; İstanbul Hükümeti Temsil Heyeti'ni İLK KEZ HUKUKEN TANIMIŞTIR."},
    {"card_number": 8, "title": "Misak-ı Milli Kararları (28 Ocak 1920)", "body": "Son Osmanlı Mebusan Meclisi'nde kabul edilmiştir. Kapitülasyonlar, sınırlar, azınlıklar, borçlar ve boğazlar ilkesi belirlenmiştir."},
    {"card_number": 9, "title": "İstanbul'un Resmen İşgali (16 Mart 1920)", "body": "Misak-ı Milli'nin kabulü üzerine İtilaf Devletleri İstanbul'u resmen işgal etmiş ve Mebusan Meclisi'ni basarak dağıtmıştır."},
    {"card_number": 10, "title": "İrade-i Milliye ve Hakimiyet-i Milliye", "body": "Milli Mücadele'nin ilk yayın organı Sivas'ta çıkarılan İrade-i Milliye gazetesidir; Ankara'ya gelince Hakimiyet-i Milliye olmuştur."}
  ],
  "topic-tarih-tbmm-ve-cepheler": [
    {"card_number": 1, "title": "I. TBMM'nin Açılışı (23 Nisan 1920)", "body": "Ankara'da kurucu, ihtilalci ve demokratik bir meclis olarak açılmıştır. En yaşlı üye Sinop Mebusu Şerif Bey açılış konuşmasını yapmıştır."},
    {"card_number": 2, "title": "Hıyanet-i Vataniye Kanunu ve İstiklal Mahkemeleri", "body": "TBMM kendine karşı çıkan ayaklanmaları bastırmak ve otorite sağlamak için yasama ve yargı yetkilerini kullanmıştır."},
    {"card_number": 3, "title": "Doğu Cephesi ve Gümrü Antlaşması", "body": "Kazım Karabekir komutasındaki Ermenilere karşı savaşılmıştır. Gümrü Antlaşması TBMM'nin İLK SİYASİ VE ASKERİ ZAFERİDİR."},
    {"card_number": 4, "title": "Güney Cephesi ve Kuvayı Milliye", "body": "Fransız ve Ermenilere karşı sadece Kuvayı Milliye (halk direnişi) savaşmıştır. Maraş (Sütçü İmam), Antep (Şahin Bey), Urfa destan yazmıştır."},
    {"card_number": 5, "title": "I. İnönü Savaşı Sonuçları (TALİMH)", "body": "Düzenli ordunun ilk zaferidir. Sonuçları: Teşkilat-ı Esasiye (Anayasa), Afganistan Dostluk Ant., Londra Konferansı, İstiklal Marşı kabulü, Hakkari devri."},
    {"card_number": 6, "title": "Londra Konferansı İpucu", "body": "İtilaf Devletleri TBMM'yi İLK KEZ HUKUKEN TANIMIŞTIR. Bekir Sami Bey katılmış, Tevfik Paşa 'Söz milletin asıl vekili TBMM'nindir' demiştir."},
    {"card_number": 7, "title": "Kütahya-Eskişehir Yenilgisi", "body": "Düzenli ordunun tek yenilgisidir. Ordu Sakarya'nın doğusuna çekilmiş, Mustafa Kemal'e 3 aylığına BAŞKOMUTANLIK yetkisi verilmiştir."},
    {"card_number": 8, "title": "Tekalif-i Milliye Emirleri (7-8 Ağustos 1921)", "body": "Mustafa Kemal'in Başkomutanlık yetkisiyle ordunun malzeme ihtiyacını karşılamak için çıkardığı milli yükümlülük emirleridir."},
    {"card_number": 9, "title": "Sakarya Meydan Muharebesi (Melhame-i Kübra)", "body": "Mustafa Kemal: 'Hattı müdafaa yoktur, sathı müdafaa vardır. O satıh bütün vatandır.' Sözünü söylemiş, gazilik ve mareşallik almıştır."},
    {"card_number": 10, "title": "Kars ve Ankara Antlaşmaları (1921)", "body": "Sakarya sonrası Kars Antlaşması ile Doğu sınırımız KESİNleşmiş; Ankara Antlaşması ile Fransa TBMM'yi tanıyan İLK İTİLAF DEVLETİ olmuştur."}
  ],
  "topic-tarih-antlasmalar-lozan": [
    {"card_number": 1, "title": "Büyük Taarruz (Başkomutanlık Meydan Muh.)", "body": "26 Ağustos 1922'de başlamış, Dumlupınar'da Yunan ordusu imha edilmiştir. Mustafa Kemal: 'Ordular ilk hedefiniz Akdeniz'dir, ileri!' demiştir."},
    {"card_number": 2, "title": "Mudanya Ateşkes Antlaşması (11 Ekim 1922)", "body": "İsmet İnönü temsil etmiştir. Savaş yapılmadan Doğu Trakya, İstanbul ve Boğazlar kurtarılmıştır. Osmanlı fiilen ve hukuken sona ermiştir."},
    {"card_number": 3, "title": "Saltanatın Kaldırılması (1 Kasım 1922)", "body": "Lozan'a iki hükümetin birden çağrılmasını önlemek ve milli egemenliği pekiştirmek için kaldırılmıştır. Osmanlı hukuken resmen bitti."},
    {"card_number": 4, "title": "Lozan Barış Konferansı Temsilcileri", "body": "TBMM'yi Dışişleri Bakanı İsmet İnönü (Başkan), Rıza Nur ve Hasan Saka temsil etmiştir."},
    {"card_number": 5, "title": "Lozan'da Taviz Verilmeyen İki Konu", "body": "Mustafa Kemal İsmet Paşa'dan KAPİTÜLASYONLAR ve ERMENİ YURDU konularında kesinlikle taviz verilmemesini istemiştir."},
    {"card_number": 6, "title": "Lozan'da Çözülen Kapitülasyonlar", "body": "Kapitülasyonlar ve Düyun-ı Umumiye (Genel Borçlar İdaresi) tamamen kaldırılmış, ekonomik bağımsızlık sağlanmıştır."},
    {"card_number": 7, "title": "Lozan'da Çözülemeyen Tek Konu (Musul)", "body": "Irak Sınırı (Musul sorunu) Türkiye ile İngiltere arasında ikili görüşmelere bırakılmış, Lozan'da çözülemeyen TEK konu olmuştur."},
    {"card_number": 8, "title": "Lozan'da Aleyhimize Çözülen Konular", "body": "Hatay (Suriye sınırı) ve Boğazlar Komisyonu (Boğazlar yönetimi) Lozan'da aleyhimize çözülmüş, daha sonra lehimize çevrilmiştir."},
    {"card_number": 9, "title": "Patrikhane ve Azınlıklar Kararı", "body": "Tüm azınlıklar Türk vatandaşı kabul edilerek Avrupalıların iç işlerimize karışması önlenmiştir. Patrikhane siyasi yetkilerinden arındırılmıştır."},
    {"card_number": 10, "title": "Lozan Antlaşması'nın Önemi", "body": "24 Temmuz 1923'te imzalanmış, Türkiye Cumhuriyeti'nin kurucu tapu senedi olmuş ve I. Dünya Savaşı antlaşmaları içinde hala geçerli tek antlaşmadır."}
  ],
  "topic-tarih-inkilaplar": [
    {"card_number": 1, "title": "Cumhuriyetin İlanı (29 Ekim 1923)", "body": "Devletin rejimi belirlenmiş, Meclis Hükümeti sisteminden Kabine Sistemine geçilmiş, M. Kemal ilk Cumhurbaşkanı, İsmet Paşa ilk Başbakan olmuştur."},
    {"card_number": 2, "title": "Halifeliğin Kaldırılması (3 Mart 1924)", "body": "Laikliğin en önemli adımıdır. Aynı gün Tevhid-i Tedrisat Kanunu çıkarılmış ve Şer'iye ve Evkaf Vekaleti kaldırılmıştır."},
    {"card_number": 3, "title": "Şer'iye ve Evkaf Vekaleti Yerine Kurulanlar", "body": "Din işleri için Diyanet İşleri Başkanlığı, vakıf işleri için Vakıflar Genel Müdürlüğü kurulmuştur."},
    {"card_number": 4, "title": "Erkan-ı Harbiye Umumiye Vekaleti", "body": "Kaldırılarak Genelkurmay Başkanlığı kurulmuş, böylece ordu siyasetten tamamen ayrılmıştır."},
    {"card_number": 5, "title": "Tevhid-i Tedrisat Kanunu (1924)", "body": "Tüm öğretim kurumları Milli Eğitim Bakanlığı'na bağlanmış, eğitimde birlik ve laikleşme sağlanmıştır."},
    {"card_number": 6, "title": "Türk Medeni Kanunu (17 Şubat 1926)", "body": "İsviçre'den uyarlanmıştır. Kadın-erkek hukuki ve sosyal eşitliği sağlanmış, tek eşlilik ve resmi nikah zorunlu olmuştur (Siyasi hak İÇERMEZ!)."},
    {"card_number": 7, "title": "Kadınlara Siyasi Hakların Verilmesi (BMI)", "body": "1930 Belediye seçimleri, 1933 Muhtarlık seçimleri, 1934 Milletvekili seçilme hakkı (Şifre: BMW / BMI)."},
    {"card_number": 8, "title": "Harf İnkılabı (1 Kasım 1928)", "body": "Latin alfabesi kabul edilmiş, okuma-yazma oranını artırmak için Millet Mektepleri açılmıştır."},
    {"card_number": 9, "title": "Kabotaj Kanunu (1 Temmuz 1926)", "body": "Türk karasularında gemi işletme ve liman hakkı Türk denizcilerine verilmiş, milliyetçilik ilkesi doğrultusunda deniz bağımsızlığı sağlanmıştır."},
    {"card_number": 10, "title": "Soyadı Kanunu (1934)", "body": "Ayrıcalık belirten unvanlar (Ağa, Paşa, Hoca) kaldırılmış, Mustafa Kemal'e TBMM tarafından 'Atatürk' soyadı verilmiştir."}
  ],
  "topic-tarih-ataturk-ilkeleri-dis-politika": [
    {"card_number": 1, "title": "Cumhuriyetçilik İlkesi", "body": "Milli egemenlik, seçim, meclis, çok partili hayat ve oy kullanma hakkı bu ilkeyle doğrudan ilgilidir."},
    {"card_number": 2, "title": "Milliyetçilik İlkesi", "body": "Milli bağımsızlık, Türk dili, Türk tarihi, Kabotaj Kanunu, İstiklal Marşı ve ortak aidiyet vurgusudur."},
    {"card_number": 3, "title": "Halkçılık İlkesi", "body": "Eşitlik, adalet, sosyal devlet, hiçbir sınıfa ayrıcalık tanınmaması ve Soyadı Kanunu bu ilkeyle ilgilidir."},
    {"card_number": 4, "title": "Devletçilik İlkesi", "body": "Özel sektörün yetersiz kaldığı durumlarda ekonominin, sanayinin ve fabrikaların devlet eliyle yapılmasıdır (Sümerbank, Etibank)."},
    {"card_number": 5, "title": "Laiklik İlkesi", "body": "Din ve devlet işlerinin ayrılması, akılcılık, bilimsellik, Halifeliğin kaldırılması ve Medeni Kanun."},
    {"card_number": 6, "title": "İnkılapçılık İlkesi", "body": "Sürekli yenileşme, çağdaşlaşma, dinamizm, takvim, saat, ölçü ve Latin harflerinin kabulüdür."},
    {"card_number": 7, "title": "Nüfus Mübadelesi (Etabli)", "body": "Yunanistan ile yaşanan İstanbul yerleşikleri dışındaki Türk ve Rum nüfusun karşılıklı değiştirilmesi olayıdır."},
    {"card_number": 8, "title": "Milletler Cemiyeti'ne Üyelik (1932)", "body": "Türkiye'nin barışçıl dış politikası sonucu İspanya ve Yunanistan'ın teklifiyle Milletler Cemiyeti'ne üye olunmuştur."},
    {"card_number": 9, "title": "Balkan Antantı (1934) ve Sadabat Paktı (1937)", "body": "Balkan Antantı (Türkiye, Yunanistan, Yugoslavya, Romanya) Batı sınırını; Sadabat Paktı (Türkiye, İran, Irak, Afganistan) Doğu sınırını korumuştur."},
    {"card_number": 10, "title": "Montrö Boğazlar Sözleşmesi (1936)", "body": "Boğazlar Komisyonu kaldırılmış, Boğazların tüm egemenliği ve silahlandırılması Türkiye'ye geçmiştir."}
  ],
  "topic-tarih-cagdas-turk-dunya": [
    {"card_number": 1, "title": "Kara Perşembe (1929 Dünya Ekonomik Bunalımı)", "body": "ABD New York borsasının çökmesiyle başlayan ve dünyayı sarsan krizdir. Türkiye'de Devletçilik ilkesi hız kazanmıştır."},
    {"card_number": 2, "title": "II. Dünya Savaşı Müttefik ve Miğfer Blokları", "body": "Müttefikler: İngiltere, Fransa, ABD, SSCB. Miğfer Devletler: Almanya, İtalya, Japonya."},
    {"card_number": 3, "title": "Türkiye'nin II. Dünya Savaşı Tutumu", "body": "Türkiye savaş boyunca tarafsız kalmış, ancak San Francisco Konferansı'na katılmak ve BM kurucu üyesi olmak için Şubat 1945'te Almanya'ya savaş ilan etmiştir."},
    {"card_number": 4, "title": "Birleşmiş Milletler (BM) Kuruluşu (1945)", "body": "Dünya barışını korumak için kurulmuştur. Güvenlik Konseyi'nin 5 daimi üyesi (Fırça/FİRÇA: Fransa, İngiltere, Rusya, Çin, ABD) veto hakkına sahiptir."},
    {"card_number": 5, "title": "Soğuk Savaş Dönemi ve Truman Doktrini", "body": "ABD ile SSCB arasındaki gerilim dönemidir. Truman Doktrini ve Marshall Planı ile Türkiye ve Yunanistan'a ABD yardımı yapılmıştır."},
    {"card_number": 6, "title": "NATO ve Türkiye'nin Üyeliği (1952)", "body": "Kuzey Atlantik Savunma İttifakı'dır. Türkiye Kore Savaşı'na asker göndererek 1952 yılında NATO'ya resmi üye olmuştur."},
    {"card_number": 7, "title": "Varşova Paktı", "body": "NATO'ya karşı SSCB liderliğinde Doğu Bloku ülkeleri tarafından kurulan askeri ittifaktır."},
    {"card_number": 8, "title": "Kıbrıs Barış Harekatı (1974)", "body": "EOKA örgütü ve Enosis'e (Kıbrıs'ı Yunanistan'a bağlama) karşı Bülent Ecevit hükümeti döneminde gerçekleştirilen harekat (Ayşe tatile çıksın parolası)."},
    {"card_number": 9, "title": "SSCB'nin Dağılması (1991) ve Bağımsızlık", "body": "SSCB'nin dağılmasıyla Azerbaycan, Kazakistan, Özbekistan, Türkmenistan ve Kırgızistan bağımsızlıklarını kazanmıştır."},
    {"card_number": 10, "title": "Türk Devletleri Teşkilatı (TDT)", "body": "Türk dili konuşan ülkelerin kurduğu uluslararası örgüttür (Türkiye, Azerbaycan, Kazakistan, Kırgızistan, Özbekistan üyedir)."}
  ]
}

def export_all_tarih_flashcards():
    base_dir = os.path.join("assets", "data", "topics", "tarih")
    os.makedirs(base_dir, exist_ok=True)
    
    total_cards = 0
    for topic_id, cards in tarih_flashcard_database.items():
        data = {
            "topic_id": topic_id,
            "flashcard_count": len(cards),
            "flashcards": cards
        }
        
        file_name = f"flashcards_{topic_id}.json"
        file_path = os.path.join(base_dir, file_name)
        
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
            
        total_cards += len(cards)
        print(f"  [OK] {topic_id} -> {len(cards)} Flashcard yazıldı: {file_path}")

    print(f"\n[BAŞARILI] TARİH DERSİNİN TÜM 12 ALT KONUSUNA AİT TOPLAM {total_cards} FLASHCARD ENTEGRE EDİLDİ!")

if __name__ == "__main__":
    export_all_tarih_flashcards()
