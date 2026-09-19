import json
import os

# Complete Flashcard database builder for Coğrafya (10 Topics x 10 Flashcards = 100 Flashcards)
cografya_flashcard_database = {
  "topic-cog-cografi-konum": [
    {"card_number": 1, "title": "Türkiye'nin Matematiksel (Mutlak) Konumu", "body": "Türkiye 36° - 42° Kuzey Paralelleri ile 26° - 45° Doğu Meridyenleri arasında yer alır."},
    {"card_number": 2, "title": "En Doğu ve En Batı Uçları", "body": "En doğusu Iğdır (Dilucu), en batısı Çanakkale (Gökçeada - Avlaka Burnu)'dur. Aralarında 19 meridyen (76 dakika) fark vardır."},
    {"card_number": 3, "title": "En Kuzey ve En Güney Uçları", "body": "En kuzeyi Sinop (İnceburun), en güneyi Hatay (Beysun köyü)'dur. Aralarında 6 paralellik (666 km) kuş uçuşu mesafe vardır."},
    {"card_number": 4, "title": "Orta Kuşakta Olmanın Sonuçları (AABC)", "body": "Akdeniz iklimi görülür, Batı rüzgarları etkilidir, Dört mevsim belirgin yaşanır, Cephesel yağışlar görülür."},
    {"card_number": 5, "title": "Yengeç Dönencesi ve Bakı Etkisi", "body": "Türkiye Yengeç Dönencesi'nin kuzeyinde olduğu için Güneş ışınları asla 90 dereceyle düşmez, dağların güney yamacı (bakı) daha sıcaktır."},
    {"card_number": 6, "title": "Gölge Boyu ve Yönü", "body": "Türkiye'de yatay düzlemdeki cisimlerin gölge boyu asla sıfır olmaz. Gölge yönü yıl boyunca daima KUZEYİ gösterir."},
    {"card_number": 7, "title": "En Uzun Sınırımız ve Komşumuz", "body": "En uzun kara sınırımız Suriye (911 km), en kısa kara sınırımız Nahçıvan (Azerbaycan - 18 km) ile olan sınırdır."},
    {"card_number": 8, "title": "En Eski ve Değişmeyen Sınırımız", "body": "İran ile olan sınırımız 1639 Kasr-ı Şirin Antlaşması ile çizilmiş olup en eski ve hemen hemen hiç değişmeyen sınırımızdır."},
    {"card_number": 9, "title": "Demiryolu Bağlantısı Olmayan Komşular", "body": "Irak ve Nahçıvan (Azerbaycan) ile demiryolu sınır kapımız yoktur. Diğer komşularla demiryolu bağlantısı mevcuttur."},
    {"card_number": 10, "title": "Ulusal Saat (Yerel Saat) Kuralı", "body": "Türkiye'de 2016'dan beri yıl boyunca 45° Doğu (Iğdır) meridyeninin yerel saati (+3 GMT) ortak ulusal saat olarak kullanılır."}
  ],
  "topic-cog-yer-sekilleri": [
    {"card_number": 1, "title": "Türkiye'nin Ortalama Yükseltisi", "body": "Türkiye'nin ortalama yükseltisi 1132 metredir. Yükselti genel olarak batıdan doğuya doğru gidildikçe artar."},
    {"card_number": 2, "title": "Orojenez (Dağ Oluşumu) Türleri", "body": "Kıvrım Dağlar (Toroslar ve Kuzey Anadolu Dağları) ve Kırık Dağlar (Ege'deki Kaz, Yunt, Bozdağlar, Aydın, Menteşe - Horst/Graben)."},
    {"card_number": 3, "title": "Volkanik Dağlarımız (Şifre: KEK - SAN)", "body": "Doğu Anadolu: Ağrı, Tendürek, Süphan, Nemrut. İç Anadolu: Erciyes, Hasan Dağ, Melendiz, Karadağ, Karacadağ."},
    {"card_number": 4, "title": "Epirojenez (Kıta Oluşumu) Örnekleri", "body": "Türkiye Alp-Himalaya orojenezi sonrası III. ve IV. Jeolojik zamanda toptan yükselmiştir. Çukurova ve Ergene çöküntü alanlarıdır."},
    {"card_number": 5, "title": "Karstik Aşınım ve Birikim Şekilleri", "body": "Kireç taşı (Kalker), Jips ve Kaya tuzu arazilerde görülür. Lapya -> Dolin -> Uvala -> Polye (En büyük aşınım) ve Traverten (Birikim)."},
    {"card_number": 6, "title": "Rüzgarların En Etkili Olduğu Bölgeler", "body": "Bitki örtüsünün cılız, iklimin kurak olduğu İç Anadolu ve Güneydoğu Anadolu'da rüzgar aşınım (Mantar kaya) ve birikim (Kumul) şekilleri görülür."},
    {"card_number": 7, "title": "Buzul (Glasyal) Şekilleri Yükseltisi", "body": "Türkiye'de buzul şekilleri 2000-2200 metrenin üzerindeki yüksek dağlarda (Hakkari Cilo, Kaçkarlar, Erciyes, Ağrı, Uludağ) görülür."},
    {"card_number": 8, "title": "Delta Ovalarımızın Oluşum Şartları", "body": "Kıyıda derinliğin az olması (sığ kıyı), kıyı akıntısının zayıf olması ve akarsuyun bol alüvyon taşıması gerekir."},
    {"card_number": 9, "title": "Önemli Delta Ovalarımız", "body": "Karadeniz: Bafra (Kızılırmak), Çarşamba (Yeşilırmak). Akdeniz: Çukurova (Seyhan-Ceyhan), Silifke (Göksu). Ege: Dikili, Menemen, Selçuk, Balat."},
    {"card_number": 10, "title": "Fay Hatlarımız ve Deprem Risk Alanları", "body": "Kuzey Anadolu (KAF), Doğu Anadolu (DAF) ve Batı Anadolu (BAF) fay hatları aktiftir. Tuz Gölü çevresi, Taşeli ve Ergene deprem riski düşük alanlardır."}
  ],
  "topic-cog-iklim-bitki": [
    {"card_number": 1, "title": "Akdeniz İklimi Özellikleri", "body": "Yazları sıcak ve kurak, kışları ılık ve yağışlıdır. En fazla yağışı KIŞIN alır. Karakteristik bitki örtüsü MAKİ (Zeytin, zakkum, defne)'dir."},
    {"card_number": 2, "title": "Karadeniz İklimi Özellikleri", "body": "Her mevsim yağışlı ve ılımandır. En fazla yağışı SONBAHARDA alır. Yağış rejimi en düzenli iklimdir. Bitki örtüsü ORMAN'dır."},
    {"card_number": 3, "title": "Karasal İklim Özellikleri", "body": "Yazları sıcak ve kurak, kışları soğuk ve kar yağışlıdır. En fazla yağışı İLKBAHARDA alır (Kırkikindi yağışları). Bitki örtüsü BOZKIR'dır."},
    {"card_number": 4, "title": "Sert Karasal İklim (Erzurum-Kars)", "body": "Yazları kısa ve serin, kışları çok soğuk geçer. En fazla yağışı YAZIN alır. Bitki örtüsü ALPIN ÇAYIR (Çernozom toprakları) dır."},
    {"card_number": 5, "title": "Türkiye'nin En Yağışlı Yeri", "body": "Doğu Karadeniz (Rize çevreleri - 2400 mm üzeri) dağların kıyıya dik ve hemen gerisinde yükselmesi nedeniyle en çok yağış alan yerdir."},
    {"card_number": 6, "title": "Türkiye'nin En Az Yağış Alan Yeri", "body": "Tuz Gölü çevresi (İç Anadolu) ve Iğdır Ovası etrafı dağlarla çevrili kuytu çöküntü alanları olduğu için en az yağış alan yerlerdir."},
    {"card_number": 7, "title": "Yerli (Zonal) Toprak Türleri", "body": "Terra-Rossa (Akdeniz Kireçtaşı üzeri kiremit kırmızısı), Çernozom (Erzurum-Kars Kara toprak - En verimli), Podzol (Batı Karadeniz Soğuk nemli)."},
    {"card_number": 8, "title": "Taşınmış (Azonal) Toprak Türleri", "body": "Alüvyal (Akarsu), Kolüvyal (Dağ etegi), Regosol (Volkanik), Moren (Buzul), Rüzgar (Lös). Mineralce verimlidir ancak katmanlaşma yoktur."},
    {"card_number": 9, "title": "Endemik Bitki Tanımı ve Örnekleri", "body": "Dünyada sadece belirli bir yörede yetişen bitkilerdir. Sığla Ağacı (Muğla/Köyceğiz), Datça Hurması, Kasnak Meşesi (Isparta), Kazdağı Göknarı."},
    {"card_number": 10, "title": "Relikt (Kalıntı) Bitki Tanımı", "body": "Geçmiş jeolojik dönem iklimlerinden günümüze ulaşmayı başarmış kalıntı bitkilerdir (Örn: Kelkit Vadisi'nde zeytin yetişmesi)."}
  ],
  "topic-cog-su-kaynaklari": [
    {"card_number": 1, "title": "Türkiye Akarsularının Genel Özellikleri", "body": "Debileri (akımları) düşüktür, rejimleri düzensizdir, rekreasyon ve hidroelektrik potansiyelleri yüksek, ULAŞIMA ELVERİŞSİZDİR (Bartın Çayı hariç)."},
    {"card_number": 2, "title": "Açık Havza ve Kapalı Havza Farkı", "body": "Sularını denize ulaştırabilen akarsular Açık Havza; ulaştıramayıp gölde/bataklıkta sonlananlar Kapalı Havzadır (Tuz Gölü, Van Gölü, Göller Yöresi)."},
    {"card_number": 3, "title": "En Uzun Akarsuyumuz (Sınırlarımız İçi)", "body": "Sınırlarımız içinde doğup yine sınırlarımız içinde denize dökülen en uzun akarsumuz KIZILIRMAK'tır (Sivas'tan doğar, Bafra'dan Karadeniz'e)."},
    {"card_number": 4, "title": "Sınırlarımız Dışında Denize Dökülenler", "body": "Fırat ve Dicle (Basra Körfezi'ne), Aras ve Kura (Hazar Denizi'ne - Kapalı Havza) dökülür."},
    {"card_number": 5, "title": "Sınırlarımız Dışından Doğup Gelenler", "body": "Meriç (Bulgaristan'dan doğar Ege'de dökülür) ve Asi (Lübnan'dan doğar Hatay'da dökülür)."},
    {"card_number": 6, "title": "En Büyük Doğal Gölümüz", "body": "Van Gölü'dür. Suları sodalıdır (Karma oluşumlu: Tektonik + Volkanik set). Taşımacılık yapılan tek gölümüzdür."},
    {"card_number": 7, "title": "En Büyük Tatlı Su Gölümüz", "body": "Beyşehir Gölü'dür. Gideğeni (ayağı) olduğu için suları tatlıdır ve içme suyu kaynağı olarak kullanılır."},
    {"card_number": 8, "title": "Tektonik Göllerimiz (Şifre: BAZİT KÖŞE)", "body": "Beyşehir, Eğirdir, Burdur, Acıgöl, İznik, Sapanca, Ulubat, Manyas (Kuş Gölü), Tuz Gölü, Seyfe, Akşehir."},
    {"card_number": 9, "title": "Heyelan Set Göllerimiz (Karadeniz)", "body": "Tortum (Erzurum), Sera (Trabzon), Abant ve Golcük (Bolu), Yedigöller, Borabay (Amasya)."},
    {"card_number": 10, "title": "En Büyük Baraj Göllerimiz", "body": "Atatürk Barajı (Fırat üzeri - En büyük), Karakaya, Keban, Altınkaya, Deriner (En yüksek gövdeli baraj Çoruh üzeri)."}
  ],
  "topic-cog-nufus-yerlesme": [
    {"card_number": 1, "title": "Türkiye Nüfus Sayımları", "body": "Cumhuriyet tarihinin ilk nüfus sayımı 1927 yılında yapılmıştır. 2007'den beri Adrese Dayalı Nüfus Kayıt Sistemi (ADNKS) kullanılır."},
    {"card_number": 2, "title": "Nüfus Piramidimizin Özellikleri", "body": "Türkiye nüfus piramidi arı kovanı şekline yaklaşmaktadır. Doğum oranları azalmakta, yaşlı nüfus oranı ve ortalama yaşam süresi artmaktadır."},
    {"card_number": 3, "title": "Nüfusun Yoğun Olduğu Yerler", "body": "Marmara (Çatalca-Kocaeli), Kıyı Ege, Çukurova, Doğu Karadeniz Kıyıları, Gaziantep-Doğu Güneydoğu SANAYİ ve TARIM merkezleridir."},
    {"card_number": 4, "title": "Nüfusun Seyrek Olduğu Yerler", "body": "Taşeli ve Teke Platoları (Karstik arazi), Menteşe Yöresi (Engebeli), Tuz Gölü Çevresi (Kurak), Erzurum-Kars (Soğuk), Yıldız Dağları (Sapa)."},
    {"card_number": 5, "title": "Aritmetik Nüfus Yoğunluğu", "body": "Toplam Nüfus / Toplam Yüzölçümü. En yüksek olduğu bölge MARMARA, en düşük olduğu bölge DOĞU ANADOLU'dur."},
    {"card_number": 6, "title": "Fizyolojik Nüfus Yoğunluğu", "body": "Toplam Nüfus / Tarım Alanları. Tarım alanlarının dar, nüfusun fazla olduğu Rize ve Doğu Karadeniz'de çok yüksektir."},
    {"card_number": 7, "title": "Toplu Yerleşme Şartları", "body": "Yerşekillerinin düz, su kaynaklarının kısıtlı olduğu İç ve Güneydoğu Anadolu'da evler birbirine yakın toplu yerleşmedir."},
    {"card_number": 8, "title": "Dağınık Yerleşme Şartları", "body": "Yerşekillerinin engebeli, su kaynaklarının bol olduğu Karadeniz Bölgesi'nde evler birbirinden uzak dağınık yerleşmedir."},
    {"card_number": 9, "title": "Kırsal Konut Malzemesi", "body": "Karadeniz'de Ahşap; İç/Güneydoğu Anadolu'da Kerpiç (Toprak); Akdeniz ve Doğu Anadolu'da Taş malzeme yaygındır."},
    {"card_number": 10, "title": "Geçici Kırsal Yerleşmeler", "body": "Yayla, Kom, Oba, Ağıl, Dam, Güzle. (Divan, Mezra, Mahalle ise SÜREKLİ kırsal yerleşmelerdir)."}
  ],
  "topic-cog-tarim-hayvancilik": [
    {"card_number": 1, "title": "Intansif (Modern) Tarım", "body": "Sulama, gübreleme, kaliteli tohum ve makine kullanımının yüksek olduğu, birim alandan en yüksek verimin alındığı gelişmiş tarımdır."},
    {"card_number": 2, "title": "Ekstansif (Geleneksel) Tarım", "body": "Doğa koşullarına bağımlı, sulama ve teknolojinin az olduğu tarımdır. Yıldan yıla üretim dalgalanması fazladır."},
    {"card_number": 3, "title": "Nadas Tarımı ve Çözümü", "body": "Toprağın nem ve mineral kazanması için bir yıl boş bırakılmasıdır. Sulamanın gelişmesi ve nöbetleşe ekim nadası azaltır."},
    {"card_number": 4, "title": "Devlet Kontrolünde Olan Ürünler", "body": "Pirinç (Sıtma riski), Kenevir ve Haşhaş (Uyuşturucu), Tütün (Kalite kontrolü), Çay (Kota sınırlaması)."},
    {"card_number": 5, "title": "Cumhuriyetin Üretim Birincisi Ürünler", "body": "Fındık, İncir, Kayısı, Kiraz, Antep Fıstığı ve Ayva üretiminde Türkiye dünya birincisidir."},
    {"card_number": 6, "title": "Zeytin ve İklim Seçiciliği", "body": "Zeytin kış ılıklığı ister. Ege, Akdeniz ve Marmara ana üretim alanıdır. Doğu Karadeniz'de (Artvin/Mikroklima) yetişir."},
    {"card_number": 7, "title": "Büyükbaş Hayvancılık (Mera)", "body": "Yaz yağışlarıyla gür yaz çayırlarının yetiştiği Erzurum-Kars ve Ardahan yöresinde mera büyükbaş hayvancılığı yaygındır."},
    {"card_number": 8, "title": "Küçükbaş Hayvancılık (Koyun/Keçi)", "body": "Bozkır ikliminin görüldüğü İç ve Güneydoğu Anadolu'da Koyun; Taşeli ve Teke platolarında Kıl Keçisi yaygındır."},
    {"card_number": 9, "title": "Kümes Hayvancılığı Yayılışı", "body": "İklimden etkilenmez! Tüketici nüfusa yakınlık nedeniyle İstanbul, Bursa, Bolu, Manisa gibi büyükşehir çevrelerinde yoğunlaşmıştır."},
    {"card_number": 10, "title": "Arıcılıkta Önde Gelen İller", "body": "Bitki çeşitliliğinin fazla olduğu Muğla (Çam balı), Ordu, Rize (Anzer balı), Kars ve Hakkari ön sıradadır."}
  ],
  "topic-cog-madenler-enerji": [
    {"card_number": 1, "title": "Demir Madeni Çıkarım Yerleri", "body": "Sivas (Divriği, Kangal) ve Malatya (Hekimhan, Hasançelebi) ana çıkarım alanlarıdır. Karabük ve Ereğli'de işlenir (Kömüre yakınlık)."},
    {"card_number": 2, "title": "Bakır Madeni Çıkarım Yerleri (KADER)", "body": "Kastamonu (Küre), Artvin (Murgul), Elazığ (Maden), Rize (Çayeli). Samsun'da işlenir (Ulaşım kolaylığı)."},
    {"card_number": 3, "title": "Krom Madeni Çıkarım Yerleri", "body": "Paslanmaz çelik yapımında kullanılır. Elazığ (Guleman) ve Muğla (Fethiye-Dalaman). Antalya ve Elazığ Ferro-Krom tesislerinde işlenir."},
    {"card_number": 4, "title": "Bor Mineralleri Rezervi", "body": "Dünya rezervinin %70'inden fazlası Türkiye'dedir. Balıkesir (Bandırma), Eskişehir (Kırka), Kütahya (Emet), Bursa (Mustafakemalpaşa)."},
    {"card_number": 5, "title": "Boksit (Alüminyum) Madeni", "body": "Hafif ve dayanıklıdır. Konya (Seydişehir) ve Antalya (Akseki). Seydişehir Alüminyum Tesisleri tek entegre tesistir."},
    {"card_number": 6, "title": "Mermer Yatakları", "body": "Türkiye'nin ihraç ettiği en önemli madendir. Afyonkarahisar, Balıkesir (Marmara Adası), Denizli, Bilecik ön sıradadır."},
    {"card_number": 7, "title": "Taş Kömürü (I. Jeolojik Zaman)", "body": "Kalorisi yüksektir, demir-çelik sanayinde kullanılır. Zonguldak ve çevresinde çıkarılır."},
    {"card_number": 8, "title": "Linyit (III. Jeolojik Zaman)", "body": "Türkiye'nin hemen her bölgesinde çıkarılır. Manisa (Soma), Kütahya (Tunçbilek, Seyitömer), Kahramanmaraş (Afşin-Elbistan)."},
    {"card_number": 9, "title": "Doğal Gaz Santrallerimiz (O H A)", "body": "Ovaakça (Bursa), Hamitabat (Kırklareli), Ambarlı (İstanbul). Kırklareli (Hamitabat) ve Mardin (Çamurlu)'da çıkarılır."},
    {"card_number": 10, "title": "Jeotermal Enerji Santralleri", "body": "Yeraltı sıcak su kaynaklarıdır (Fay hatları). Denizli (Sarayköy) ve Aydın (Germencik) santralleri meşhurdur."}
  ],
  "topic-cog-sanayi-ulasim-ticaret": [
    {"card_number": 1, "title": "Sanayinin Kuruluşunda Ham Maddeye Yakınlık", "body": "Çabuk bozulan ürünlerde fabrika hammadde yanına kurulur. Çay (Rize), Şeker pancarı (İç Anadolu), Konserve/Zeytinyağı (Ege)."},
    {"card_number": 2, "title": "Sanayide Enerji Kaynağına Yakınlık", "body": "Karabük ve Ereğli Demir-Çelik Fabrikaları taş kömürüne (enerjiye) yakınlık nedeniyle buraya kurulmuştur."},
    {"card_number": 3, "title": "Sanayide Ulaşıma Yakınlık", "body": "Samsun Bakır İşletmesi ve İzmit İpraş Petrol Rafinerisi hammaddesi dışarıdan geldiği için ULAŞIM/LİMAN kolaylığıyla kurulmuştur."},
    {"card_number": 4, "title": "Petrol Rafinerilerimiz", "body": "İzmit (İpraş), İzmir (Aliağa), Mersin (Ataş), Kırıkkale (Orta Anadolu) ve Batman (Hammaddeye yakın tek rafineri)."},
    {"card_number": 5, "title": "Pamuklu Dokuma Sanayii", "body": "Adana, İzmir, Aydın, Denizli, Gaziantep, Kayseri ve İstanbul ön plandadır."},
    {"card_number": 6, "title": "Otomotiv Sanayii Merkezleri", "body": "Bursa, Kocaeli, Sakarya, İzmir, Aksaray ve Adana ana üretim merkezleridir."},
    {"card_number": 7, "title": "Demiryolu Ulaşımı Olmayan İllerimiz", "body": "Doğu Karadeniz (Trabzon, Rize, Artvin), Antalya, Muğla, Sinop, Kastamonu, Çanakkale, Hakkari'ye demiryolu ULAŞMAZ."},
    {"card_number": 8, "title": "En Gelişmiş ve Ucuz Taşıma Türü", "body": "Uluslararası ticarette en ucuz taşıma türü DENİZ YOLU, en pahalı taşıma türü HAVA YOLU'dur."},
    {"card_number": 9, "title": "Türkiye'nin İhracat (Dış Satım) Ürünleri", "body": "Motorlu kara taşıtları, beyaz eşya, tekstil, fındık, bor, mermer, çimento, krom, kablo."},
    {"card_number": 10, "title": "Türkiye'nin İthalat (Dış Alım) Ürünleri", "body": "Ham petrol, doğal gaz, ham demir-çelik, elektronik cihazlar, ilaç, iş makinesi, uçak."}
  ],
  "topic-cog-turizm-unesco": [
    {"card_number": 1, "title": "UNESCO Dünya Miras Listesi İlk Eserimiz", "body": "Türkiye'den UNESCO Dünya Miras Listesi'ne giren ilk alan Divriği Ulu Camii ve Darüşşifası'dır (Sivas - 1985)."},
    {"card_number": 2, "title": "UNESCO Listesindeki En Son Eserimiz", "body": "2023 yılında eklenen Ankara (Gordion Antik Kenti) ve 2023'te eklenen Ahşap Direkli ve Kirişli Camilerdir."},
    {"card_number": 3, "title": "Hem Doğal Hem Kültürel Varlıklarımız", "body": "Karma Miras Alanları: Pamukkale - Hierapolis (Denizli) ve Göreme Milli Parkı - Kapadokya (Nevşehir)."},
    {"card_number": 4, "title": "Göbeklitepe (Şanlıurfa)", "body": "Tarihin sıfır noktası kabul edilen, bilinen en eski tapınak kompleksidir (UNESCO 2018)."},
    {"card_number": 5, "title": "Çatalhöyük (Konya)", "body": "İnsanlık tarihinin ilk yerleşik kent modellerinden biri olan Neolitik kentin adıdır."},
    {"card_number": 6, "title": "Kış (Kayak) Turizmi Merkezleri", "body": "Bursa (Uludağ), Erzurum (Palandöken), Kayseri (Erciyes), Bolu (Kartalkaya), Kars (Sarıkamış - Kristal kar)."},
    {"card_number": 7, "title": "Inanç Turizmi Merkezleri", "body": "Meryem Ana Evi (İzmir/Efes), Sumela Manastırı (Trabzon), Saint Pierre Kilisesi (Hatay), Akdamar Kilisesi (Van)."},
    {"card_number": 8, "title": "Cittaslow (Sakin Şehir) İlk Kenti", "body": "Türkiye'nin ilk sakin şehri (Cittaslow) İzmir - SEFERİHİSAR'dır."},
    {"card_number": 9, "title": "Kruvaziyer Turizmi Limanları", "body": "Lüks dev yolcu gemilerinin yanaştığı ana limanlarımız: Kuşadası (Aydın - En çok yanaşan), İstanbul ve İzmir'dir."},
    {"card_number": 10, "title": "Yayla Turizmi Merkezi", "body": "Doğu Karadeniz (Rize Ayder Yaylası, Trabzon Uzungöl) ve Akdeniz Toros yaylaları en gelişmiş alanlardır."}
  ],
  "topic-cog-bolgeler-kalkinma": [
    {"card_number": 1, "title": "GAP (Güneydoğu Anadolu Projesi)", "body": "Fırat ve Dicle nehirleri üzerindeki barajlarla sulama ve enerji projesidir. Pamuk ve mısır üretimi patlamıştır."},
    {"card_number": 2, "title": "DOKAP (Doğu Karadeniz Projesi)", "body": "Ulaşım, yayla turizmi (Yeşil Yol), balıkçılık ve arıcılığı geliştirmeyi hedefler. Taş kömürü çıkarımı içermez!"},
    {"card_number": 3, "title": "ZBK (Zonguldak-Bartın-Karabük Projesi)", "body": "Kömür ve demir-çelik sanayisine bağımlılığı azaltmak, ekonomik çeşitlilik ve yeni iş alanları yaratmak projesidir."},
    {"card_number": 4, "title": "KOP (Konya Ovası Projesi)", "body": "Göksu Nehri'nin sularını Mavi Tünel ile Konya Ovası'na aktararak yeraltı su çekimini ve obruk oluşumunu engelleme projesidir."},
    {"card_number": 5, "title": "DAP (Doğu Anadolu Projesi)", "body": "Hayvancılığı geliştirmek, mera ıslahı yapmak ve et-süt entegre tesislerini artırmak ana hedefidir."},
    {"card_number": 6, "title": "YHGP (Yeşilırmak Havzası Gelişim Projesi)", "body": "Amasya, Çorum, Samsun, Tokat illerinde erozyon, su kirliliği ve taşkınları önleme odaklı projedir."},
    {"card_number": 7, "title": "Serbest Ticaret Bölgeleri", "body": "Gümrük ve vergi muafiyeti sağlayan alanlardır. Mersin, Ege (İzmir), Trabzon, Mardin serbest bölgeleri örnektir."},
    {"card_number": 8, "title": "Karstik Arazi Bölgemiz", "body": "Akdeniz Bölgesi (Teke ve Taşeli Platoları). Kireçtaşı yaygındır, su yer altına sızar, tarım zordur."},
    {"card_number": 9, "title": "Güneş Enerjisi Potansiyeli En Yüksek", "body": "Güneydoğu Anadolu ve Akdeniz bölgeleridir (Yıllık güneşlenme süresi 3000 saatin üstündedir)."},
    {"card_number": 10, "title": "Rüzgar Enerjisi Potansiyeli En Yüksek", "body": "Marmara (Çanakkale, Balıkesir) ve Ege (İzmir, Alaçatı) bölgeleridir."}
  ]
}

def export_all_cografya_flashcards():
    base_dir = os.path.join("assets", "data", "topics", "cografya")
    os.makedirs(base_dir, exist_ok=True)
    
    total_cards = 0
    for topic_id, cards in cografya_flashcard_database.items():
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

    print(f"\n[BAŞARILI] COĞRAFYA DERSİNİN TÜM 10 ALT KONUSUNA AİT TOPLAM {total_cards} FLASHCARD ENTEGRE EDİLDİ!")

if __name__ == "__main__":
    export_all_cografya_flashcards()
