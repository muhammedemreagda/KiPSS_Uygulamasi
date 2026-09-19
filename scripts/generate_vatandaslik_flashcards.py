import json
import os

# Complete Flashcard database builder for Vatandaşlık & Anayasa (10 Topics x 10 Flashcards = 100 Flashcards)
vatandaslik_flashcard_database = {
  "topic-vat-hukukun-temel-kavramlari": [
    {"card_number": 1, "title": "Toplumsal Düzen Kuralları", "body": "Din, ahlak, görgü ve hukuk kurallarıdır. Hukuk kurallarını diğerlerinden ayıran temel fark MADDİ YAPTIRIMLI (Devlet gücüne dayalı) olmasıdır."},
    {"card_number": 2, "title": "Hukuki Yaptırım (Müeyyide) Türleri", "body": "Ceza, Cebri İcra, Tazminat, Hükümsüzlük (İptal, Yokluk, Butlan)."},
    {"card_number": 3, "title": "Yokluk ve Butlan Farkı", "body": "Yokluk: Kurucu unsurun olmamasıdır (İmamsız nikah). Butlan: Emredici kurala aykırılıktır (Kardeşle evlenme - Mutlak Butlan)."},
    {"card_number": 4, "title": "Pozitif (Müspet) Hukuk", "body": "Bir ülkede belirli bir zamanda yürürlükte bulunan YAZILI VE YAZISIZ hukuk kurallarının tamamıdır."},
    {"card_number": 5, "title": "Mevzu Hukuk (Mevzuat)", "body": "Bir ülkede yetkili makamlar tarafından konulmuş SADECE YAZILI hukuk kurallarının (Anayasa, Kanun, Yönetmelik) tamamıdır."},
    {"card_number": 6, "title": "Hak Ehliyeti ve Fiil Ehliyeti", "body": "Hak Ehliyeti: Sağ ve tam doğmak şartıyla ANNE KARNINA DÜŞTÜĞÜ ANDA başlar. Fiil Ehliyeti: Reşit (18 yaş), ayırt etme gücü ve kısıtlı olmamakla başlar."},
    {"card_number": 7, "title": "Evlenme İle Ergin Olma (Rüşt)", "body": "Normal erginlik yaşı 18'dir. Olağan evlenme yaşı 17, olağanüstü evlenme yaşı (mahkeme kararıyla) 16'dır."},
    {"card_number": 8, "title": "Mahkeme Kararıyla Erginlik (Kazai Rüşt)", "body": "15 yaşını dolduran küçüğün kendi isteği, velisinin rızası ve mahkeme kararı ile ergin kılınmasıdır."},
    {"card_number": 9, "title": "Gaiplik Kararı ve Süreleri", "body": "Ölüm tehlikesi içinde kaybolmada 1 YIL; uzun süredir haber alınamama durumunda 5 YIL sonra mahkemeden gaiplik istenir. Miras için güvence süresi 5 ve 15 yıldır."},
    {"card_number": 10, "title": "Hukuki Hakların Kazanılması ve Kullanılması", "body": "Hakların kazanılmasında İYİNİYET (Objektif); hakların kullanılmasında ve borçların ifasında DÜRÜSTLÜK (Subjektif) kuralı geçerlidir."}
  ],
  "topic-vat-anayasa-genel-esaslar": [
    {"card_number": 1, "title": "1982 Anayasası'nın İlk 3 Maddesi", "body": "1. Madde: Devletin şekli Cumhuriyettir. 2. Madde: Devletin nitelikleri (Demokratik, laik, sosyal, hukuk devleti). 3. Madde: Dili Türkçe, başkenti Ankara, bayrağı Ay Yıldızlı al bayrak, marşı İstiklal Marşı'dır."},
    {"card_number": 2, "title": "Değiştirilemez 4. Madde Şifresi", "body": "Anayasanın 1, 2 ve 3. maddeleri değiştirilemez, değiştirilmesi teklif dahi edilemez."},
    {"card_number": 3, "title": "Sert (Katı) ve Yumuşak Anayasa", "body": "Değiştirilmesi zor usullere bağlanan ve değiştirilemez maddeleri olan anayasalar Serttir. 1921 Anayasası hariç tüm anayasalarımız serttir."},
    {"card_number": 4, "title": "Çerçeve Anayasa Tanımı", "body": "Kısa, öz ve sadece genel esasları düzenleyen anayasadır. Türk tarihinin TEK çerçeve anayasası 1921 Anayasası (Teşkilat-ı Esasiye)'dır."},
    {"card_number": 5, "title": "Sosyal Devlet İlkesi Gereği", "body": "Fırsat eşitliği sağlamak, kamulaştırma, devletleştirme, vergi adaleti ve sosyal güvenlik hakları sunmaktır."},
    {"card_number": 6, "title": "Hukuk Devleti İlkesi Gereği", "body": "Kanuni hakim güvencesi, idarenin yargısal denetimi, mahkemelerin bağımsızlığı ve kazanılmış haklara saygıdır."},
    {"card_number": 7, "title": "Egemenliğin Kullanılması (Madde 6)", "body": "Egemenlik kayıtsız şartsız milletindir. Türk milleti egemenliğini anayasanın koyduğu esaslara göre yetkili organları eliyle kullanır."},
    {"card_number": 8, "title": "Kuvvetler Ayrılığı İlkesi", "body": "Yasama yetkisi TBMM'ye, Yürütme yetkisi Cumhurbaşkanı'na, Yargı yetkisi Bağımsız ve Tarafsız Mahkemelere aittir."},
    {"card_number": 9, "title": "Üniter Devlet Yapısı", "body": "Devletin ülkesi ve milletiyle bölünmez bir bütün olması; tek anayasa, tek meclis ve tek yargı sisteminin bulunmasıdır."},
    {"card_number": 10, "title": "Anayasanın Bağlayıcılığı ve Üstünlüğü", "body": "Anayasa hükümleri yasama, yürütme, yargı organlarını ve idare makamlarını bağlayan en üstün hukuk kurallarıdır."}
  ],
  "topic-vat-yasama-tbmm": [
    {"card_number": 1, "title": "TBMM Üye Tamsayısı ve Seçim Dönemi", "body": "TBMM 600 milletvekilinden oluşur. Genel seçimler 5 YILDA BİR Cumhurbaşkanlığı seçimiyle aynı gün yapılır."},
    {"card_number": 2, "title": "Milletvekili Seçilme Yeterliliği", "body": "Türk vatandaşı olmak, 18 yaşını doldurmak, en az ilkokul mezunu olmak, kısıtlı olmamak, taksirli suçlar hariç 1 yıldan fazla hapis yatmamış olmak."},
    {"card_number": 3, "title": "Seçim İçin İstifa Etmesi Gerekenler", "body": "Hakimler, savcılar, yüksek yargı mensupları, TSK mensupları ve memurlar aday olmak için istifa etmelidir. Seçilemezlerse görevlerine dönemeyenler: Hakimler, savcılar ve TSK mensuplarıdır."},
    {"card_number": 4, "title": "Yasama Dokunulmazlığı", "body": "Milletvekilinin tutuklanmasını, sorgulanmasını ve yargılanmasını engeller (Nitelikli çoğunlukla kaldırılabilir). Sadece ceza davalarını kapsar."},
    {"card_number": 5, "title": "Yasama Sorumsuzluğu (Kürsü Hürriyeti)", "body": "Milletvekilinin meclis çalışmalarındaki oy, söz ve düşüncelerinden ÖMÜR BOYU sorumlu tutulamamasıdır. Asla KALDIRILAMAZ."},
    {"card_number": 6, "title": "Milletvekilliğinin Düşme Durumları", "body": "İstifa (Meclis kararıyla), kesin hüküm giyme (Bildirimle), kısıtlanma (Bildirimle), bağdaşmayan görevde ısrar etme ve devamsızlık (1 ayda 5 birleşim)."},
    {"card_number": 7, "title": "Milletvekilliğini DÜŞÜRMEYEN Durumlar", "body": "TBMM Başkanı seçilmek, bakan veya Cumhurbaşkanı yardımcısı olmak (Milletvekilliği kendiliğinden sona erer ama 'düşme' kararı değildir)."},
    {"card_number": 8, "title": "TBMM Toplantı ve Karar Yetersayısı", "body": "Toplantı Yetersayısı: Üye tamsayısının 1/3'ü (200 milletvekili). Karar Yetersayısı: Toplantıya katılanların salt çoğunluğudur; ancak üye tamsayısının 1/4'ünün 1 fazlasından (151) az olamaz."},
    {"card_number": 9, "title": "Anayasa Değişikliği Nisapları", "body": "Teklif için 1/5 (120 milletvekili). Kabul için 3/5 (360 milletvekili - Referandumlu kabul) veya 2/3 (400 milletvekili - Doğrudan onay)."},
    {"card_number": 10, "title": "TBMM Bilgi Edinme Yolları", "body": "Yazılı Soru, Genel Görüşme, Meclis Araştırması, Meclis Soruşturması. (Gensoru ve Sözlü Soru 2017 değişikliğiyle KALDIRILMIŞTIR!)."}
  ],
  "topic-vat-yurutme-cb": [
    {"card_number": 1, "title": "Cumhurbaşkanı Seçilme Şartları", "body": "Türk vatandaşı olmak, 40 yaşını doldurmak, yükseköğrenim (üniversite) mezunu olmak ve milletvekili seçilme yeterliliğine sahip olmak."},
    {"card_number": 2, "title": "Cumhurbaşkanı Seçim Usulü", "body": "Halk tarafından seçilir. Görev süresi 5 YILDIR. Bir kimse en fazla İKİ DEFA Cumhurbaşkanı seçilebilir."},
    {"card_number": 3, "title": "Cumhurbaşkanlığına Aday Gösterme", "body": "Siyasi parti grupları, en son seçimde tek başına veya toplamda en az %5 oy almış partiler veya en az 100 BİN SEÇMEN aday gösterebilir."},
    {"card_number": 4, "title": "Cumhurbaşkanı Seçimi Kazanma Oranı", "body": "Geçerli oyların SALT ÇOĞUNLUĞUNU (%50 + 1 oy) alan aday Cumhurbaşkanı seçilir."},
    {"card_number": 5, "title": "Cumhurbaşkanına Vekalet Etme", "body": "Cumhurbaşkanlığı makamının boşalması veya hastalık/yurtdışı durumlarında CUMHURBAŞKANI YARDIMCISI vekalet eder."},
    {"card_number": 6, "title": "Cumhurbaşkanlığı Kararnamesi (CBK)", "body": "Yürütme yetkisine ilişkin konularda çıkarılır. Temel haklar, kişisel haklar ve siyasi haklar CBK ile DÜZENLENEMEZ (Sadece Sosyal Haklar düzenlenebilir)."},
    {"card_number": 7, "title": "Olağanüstü Hal (OHAL) CBK'sı", "body": "OHAL durumlarında çıkarılır. Hak ve özgürlükler kısıtlanabilir. Resmi Gazetede yayımlandığı gün TBMM onayına sunulur."},
    {"card_number": 8, "title": "OHAL İlan Etme Yetkisi", "body": "Tabii afet, ağır ekonomik kriz veya şiddet olaylarında OLAĞANÜSTÜ HALİ CUMHURBAŞKANI İLAN EDER. Süresi en fazla 6 aydır, uzatma yetkisi TBMM'ye aittir."},
    {"card_number": 9, "title": "Cumhurbaşkanının Cezai Sorumluluğu", "body": "Suç işlediği iddiasıyla TBMM üye tamsayısının 3/10'unun teklifi, 3/5'inin kararıyla soruşturma açılır. 2/3 (400) kararla Yüce Divan'a sevk edilir."},
    {"card_number": 10, "title": "Devlet Denetleme Kurulu (DDK)", "body": "Cumhurbaşkanlığına bağlıdır. Başkan ve üyelerini Cumhurbaşkanı atar. Yargı organları HARİÇ tüm kamu kurum ve kuruluşlarını denetler."}
  ],
  "topic-vat-yargi-organlari": [
    {"card_number": 1, "title": "1982 Anayasası'na Göre Yüksek Mahkemeler", "body": "Anayasa Mahkemesi, Yargıtay, Danıştay, Uyuşmazlık Mahkemesi. (Askeri Yargıtay ve AYİM 2017'de KALDIRILMIŞTIR!)."},
    {"card_number": 2, "title": "Anayasa Mahkemesi (AYM) Üye Sayısı", "body": "Toplam 15 üyeden oluşur. 12 üyesini Cumhurbaşkanı, 3 üyesini TBMM seçer. Görev süreleri 12 YILDIR (Tekrar seçilemezler)."},
    {"card_number": 3, "title": "AYM Bireysel Başvuru Hakkı (2010)", "body": "Anayasada güvence altına alınmış temel hakları ihlal edilen herkes, iç hukuk yollarını tükettikten sonra 30 GÜN içinde AYM'ye bireysel başvuru yapabilir."},
    {"card_number": 4, "title": "Yüce Divan Sıfatıyla Yargılama", "body": "AYM; Cumhurbaşkanı, Bakanlar, AYM/Yargıtay/Danıştay üyeleri, HSK üyeleri, Sayıştay Başkanı, TBMM Başkanı ve Genelkurmay Başkanı ile Kuvvet Komutanlarını yargılar."},
    {"card_number": 5, "title": "Yargıtay (Adli Yargının Son İnceleme Mercii)", "body": "Adliye mahkemelerince verilen karar ve hükümlerin son inceleme merciidir. Üyelerini HAKİMLER VE SAVCILAR KURULU (HSK) seçer."},
    {"card_number": 6, "title": "Danıştay (İdari Yargının Son İnceleme Mercii)", "body": "İdari mahkemelerce verilen kararların son inceleme merciidir. Üyelerinin 3/4'ünü HSK, 1/4'ünü CUMHURBAŞKANI seçer."},
    {"card_number": 7, "title": "Uyuşmazlık Mahkemesi Görevi", "body": "Adli ve idari yargı mercileri arasındaki görev ve hüküm uyuşmazlıklarını kesin olarak çözen mahkemedir. Başkanı AYM kendi üyeleri arasından seçer."},
    {"card_number": 8, "title": "Hakimler ve Savcılar Kurulu (HSK)", "body": "13 üyeden oluşur. Başkanı ADALET BAKANI'dır. Adalet Bakanı Müsteşarı tabii üyedir. 4 üyeyi Cumhurbaşkanı, 7 üyeyi TBMM seçer."},
    {"card_number": 9, "title": "Sayıştay (Mali Denetim Organı)", "body": "TBMM adına kamu kurumlarının gelir, gider ve mallarını denetleyen yüksek mali denetim organıdır (Anayasada Yüksek Mahkeme olarak sayılmaz)."},
    {"card_number": 10, "title": "Hakimlik ve Savcılık Teminatı", "body": "Hakimler ve savcılar azlolunamaz, kendileri istemedikçe anayasada gösterilen yaştan (65 yaş) önce emekliye ayrılamaz."}
  ],
  "topic-vat-temel-haklar": [
    {"card_number": 1, "title": "Temel Hak ve Hürriyetlerin Sınırlanması", "body": "Temel haklar ancak KANUNLA, anayasanın sözüne ve ruhuna uygun olarak, ölçülülük ilkesi gözetilerek ve hakkın özüne dokunulmadan sınırlanabilir."},
    {"card_number": 2, "title": "Durdurulamayacak Çekirdek Haklar (OHAL dahil)", "body": "Yaşama hakkı, tıbbi zorunluluklar hariç vücut bütünlüğü, din ve vicdan hürriyeti, suç ve cezaların geriye yürümemesi, masumiyet karinesi."},
    {"card_number": 3, "title": "Kişi Hakları ve Ödevleri (Negatif Statü / Koruyucu)", "body": "Devletin dokunamayacağı haklardır: Kişi dokunulmazlığı, özel hayatın gizliliği, konut dokunulmazlığı, haberleşme hürriyeti, mülkiyet hakkı."},
    {"card_number": 4, "title": "Sosyal ve Ekonomik Haklar (Pozitif Statü / İsteme)", "body": "Bireyin devletten isteyebileceği haklardır: Eğitim hakkı, çalışma hakkı, sağlık hakkı, konut hakkı, grev ve lokavt hakkı."},
    {"card_number": 5, "title": "Siyasi Haklar ve Ödevler (Aktif Statü / Katılma)", "body": "Vatandaşlık hakkı, seçme-seçilme hakkı, parti kurma-girme hakkı, kamu hizmetine girme hakkı, dilekçe hakkı, vergi ödevi, vatan hizmeti."},
    {"card_number": 6, "title": "Siyasi Partilere Üye Olamayacaklar", "body": "Hakimler, savcılar, yüksek yargı mensupları, memurlar, TSK mensupları ve henüz lise dengi öğrenimdeki öğrenciler parti üyesi olamaz."},
    {"card_number": 7, "title": "Siyasi Partilerin Kapatılması", "body": "Yargıtay Cumhuriyet Başsavcısı'nın açtığı dava üzerine ANAYASA MAHKEMESİ tarafından kapatılır (Kabul için 2/3 oy çokluğu gerekir)."},
    {"card_number": 8, "title": "Türk Vatandaşlığının Kazanılması ve Kaybı", "body": "Soy bağı veya doğum yeri ile kazanılır. Hiçbir Türk vatana bağlılıkla bağdaşmayan bir eylemde bulunmadıkça vatandaşlıktan çıkarılamaz."},
    {"card_number": 9, "title": "Vatandaşlıktan Çıkarma Kararına Yargı Yolu", "body": "Vatandaşlıktan çıkarma kararlarına karşı yargı yolu açıktır. İlk derece mahkemesi olarak DANIŞTAY'a dava açılır."},
    {"card_number": 10, "title": "Dilekçe, Bilgi Edinme ve Kamu Denetçisine Başvuru", "body": "Vatandaşlar ve karşılıklılık esası gözetilmek şartıyla Türkiye'de ikamet eden yabancılar TBMM'ye ve yetkili makamlara yazılı başvurabilir."}
  ],
  "topic-vat-idare-merkezi-tasra": [
    {"card_number": 1, "title": "İdarenin Kanuniliği İlkesi", "body": "İdarenin tüm eylem, işlem ve kuruluşları kanuna dayanmak zorundadır (Anayasa Madde 123)."},
    {"card_number": 2, "title": "İdarenin Bütünlüğü (Hiyerarşi ve Vesayet)", "body": "İdarenin birliğini sağlayan iki araç vardır: Hiyerarşi (Aynı tüzel kişilik içindeki üst-üst ilişkisi) ve İdari Vesayet (Ayrı tüzel kişilikler arası denetim)."},
    {"card_number": 3, "title": "İdari Vesayet Örneği", "body": "İçişleri Bakanı'nın (Merkezi İdare) bir Belediye Başkanı'nı (Mahalli İdare) geçici olarak görevden uzaklaştırması İDARİ VESAYET'tir."},
    {"card_number": 4, "title": "Hiyerarşi Örneği", "body": "Vali'nin İl Milli Eğitim Müdürü'ne emretmesi veya Kaymakam'ın İlçe Nüfus Müdürü'ne talimat vermesi HİYERARŞİ'dir."},
    {"card_number": 5, "title": "Merkezden Yönetimin Yetki Genişliği", "body": "Merkeze danışmadan merkezin adına karar alabilme yetkisidir. Türkiye'de yetki genişliği SADECE VALİ'ye tanınmıştır."},
    {"card_number": 6, "title": "Başkent Teşkilatı Yardımcı Kuruluşları", "body": "Danıştay (İdari danışma), Sayıştay (Mali denetim), Milli Güvenlik Kurulu (MGK - Siyasi danışma)."},
    {"card_number": 7, "title": "İl Genel İdaresi Organları", "body": "Vali (Devletin ve Cumhurbaşkanının temsilcisi), İl İdare Şube Başkanları (Müdürler) ve İl İdare Kurulu."},
    {"card_number": 8, "title": "İlçe İdaresi Organları", "body": "Kaymakam (Cumhurbaşkanının temsilcisi), İlçe İdare Şube Başkanları ve İlçe İdare Kurulu."},
    {"card_number": 9, "title": "Vali ve Kaymakam Atanma Farkı", "body": "Vali Cumhurbaşkanı kararıyla atanır (İstisnai memurluktur). Kaymakam ise Cumhurbaşkanı onayıyla atanır (Meslek memurluğudur)."},
    {"card_number": 10, "title": "Kamu Tüzel Kişiliği (KTK) Kurulması", "body": "Kamu tüzel kişiliği ancak KANUNLA veya CUMHURBAŞKANLIĞI KARARNAMESİ ile kurulur."}
  ],
  "topic-vat-idare-mahalli-idareler": [
    {"card_number": 1, "title": "Mahalli İdare (Yerel Yönetim) Türleri", "body": "İl Özel İdaresi, Belediye, Büyükşehir Belediyesi ve Köy'dür. Anayasada sayılan yerel yönetim organları bunlardır."},
    {"card_number": 2, "title": "İl Özel İdaresi Organları", "body": "Vali (Yürütme organı), İl Genel Meclisi (Karar organı - Seçimle gelir), İl Encümeni (Danışma/İcra organı)."},
    {"card_number": 3, "title": "İl Genel Meclisi Başkanı", "body": "İl Genel Meclisi kendi üyeleri arasından seçtiği bir başkanı meclis başkanı yapar (Vali başkanlık etmez!)."},
    {"card_number": 4, "title": "Belediye Kurulma Şartı", "body": "Nüfusu 5.000 ve üzeri olan yerleşim yerlerinde CUMHURBAŞKANI KARARI ile belediye kurulabilir. İl ve ilçe merkezlerinde nüfusa bakılmaksızın kurulur."},
    {"card_number": 5, "title": "Büyükşehir Belediyesi Kurulma Şartı", "body": "Toplam nüfusu 750.000 ve üzeri olan illerde KANUNLA kurulur. Şu an Türkiye'de 30 Büyükşehir Belediyesi vardır."},
    {"card_number": 6, "title": "Belediye Organları", "body": "Belediye Başkanı (Yürütme organı), Belediye Meclisi (Karar organı), Belediye Encümeni (Danışma/Karar organı)."},
    {"card_number": 7, "title": "Belediye Başkanlığının Düşmesi Kararı", "body": "Seçilme yeterliliğini kaybeden Belediye Başkanı'nın başkanlığını düşürme kararı DANIŞTAY tarafından verilir."},
    {"card_number": 8, "title": "Köy Kurulma Şartı ve Organları", "body": "Nüfusu 2.000 ile 150 arasında olan yerlerdir. İÇİŞLERİ BAKANLIĞI kararı ile kurulur. Organları: Muhtar, İhtiyar Heyeti, İmece/Salma."},
    {"card_number": 9, "title": "Köyün Doğrudan Demokrasi Organı (Köy Derneği)", "body": "Köyde bulunan tüm seçmenlerin oluşturduğu kuruldur. Muhtarı ve İhtiyar Heyeti'ni seçer, isteğe bağlı işleri zorunlu kılar."},
    {"card_number": 10, "title": "Mahalle Kırsal/Mahalli İdare Değildir!", "body": "Mahalle bir mahalli idare birimi değildir! Kamu tüzel kişiliği (KTK) YOKTUR. Belediyeye bağlı bir yönetim birimidir."}
  ],
  "topic-vat-memurluk-hukuku": [
    {"card_number": 1, "title": "657 Sayılı DMK Temel İlkeleri", "body": "Liyakat (Yetenek ve başarıya göre yükselme), Kariyer (Meslekte en yüksek dereceye kadar ilerleme), Sınıflandırma (Görevin gerektirdiği sınıflara ayrılma)."},
    {"card_number": 2, "title": "Memurluğa Girişte Yaş Sınırı", "body": "Genel olarak 18 yaşını dolduranlar memur olabilir. Bir meslek veya sanat okulunu bitirenler Kazai Rüşt (15 yaş) kararı ile memur olabilir."},
    {"card_number": 3, "title": "Memurlukta Adaylık Süresi", "body": "Memurlukta adaylık süresi EN AZ 1 YIL, EN ÇOK 2 YILDIR. Adaylık süresince başka kuruma nakil yapılamaz."},
    {"card_number": 4, "title": "Memur Çalışma Saatleri (Haftalık)", "body": "Haftalık çalışma süresi genel olarak 40 saattir. Cumartesi ve Pazar günleri tatildir."},
    {"card_number": 5, "title": "Memur Yıllık İzin Süreleri", "body": "Hizmet süresi 1 yıldan 10 yıla kadar olanlar için 20 GÜN; 10 yıldan fazla olanlar için 30 GÜN yıllık izin verilir."},
    {"card_number": 6, "title": "Memurlara Verilen Disiplin Cezaları", "body": "Uyarma, Kınama, Aylıktan Kesme (1/30 - 1/8 arası), Kademe İlerlemesinin Durdurulması (1-3 yıl arası), Devlet Memurluğundan Çıkarma."},
    {"card_number": 7, "title": "Memurluktan Çıkarma Cezasının Yetkilisi", "body": "Devlet memurluğundan çıkarma cezası amirler tarafından değil, YÜKSEK DİSİPLİN KURULU tarafından verilir."},
    {"card_number": 8, "title": "Memur Disiplin Cezalarına Yargı Yolu", "body": "Uyarma ve kınama dahil tüm disiplin cezalarına karşı yargı yolu (İdare Mahkemesi) AÇIKTIR."},
    {"card_number": 9, "title": "Memurların Ticaret Yasağı", "body": "Memurlar Türk Ticaret Kanununa göre tacir veya esnaf sayılamaz, ticaret ve sanayi müesseselerinde görev alamazlar."},
    {"card_number": 10, "title": "Memurluğu Sona Erdiren Durumlar", "body": "Çekilme (Müstafi), Çıkarılma, Memurluk şartlarını kaybetme, Emeklilik ve Ölüm. (Açığa alınma memurluğu sona erdirmez!)."}
  ],
  "topic-vat-uluslararasi-kuruluslar": [
    {"card_number": 1, "title": "Birleşmiş Milletler (BM) Merkezi ve Kurucusu", "body": "1945'te kurulmuştur. Merkezi New York'tadır. Türkiye BM'nin 51 KURUCU üyesinden biridir."},
    {"card_number": 2, "title": "BM Güvenlik Konseyi Daimi Üyeleri (FIRÇA)", "body": "Fransa, İngiltere, Rusya, Çin, Amerika Birleşik Devletleri (ABD). Bu 5 ülkenin veto hakkı vardır."},
    {"card_number": 3, "title": "NATO (Kuzey Atlantik Antlaşması Örgütü)", "body": "1949'da kurulmuştur. Merkezi Brüksel (Belçika)'dedir. Türkiye NATO'ya 1952 yılında (Kore Savaşı sonrası) üye olmuştur."},
    {"card_number": 4, "title": "Avrupa Konseyi (AK) ve Türkiye", "body": "1949'da kurulmuştur. Merkezi Strazburg (Fransa)'dır. Türkiye 1949'da kurucu üyeler arasında katılmıştır. AİHM bu konseye bağlıdır."},
    {"card_number": 5, "title": "Avrupa Birliği (AB) Kurucu Antlaşmaları", "body": "1957 Roma Antlaşması ile (AET) kurulmuş, 1992 Maastricht Antlaşması ile adı Avrupa Birliği olmuştur."},
    {"card_number": 6, "title": "AB'ye Üye Olmayan Avrupa Ülkeleri", "body": "İsviçre, Norveç, İzlanda ve Birleşik Krallık (İngiltere - Brexit ile ayrıldı) Avrupa Birliği üyesi değildir."},
    {"card_number": 7, "title": "İslam İşbirliği Teşkilatı (İİT)", "body": "1969 Mescid-i Aksa yangını sonrası kurulmuştur. Merkezi Cidde (Suudi Arabistan)'dir. Türkiye kurucu üyedir."},
    {"card_number": 8, "title": "D-8 (Developing 8) Ülkeleri (Şifre: NİGERİYA M BAP)", "body": "1997'de Necmettin Erbakan öncülüğünde kurulan gelişmekte olan 8 Müslüman ülke: Türkiye, İran, Pakistan, Bangladeş, Malezya, Endonezya, Mısır, Nijerya."},
    {"card_number": 9, "title": "Türk Devletleri Teşkilatı (TDT)", "body": "2009 Nahçıvan Anlaşması ile kurulmuştur. Merkezi İstanbul'dadır. Üyeler: Türkiye, Azerbaycan, Kazakistan, Kırgızistan, Özbekistan."},
    {"card_number": 10, "title": "Karadeniz Ekonomik İşbirliği (KEİ)", "body": "1992'de Türkiye öncülüğünde İstanbul'da kurulmuştur. Merkezi İstanbul'dadır. Karadeniz'e kıyısı olan ve bölgesel ülkeleri kapsar."}
  ]
}

def export_all_vatandaslik_flashcards():
    base_dir = os.path.join("assets", "data", "topics", "vatandaslik")
    os.makedirs(base_dir, exist_ok=True)
    
    total_cards = 0
    for topic_id, cards in vatandaslik_flashcard_database.items():
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

    print(f"\n[BAŞARILI] VATANDAŞLIK & ANAYASA DERSİNİN TÜM 10 ALT KONUSUNA AİT TOPLAM {total_cards} FLASHCARD ENTEGRE EDİLDİ!")

if __name__ == "__main__":
    export_all_vatandaslik_flashcards()
