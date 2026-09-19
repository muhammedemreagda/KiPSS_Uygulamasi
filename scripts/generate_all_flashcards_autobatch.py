import json
import os

# Complete Flashcard database builder for Türkçe (All 15 Topics x 10 Flashcards = 150 Flashcards)
flashcard_database = {
  "topic-turkce-sozcukte-anlam": [
    {"card_number": 1, "title": "Gerçek (Temel) Anlam", "body": "Bir sözcüğün zihinde uyandırdığı ilk ve asıl anlamdır. Örnek: 'Soğuk sudan boğazı ağrıdı' cümlesindeki soğuk kelimesi ısı düşüklüğünü ifade eder ve gerçek anlamındadır."},
    {"card_number": 2, "title": "Mecaz Anlam", "body": "Sözcüğün gerçek anlamından tamamen uzaklaşarak kazandığı soyut yeni anlamdır. Örnek: 'Bize karşı çok soğuk davrandı' cümlesinde soğuk kelimesi samimiyetsiz anlamında mecazdır."},
    {"card_number": 3, "title": "Yan Anlam", "body": "Gerçek anlamla şekil veya işlev benzerliği kurularak kazanılan yaklaştırılmış anlamdır. Örnek: 'Masanın ayağı kırıldı' örneğinde insandaki ayak organından benzetme yapılmıştır."},
    {"card_number": 4, "title": "Terim Anlam Altın Kuralı", "body": "Bir bilim, sanat, spor veya meslek dalına özgü özel kavramları karşılayan sözcüklerdir. Örnek: 'Hücre' biyolojide terim anlamlıyken, 'hapis hücresi' derken gerçek anlamdadır."},
    {"card_number": 5, "title": "Somutlaştırma (Somutlama)", "body": "Soyut bir kavramın daha anlaşılır kılınmak için somut bir nesneymiş gibi anlatılmasıdır. Örnek: 'Aşk bir alevdir' derken soyut aşk kavramı somut bir nesneye benzetilmiştir."},
    {"card_number": 6, "title": "Soyutlaştırma (Soyutlama)", "body": "Somut anlamlı bir sözcüğün mecazlaşarak soyut bir anlam kazanmasıdır. Örnek: 'Bu işte senin de parmağın var' cümlesindeki parmak somut değil, rol/katkı anlamında soyuttur."},
    {"card_number": 7, "title": "Ad Aktarması (Mecazımürsel)", "body": "Benzetme amacı gütmeden bir sözcüğün başka bir sözcük yerine kullanılmasıdır. Örnek: 'Tüm ev maçı izliyordu' derken kastedilen ev değil, evin içindeki insanlardır."},
    {"card_number": 8, "title": "Duyular Arası Aktarma", "body": "Bir duyuya ait algının başka bir duyuya aktarılarak anlatılmasıdır. Örnek: 'Tatlı bir gülüş' ifadesinde tat duyusu (tatlı), görme duyusuna (gülüş) aktarılmıştır."},
    {"card_number": 9, "title": "Dolaylama Şifresi", "body": "Tek kelimeyle anlatılabilecek bir kavramı birden fazla kelimeyle süsleyerek anlatmaktır. Örnek: Kömür yerine 'kara elmas', balık yerine 'derya kuzusu' denmesi dolaylamadır."},
    {"card_number": 10, "title": "Güzel Adlandırma", "body": "Korkutucu veya rahatsız edici kavramların daha nazik sözcüklerle ifade edilmesidir. Örnek: Verem hastalığı yerine 'ince hastalık', ölüm yerine 'son yolculuk' denmesi."}
  ],
  "topic-turkce-cumlede-anlam": [
    {"card_number": 1, "title": "Öznel (Subjektif) Cümle", "body": "Kişisel duygu, beğeni veya yorum içeren, kanıtlanamayan yargılardır. Örnek: 'Bu roman Türk edebiyatının en sürükleyici eseridir' ifadesi kişisel değerlendirmedir."},
    {"card_number": 2, "title": "Nesnel (Objektif) Cümle", "body": "Kişiden kişiye değişmeyen, ölçülebilen veya doğruluğu kanıtlanabilen yargılardır. Örnek: 'Roman toplam 320 sayfadan oluşmaktadır' cümlesi nesnel bir bilgidir."},
    {"card_number": 3, "title": "Neden-Sonuç Cümlesi Testi", "body": "Eylemin gerçekleşme gerekçesini belirtir; '-dığı için' kelimesiyle test edilir ve her iki eylem de gerçekleşmiştir. Örnek: 'Yağmur yağdığı için maç iptal edildi.'"},
    {"card_number": 4, "title": "Amaç-Sonuç Cümlesi Ayrımı", "body": "Henüz gerçekleşmemiş bir hedefe ulaşmak amacıyla yapılan eylemleri anlatır; '-mek amacıyla' ifadesi koyulabilir. Örnek: 'Sınavı kazanmak amacıyla gece gündüz çalıştı.'"},
    {"card_number": 5, "title": "Koşul-Sonuç (Şart) Cümlesi", "body": "Bir olayın gerçekleşmesinin başka bir olaya bağlandığı yargılardır. Örnek: 'Düzenli tekrar yaparsan konuları daha hızlı kavrarsın' cümlesinde -se/-sa koşul ekidir."},
    {"card_number": 6, "title": "Doğrudan Anlatım Şifresi", "body": "Başkasının sözünün hiçbir değişikliğe uğratılmadan, tırnak içinde veya 'dedi' ifadesiyle iletilmesidir. Örnek: Öğretmen, 'Yarın sözlü var' dedi."},
    {"card_number": 7, "title": "Dolaylı Anlatım Şifresi", "body": "Başkasının söylediği sözün kendi cümlelerimizle değiştirilerek aktarılmasıdır; genellikle '-diğini söyledi' kalıbı kullanılır. Örnek: Öğretmen yarın sözlü yapacağını söyledi."},
    {"card_number": 8, "title": "Üslup (Biçem) Cümlesi", "body": "Yazarın duygu ve düşüncelerini nasıl anlattığını, dil ve anlatım özelliklerini belirtir. Örnek: 'Yazar eserinde süslü ve devrik cümlelere sıkça yer vermiştir.'"},
    {"card_number": 9, "title": "İçerik (Konu) Cümlesi", "body": "Eserde ne anlatıldığını, konunun ne olduğunu belirten cümlelerdir. Örnek: 'Şair bu şiirinde çocukluğuna duyduğu özlemi dile getirmiştir.'"},
    {"card_number": 10, "title": "Sitem ve Kanıksama Farkı", "body": "Sitem, sevilen birine kırgınlığı hafifçe belirtmektir ('Düğününe beni çağırmadın'). Kanıksama ise çok tekrarlanan bir duruma alışmaktır ('Benzin zamlarına alıştık')."}
  ],
  "topic-turkce-paragraf-ana-fikir": [
    {"card_number": 1, "title": "Ana Fikir (Ana Düşünce)", "body": "Yazarın okuyucuya vermek istediği temel mesaj, öğüt veya asıl düşüncedir. Paragrafın genelini kapsar ve genellikle sonuç cümlelerinde yoğunlaşır."},
    {"card_number": 2, "title": "Konu ile Ana Fikir Farkı", "body": "Konu 'Paragrafta ne anlatılıyor?' sorusuna yanıt verirken; Ana fikir 'Yazar bu konuda okura ne mesaj veriyor?' sorusunun yanıtıdır."},
    {"card_number": 3, "title": "Yardımcı Fikirler", "body": "Ana fikri destekleyen, açıklayan ve zenginleştiren yan düşüncelerdir. Yanıtı parça içinde birebir bulunan soru tipleridir."},
    {"card_number": 4, "title": "Paragrafta Başlık Bulma", "body": "Başlık, paragrafın konusunu en özlü şekilde özetleyen, anahtar kelimeleri içeren 1-3 kelimelik ifadedir."},
    {"card_number": 5, "title": "Anahtar Kelime Tekniği", "body": "Paragrafta en çok tekrarlanan ve metnin özünü oluşturan kavramlar anahtar kelimelerdir; ana fikre ulaşmada en büyük ipucudur."},
    {"card_number": 6, "title": "Oysa / Oysaki Geçiş İfadeleri", "body": "'Oysa', 'ancak', 'fakat', 'ne var ki' gibi bağlaçlardan sonra gelen cümleler genellikle yazarın asıl ana düşüncesini barındırır."},
    {"card_number": 7, "title": "Vurgulanan Düşünce", "body": "Yazarın özellikle altını çizdiği, okuyucunun zihnine kazımak istediği en önemli mesajdır."},
    {"card_number": 8, "title": "Paragrafta Soru-Cevap Uyumsuzluğu", "body": "Soru metne uygun görünse de paragrafın ilk cümlesi sorunun doğrudan yanıtı olmalıdır; ilk cümleye odaklanın."},
    {"card_number": 9, "title": "Çıkarım Yapma Cümleleri", "body": "Metinde doğrudan yazmayan fakat paragraftaki ipuçlarından hareketle ulaşılan mantıksal sonuçlardır."},
    {"card_number": 10, "title": "Paragrafta Olumsuz Soru Kökleri", "body": "'Değinilmemiştir', 'ulaşılamaz', 'çıkarılamaz' sorularında önce seçenekler okunup anahtar kelimeler çizilmeli, sonra paragraf taranmalıdır."}
  ],
  "topic-turkce-paragraf-yapi": [
    {"card_number": 1, "title": "Giriş Cümlesi Özellikleri", "body": "Giriş cümlesi bağımsızdır; 'bu yüzden', 'oysa', 'çünkü', 'ama' gibi bağlayıcı unsurlarla veya kendinden önce bir cümle varmış hissiyle başlamaz."},
    {"card_number": 2, "title": "Gelişme Bölümü Özellikleri", "body": "Düşüncenin örnekler, karşılaştırmalar ve tanık göstermelerle geliştirildiği, ayrıntılara girildiği bölümdür."},
    {"card_number": 3, "title": "Sonuç Cümlesi İpuçları", "body": "'Özetle', 'kısacası', 'sonuç olarak', 'demek ki' gibi toparlayıcı ifadelerle başlayan ve ana fikri özetleyen son cümledir."},
    {"card_number": 4, "title": "Akışı Bozan Cümleyi Bulma", "body": "Paragrafta anlatılan genel konunun dışına çıkan veya konunun farklı bir yönüne değinen cümle akışı bozar."},
    {"card_number": 5, "title": "Paragrafı İki Parçaya Bölme", "body": "Yazarın yeni bir konuya veya aynı konunun farklı bir bakış açısına geçtiği cümle ikinci paragrafın ilk cümlesidir."},
    {"card_number": 6, "title": "Cümle Yerleştirme Tekniği", "body": "Verilen cümlenin öncesindeki ve sonrasındaki cümlelerle zamir (bu, şu), bağlaç ve anlam mantığı yönünden tam uyumlu olması gerekir."},
    {"card_number": 7, "title": "Paragraf Tamamlama (Boşluk Bırakma)", "body": "Boşluktan önceki ve sonraki cümleler arasındaki mantık bağını kuran en uygun seçenek doğru cevaptır."},
    {"card_number": 8, "title": "Cümlelerin Yerini Değiştirme", "body": "Olay ya da düşünce akışındaki kronolojik/mantıksal kopukluğu düzeltecek ikili cümle değişimini bulma yöntemidir."},
    {"card_number": 9, "title": "Bağlantı Unsuru Takibi", "body": "'Bu durum', 'söz konusu olay', 'nitelikli eser' gibi gönderme yapan sözcükler cümle sıralamasında rehberdir."},
    {"card_number": 10, "title": "Paragrafta Kronolojik Akış", "body": "Olay anlatımlarında zaman sıralamasına (önce, sonra, daha sonra, en sonunda) dikkat edilmelidir."}
  ],
  "topic-turkce-anlatim-bicimleri": [
    {"card_number": 1, "title": "Öyküleyici Anlatım (Öyküleme)", "body": "Olay, kişi, yer ve zaman ögelerine dayanır. Olaylar bir film şeridi gibi akıp gider; hareket ve eylem ön plandadır."},
    {"card_number": 2, "title": "Betimleyici Anlatım (Betimleme)", "body": "Kelimelerle resim çizme sanatıdır. Duyu organlarına hitap eden sıfatlar ve görsellik ön plandadır, eylem durağandır."},
    {"card_number": 3, "title": "Açıklayıcı Anlatım (Açıklama)", "body": "Okuyucuya bilgi vermek, öğretmek amacıyla yazılır. Sade, nesnel ve yalın bir dil kullanılır; makale ve ders kitaplarında yaygındır."},
    {"card_number": 4, "title": "Tartışmacı Anlatım (Tartışma)", "body": "Yerleşik bir düşünceyi değiştirmek veya kendi görüşünü kabul ettirmek için yazılır. 'Sizce de öyle değil mi?', 'Bence...' gibi ifadeler içerir."},
    {"card_number": 5, "title": "Tanımlama İpucu", "body": "'Bu nedir?' sorusuna yanıt veren, -dır/-dir veya 'denir' ile biten cümlelerdir. Örnek: 'Şiir, duyguların ritmik ifadesidir.'"},
    {"card_number": 6, "title": "Örnekleme İpucu", "body": "Soyut bir düşünceyi somutlaştırmak için konuyla ilgili bilinen nesne, kişi veya eser isimlerinin sıralanmasıdır."},
    {"card_number": 7, "title": "Tanık Gösterme (Alıntı Yapma)", "body": "Düşünceyi inandırıcı kılmak için alanında uzman bir kişinin ismiyle birlikte sözünün birebir aktarılmasıdır."},
    {"card_number": 8, "title": "Karşılaştırma İpucu", "body": "İki kavram, olay veya durum arasındaki benzerlik ya da farklılıkların 'en', 'daha', 'ise', 'göre' sözcükleriyle ortaya konmasıdır."},
    {"card_number": 9, "title": "Sayısal Verilerden Yararlanma", "body": "Düşünceyi kanıtlamak için anket, istatistik, grafik veya araştırma sonuçlarına ait rakamsal verilerin kullanılmasıdır."},
    {"card_number": 10, "title": "Benzetme İpucu", "body": "Aralarında ilgi bulunan iki şeyden zayıf olanın güçlü olana 'gibi', 'sanki', 'adeta' kelimeleriyle benzetilmesidir."}
  ],
  "topic-turkce-ses-bilgisi": [
    {"card_number": 1, "title": "Ünlü (Sesli) Düşmesi", "body": "İki heceli bazı kelimeler ünlü ile başlayan ek aldığında ikinci hecedeki dar ünlü düşer. Örnek: akıl + ı → aklı, burun + um → burnum."},
    {"card_number": 2, "title": "Ünsüz Yumuşaması (Değişimi)", "body": "p, ç, t, k ile biten kelimeler ünlüyle başlayan ek aldığında b, c, d, ğ'ye dönüşür. Örnek: kitap + ı → kitabı, ağaç + a → ağaca."},
    {"card_number": 3, "title": "Ünsüz Sertleşmesi (Benzeşmesi)", "body": "Fıstıkçı Şahap (f, s, t, k, ç, ş, h, p) ile biten kelimelere c, d, g ile başlayan ek gelirse ek ç, t, k'ye dönüşür. Örnek: kitap + cı → kitapçı."},
    {"card_number": 4, "title": "Ünlü Daralması İpucu", "body": "a, e geniş ünlüleriyle biten fiillere '-yor' eki geldiğinde a, e sesleri ı, i, u, ü'ye daralır. Örnek: başla - yor → başlıyor."},
    {"card_number": 5, "title": "Ünsüz Türemesi (İkizleşme)", "body": "Arapça kökenli bazı kelimeler etmek/olmak yardımcı fiili veya ünlüyle başlayan ek aldığında ikizleşir. Örnek: his + etmek → hissetmek, hak + ı → hakkı."},
    {"card_number": 6, "title": "Ünlü Türemesi", "body": "Cık/cik küçültme eki alan bazı kelimelerde türeme olur. Örnek: az + cık → azıcık, dar + cık → daracık, bir + cik → biricik."},
    {"card_number": 7, "title": "Ünsüz Düşmesi İpucu", "body": "k ünsüzüyle biten bazı kelimeler -cık/-cik küçültme eki aldığında k ünsüzü düşer. Örnek: küçük + cük → küçücük, minik + cik → minicik."},
    {"card_number": 8, "title": "Dudak Ünsüzlerinin Benzeşmesi (n-m değişimi)", "body": "b sesinden önce gelen n sesi m'ye dönüşür. Örnek: saklan-baç → saklambaç, dolan-baç → dolambaç (Özel isimlerde uygulanmaz: İstanbul)."},
    {"card_number": 9, "title": "Ulama İpucu", "body": "Ünsüzle biten bir kelimeden sonra ünlüyle başlayan bir kelime geldiğinde iki kelimenin birleşikmiş gibi okunmasıdır (Noktalama işareti varsa ulama olmaz)."},
    {"card_number": 10, "title": "Büyük Ünlü Uyumu Kuralı", "body": "Bir kelimenin ilk hecesindeki ünlü kalınsa (a, ı, o, u) diğer heceler de kalın; inceyse (e, i, ö, ü) diğerleri de ince olmalıdır."}
  ],
  "topic-turkce-sozcuk-yapisi": [
    {"card_number": 1, "title": "Kök Kavramı ve Türleri", "body": "Sözcüğün anlamlı en küçük yapı birimidir. İsim kökü (mak/mek almayan: ev, su) ve Fiil kökü (mak/mek alan: gel-, yaz-) olarak ikiye ayrılır."},
    {"card_number": 2, "title": "Ortak (Kökdeş) Kök", "body": "Aralarında anlam bağı bulunan, hem isim hem fiil olarak kullanılabilen köklerdir. Örnek: boya (isim) / boyamak (fiil)."},
    {"card_number": 3, "title": "Sesteş (Eş Sesli) Kök", "body": "Yazılışları aynı fakat anlamları tamamen farklı olan köklerdir. Örnek: yaz (mevsim) / yazmak (fiil)."},
    {"card_number": 4, "title": "Yapım Eki İşlevi", "body": "Eklendiği sözcüğün anlamını veya türünü değiştiren eklerdir; yeni bir kelime (türemiş sözcük) türetir. Örnek: göz-lük, sev-gi."},
    {"card_number": 5, "title": "Çekim Eki İşlevi", "body": "Sözcüğün anlamını değiştirmeyen, cümledeki görevini ve diğer sözcüklerle ilişkisini düzenleyen eklerdir. Örnek: ev-de, kitap-lar."},
    {"card_number": 6, "title": "Basit Sözcük Yapısı", "body": "Yapım eki almamış sözcüklerdir. Çekim eki alabilirler ancak yeni bir anlam kazanmazlar. Örnek: Evlerden, masada."},
    {"card_number": 7, "title": "Türemiş Sözcük Yapısı", "body": "En az bir tane yapım eki almış sözcüklerdir. Örnek: Bil-gi-li, göz-lük-çü."},
    {"card_number": 8, "title": "Birleşik Sözcük Yapısı", "body": "En az iki sözcüğün birleşip kalıplaşmasıyla oluşan yeni sözcüklerdir. Örnek: Çanakkale, gecekondu, aslanağzı."},
    {"card_number": 9, "title": "İyelik (Aitlik) Ekleri", "body": "İsmin neye veya kime ait olduğunu belirten eklerdir. Örnek: ev-im (benim), ev-in (senin), ev-i (onun)."},
    {"card_number": 10, "title": "Hal (Durum) Ekleri", "body": "İsmin yükleme (-i), yönelme (-e), bulunma (-de) ve ayrılma (-den) hallerini belirten eklerdir."}
  ],
  "topic-turkce-sozcuk-turleri": [
    {"card_number": 1, "title": "İsim (Ad) ve Türleri", "body": "Canlı, cansız tüm varlıkları ve kavramları karşılayan sözcüklerdir. Özel isim (Ankara), Cins isim (masa), Somut (taş), Soyut (sevgi)."},
    {"card_number": 2, "title": "Sıfat (Önad) Altın Kuralı", "body": "Sıfatlar mutlaka bir isimden önce gelir ve o ismi niteler ya da belirtir. Örnek: Kırmızı elma (Niteleme), Bu kitap (İşaret)."},
    {"card_number": 3, "title": "Zamir (Adıl) Altın Kuralı", "body": "İsmin yerini tutan sözcüklerdir; arkasından isim gelmez. Örnek: 'Bu çok güzel' (İşaret zamiri), 'O dün geldi' (Kişi zamiri)."},
    {"card_number": 4, "title": "Zarf (Belirteç) Altın Kuralı", "body": "Fiilleri, fiilimsileri, sıfatları veya kendi türünden sözcükleri durum, zaman, miktar, yön yönünden etkiler. Örnek: Hızlı koştu."},
    {"card_number": 5, "title": "Edat (İlgeç) Tanıma Testi", "body": "Tek başına anlamı olmayan, cümle içinde kelimeler arasında anlam ilgisi kuran sözcüklerdir. Örnek: gibi, kadar, için, göre."},
    {"card_number": 6, "title": "Bağlaç Tanıma Testi", "body": "Eş görevli sözcükleri veya cümleleri birbirine bağlayan sözcüklerdir; cümleden çıkarılınca anlam bozulmaz. Örnek: ve, veya, ama, çünkü."},
    {"card_number": 7, "title": "İşaret Sıfatı vs İşaret Zamiri", "body": "'Bu arabayı aldım' cümlesindeki 'bu' ismi etkilediği için sıfattır. 'Bunu aldım' cümlesindeki 'bunu' ismin yerini tuttuğu için zamirdir."},
    {"card_number": 8, "title": "Soru Sıfatı vs Soru Zamiri", "body": "'Hangi kitabı okudun?' ifadesinde 'hangi' sıfattır. 'Hangisini okudun?' ifadesinde 'hangisini' zamirdir."},
    {"card_number": 9, "title": "Zaman Zarfı İpucu", "body": "Fiile sorulan 'Ne zaman?' sorusuna yanıt verir. Örnek: 'Dün akşam bize geldi' cümlesinde 'dün akşam' zaman zarfıdır."},
    {"card_number": 10, "title": "Miktar (Azlık-Çokluk) Zarfı", "body": "Fiile veya sıfata sorulan 'Ne kadar?' sorusuna yanıt verir. Örnek: 'Çok çalıştı', 'En güzel tablo'."}
  ],
  "topic-turkce-fiiller-cati": [
    {"card_number": 1, "title": "İsim-Fiil (Mastar) Ekleri", "body": "Fiil kök veya gövdelerine gelen '-ma, -ış, -mak' (Mayışmak) ekleridir. Örnek: Kitap okumak insanı geliştirir."},
    {"card_number": 2, "title": "Sıfat-Fiil (Ortaç) Ekleri", "body": "Fiillere gelen '-an, -ası, -mez, -ar, -dik, -ecek, -miş' (Anası mezar dikecekmiş) ekleridir. Örnek: Koşan çocuk düştü."},
    {"card_number": 3, "title": "Zarf-Fiil (Ulaç/Bağ-Fiil) Ekleri", "body": "Fiillere gelen '-ken, -alı, -esi, -em, -meden, -ince, -ip, -arak' ekleridir. Örnek: Gülerek içeri girdi."},
    {"card_number": 4, "title": "Geçişli Fiil Testi (Onu Testi)", "body": "Nesne alabilen fiillerdir. Fiilin başına 'onu' kelimesi getirildiğinde anlamlı oluyorsa fiil geçişlidir. Örnek: (Onu) okudu."},
    {"card_number": 5, "title": "Geçişsiz Fiil Testi", "body": "Nesne alamayan fiillerdir. Fiilin başına 'onu' kelimesi getirildiğinde anlamsız olur. Örnek: (Onu) güldü (Anlamsız)."},
    {"card_number": 6, "title": "Etken Fiil Özelliği", "body": "İşi yapan gerçek bir öznenin (açık veya gizli) bulunduğu fiillerdir. Örnek: Ali camı kırdı (Özne: Ali)."},
    {"card_number": 7, "title": "Edilgen Fiil Özelliği", "body": "İşi yapanın belli olmadığı, '-l' veya '-n' eki alan fiillerdir; özne sözde öznedir. Örnek: Cam kırıldı."},
    {"card_number": 8, "title": "Dönüşlü Fiil Özelliği", "body": "İşi yapanın ve işten etkilenenin aynı kişi olduğu, '-l' veya '-n' eki alan fiillerdir. Örnek: Ahmet süslendi."},
    {"card_number": 9, "title": "İşteş Fiil Özelliği", "body": "Eylemin birden fazla kişi tarafından birlikte veya karşılıklı yapıldığını belirten, '-ş' eki alan fiillerdir. Örnek: Kuşlar uçuştu."},
    {"card_number": 10, "title": "Oldurgan ve Ettirgen Fiil", "body": "Geçişsiz fiilin '-r, -t, -tır' ile geçişli yapılması Oldurgan; zaten geçişli olan fiilin geçişlilik derecesinin artırılması Ettirgendir."}
  ],
  "topic-turkce-cumlenin-ogeleri": [
    {"card_number": 1, "title": "Cümlenin Temel Ögeleri", "body": "Bir cümlenin oluşması için şart olan temel ögeler Yüklem ve Özne'dir. Yüklemsiz cümle olmaz."},
    {"card_number": 2, "title": "Yüklem Bulma Altın Kuralı", "body": "Cümledeki yargıyı bildiren ögedir. Ögeler bulunurken ilk olarak yüklem tespit edilir ve tüm sorular yükleme sorulur."},
    {"card_number": 3, "title": "Özne Bulma Soruları", "body": "Yükleme sorulan 'Kim?' ve 'Ne?' sorularının yanıtıdır. Yüklemden hemen sonra bulunmalıdır."},
    {"card_number": 4, "title": "Nesne (Belirtili ve Belirtisiz)", "body": "Yükleme sorulan 'Neyi, Kimi?' soruları Belirtili Nesneyi (-i hali); 'Ne?' sorusu Belirtisiz Nesneyi verir."},
    {"card_number": 5, "title": "Dolaylı Tümleç (Yer Tamlayıcısı)", "body": "Yükleme sorulan '-e, -de, -den' eklerini içeren soruların (Nereye, Nerede, Nereden, Kime...) yanıtıdır."},
    {"card_number": 6, "title": "Zarf Tümleci Soruları", "body": "Yükleme sorulan 'Nasıl, Ne zaman, Ne kadar, Neden, Niçin?' sorularının yanıtıdır."},
    {"card_number": 7, "title": "Edat Tümleci Soruları", "body": "Yükleme sorulan 'Ne ile, Kimin ile, Ne için, Kimin için?' sorularının yanıtıdır."},
    {"card_number": 8, "title": "Tamlamaları Bölmeme Kuralı", "body": "Cümlenin ögeleri bulunurken isim tamlamaları, sıfat tamlamaları ve deyimler asla bölünmez; tek bir öge kabul edilir."},
    {"card_number": 9, "title": "Ara Söz ve Ara Cümle", "body": "İki virgül veya iki kısa çizgi arasında yer alan, bir ögenin açıklayıcısı olan veya bağımsız giren ifadelerdir."},
    {"card_number": 10, "title": "Vurgulanan Öge İpucu", "body": "Fiil cümlelerinde vurgulanan öge, yüklemden hemen önce gelen ögedir."}
  ],
  "topic-turkce-cumle-turleri": [
    {"card_number": 1, "title": "Yüklemin Türüne Göre Cümleler", "body": "Yüklemi çekimli fiil olan cümleler 'Fiil Cümlesi'; yüklemi isim veya isim soylu sözcük olan cümleler 'İsim Cümlesi'dir."},
    {"card_number": 2, "title": "Yüklemin Yerine Göre Cümleler", "body": "Yüklemi sonda olan cümleler 'Kurallı (Düz)'; yüklemi sonda olmayan cümleler 'Devrik'; yüklemi bulunmayan cümleler 'Eksiltili' cümledir."},
    {"card_number": 3, "title": "Basit Cümle Yapısı", "body": "İçinde tek bir yargı (yüklem) bulunan, fiilimsi veya başka yan yargı içermeyen cümlelerdir. Örnek: 'Dün akşam eve erken geldi.'"},
    {"card_number": 4, "title": "Birleşik Cümle Yapısı", "body": "Tek bir yüklemi olan ve içinde en az bir fiilimsi (yan cümlecik) barındıran cümlelerdir. Örnek: 'Okula yürüyerek gitti.'"},
    {"card_number": 5, "title": "Sıralı Cümle Yapısı", "body": "Aralarında anlam bağı bulunan en az iki bağımsız cümlenin virgül (,) veya noktalı virgülle (;) birbirine bağlanmasıdır."},
    {"card_number": 6, "title": "Bağlı Cümle Yapısı", "body": "Birden fazla cümlenin birbirine 've, veya, ama, fakat, çünkü' gibi bağlaçlarla bağlanmasıyla oluşan yapıdır."},
    {"card_number": 7, "title": "Bağımlı Sıralı Cümle", "body": "Sıralı cümlelerde en az bir ögenin (özne, nesne vb.) ortak kullanıldığı cümlelerdir. Örnek: 'Ahmet geldi, (Ahmet) oturdu.'"},
    {"card_number": 8, "title": "Bağımsız Sıralı Cümle", "body": "Sıralı cümlelerde hiçbir öge ortaklığının bulunmadığı, cümlelerin sadece anlamca bağlandığı yapıdır."},
    {"card_number": 9, "title": "Anlamına Göre Olumlu/Olumsuz", "body": "Eylemin yapıldığını belirten cümleler olumlu; -me/-ma, yok, değil, siz/siz ekleriyle yapılmadığını belirtenler olumsuzdur."},
    {"card_number": 10, "title": "Biçimce Olumsuz Anlamca Olumlu", "body": "'Seni sevmiyor değilim' cümlesi biçimce olumsuz (değilim var) ama anlamca olumludur (seviyorum)."}
  ],
  "topic-turkce-anlatim-bozukluklari": [
    {"card_number": 1, "title": "Gereksiz Sözcük Kullanımı", "body": "Aynı anlama gelen sözcüklerin veya eklerin bir arada kullanılmasıdır. Örnek: 'Gizli sırlarını bana anlattı' (Sır zaten gizlidir)."},
    {"card_number": 2, "title": "Sözcüğün Yanlış Anlamda Kullanımı", "body": "Yazılışları benzeyen veya karıştırılan sözcüklerin yanlış yerde kullanılmasıdır. Örnek: 'Öğrencilerin fidan dikmesini sağladı' (Sağladı değil, sağladı olumlu; neden oldu olumsuzdur)."},
    {"card_number": 3, "title": "Çelişen Sözcüklerin Kullanılması", "body": "Kesinlik ve olasılık bildiren sözcüklerin aynı cümlede kullanılmasıdır. Örnek: 'Tam olarak 5 yıl kadar önceydi.'"},
    {"card_number": 4, "title": "Sözcüğün Yanlış Yerde Kullanımı", "body": "Sözcüğün cümledeki yerinin yanlış olması anlam karışıklığına yol açar. Örnek: 'Çok güneşte kalma' yerine 'Güneşte çok kalma' olmalı."},
    {"card_number": 5, "title": "Mantar Mantık Hatası", "body": "Mantık ve sıralama hatalarıdır. Örnek: 'Bırakın patates doğramayı, yemek bile yapamaz' (Yemek yapmak daha zordur, sıra yanlış)."},
    {"card_number": 6, "title": "Özne-Yüklem Uyumsuzluğu", "body": "Tekillik-çoğulluk veya kişi uyumsuzluğudur. Örnek: 'Ağaçlar yapraklarını döktüler' yanlış; organ ve bitki çoğul özneyse yüklem tekil olur: döktü."},
    {"card_number": 7, "title": "Öge Eksikliği (Sıralı Cümlelerde)", "body": "Ortak öge kullanımından doğan bozukluktur. Örnek: 'Sana inanıyor ve (seni) destekliyoruz' cümlesinde nesne eksiktir."},
    {"card_number": 8, "title": "Tamlama Hataları", "body": "İsim ve sıfatların aynı tamlayana bağlanmasıdır. Örnek: 'Resmi ve özel kuruluşlar' yerine 'Resmi kuruluşlar ve özel kuruluşlar' olmalı."},
    {"card_number": 9, "title": "Zamire Bağlı Anlam Belirsizliği", "body": "Cümlede kastedilen kişinin kim olduğunun açık olmamasıdır. Örnek: 'Okula gitmediğini duydum' (Senin mi, onun mu?)."},
    {"card_number": 10, "title": "Çatı Uyumsuzluğu", "body": "Bir birleşik cümlede fiilimsiler ile yüklemin etkenlik/edilgenlik yönünden uyumsuz olmasıdır."}
  ],
  "topic-turkce-yazim-kurallari": [
    {"card_number": 1, "title": "Bitişik Yazılan Ki Altın Kuralı", "body": "Ki'den sonra '-ler' eki getirildiğinde anlamlı oluyorsa bitişik (kestikiler -> anlamlı), anlamsız oluyorsa ayrı yazılır."},
    {"card_number": 2, "title": "Bitişik Yazılan De/Da Testi", "body": "Cümleden çıkarıldığında cümlenin anlamı tamamen bozuluyorsa bulunma ekidir ve bitişik yazılır; bozulmuyorsa bağlaçtır ve ayrı yazılır."},
    {"card_number": 3, "title": "Bitişik Birleşik Kelime Şifresi", "body": "İki kelimeden ikincisi veya her ikisi birleşme sırasında anlam değişikliğine uğrarsa bitişik yazılır. Örnek: Kuşburnu, keçiboynuzu."},
    {"card_number": 4, "title": "Ses Düşmesi / Türemesi Bitişikliği", "body": "Etmek, olmak yardımcı fiilleriyle kurulan birleşik fiillerde ses düşmesi veya türemesi varsa bitişik yazılır. Örnek: Kaybolmak, hissetmek."},
    {"card_number": 5, "title": "Büyük Harflerin Kullanımı", "body": "Unvanlar, saygı sözleri, kurum isimleri büyük harfle başlar. Örnek: Mustafa Kemal Paşa, Türk Dil Kurumu."},
    {"card_number": 6, "title": "Tarihlerin Yazımı Kuralı", "body": "Belirli bir günü ve ayı bildiren tarih sayıları büyük harfle başlar. Örnek: 29 Ekim 1923 (Ekim büyük)."},
    {"card_number": 7, "title": "Sayıların Yazılışı", "body": "Sayılar metin içerisinde harfle yazılır (on beş gün). Ancak senet, çek vb. ticari belgelerde bitişik yazılır (onbeşTL)."},
    {"card_number": 8, "title": "İkilemelerin Yazılışı Altın Kuralı", "body": "İkilemeler her zaman ayrı yazılır ve aralarına hiçbir noktalama işareti girmez. Örnek: Baş başa, el ele, ağır ağır."},
    {"card_number": 9, "title": "Kısaltmalara Gelen Ekler", "body": "Büyük harfle yapılan kısaltmalara gelen ekler kısaltmanın son harfinin okunuşuna göre gelir. Örnek: TDK'den (TDK'dan değil)."},
    {"card_number": 10, "title": "Yer İsimlerinde Unvan Yazımı", "body": "Yer adlarında ilk isimden sonra gelen deniz, dağ, nehir vb. tür bildiren ikinci isimler büyük harfle başlar. Örnek: Ağrı Dağı, Van Gölü."}
  ],
  "topic-turkce-noktalama": [
    {"card_number": 1, "title": "Nokta (.) Kullanım Alanları", "body": "Cümlenin sonuna, bazı kısaltmaların sonuna (Dr.), sayılardan sonra sıra bildirmek için (3.) ve tarihlerin arasına konur."},
    {"card_number": 2, "title": "Virgül (,) Altın Kuralları", "body": "Eş görevli sözcükleri ayırmak, sıralı cümleleri bölmek ve özneyi vurgulamak için konur. Metinde ve, veya, de, ki bağlaçlarından önce/sonra konmaz!"},
    {"card_number": 3, "title": "Noktalı Virgül (;) Şifresi", "body": "Cümle içinde virgüllerle ayrılmış tür veya takımları ayırmak ve ögeleri arasında virgül bulunan sıralı cümleleri ayırmak için kullanılır."},
    {"card_number": 4, "title": "İki Nokta (:) Kullanımı", "body": "Kendisiyle ilgili örnek verilecek veya açıklama yapılacak cümlenin sonuna konur. İki noktadan sonra gelen açıklama cümle ise büyük, örnekler dizisiyse küçük başlar."},
    {"card_number": 5, "title": "Üç Nokta (...) Kullanımı", "body": "Tamamlanmamış (eksiltili) cümlelerin sonuna ve kaba sayıldığı için açıklanmak istenmeyen kelimelerin yerine konur."},
    {"card_number": 6, "title": "Soru İşareti (?) İpucu", "body": "Soru eki veya sözü içeren cümlelerin sonuna konur. Soru ifadesi taşıyan ancak yan cümlecik olan yapılarda konmaz (Ne zaman geleceğini bilmiyorum.)."},
    {"card_number": 7, "title": "Ünlem İşareti (!) Kullanımı", "body": "Sevinç, korku, şaşma gibi duyguları belirten söz veya cümlelerin sonuna konur. Yay ayraç içinde (!) alay/küçümseme anlamı katar."},
    {"card_number": 8, "title": "Kısa Çizgi (-) Kullanımı", "body": "Satıra sığmayan kelimeleri bölerken, kelimelerin kök ve eklerini ayırırken ve ara sözlerin başında/sonunda kullanılır."},
    {"card_number": 9, "title": "Kesme İşareti (') Kullanımı", "body": "Özel isimlere gelen çekim eklerini ayırmak için kullanılır. Kurum, kuruluş ve kurul adlarına gelen ekler kesmeyle ayrılmaz! (Türk Dil Kurumuna)"},
    {"card_number": 10, "title": "Tırnak İşareti (\") Kullanımı", "body": "Başka bir kimseden veya yazıdan olduğu gibi aktarılan sözler ile özellikle vurgulanmak istenen sözler tırnak içine alınır."}
  ],
  "topic-turkce-sozel-mantik": [
    {"card_number": 1, "title": "Sözel Mantık Tablo Kurma", "body": "Verilen bilgilere göre sabit olan öge (günler, katlar, kişiler) tablo başlığı yapılır; değişken unsurlar tabloya yerleştirilir."},
    {"card_number": 2, "title": "Kesin Bilgiler İle Başla", "body": "Metinde 'kesinlikle', 'tam olarak' şeklinde belirtilen bilgileri doğrudan tabloya işleyin; olasılıkları kenara not edin."},
    {"card_number": 3, "title": "Olasılıkları İki Tablo ile Çöz", "body": "İki farklı ihtimal varsa tek tabloda karıştırmak yerine 1. ve 2. ihtimal tabloları oluşturup ayrı ayrı deneyin."},
    {"card_number": 4, "title": "Sıralama Soruları Taktiği", "body": "Önce-sonra, hemen önünde-hemen arkasında ifadelerine dikkat edin; paket (blok) bilgiler (örn: A ve B peş peşe) oluşturun."},
    {"card_number": 5, "title": "Eşleştirme Soruları Taktiği", "body": "Kişi-ürün veya kişi-şehir eşleştirmelerinde sayıca az olan grubu sabit başlık olarak tabloya yerleştirin."},
    {"card_number": 6, "title": "Olumsuz İfadeleri Kaçırma", "body": "'A kişisi X ürününü almamıştır' gibi olumsuz verileri tablonun ilgili hücresine üstü çizili olarak not edin."},
    {"card_number": 7, "title": "Kalan Ögeler Mantığı", "body": "Tabloda dolmayan boşluklara sadece geriye kalan ögeler girebilir; seçeneklerde bu kalan ögeleri sorgulayın."},
    {"card_number": 8, "title": "Paket (Blok) Oluşturma", "body": "'A ile B arasından bir kişi vardır' ifadesini A _ B şeklinde paket yapıp tablo boşluklarına sığdırın."},
    {"card_number": 9, "title": "Soru Köküne Göre Çözüm", "body": "'Hangisi kesinlikle doğrudur?' sorularında her iki olasılıkta da değişmeyen tek ortak bilgiyi arayın."},
    {"card_number": 10, "title": "Zaman Yönetimi Altın Kuralı", "body": "Tabloyu doğru kurmak sorunun %80'ini çözer. Tablo kurulumuna 1.5-2 dakika ayırmaktan çekinmeyin, sorular saniyeler içinde çözülecektir."}
  ]
}

def export_all_generated_flashcards():
    base_dir = os.path.join("assets", "data", "topics")
    
    total_cards = 0
    for topic_id, cards in flashcard_database.items():
        course_folder = "turkce" if "turkce" in topic_id else "general"
        topic_dir = os.path.join(base_dir, course_folder)
        os.makedirs(topic_dir, exist_ok=True)
        
        data = {
            "topic_id": topic_id,
            "flashcard_count": len(cards),
            "flashcards": cards
        }
        
        file_name = f"flashcards_{topic_id}.json"
        file_path = os.path.join(topic_dir, file_name)
        
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
            
        total_cards += len(cards)
        print(f"  [OK] {topic_id} -> {len(cards)} Flashcard yazıldı: {file_path}")

    # Master Consolidated Flashcards File
    master_path = os.path.join("assets", "data", "sample_flashcards_master.json")
    with open(master_path, "w", encoding="utf-8") as f:
        json.dump(flashcard_database, f, ensure_ascii=False, indent=2)

    print(f"\n[BAŞARILI] TÜRKÇE DERSİNİN TÜM 15 ALT KONUSUNA AİT TOPLAM {total_cards} FLASHCARD UYGULAMAYA ENTEGRE EDİLDİ!")

if __name__ == "__main__":
    export_all_generated_flashcards()
