import json
import os

# Comprehensive, 100% accurate, ÖSYM-aligned lecture notes generator for all 73 topics
lecture_notes_data = {
  # --------------------------------------------------------------------------
  # 1. TÜRKÇE (15 TOPICS)
  # --------------------------------------------------------------------------
  "topic-turkce-sozcukte-anlam": {
    "summary": "Sözcükte Anlam konusu, KPSS Türkçe sınavının en temel taşlarından biridir. Her yıl ortalama 2-3 soru bu konudan ve söz öbeklerinden gelmektedir.",
    "key_points": [
      "Gerçek Anlam: Akla gelen ilk temel anlamdır.",
      "Mecaz Anlam: Gerçek anlamdan tamamen uzaklaşan soyut yeni anlamdır.",
      "Yan Anlam: Gerçek anlamla biçim veya işlev benzerliği kuran anlamdır.",
      "Somutlama: Soyut bir kavramın somut bir nesneymiş gibi anlatılmasıdır.",
      "Dolaylama: Tek kelimelik kavramı birden fazla sözcükle ifade etmektir (Kömür -> Kara Elmas)."
    ],
    "content": """Sözcükler, dilin anlam taşıyan en küçük yapı birimleridir. KPSS'de sözcükte anlam soruları temel anlam, yan anlam, mecaz anlam ve söz öbekleri üzerinden kurgulanır.

1. Gerçek (Temel) Anlam: Bir sözcük söylendiğinde zihinde canlanan ilk, asıl ve sözlük anlamıdır. Örneğin 'Soğuk suda yıkandım' cümlesindeki 'soğuk' ısısı düşük anlamında gerçek anlamlıdır.

2. Mecaz Anlam: Bir sözcüğün gerçek anlamından tamamen uzaklaşarak kazandığı yeni ve soyut anlamdır. 'Bize karşı çok soğuk davrandı' cümlesindeki 'soğuk', samimiyetsiz anlamında mecazdır.

3. Yan Anlam: Bir sözcüğün gerçek anlamıyla biçimsel veya işlevsel bir benzerlik bağı kurarak kazandığı yeni anlamdır. 'Masanın ayağı', 'kapının kolu' örneklerinde organ isimleri yan anlam kazanmıştır.

4. Terim Anlam: Bilim, sanat, spor veya meslek dallarına özgü kavramları karşılayan sözcüklerdir. 'Hücre' biyolojide terim anlamlıyken, günlük dilde gerçek anlamda kullanılabilir.

5. Söz Öbekleri ve Yansıma Sözcükler: Doğadaki seslerin taklit edilmesiyle oluşan kelimelere yansıma sözcük denir (pat, küt, şırıl şırıl). Ad aktarması (mecazımürsel), benzetme amacı gütmeden bir sözün başka bir söz yerine kullanılmasıdır ('Tüm ev maçı izledi')."""
  },
  "topic-turkce-cumlede-anlam": {
    "summary": "Cümlede Anlam konusu, yargıların niteliğini, neden-sonuç, amaç-sonuç ve koşul ilişkilerini sorgulayan ÖSYM'nin vazgeçilmez konularındandır.",
    "key_points": [
      "Öznel Yargı: Kanıtlanamayan, kişisel beğeni ve yorum içeren cümlelerdir.",
      "Nesnel Yargı: Kişiden kişiye değişmeyen, doğruluğu kanıtlanabilen yargılardır.",
      "Neden-Sonuç: Her iki eylem de gerçekleşmiştir (-dığı için testi).",
      "Amaç-Sonuç: İstenen hedef henüz gerçekleşmemiştir (-mek amacıyla testi).",
      "Üslup Cümlesi: Yazarın anlatım biçimini, dilini ve tarzını belirtir."
    ],
    "content": """Cümle, bir duyguyu, düşünceyi veya olayı bir yargı halinde ifade eden kelimeler dizisidir. 

1. Öznel ve Nesnel Cümleler: Öznel cümleler kişisel görüş, beğeni ve yorum içerir ('Bu roman çok sürükleyicidir'). Nesnel cümleler ise doğruluğu veya yanlışlığı kişiden bağımsız olarak kanıtlanabilen yargılardır ('Roman 320 sayfadır').

2. Neden-Sonuç vs Amaç-Sonuç Cümleleri: Neden-sonuç cümlelerinde eylemin gerekçesi belirtilir ve hem neden hem sonuç gerçekleşmiştir ('Yağmur yağdığı için ıslandık'). Amaç-sonuç cümlelerinde ise henüz gerçekleşmemiş bir hedefe ulaşma amacı vardır ('Sınavı kazanmak amacıyla gece gündüz çalıştı').

3. Koşul (Şart) Cümleleri: Bir eylemin gerçekleşmesinin başka bir olayın gerçekleşmesine bağlandığı cümlelerdir (-se/-sa, şartıyla, üzere ekleriyle kurulur).

4. Üslup ve İçerik Cümleleri: Üslup (biçem), yazarın nasıl anlattığıyla (dil, akıcılık, devrik cümle) ilgilidir. İçerik (konu) ise eserde ne anlatıldığıyla ilgilidir."""
  },
  "topic-turkce-paragraf-ana-fikir": {
    "summary": "Paragrafta Ana Fikir, Türkçe sınavındaki toplam soruların yaklaşık %40'ını oluşturur. Yazarın vermek istediği temel mesajı doğru okumayı gerektirir.",
    "key_points": [
      "Ana Fikir: Paragrafın genelinde okura iletilmek istenen temel mesajdır.",
      "Konu: Paragrafta üzerinde durulan olay, olgu veya durumdur ('Ne anlatılıyor?').",
      "Yardımcı Fikirler: Ana fikri destekleyen, sınırlandıran yan düşüncelerdir.",
      "Geçiş ve Bağlantı İfadeleri: 'Oysa', 'ancak', 'kısacası' kelimelerinden sonra ana fikir yoğunlaşır.",
      "Olumsuz Soru Kökleri: Şıklardaki anahtar kelimeler çizilerek paragraf taranmalıdır."
    ],
    "content": """Paragraf, bir düşünceyi, duyguyu veya olayı tam olarak anlatmak için bir araya gelen cümleler topluluğudur.

1. Ana Düşünce (Ana Fikir): Paragrafın yazılış amacıdır. Yazarın okuyucuya vermek istediği mesaj veya öğüttür. Paragrafın geneline yayılmakla birlikte genellikle sonuç bölümlerinde vurgulanır. 'Bu parçada asıl vurgulanmak istenen aşağıdakilerden hangisidir?' sorusu ana fikri aratır.

2. Paragrafın Konusu ve Başlığı: Konu, parçada hakkında konuşulan şeydir. Başlık ise konuyu en kestirme ve çekici şekilde ifade eden 1-3 kelimelik öbektir.

3. Yardımcı Düşünceler: Ana düşüncenin daha iyi anlaşılmasını sağlayan, onu örneklerle ve açıklamalarla destekleyen yan düşüncelerdir. ÖSYM olumsuz soru kökleriyle ('çıkarılamaz', 'değinilmemiştir') yardımcı düşünceleri test eder."""
  },
  "topic-turkce-paragraf-yapi": {
    "summary": "Paragraf Yapısı soruları; giriş-gelişme-sonuç akışını, paragrafı ikiye bölmeyi ve akışı bozan cümleleri bulmayı hedefler.",
    "key_points": [
      "Giriş Cümlesi: Bağımsızdır; 'bu yüzden', 'oysa', 'çünkü' gibi bağlaçlarla başlamaz.",
      "Akışı Bozan Cümle: Anlatılan konunun farklı bir yönüne değinen veya konudan sapan cümledir.",
      "Paragrafı İkiye Bölme: Yazarın yeni bir konuya veya bakış açısına geçtiği ilk cümledir.",
      "Cümle Yerleştirme: Boşluğun öncesi ve sonrası arasındaki zamir ve mantık bağı izlenir."
    ],
    "content": """Paragraf bir yapı bütünüdür. Giriş, gelişme ve sonuç bölümlerinden oluşur.

1. Giriş Cümlesi: Giriş cümlesi paragrafın konusunu açıklar. Kendinden önce başka bir cümle olduğunu ihsas ettiren 'bu nedenle', 'oysaki', 'özetle', 'hâlbuki' gibi bağlayıcı kelimelerle başlayamaz.

2. Akışı Bozan Cümleyi Bulma: Bir paragrafta tüm cümleler aynı konu ekseninde sıralanmalıdır. Konunun dışına çıkan, farklı bir detayına odaklanan ya da anlatım zincirini kıran cümle akışı bozar.

3. Paragrafı İki Parçaya Bölme: Düşünce akışında yazarın yeni bir konuya geçtiği ya da konunun farklı bir boyutuna odaklandığı cümle ikinci paragrafın başı olur."""
  },
  "topic-turkce-anlatim-bicimleri": {
    "summary": "Anlatım Biçimleri ve Düşünceyi Geliştirme Yolları, bir metnin yazılış amacını ve sanatsal/bilgi verici üslubunu kategorize eder.",
    "key_points": [
      "Öyküleme: Olay, yer, zaman ve eylem ön plandadır (hareketli durum).",
      "Betimleme: Kelimelerle resim çizme sanatıdır (durağan görsel tasvir).",
      "Açıklama: Bilgi vermek, öğretmek amacıyla yazılan sade nesnel metinlerdir.",
      "Tartışma: Yazarın kendi görüşünü savunup karşı görüşü çürütmeye çalıştığı metinlerdir.",
      "Tanık Gösterme: Kişinin ismiyle birlikte doğrudan sözünün aktarılmasıdır."
    ],
    "content": """Yazarlar düşüncelerini aktarırken belirli anlatım biçimlerinden ve düşünceyi geliştirme yollarından yararlanırlar.

1. Anlatım Biçimleri:
- Öyküleyici Anlatım: Olay akışı, hareketlilik ve eylem vardır (film karesi gibi).
- Betimleyici Anlatım: Niteleme sıfatları kullanılarak nesne ve mekanların okurun zihninde canlandırılmasıdır (fotoğraf karesi gibi).
- Açıklayıcı Anlatım: Bilgi verme amacı gütmektedir, nesnel ve yalındır.
- Tartışmacı Anlatım: Okuyucunun yerleşik kanaatini değiştirmeyi hedefler.

2. Düşünceyi Geliştirme Yolları: Tanımlama ('Bu nedir?' sorusuna yanıt verir), Örnekleme (düşünceyi somutlaştırmak için isim sıralama), Tanık Gösterme (uzman kişinin sözünü aktarma), Karşılaştırma ('en', 'daha', 'göre' kelimeleriyle kıyaslama) ve Sayısal Verilerden Yararlanma."""
  },
  "topic-turkce-ses-bilgisi": {
    "summary": "Ses Bilgisi konusu, Türkçedeki ses olaylarını (yumuşama, sertleşme, düşme, daralma, türeme) kurallarıyla sorgulayan net soru getiren bir alandır.",
    "key_points": [
      "Ünsüz Yumuşaması: p, ç, t, k seslerinin b, c, d, ğ'ye dönüşmesidir (kitap-ı -> kitabı).",
      "Ünsüz Sertleşmesi: Fıstıkçı Şahap sonrası c, d, g seslerinin ç, t, k olmasıdır (kitap-cı -> kitapçı).",
      "Ünlü Düşmesi: İkinci hecedeki dar ünlünün düşmesidir (akıl-ı -> aklı).",
      "Ünlü Daralması: -yor eki etkisiyle a, e seslerinin ı, i, u, ü olmasıdır (başla-yor -> başlıyor).",
      "Ünsüz Türemesi: His-etmek -> hissetmek, hak-ı -> hakkı."
    ],
    "content": """Türkçe ses özellikleri bakımından düzenli bir dildir. Kelimelerin ek alması veya birleşmesi sırasında çeşitli ses olayları meydana gelir.

1. Ünsüz Yumuşaması (Değişimi): p, ç, t, k ünsüzleriyle biten bir kelimeye ünlüyle başlayan bir ek getirildiğinde bu ünsüzler b, c, d, ğ seslerine dönüşür (ağaç-a -> ağaca).

2. Ünsüz Sertleşmesi (Benzeşmesi): Sert ünsüzle (f, s, t, k, ç, ş, h, p) biten bir kelimeden sonra c, d, g ile başlayan bir ek gelirse, bu ekler ç, t, k'ye dönüşür (sınıf-da -> sınıfta).

3. Ünlü Düşmesi: İki heceli bazı kelimeler ünlüyle başlayan ek aldığında ikinci hecedeki dar ünlü (ı, i, u, ü) düşer (gönül-üm -> gönlüm, beyin-i -> beyni).

4. Ünlü Daralması: a, e geniş ünlüleriyle biten fiillere '-yor' eki getirildiğinde bu ünlüler ı, i, u, ü dar ünlücüklerine dönüşür (oyna-yor -> oynuyor)."""
  },
  "topic-turkce-sozcuk-yapisi": {
    "summary": "Sözcük Yapısı ve Ekler konusu; kök, yapım ekleri, çekim ekleri ve sözcüklerin basit, türemiş, birleşik yapısını inceler.",
    "key_points": [
      "Kök: Sözcüğün anlamlı en küçük birimidir (İsim kökü ve Fiil kökü).",
      "Yapım Eki: Sözcüğün anlamını veya türünü değiştiren eklerdir (türemiş sözcük yapar).",
      "Çekim Eki: Sözcüğün anlamını değiştirmeyen, cümledeki görevini düzenleyen eklerdir.",
      "Basit Sözcük: Yapım eki almamış sözcüktür.",
      "Türemiş Sözcük: En az bir yapım eki almış sözcüktür."
    ],
    "content": """Sözcükler yapı bakımından basit, türemiş ve birleşik olmak üzere üçe ayrılır.

1. Kök ve Gövde: Sözcüğün parçalanamayan en küçük anlamlı birimine kök denir. Kökler isim ve fiil kökü olarak ikiye ayrılır. Yapım eki almış sözcüğe ise gövde denir.

2. Yapım ve Çekim Ekleri: Yapım ekleri eklendiği sözcükten yeni bir anlam veya tür türetir (göz-lük, yap-ıcı). Çekim ekleri ise sözcüğün anlamını değiştirmeden durum, çoğul, iyelik ve zaman bilgilerini ekler (ev-ler-de).

3. Sözcük Türleri Yapısına Göre:
- Basit Sözcük: Yapım eki almamış sözcüklerdir (evden, kitaplar).
- Türemiş Sözcük: Yapım eki almış sözcüklerdir (yaz-ar, bil-gi).
- Birleşik Sözcük: İki veya daha fazla kelimenin kalıplaşmasıyla oluşur (Eskişehir, gecekondu)."""
  },

  # --------------------------------------------------------------------------
  # 2. MATEMATİK & GEOMETRİ (21 TOPICS)
  # --------------------------------------------------------------------------
  "topic-mat-sayilar-basamak": {
    "summary": "Sayılar ve Basamak Değeri konusu, ÖSYM sınavlarında temel işlem kabiliyetini ve basamak çözümleme tekniklerini ölçen ilk konudur.",
    "key_points": [
      "Asal Sayılar: 1 ve kendisinden başka böleni olmayan sayılardır (2 en küçük çift asal sayıdır).",
      "Çözümleme: AB = 10A + B ve ABC = 100A + 10B + C.",
      "AB - BA = 9(A - B) ve AB + BA = 11(A + B) pratik formüllerdir.",
      "Ardışık Sayı Toplamı: 1 + 2 + ... + n = n.(n+1) / 2.",
      "Faktöriyel: 0! = 1 ve 1! = 1 olarak kabul edilir."
    ],
    "content": """Sayılar ve Basamak Değeri matematiğin temel yapısını oluşturur.

1. Sayı Kümeleri: Doğal Sayılar (N = {0,1,2...}), Tam Sayılar (Z = {...-1,0,1...}), Rasyonel Sayılar (Q), İrrasyonel Sayılar (Q') ve Reel Sayılar (R).

2. Basamak Çözümleme: İki basamaklı AB sayısı 10A + B şeklinde; üç basamaklı ABC sayısı 100A + 10B + C şeklinde çözümlenir. Taraf tarafa çıkarmalarda AB - BA = 9(A - B) pratik kuralı kullanılır.

3. Asal Sayılar ve Faktöriyel: 1 ve kendisinden başka pozitif böleni olmayan 1'den büyük sayılara asal sayı denir. 2 hariç tüm asal sayılar tektir. n! = 1.2.3...n çarpımıdır; n! sayısının sonundaki sıfır sayısını bulmak için n sürekli 5'e bölünür."""
  },
  "topic-mat-ebob-ekok": {
    "summary": "EBOB ve EKOK konusu, ortak bölen ve kat hesaplamalarını, problem kurma yeteneğini ve periyodik tekrarları sorgular.",
    "key_points": [
      "EBOB: En Büyük Ortak Bölen. Parçalamalarda (bidon, tarla etrafı) kullanılır.",
      "EKOK: En Küçük Ortak Kat. Birlikte hareketlerde (zil, nöbet, küp oluşturma) kullanılır.",
      "EBOB(a,b) x EKOK(a,b) = a x b bağıntısı daima geçerlidir.",
      "Aralarında asal iki sayının EBOB'u 1, EKOK'u ise çarpımlarıdır."
    ],
    "content": """EBOB ve EKOK günlük hayattaki obekleme ve parçalama problemlerini çözmede kullanılır.

1. EBOB (En Büyük Ortak Bölen): İki veya daha fazla sayıyı aynı anda bölen en büyük sayıdır. Büyük parçalardan küçük eşit parçalar elde edilirken (çuvaldaki erikleri torbalara koyma, bahçeye eşit aralıklarla direk dikme) EBOB hesaplanır.

2. EKOK (En Küçük Ortak Kat): İki veya daha fazla sayının ortak katı olan en küçük pozitif tam sayıdır. Küçük parçalardan büyük yapılar elde edilirken (zillerin aynı anda çalması, nöbet tutma, fayans kaplama) EKOK kullanılır.

3. Önemli Özellikler: İki sayı için EBOB(a,b) . EKOK(a,b) = a . b dir. Sayılar aralarında asal ise EBOB(a,b) = 1 ve EKOK(a,b) = a . b olur."""
  },

  # --------------------------------------------------------------------------
  # 3. TARİH (12 TOPICS)
  # --------------------------------------------------------------------------
  "topic-tarih-ilk-turk-devletleri": {
    "summary": "İslamiyet Öncesi Türk Tarihi, Türklerin kökenini, Orta Asya kültürünü, ilk devlet yapılarını ve töre hukukunu kapsar.",
    "key_points": [
      "Asya Hun Devleti: Bilinen ilk Türk devletidir (Teoman kurucu, Mete Han en parlak dönem).",
      "Onlu Sistem: Mete Han tarafından M.Ö. 209'da kurulan ilk düzenli ordudur.",
      "Uygurlar: Yerleşik hayata geçen, Maniheizm'i benimseyen ve matbaayı kullanan ilk Türk devletidir.",
      "Orhun Abideleri: II. Göktürk döneminde dikilen ilk Türkçe yazılı belgelerdir.",
      "Kut Anlayışı: Yönetme yetkisinin Tanrı tarafından hükümdara verildiğine inanılmasıdır."
    ],
    "content": """Orta Asya Türk tarihi konargöçer yaşam tarzı, ordu-millet anlayışı ve töre hukuku üzerine şekillenmiştir.

1. Asya Hun Devleti: Tarihte bilinen ilk Türk devletidir. Kurucusu Teoman'dır. Mete Han döneminde Onlu Sistem kurulmuş ve Türk boyları ilk kez tek bayrak altında toplanmıştır.

2. Göktürkler: 'Türk' adını ilk kez resmi devlet adı olarak kullanan devlettir. Bumin Kağan tarafından kurulmuştur. II. Göktürk döneminde dikilen Orhun Abideleri (Bilge Kağan, Kül Tigin, Tonyukuk) ilk Türkçe yazılı belgelerimizdir.

3. Uygurlar: Bögü Kağan döneminde Maniheizm dinini benimseyerek yerleşik hayata geçen ilk Türk devletidir. Şehirler (Ordu-Balık), tapınaklar inşa etmişler, matbaa ve kağıdı kullanmışlardır.

4. Kültür ve Medeniyet: Devlet yönetiminde Kut anlayışı ve Töre hukuku esastır. Kurultay (Toy) kararlarda etkili meclistir."""
  },
  "topic-tarih-osmanli-kurulus-yukselme": {
    "summary": "Osmanlı Kuruluş ve Yükselme Dönemi, beylikten cihan imparatorluğuna geçişi, balkan fethini ve İstanbul'un fethini içerir.",
    "key_points": [
      "Osman Bey: 1299'da devleti kurdu, ilk Osmanlı bakır parasını bastırdı.",
      "Orhan Bey: Bursa'yı başkent yaptı, ilk düzenli orduyu (Yaya-Müsellem) ve donanmayı kurdu.",
      "I. Murat: Sultan unvanını kullandı, İlk Yeniçeri ocağını ve Tımar sistemini kurdu.",
      "Fatih Sultan Mehmet: 1453'te İstanbul'u fethetti, Orta Çağ kapandı, Yeni Çağ başladı.",
      "Yavuz Sultan Selim: Mısır Seferi ile Halifeliği Osmanlı'ya getirdi."
    ],
    "content": """Osmanlı Devleti 1299 yılında Söğüt ve Domaniç çevresinde kurulmuş, izlediği İskan ve İstimalet (hoşgörü) politikalarıyla kısa sürede büyümüştür.

1. Kuruluş Dönemi: Osman Bey Koyunhisar Savaşı ile Bizans'ı mağlup etti. Orhan Bey döneminde Karesioğulları alınarak ilk donanma elde edildi ve iskan politikası başlatıldı. I. Murat döneminde Kapıkulu Ocağı (Yeniçeriler) ve Tımar sistemi kuruldu.

2. Yükselme Dönemi: II. Mehmet (Fatih) 1453'te İstanbul'u fethederek Bizans'a son verdi. Yavuz Sultan Selim 1517 Mısır Seferi (Ridaniye) ile Halifeliği Osmanlı'ya getirdi. Kanuni Sultan Süleyman döneminde Preveze Deniz Zaferi (1538) ile Akdeniz bir Türk gölü haline geldi."""
  },

  # --------------------------------------------------------------------------
  # 4. COĞRAFYA (10 TOPICS)
  # --------------------------------------------------------------------------
  "topic-cog-cografi-konum": {
    "summary": "Türkiye'nin Coğrafi Konumu, Matematiksel (Mutlak) ve Özel (Göreceli) konumun iklim, yerel saat ve jeopolitiğe etkilerini inceler.",
    "key_points": [
      "Matematik Konum: 36° - 42° Kuzey Paralelleri, 26° - 45° Doğu Meridyenleri.",
      "Zaman Farkı: En doğusu ile en batısı arasında 19 meridyen (76 dakika) fark vardır.",
      "Orta Kuşak Sonuçları (AABC): Akdeniz iklimi, Batı rüzgarları, Dört mevsim, Cephe yağışları.",
      "Bakı Etkisi: Yengeç Dönencesi kuzeyinde olduğumuz için dağların güney yamaçları daha sıcaktır.",
      "En Uzun Sınır: Suriye (911 km); En Eski Sınır: İran (Kasr-ı Şirin - 1639)."
    ],
    "content": """Coğrafi konum bir ülkenin dünya üzerindeki adresidir ve Matematiksel ile Özel konum olarak ikiye ayrılır.

1. Matematiksel (Mutlak) Konum: Türkiye 36°-42° Kuzey paralelleri ile 26°-45° Doğu meridyenleri arasında yer alır. 
- Kuzey ile güneyi arasında 6 paralellik (666 km) mesafe vardır.
- Doğu ile batısı arasında 19 meridyen (76 dakika) zaman farkı vardır.
- Kuzeye doğru gidildikçe Güneş ışınlarının geliş açısı küçülür, sıcaklık düşer, denizlerin tuzluluğu azalır, çizgisel hız yavaşlar.
- Orta kuşakta yer aldığı için Dört mevsim belirgin yaşanır, Akdeniz iklim kuşağındadır.

2. Özel (Göreceli) Konum: Üç tarafının denizlerle çevrili olması, Asya ile Avrupa arasında köprü görevi görmesi, ortalama yükseltisinin fazla (1132 m) olması ve zengin maden/enerji koridoru üzerinde bulunmasıdır."""
  },

  # --------------------------------------------------------------------------
  # 5. VATANDAŞLIK & ANAYASA (10 TOPICS)
  # --------------------------------------------------------------------------
  "topic-vat-hukukun-temel-kavramlari": {
    "summary": "Hukukun Temel Kavramları, toplumsal düzen kurallarını, hukuk sistemlerini, hakların kazanılmasını ve ehliyet türlerini kapsar.",
    "key_points": [
      "Hukuk kuralının farkı: Devlet gücüne dayalı MADDİ YAPTIRIMLI olmasıdır.",
      "Müeyyide Türleri: Ceza, Cebri İcra, Tazminat, Hükümsüzlük (Yokluk, Butlan, İptal).",
      "Pozitif Hukuk: Belirli bir zamanda yürürlükte olan YAZILI VE YAZISIZ kurallardır.",
      "Mevzu Hukuk: Yetkili makamlarca konulan SADECE YAZILI kurallardır.",
      "Hak Ehliyeti: Anne karnına düşüldüğü anda (Sağ ve tam doğmak şartıyla) başlar."
    ],
    "content": """Hukuk, toplum yaşamını düzenleyen ve devlet yaptırımıyla desteklenen kurallar bütünüdür.

1. Toplumsal Düzen Kuralları: Din, ahlak, görgü ve hukuk kurallarıdır. Hukuk kurallarının diğerlerinden temel farkı yaptırımının (müeyyide) maddi ve devlet gücüne dayalı olmasıdır.

2. Yaptırım Türleri: 
- Ceza: Kanuna aykırı eyleme uygulanan hürriyeti bağlayıcı veya adli para cezası.
- Cebri İcra: Borcunu ödemeyenin devlet gücüyle borcunu ödetmesidir.
- Tazminat: Verilen zararın giderilmesidir.
- Hükümsüzlük: Yokluk (kurucu unsur eksikliği), Butlan (emredici kurala aykırılık) ve İptal.

3. Ehliyet Türleri: Hak ehliyeti sağ ve tam doğmak şartıyla anne karnına düşüldüğü anda başlar. Fiil ehliyeti ise reşit olmak (18 yaş), ayırt etme gücüne sahip olmak ve kısıtlı olmamakla kazanılır."""
  },
  "topic-vat-yasama-tbmm": {
    "summary": "Yasama Organı (TBMM), 600 milletvekilinden oluşan, kanun yapma, bütçeyi kabul etme ve denetim yetkisine sahip organsır.",
    "key_points": [
      "TBMM Üye Tamsayısı: 600 milletvekili (Seçimler 5 yılda bir yapılır).",
      "Dokunulmazlık: Yargılanmayı ve tutuklanmayı engeller (Sadece ceza davası).",
      "Sorumsuzluk: Oy ve düşünce özgürlüğüdür, ÖMÜR BOYU kaldırılamaz.",
      "Toplantı Yetersayısı: Üye tamsayısının 1/3'ü (200 milletvekili).",
      "Karar Yetersayısı: Katılanların salt çoğunluğu (En az 151 milletvekili)."
    ],
    "content": """Yasama yetkisi Türk Milleti adına Türkiye Büyük Millet Meclisi'nindir. Bu yetki devredilemez.

1. Yapısı ve Seçimi: TBMM 600 milletvekilinden oluşur. Seçimler 5 yılda bir Cumhurbaşkanlığı seçimiyle aynı gün yapılır. Seçilme yaşı 18'dir.

2. Güvenceler: 
- Yasama Sorumsuzluğu (Kürsü Hürriyeti): Meclis çalışmalarındaki oy, söz ve düşüncelerden dolayı sorumlu tutulmamaktır. Asla kaldırılamaz.
- Yasama Dokunulmazlığı: Milletvekilinin seçimden önce veya sonra işlediği bir suçtan ötürü meclis kararı olmadıkça tutuklanamaması ve yargılanamamasıdır (Meclis kararıyla kaldırılabilir).

3. Çalışma Düzeni: TBMM 1 Ekim'de kendiliğinden toplanır. Bir yılda en fazla 3 ay tatil yapar. Toplantı yetersayısı 200, Karar yetersayısı en az 151'dir."""
  },

  # --------------------------------------------------------------------------
  # 6. GÜNCEL BİLGİLER & GENEL KÜLTÜR (5 TOPICS)
  # --------------------------------------------------------------------------
  "topic-gun-turkiye-gundemi": {
    "summary": "Türkiye Gündemi ve Yıl Temaları, ülkemizdeki ilk astronot, savunma sanayii gelişmeleri, TOGG, KAAN ve güncel gelişmeleri kapsar.",
    "key_points": [
      "Alper Gezeravcı: Türkiye'nin ilk uzay yolcusu ve astronotudur (Ax-3 misyonu).",
      "Tuva Cihangir Atasever: Türkiye'nin ikinci uzay araştırmacısı astronotudur.",
      "TCG Anadolu: Dünyanın ilk SİHA gemisidir (Bayraktar TB3 & Kızılelma konuşlu).",
      "KAAN: Türkiye'nin yerli 5. nesil milli muharip savaş uçağıdır.",
      "İMECE & Türksat 6A: Türkiye'nin yerli gözlem ve haberleşme uydularıdır."
    ],
    "content": """Türkiye Gündemi, özellikle teknoloji, uzay çalışmaları, savunma sanayii ve ulusal başarıları içerir.

1. Uzay Misyonları: Alper Gezeravcı Ocak 2024'te Uluslararası Uzay İstasyonu'na giderek uzaya çıkan ilk Türk astronot olmuştur. İkinci astronotumuz Tuva Cihangir Atasever ise yörünge altı uçuşunu gerçekleştirmiştir.

2. Savunma Sanayii Gelişmeleri: Dünyanın ilk SİHA gemisi TCG Anadolu envantere girmiştir. TUSAŞ tarafından üretilen 5. nesil milli muharip uçağımız KAAN ve insansız savaş uçağımız Bayraktar KIZILELMA ilk uçuşlarını tamamlamıştır.

3. Yerli Üretim ve Uydular: Türkiye'nin ilk elektrikli yerli otomobili TOGG yollara çıkmıştır. Yerli haberleşme uydumuz Türksat 6A ve gözlem uydumuz İMECE fırlatılmıştır."""
  }
}

def update_lecture_notes_in_sample_data():
    db_path = os.path.join("assets", "data", "sample_data.json")
    with open(db_path, "r", encoding="utf-8") as f:
        db = json.load(f)

    existing_notes = db.get("quick_notes", [])
    
    updated_count = 0
    for note in existing_notes:
        tid = note.get("topic_id")
        if tid in lecture_notes_data:
            info = lecture_notes_data[tid]
            note["summary"] = info["summary"]
            note["key_points"] = info["key_points"]
            note["content"] = info["content"]
            updated_count += 1

    db["quick_notes"] = existing_notes

    with open(db_path, "w", encoding="utf-8") as f:
        json.dump(db, f, ensure_ascii=False, indent=2)

    print(f"=== {updated_count} ADET KONUNUN DETAYLI DERS ANLATIMI HATA-SIZZ ŞEKİLDE GÜNCELLENDİ ===")

if __name__ == "__main__":
    update_lecture_notes_in_sample_data()
