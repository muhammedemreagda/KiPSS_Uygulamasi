import json
import os

# Complete Flashcard database builder for Matematik & Geometri (21 Topics x 10 Flashcards = 210 Flashcards)
math_flashcard_database = {
  "topic-mat-sayilar-basamak": [
    {"card_number": 1, "title": "Asal Sayı Altın Kuralı", "body": "1'den ve kendisinden başka pozitif böleni olmayan 1'den büyük doğal sayılardır. En küçük ve tek çift asal sayı 2'dir (3, 5, 7, 11...)."},
    {"card_number": 2, "title": "Aralarında Asal Sayılar", "body": "1'den başka ortak pozitif böleni olmayan sayılardır. Sayıların kendilerinin asal olması gerekmez. Örnek: 8 ile 9 aralarında asaldır."},
    {"card_number": 3, "title": "Çift ve Tek Sayılar Mantığı", "body": "Tek x Tek = Tek; Çift x Her Şey = Çift. Çarpımın sonucu tek ise çarpanların hepsi tektir; çift ise en az bir çarpan çifttir."},
    {"card_number": 4, "title": "Basamak Değer Çözümlemesi", "body": "AB iki basamaklı sayısı 10A + B; ABC üç basamaklı sayısı 100A + 10B + C olarak çözümlenir."},
    {"card_number": 5, "title": "AB - BA Çıkarma İpucu", "body": "İki basamaklı AB ve BA sayılarının farkı: AB - BA = 9(A - B) formülü ile pratik şekilde bulunur."},
    {"card_number": 6, "title": "AB + BA Toplama İpucu", "body": "İki basamaklı AB ve BA sayılarının toplamı: AB + BA = 11(A + B) formülü ile hesaplanır."},
    {"card_number": 7, "title": "Faktöriyel Tanımı ve 0!", "body": "n! = 1.2.3...n çarpımıdır. 0! = 1 ve 1! = 1 olarak kabul edilir. n! ifadesinde n >= 0 olmalıdır."},
    {"card_number": 8, "title": "Sonu 0 İle Biten Faktöriyel", "body": "n! sayısının sonundaki sıfır sayısını bulmak için n sayısı sürekli 5'e bölünür ve bölüm rakamları toplanır."},
    {"card_number": 9, "title": "Pozitif Tam Bölen Sayısı (PBS)", "body": "Bir sayının asal çarpanlarına ayrılmış hali a^x . b^y ise, Pozitif Bölen Sayısı = (x+1)(y+1) formülüyle bulunur."},
    {"card_number": 10, "title": "Ardışık Sayılar Toplam Formülü", "body": "1'den n'e kadar olan ardışık sayıların toplamı: n.(n+1) / 2 formülü ile hesaplanır."}
  ],
  "topic-mat-ebob-ekok": [
    {"card_number": 1, "title": "EBOB (En Büyük Ortak Bölen)", "body": "İki veya daha fazla sayıyı aynı anda bölen en büyük pozitif tam sayıdır. Örnek: EBOB(12, 18) = 6'dır."},
    {"card_number": 2, "title": "EKOK (En Küçük Ortak Kat)", "body": "İki veya daha fazla sayının ortak katı olan en küçük pozitif tam sayıdır. Örnek: EKOK(12, 18) = 36'dır."},
    {"card_number": 3, "title": "EBOB x EKOK Formülü", "body": "İki a ve b doğal sayısı için: EBOB(a,b) x EKOK(a,b) = a x b formülü daima geçerlidir."},
    {"card_number": 4, "title": "Aralarında Asal Sayılarda EBOB-EKOK", "body": "a ve b aralarında asal ise EBOB(a,b) = 1 ve EKOK(a,b) = a x b olur. Örnek: EBOB(8,9)=1, EKOK(8,9)=72."},
    {"card_number": 5, "title": "Bidon / Poşet Problemleri (EBOB)", "body": "Büyük parçalardan küçük parçalar elde ediliyorsa (çuvaldaki pirinçleri torbalara koyma, tarlanın etrafına direk dikme) EBOB kullanılır."},
    {"card_number": 6, "title": "Zil / Otobüs Problemleri (EKOK)", "body": "Küçük parçalardan büyük zamanlar veya yapılar oluşturuluyorsa (zillerin aynı anda çalması, nöbet tutma) EKOK kullanılır."},
    {"card_number": 7, "title": "Karesel Fayans Kaplama (EKOK)", "body": "Boyutları verilen tuğlalarla küp yapma veya dikdörtgen yüzeyi kare fayanslarla kaplama sorularında EKOK hesaplanır."},
    {"card_number": 8, "title": "Bahçe Etrafına Direk Dikme", "body": "Kenarları a ve b olan dikdörtgen bahçenin köşelerine de gelmek şartıyla eşit aralıklarla direk dikilirse, direk sayısı = Çevre / EBOB(a,b)."},
    {"card_number": 9, "title": "Kesirli Sayılarda EKOK Formülü", "body": "a/b ve c/d kesirlerinin EKOK'u = EKOK(a,c) / EBOB(b,d) formülü ile bulunur."},
    {"card_number": 10, "title": "Ardışık Sayılarda EBOB", "body": "Ardışık iki pozitif tam sayının EBOB'u daima 1'dir. Örnek: EBOB(14, 15) = 1."}
  ],
  "topic-mat-bolunebilme": [
    {"card_number": 1, "title": "2 İle Bölünebilme Kuralı", "body": "Bir sayının birler basamağı çift (0, 2, 4, 6, 8) ise sayı 2 ile tam bölünür."},
    {"card_number": 2, "title": "3 İle Bölünebilme Kuralı", "body": "Bir sayının rakamları toplamı 3 veya 3'ün katı ise sayı 3 ile tam bölünür."},
    {"card_number": 3, "title": "4 İle Bölünebilme Kuralı", "body": "Bir sayının son iki basamağı 00 veya 4'ün katı ise sayı 4 ile tam bölünür. Örnek: 316, 500."},
    {"card_number": 4, "title": "5 İle Bölünebilme Kuralı", "body": "Bir sayının birler basamağı 0 veya 5 ise sayı 5 ile tam bölünür."},
    {"card_number": 5, "title": "8 İle Bölünebilme Kuralı", "body": "Bir sayının son üç basamağı 000 veya 8'in katı ise sayı 8 ile tam bölünür."},
    {"card_number": 6, "title": "9 İle Bölünebilme Kuralı", "body": "Bir sayının rakamları toplamı 9 veya 9'un katı ise sayı 9 ile tam bölünür."},
    {"card_number": 7, "title": "10 İle Bölünebilme Kuralı", "body": "Bir sayının birler basamağı 0 ise sayı 10 ile tam bölünür. Birler basamağındaki rakam aynı zamanda 10'a bölümünden kalandır."},
    {"card_number": 8, "title": "11 İle Bölünebilme Testi (+ - +)", "body": "Sayının rakamları sağdan sola doğru sırasıyla +, -, +, - işaretleriyle çarpılıp toplanır. Sonuç 11'in katı olmalıdır."},
    {"card_number": 9, "title": "Aralarında Asal Çarpan Kuralı", "body": "Bir sayı aralarında asal iki sayıya tam bölünüyorsa çarpımlarına da bölünür. Örnek: Hem 3 hem 4'e bölünen sayı 12'ye de bölünür."},
    {"card_number": 10, "title": "45 İle Bölünebilme Şifresi", "body": "Bir sayının 45 ile bölünebilmesi için aralarında asal olan hem 5'e hem de 9'a tam bölünmesi gerekir. Önce 5 kuralı incelenir."}
  ],
  "topic-mat-denklemler-esitsizlikler": [
    {"card_number": 1, "title": "Birinci Dereceden Denklem", "body": "ax + b = 0 denkleminde x = -b/a çözümdür. a = 0 ve b = 0 ise çözüm kümesi Tüm Reel Sayılardır (R)."},
    {"card_number": 2, "title": "Çözümsüz Denklem (Boş Küme)", "body": "ax + b = 0 denkleminde a = 0 ve b != 0 ise denklem sağlanmaz, Çözüm Kümesi = Boş Küme (Ø) olur."},
    {"card_number": 3, "title": "Eşitsizliklerde Yön Değiştirme Kuralı", "body": "Bir eşitsizliğin her iki tarafı negatif (-) bir sayı ile çarpılır veya bölünürse eşitsizlik sembolü yön değiştirir."},
    {"card_number": 4, "title": "Taraf Tarafa Toplama Eşitsizlik", "body": "Aynı yönlü eşitsizlikler taraf tarafa toplanabilir. Fakat taraf tarafa çıkarma veya bölme YAPILAMAZ."},
    {"card_number": 5, "title": "Mutlak Değer Tanımı", "body": "Bir sayının başlangıç noktasına (0) olan uzaklığıdır; sonucu asla negatif olamaz (|x| >= 0)."},
    {"card_number": 6, "title": "|x| = a Denklemi Çözümü", "body": "a > 0 olmak üzere |x| = a ise x = a veya x = -a olmak üzere iki farklı durum incelenir."},
    {"card_number": 7, "title": "|x| < a Eşitsizliği Çözümü", "body": "a > 0 için |x| < a ifadesi -a < x < a şeklinde aralık olarak çözülür."},
    {"card_number": 8, "title": "|x| > a Eşitsizliği Çözümü", "body": "a > 0 için |x| > a ifadesi x > a veya x < -a şeklinde iki ayrı durum olarak çözülür."},
    {"card_number": 9, "title": "Karesi Kendisinden Küçük Sayılar", "body": "x^2 < x şartını sağlayan sayılar 0 ile 1 arasındaki pozitif basit kesirlerdir (0 < x < 1)."},
    {"card_number": 10, "title": "İki Bilinmeyenli Denklem Sistemi", "body": "Yok etme veya yerine koyma metodu kullanılarak değişkenlerden biri elenir ve diğer bilinmeyen bulunur."}
  ],
  "topic-mat-uslu-koklu": [
    {"card_number": 1, "title": "Üslü Sayılarda Çarpma", "body": "Tabanlar aynı ise üsler toplanır (a^x . a^y = a^(x+y)); üsler aynı ise tabanlar çarpılır (a^x . b^x = (a.b)^x)."},
    {"card_number": 2, "title": "Üslü Sayılarda Bölme", "body": "Tabanlar aynı ise payın üssünden paydanın üssü çıkarılır (a^x / a^y = a^(x-y))."},
    {"card_number": 3, "title": "Üssün Üssü Kuralı", "body": "(a^x)^y = a^(x.y) şeklinde üsler birbiriyle çarpılır."},
    {"card_number": 4, "title": "Negatif Üs Kuralı", "body": "a^(-n) = 1 / a^n demektir. Sayının rasyonel tersi alınarak üs pozitif yapılır. Örnek: 2^(-3) = 1/8."},
    {"card_number": 5, "title": "Sıfırıncı Üs Kuralı", "body": "Sıfır hariç tüm sayıların sıfırıncı üssü 1'dir (a^0 = 1). 0^0 ifadesi ise belirsizdir."},
    {"card_number": 6, "title": "Köklü Sayıyı Üslü Yazma", "body": "n. dereceden kök(a^m) ifadesi üslü olarak a^(m/n) şeklinde yazılır."},
    {"card_number": 7, "title": "Köklü Sayılarda Toplama-Çıkarma", "body": "Kök dereceleri ve kök içleri aynı olan köklü sayılar katsayıları toplanıp çıkarılarak işlenir."},
    {"card_number": 8, "title": "Kökten Dışarı Çıkarma", "body": "kök(a^2 . b) ifadesinde karesi olan a dışarı çıkar, b kök içinde kalır: a.kök(b). Örnek: kök(12) = 2.kök(3)."},
    {"card_number": 9, "title": "Eşlenik İle Genişletme", "body": "Paydasında köklü sayı olan kesirlerde pay ve payda paydayı kökten kurtarmak için eşleniğiyle çarpılır. Örnek: 1 / kök(2) = kök(2)/2."},
    {"card_number": 10, "title": "Çift Dereceli Kök İçerisi", "body": "Derecesi çift olan köklü ifadelerin içi asla negatif olamaz (kök(x) için x >= 0 olmalıdır)."}
  ],
  "topic-mat-kumeler": [
    {"card_number": 1, "title": "Küme ve Eleman Sayısı", "body": "İyi tanımlanmış nesneler topluluğuna küme denir. A kümesinin eleman sayısı s(A) ile gösterilir."},
    {"card_number": 2, "title": "Alt Küme Sayısı Formülü", "body": "n elemanlı bir kümenin alt küme sayısı 2^n formülü ile hesaplanır."},
    {"card_number": 3, "title": "Özalt Küme Sayısı", "body": "Kümenin kendisi hariç alt kümeleridir. n elemanlı kümenin özalt küme sayısı 2^n - 1'dir."},
    {"card_number": 4, "title": "Kümelerde Birleşim (A U B)", "body": "A ve B kümelerinin tüm elemanlarının bir kez yazılarak oluşturduğu kümedir: s(A U B) = s(A) + s(B) - s(A n B)."},
    {"card_number": 5, "title": "Kümelerde Kesişim (A n B)", "body": "Hem A hem de B kümesinde ortak olarak bulunan elemanların oluşturduğu kümedir."},
    {"card_number": 6, "title": "Ayrık Kümeler", "body": "Ortak elemanı olmayan kümelerdir. Ayrık kümelerde kesişim boş kümedir (A n B = Ø)."},
    {"card_number": 7, "title": "Fark Kümesi (A - B)", "body": "A kümesinde olup B kümesinde olmayan elemanların oluşturduğu kümedir."},
    {"card_number": 8, "title": "Tümleyen Küme (A')", "body": "Evrensel kümede (E) olup A kümesinde olmayan elemanlardır: s(A) + s(A') = s(E)."},
    {"card_number": 9, "title": "De Morgan Kuralları", "body": "(A U B)' = A' n B' ve (A n B)' = A' U B' şeklinde tümleyen dağılır."},
    {"card_number": 10, "title": "Venn Şeması İle Problem Çözümü", "body": "Dil/Spor bilmeyenler ve bilenler problemlerinde önce kesişim bölgesi (her ikisini bilenler) doldurulur."}
  ],
  "topic-mat-hiz-zaman-yol": [
    {"card_number": 1, "title": "Temel Yol Formülü", "body": "Yol = Hız x Zaman (x = V . t). Buradan Hız = Yol / Zaman (V = x/t) türetilir."},
    {"card_number": 2, "title": "Zıt Yönlü Hareket (Karşılaşma)", "body": "Birbirine doğru hareket eden iki aracın karşılaşma süresi t = Yol / (V1 + V2) formülüyle bulunur. Hızlar toplanır."},
    {"card_number": 3, "title": "Aynı Yönlü Hareket (Yetişme)", "body": "Arkadaki hızlı aracın öndekine yetişme süresi t = Aradaki Yol / (V1 - V2) formülüyle bulunur. Hızlar çıkarılır."},
    {"card_number": 4, "title": "Ortalama Hız Formülü", "body": "Ortalama Hız = Toplam Yol / Toplam Zaman formülü ile hesaplanır. Hızların aritmetik ortalaması ALINMAZ."},
    {"card_number": 5, "title": "Eşit Mesafede Ortalama Hız", "body": "Bir yolu V1 hızıyla gidip V2 hızıyla dönen aracın ortalama hızı = 2.V1.V2 / (V1 + V2) harmonic ortalamadır."},
    {"card_number": 6, "title": "Tren ve Tünel Problemi", "body": "Trenin tüneli tamamen geçmesi için alması gereken toplam yol = Tünel Boyu + Trenin Kendi Boyudur."},
    {"card_number": 7, "title": "Akıntı / Rüzgar Problemi", "body": "Akıntı yönünde giderken Hız = V_tekne + V_akıntı; akıntıya karşı giderken Hız = V_tekne - V_akıntı olur."},
    {"card_number": 8, "title": "Dairesel Pistte Karşılaşma", "body": "Zıt yönde koşan iki hareketli pistin çevresini V1 + V2 hızıyla tamamlar: Çevre = (V1 + V2) . t."},
    {"card_number": 9, "title": "Dairesel Pistte Yan Yana Gelme", "body": "Aynı yönde koşan hızlı olanın yavaş olana tur takması için gereken zaman: Çevre = (V1 - V2) . t."},
    {"card_number": 10, "title": "km/s 'yi m/s 'ye Çevirme", "body": "km/saat cinsinden verilen hızı m/saniye yapmak için sayı 5/18 ile çarpılır. Örnek: 90 km/s = 25 m/s."}
  ],
  "topic-mat-yuzde-oran": [
    {"card_number": 1, "title": "Bir Sayının Yüzdesini Bulma", "body": "A sayısının %X'i = A . (X / 100) işlemi ile hesaplanır. Örnek: 200'ün %15'i = 200 . 15/100 = 30."},
    {"card_number": 2, "title": "Yüzde Değişimi Hesaplama", "body": "Artış veya azalış yüzdesi = (Değişim Miktarı / İlk Miktar) . 100 formülüyle bulunur."},
    {"card_number": 3, "title": "100x Değişken Kabul Etme", "body": "Yüzde problemlerinde bilinmeyen sayıya 'x' yerine '100x' demek küsuratlı işlemlerden kurtarır."},
    {"card_number": 4, "title": "Üst Üste Yüzde Zam (Bileşik)", "body": "100 TL'lik ürüne %20 zam (120 TL), ardından %10 zam yapılırsa son fiyat 120 + 12 = 132 TL olur."},
    {"card_number": 5, "title": "Doğru Orantı Tanımı", "body": "İki çokluktan biri artarken diğeri de aynı oranda artıyorsa doğru orantılıdır (a / b = k). Çapraz çarpım yapılır."},
    {"card_number": 6, "title": "Ters Orantı Tanımı", "body": "İki çokluktan biri artarken diğeri aynı oranda azalıyorsa ters orantılıdır (a . b = k). Yan yana çarpım yapılır."},
    {"card_number": 7, "title": "Orantı Sabiti (k) Mantığı", "body": "a, b, c sayıları sırasıyla 2, 3, 5 ile orantılı ise a=2k, b=3k, c=5k kabul edilir."},
    {"card_number": 8, "title": "Aritmetik Ortalama", "body": "Sayıların toplamının sayı adedine bölünmesidir: A.O = (x1 + x2 + ... + xn) / n."},
    {"card_number": 9, "title": "Geometrik Ortalama", "body": "n adet sayının çarpımının n. dereceden köküdür. İki sayı için G.O = kök(a . b)."},
    {"card_number": 10, "title": "Karışım Problemleri Yüzdesi", "body": "Saf Madde Miktarı / Toplam Karışım Miktarı = Karışımın Yüzdesi / 100 formülü kullanılır."}
  ],
  "topic-mat-kar-zarar": [
    {"card_number": 1, "title": "Maliyet, Satış ve Kâr İlişkisi", "body": "Satış Fiyatı = Maliyet + Kâr. Kâr tutarı = Maliyet x (Kâr Yüzdesi / 100)."},
    {"card_number": 2, "title": "Maliyet ve Zarar İlişkisi", "body": "Satış Fiyatı = Maliyet - Zarar. Zarar tutarı = Maliyet x (Zarar Yüzdesi / 100)."},
    {"card_number": 3, "title": "Etiket Fiyatı Üzerinden İndirim", "body": "İndirimli Fiyat = Etiket Fiyatı - İndirim Tutarı. İndirim daima Etiket Fiyatı üzerinden hesaplanır."},
    {"card_number": 4, "title": "Maliyete 100x Verme Taktiği", "body": "Ürünün maliyetine 100x denir. %30 kârla satış 130x, bu fiyat üzerinden %10 indirim ise 130x - 13x = 117x olur."},
    {"card_number": 5, "title": "Enflasyon ve Alım Gücü", "body": "Maaşa yapılan zam oranı enflasyon oranından düşükse alım gücü düşer, yüksekse alım gücü artar."},
    {"card_number": 6, "title": "Çürük / Fire Verme Problemleri", "body": "Meyve çürüyüp fire verirse kilogram maliyeti artar. Toplam ödenen para / Kalan sağlam miktar = Yeni Birim Maliyet."},
    {"card_number": 7, "title": "Hileli Tartı Problemleri", "body": "Eksik tartan tartı satıcıya kâr sağlar. 1000 gr yerine 800 gr tartan satıcı %25 kâr elde eder (200/800 = 1/4)."},
    {"card_number": 8, "title": "Kâr Oranı Neye Göre Hesaplanır?", "body": "Aksi belirtilmedikçe kâr veya zarar oranı daima MALİYET FİYATINA göre hesaplanır."},
    {"card_number": 9, "title": "Kapatıyoruz İndirimi Şifresi", "body": "Maliyeti 100 olan mala %50 zam yapıp (150), sonra %50 indirim yapılırsa sonuç 75 olur (%25 zarar edilir)."},
    {"card_number": 10, "title": "Faiz Hesaplama Formülü", "body": "Yıllık Faiz = (Ana Para . Faiz Oranı . Zaman) / 100 (F = A.n.t / 100)."}
  ],
  "topic-mat-isci-havuz": [
    {"card_number": 1, "title": "Bir Günde Yapılan İş Mantığı", "body": "Bir işçi işin tamamını x günde bitiriyorsa, 1 günde işin 1/x kadarını yapar."},
    {"card_number": 2, "title": "Birlikte Çalışma Formülü", "body": "A işçi x günde, B işçi y günde bitiriyorsa ikisi birlikte t günde: (1/x + 1/y) . t = 1 (İşin tamamı 1'dir)."},
    {"card_number": 3, "title": "İşçi Sayısı ile Zaman Orantısı", "body": "İşçi sayısı ile işin bitme süresi TERS ORANTILIDIR. İşçi sayısı artarsa işin bitme süresi kısalır."},
    {"card_number": 4, "title": "İş Kapasitesi (Hız) İlişkisi", "body": "İşçinin çalışma hızı (kapasitesi) ile işi bitirme süresi TERS ORANTILIDIR. Hızı 2 katına çıkanın süresi yarıya iner."},
    {"card_number": 5, "title": "Birlikte Başlayıp Ayrılma", "body": "Birlikte t1 gün çalışıp A ayrılırsa: (1/x + 1/y).t1 + (1/y).t2 = 1 formülü kullanılır."},
    {"card_number": 6, "title": "Orantı Kurma İş Problemi", "body": "Yapılan İş 1 / Diğer Verilerin Çarpımı 1 = Yapılan İş 2 / Diğer Verilerin Çarpımı 2 formülü hayat kurtarır."},
    {"card_number": 7, "title": "Musluk Havuz Doldurma-Boşaltma", "body": "Dolduran musluklar +, boşaltan musluk - olarak alınır: (1/A + 1/B - 1/C) . t = 1."},
    {"card_number": 8, "title": "Havuzun Ortasındaki Boşaltan Musluk", "body": "Ortadaki musluk sadece kendi seviyesinin üzerindeki kısmı boşaltabilir, alt kısma etkisi yoktur."},
    {"card_number": 9, "title": "Eşit Kapasiteli İşçiler", "body": "n tane eşit kapasiteli işçi birlikte çalışırsa iş tek işçinin bitirme süresinin n'e bölünmesiyle bulunur (t / n)."},
    {"card_number": 10, "title": "İş miktarını 100 Veya EKOK Seçme", "body": "Kesirlerle uğraşmamak için toplam iş miktarına günlerin EKOK'u değer olarak atanabilir."}
  ],
  "topic-mat-yas-problemleri": [
    {"card_number": 1, "title": "Yaş Farkı Asla Değişmez!", "body": "İki kişi arasındaki yaş farkı yıllar geçse de DAİMA SABİTTİR, değişmez."},
    {"card_number": 2, "title": "n Yıl Sonraki ve Önceki Yaş", "body": "Bugünkü yaşı x olan bir kişinin n yıl sonraki yaşı x + n; n yıl önceki yaşı x - n olur."},
    {"card_number": 3, "title": "Kişi Sayısına Göre Toplam Yaş", "body": "k kişilik bir grubun bugünkü yaşları toplamı T ise, n yıl sonraki yaş toplamı T + (k . n) olur."},
    {"card_number": 4, "title": "Doğum Yılı ve Yaş İlişkisi", "body": "Erken doğan kişi daha BÜYÜK, geç doğan kişi daha KÜÇÜK olur. Örnek: 1990 doğumlu, 1995 doğumludan 5 yaş büyüktür."},
    {"card_number": 5, "title": "'Senin Yaşına Geldiğimde' Şifresi", "body": "A, B'nin yaşına geldiğinde aradan geçen zaman (B - A) kadardır. Her ikisinin yaşına da (B - A) eklenir."},
    {"card_number": 6, "title": "Yaş Ortalaması Değişimi", "body": "k kişilik grubun yaş ortalaması A ise, n yıl sonra yaş ortalaması A + n olur (gruptan giren/çıkan yoksa)."},
    {"card_number": 7, "title": "Oran Verilen Yaş Problemleri", "body": "Babanın yaşı çocuğun yaşının 3 katı ise çocuğa x, babaya 3x denir. 5 yıl sonra (x+5) ve (3x+5) denklem kurulur."},
    {"card_number": 8, "title": "İki Kişinin Yaşları Toplamı", "body": "İki kişinin yaşları toplamı A ise biri x diğeri (A - x) olarak tek bilinmeyenle ifade edilebilir."},
    {"card_number": 9, "title": "Bugünkü Yaş Bulma", "body": "Yaş hesaplamalarında bulunan x değeri soruda istenen kişinin bugünkü yaşı mı kontrol edilmelidir."},
    {"card_number": 10, "title": "Geçen Zaman Şifresi", "body": "İki farklı zamandaki yaşlar verildiğinde geçen süre = (Son Yaş - İlk Yaş) kadardır."}
  ],
  "topic-mat-kesir-problemleri": [
    {"card_number": 1, "title": "Kesrin Değeri ve Katları", "body": "Değeri a/b olan bir kesrin payına a.k, paydasına b.k denilerek denklem kurulur."},
    {"card_number": 2, "title": "Payda Çarpımı Katı Verme Taktiği", "body": "Kesir problemlerinde bütüne (telin boyuna, paraya) paydaların EKOK'u veya çarpımı kat olarak verilir (Örn: 1/3 ve 1/4 için 12x)."},
    {"card_number": 3, "title": "Telin Orta Noktası Kayma Miktarı", "body": "Bir telin bir ucundan x uzunluğunda parça kesilirse, telin orta noktası kalkan parçanın yarısı kadar (x / 2) kayar."},
    {"card_number": 4, "title": "Kalanın Kesri İfadesi", "body": "Paranın 1/3'ünü harcayıp 'kalanın' 1/4'ü denirse; önce kalan (2/3) bulunur, sonra 2/3 . 1/4 hesabı yapılır."},
    {"card_number": 5, "title": "Kova / Depo Ağırlığı Problemi", "body": "Kabın kendi ağırlığı (dara) c olsun. Tam dolu kova ağırlığı = c + Su. Yarısı dolu kova = c + Su/2."},
    {"card_number": 6, "title": "Merdiven Basamakları Problemi", "body": "Basamakları 2'şer 2'şer çıkıp 3'er 3'er inen kişinin adım sayısı x ise: Toplam Basamak = 2 . x1 = 3 . x2."},
    {"card_number": 7, "title": "Topun Zıplama Problemi", "body": "h yüksekliğinden bırakılan top her seferinde k/m oranında zıplıyorsa; 1. zıplama = h.(k/m), 2. zıplama = h.(k/m)^2."},
    {"card_number": 8, "title": "Kesirlerde Toplama-Çıkarma", "body": "Paydaları eşit olmayan kesirlerde önce paydalar eşitleme (genişletme) yapılır, sonra işlem tamamlanır."},
    {"card_number": 9, "title": "Kesirlerde Bölme İşlemi", "body": "Birinci kesir aynen yazılır, ikinci kesir ters çevrilip (takla attırılarak) birinciyle çarpılır."},
    {"card_number": 10, "title": "Bileşik ve Basit Kesir Farkı", "body": "Payı paydasından mutlak değerce küçük olanlar Basit kesir (|a| < |b|); büyük veya eşit olanlar Bileşik kesirdir."}
  ],
  "topic-mat-sayi-problemleri": [
    {"card_number": 1, "title": "Tek Bilinmeyen Kullanma Sanatı", "body": "İki sayının toplamı 50 ise birinciye x, ikinciye (50 - x) diyerek denklem sayısını teke düşürün."},
    {"card_number": 2, "title": "Kuyruk Problemleri (Önden ve Arkadan)", "body": "Sırada baştan n. sırada, sondan m. sırada olan kişi için Toplam Kişi Sayısı = n + m - 1 (Kişi iki kez sayıldığı için 1 çıkarılır)."},
    {"card_number": 3, "title": "Kuyrukta İki Kişi Arasındaki Sayı", "body": "A baştan x., B sondan y. ve aralarında k kişi varsa; A ile B yer değiştirmediyse Toplam = x + y + k."},
    {"card_number": 4, "title": "Adım Problemleri (İleri-Geri)", "body": "7 adım ileri 2 adım geri atan biri 9 adımda 5 adım ilerler. Toplam adım sayısı 9'a bölünerek periyot hesaplanır."},
    {"card_number": 5, "title": "Mum Problemleri", "body": "Boyları eşit iki mum t1 ve t2 saatte yanıyorsa mumların boyuna t1 ve t2'nin EKOK'u denilerek birim zamandaki erime hesaplanır."},
    {"card_number": 6, "title": "Ceviz / Sıra Paylaştırma", "body": "Öğrenciler sıralara 2'şer oturunca 5 kişi ayakta kalıyorsa Öğrenci Sayısı = 2x + 5 (x: sıra sayısı)."},
    {"card_number": 7, "title": "Bilet Fiyatı ve Kişi Sayısı", "body": "Bir grubun ödeyeceği toplam hesap = (Kişi Sayısı) x (Kişi Başına Düşen Miktar). Bazıları ödemezse diğerlerinin payı artar."},
    {"card_number": 8, "title": "Taksi Metre Problemi", "body": "Ödenecek Taksi Ücreti = Açılış Ücreti + (Gidilen KM x KM Başına Ücret)."},
    {"card_number": 9, "title": "Yanlış Doğruyu Götüren Sınav", "body": "4 yanlış 1 doğruyu götürüyorsa Net Sayısı = Doğru Sayısı - (Yanlış Sayısı / 4) formülü ile hesaplanır."},
    {"card_number": 10, "title": "Bozuk Para / Banknot Sayısı", "body": "5 TL ve 10 TL'lik toplam 20 banknot varsa 5 TL'lik x adet, 10 TL'lik (20-x) adet kabul edilip tutar eşitlenir."}
  ],
  "topic-mat-sayi-dizileri": [
    {"card_number": 1, "title": "Aritmetik Dizi Tanımı", "body": "Ardışık terimleri arasındaki fark sabit olan dizilerdir. Ortak fark d ise: a_n = a_1 + (n - 1).d."},
    {"card_number": 2, "title": "Aritmetik Dizide Terim Toplamı", "body": "İlk n terim toplamı S_n = (n / 2) . (a_1 + a_n) formülü ile bulunur."},
    {"card_number": 3, "title": "Geometrik Dizi Tanımı", "body": "Ardışık terimleri arasındaki oran sabit olan dizilerdir. Ortak çarpan r ise: a_n = a_1 . r^(n - 1)."},
    {"card_number": 4, "title": "Fibonacci Sayı Dizisi", "body": "Her terimin kendinden önceki iki terimin toplamı olduğu dizidir: 1, 1, 2, 3, 5, 8, 13, 21, 34..."},
    {"card_number": 5, "title": "Terim Sayısı Formülü", "body": "Düzenli artan bir dizide Terim Sayısı = [(Son Terim - İlk Terim) / Artış Miktarı] + 1."},
    {"card_number": 6, "title": "Ortanca Terim İle Toplam", "body": "Terim sayısı tek olan aritmetik dizilerde Toplam = Ortanca Terim x Terim Sayısı."},
    {"card_number": 7, "title": "Ardışık Çift Sayılar Toplamı", "body": "2 + 4 + 6 + ... + 2n şeklindeki çift sayıların toplamı n.(n + 1) formülü ile hesaplanır."},
    {"card_number": 8, "title": "Ardışık Tek Sayılar Toplamı", "body": "1 + 3 + 5 + ... + (2n - 1) şeklindeki tek sayıların toplamı n^2 formülü ile hesaplanır."},
    {"card_number": 9, "title": "Genel Terim (a_n) Mantığı", "body": "Bir dizide n yerine 1 yazılarak 1. terim (a_1), n yerine 2 yazılarak 2. terim (a_2) elde edilir."},
    {"card_number": 10, "title": "Üstel Dizi Özelliği", "body": "Geometrik dizide her terim kendisine eşit uzaklıktaki terimlerin geometrik ortalamasıdır: (a_k)^2 = a_(k-p) . a_(k+p)."}
  ],
  "topic-mat-sekil-oruntuleri": [
    {"card_number": 1, "title": "Şekil Örüntüsü Adım Analizi", "body": "Şekil örüntülerinde 1, 2 ve 3. adımlardaki kibrit/çubuk/kare sayıları sayı dizisine çevrilerek genel kural bulunur."},
    {"card_number": 2, "title": "Adım Miktarı Doğrusal Kural", "body": "Her adımda kibrit sayısı 3 artıyorsa genel terim 3n ile başlar. 1. adımda 4 kibrit varsa kural (3n + 1)'dir."},
    {"card_number": 3, "title": "Karesel Şekil Örüntüleri", "body": "Nokta veya kare sayısı 1, 4, 9, 16... şeklinde ilerliyorsa n. adımdaki eleman sayısı n^2 ile ifade edilir."},
    {"card_number": 4, "title": "Üçgensel Sayılar Dizisi", "body": "1, 3, 6, 10, 15... şeklinde giden örüntülerde n. adımdaki eleman sayısı n.(n+1) / 2 formülüdür."},
    {"card_number": 5, "title": "Periyodik Tekrar Eden Şekiller", "body": "Şekil dizilimi her 5 adımda bir başa dönüyorsa (ABCDEABCDE...), 43. adımdaki şekil için 43'ün 5'e bölümünden kalan 3 kullanılır (C)."},
    {"card_number": 6, "title": "İçi İçe Geçen Kareler Örüntüsü", "body": "Her adımda karelerin kenarları yarıya iniyorsa alanlar 1/4 oranında küçülür (Geometrik azalış)."},
    {"card_number": 7, "title": "Köşe Noktaları Çakışması", "body": "Yan yana dizilen altıgen/karelerde ortak kenarlar tekrar sayılmamalıdır (n adet kare için çubuk sayısı 3n + 1)."},
    {"card_number": 8, "title": "Katlanıp Kesilen Kağıt Şekli", "body": "Kağıt 2'ye katlanıp kesilirse simetri eksenine göre açıldığında 2 katı parça ve simetrik delikler oluşur."},
    {"card_number": 9, "title": "Küp İstifleme (Birim Küp)", "body": "Piramit şeklinde üst üste konan küplerde katlardaki küp sayıları 1, 3, 6 veya 1, 4, 9 dizilimini takip eder."},
    {"card_number": 10, "title": "Saat Yönünde Dönme Örüntüsü", "body": "Şekil her adımda 90 derece dönüyorsa 4 adımda bir başa döner. n. adımdaki yön n mod 4 ile bulunur."}
  ],
  "topic-mat-grafik-tablo-detay": [
    {"card_number": 1, "title": "Daire Grafiği Açısı (360 Derece)", "body": "Daire grafiğinde tüm verilerin toplamı 360 derecelik açıya karşılık gelir. Orantı 360 derece üzerinden kurulur."},
    {"card_number": 2, "title": "Daire Grafiğinde Yüzde Derece Dönüşümü", "body": "%100 dilim 360 derece ise, %1'lik dilim 3.6 dereceye denk gelir. Örnek: %25 dilim = 90 derecelik dik açıdır."},
    {"card_number": 3, "title": "Çizgi Grafiği Kullanım Amacı", "body": "Zaman içindeki sürekli değişimi, artış/azalış trendlerini ve sıcaklık/döviz takibini göstermek için en uygun grafiktir."},
    {"card_number": 4, "title": "Sütun Grafiği Kullanım Amacı", "body": "Farklı kategorilerin veya grupların miktarlarını birbiriyle karşılaştırmak için kullanılır."},
    {"card_number": 5, "title": "Grafikte Yüzde Değişim Bulma", "body": "Artış Oranı = [(Son Değer - İlk Değer) / İlk Değer] x 100 formülüyle grafik üzerinden hesaplanır."},
    {"card_number": 6, "title": "İki Grafiği Birbirine Bağlama", "body": "Birinci grafikte bulunan toplam miktar (örn: ürün sayısı), ikinci grafikteki açılara ortak oran olarak dağıtılır."},
    {"card_number": 7, "title": "Tablo Okumada Satır-Sütun Kesişimi", "body": "İki boyutlu tablolarda yatay satır ile dikey sütunun kesiştiği hücre aranan veriyi verir."},
    {"card_number": 8, "title": "Eğim ve Grafik Hızı", "body": "Yol-Zaman grafiğinde çizginin eğimi (dikey/yatay) hızı verir. Çizgi ne kadar dikse hız o kadar yüksektir."},
    {"card_number": 9, "title": "Grafikte Kâr-Zarar Bölgesi", "body": "Gelir-Gider grafiğinde Gelir çizgisi Gider çizgisinin üstündeyse KÂR, altındaysa ZARAR bölgesidir."},
    {"card_number": 10, "title": "Grafik Sorularında Birim Kontrolü", "body": "Eksenlerdeki sayıların (Bin), (Milyon) veya (kg/ton) cinsinden olup olmadığına mutlaka dikkat edilmelidir."}
  ],
  "topic-mat-siralama-gruplama": [
    {"card_number": 1, "title": "Permütasyon (Sıralama)", "body": "n adet elemanın r'li sıralanışıdır: P(n,r) = n! / (n - r)!. Elemanların sırası (dizilişi) önemlidir."},
    {"card_number": 2, "title": "Kombinasyon (Seçme / Gruplama)", "body": "n eleman arasından r eleman seçilmesidir: C(n,r) = n! / [r! . (n - r)!]. Sıralama önemsizdir, sadece seçim yapılır."},
    {"card_number": 3, "title": "Faktöriyel Pratik Permütasyon", "body": "P(5, 3) hesaplanırken 5'ten geriye doğru 3 tane sayı çarpılır: 5 . 4 . 3 = 60."},
    {"card_number": 4, "title": "Tekrarlı Permütasyon Kuralı", "body": "Bazı elemanları aynı olan n elemanın farklı sıralanışı: n! / (n1! . n2! ...). Örnek: KELEBEK kelimesi harf sıralanışı."},
    {"card_number": 5, "title": "Yuvarlak Masa Permütasyonu", "body": "n kişinin yuvarlak bir masa etrafında farklı diziliş sayısı (n - 1)! formülü ile bulunur."},
    {"card_number": 6, "title": "Kombinasyon Özellikleri", "body": "C(n, 0) = 1, C(n, n) = 1 ve C(n, a) = C(n, b) ise a + b = n olur. Örnek: C(10, 3) = C(10, 7)."},
    {"card_number": 7, "title": "Klasik Olasılık Formülü", "body": "Bir A olayının olasılığı P(A) = İstenen Durum Sayısı / Tüm Olası Durumların Sayısı formülüyle hesaplanır."},
    {"card_number": 8, "title": "İmkansız ve Kesin Olasılık", "body": "Olasılık değeri daima 0 ile 1 arasındadır (0 <= P(A) <= 1). 0 İmkansız Olay, 1 Kesin Olaydır."},
    {"card_number": 9, "title": "Bağımsız Olayların Olasılığı", "body": "A ve B olayları birbirinden bağımsız ise birlikte gerçekleşme olasılığı P(A n B) = P(A) . P(B)'dir."},
    {"card_number": 10, "title": "Tümleyen Olasılık (1 - İstenmeyen)", "body": "'En az bir' sorularında İstenen Olasılık = 1 - (Hiç Olmama Olasılığı) taktiği soruyu çok kısaltır."}
  ],
  "topic-geo-ucgenler": [
    {"card_number": 1, "title": "Üçgenin İç ve Dış Açıları", "body": "Herhangi bir üçgenin iç açıları toplamı 180 derece, dış açıları toplamı 360 derecedir."},
    {"card_number": 2, "title": "İki İç Açı Bir Dış Açıya Eşittir", "body": "Bir üçgende bir dış açının ölçüsü, kendisine komşu olmayan iki iç açının ölçüleri toplamına eşittir."},
    {"card_number": 3, "title": "Üçgen Eşitsizliği Kuralı", "body": "Bir üçgende bir kenar uzunluğu diğer iki kenarın toplamından küçük, farkının mutlak değerinden büyüktür: |b-c| < a < b+c."},
    {"card_number": 4, "title": "Pisagor Teoremi (Dik Üçgen)", "body": "Bir dik üçgende hipotenüsün karesi dik kenarların kareleri toplamına eşittir: a^2 + b^2 = c^2."},
    {"card_number": 5, "title": "Özel Dik Üçgenler (Kenarlarına Göre)", "body": "3-4-5, 5-12-13, 8-15-17, 7-24-25 ve bunların katları olan üçgenler soru çözdürür."},
    {"card_number": 6, "title": "30-60-90 Özel Dik Üçgeni", "body": "30 derecenin karşısı x ise; 90 derecenin karşısı 2x, 60 derecenin karşısı x.kök(3) olur."},
    {"card_number": 7, "title": "45-45-90 İkizkenar Dik Üçgen", "body": "Dik kenarlar x ise hipotenüs kenarların kök(2) katıdır (x.kök(2))."},
    {"card_number": 8, "title": "Öklid Bağıntıları (Dikine Dik)", "body": "Dik açıdan dik inildiğinde yükseklik h^2 = p . k ; kenarlar b^2 = k . a dır."},
    {"card_number": 9, "title": "Muhteşem Üçlü Kuralı", "body": "Bir dik üçgende hipotenüse ait kenarortay uzunluğu, hipotenüste böldüğü parçaların uzunluğuna eşittir."},
    {"card_number": 10, "title": "Üçgende Alan Formülü", "body": "Üçgenin Alanı = (Taban x O Taban Ait Yükseklik) / 2 veya Sinüslü Alan = 1/2 . a . b . sin(C)."}
  ],
  "topic-geo-dortgenler": [
    {"card_number": 1, "title": "Dörtgenin İç Açıları Toplamı", "body": "Bütün konveks dörtgenlerin iç açıları toplamı 360 derece, dış açıları toplamı 360 derecedir."},
    {"card_number": 2, "title": "Paralelkenar Özellikleri", "body": "Karşılıklı kenarları paralel ve eşittir. Karşılıklı açılar eşit, komşu açılar toplamı 180 derecedir. Köşegenler birbirini ortalar."},
    {"card_number": 3, "title": "Eşkenar Dörtgen Özellikleri", "body": "Tüm kenarları eşittir. KÖŞEGENLER DİK KESİŞİR ve açıortaydır. Alan = (e . f) / 2 (Köşegenler çarpımının yarısı)."},
    {"card_number": 4, "title": "Dikdörtgen Özellikleri", "body": "Açıları 90'ar derece olan paralelkenardır. Köşegen uzunlukları birbirine eşittir (e = f). Alan = a . b."},
    {"card_number": 5, "title": "Kare Özellikleri", "body": "Tüm kenarları eşit, açıları 90 derece olan düzgün dörtgendir. Köşegenler eşit, dik kesişir ve 45 derecelik açıortaydır."},
    {"card_number": 6, "title": "Yamuk (Trapez) ve Orta Taban", "body": "Alt ve üst tabanı paralel olan dörtgendir. Orta Taban = (Alt Taban + Üst Taban) / 2. Alan = Orta Taban x Yükseklik."},
    {"card_number": 7, "title": "İkizkenar Yamuk Özellikleri", "body": "Paralel olmayan yan kenarları eşit olan yamuktur. Taban açıları eşittir ve köşegen uzunlukları birbirine eşittir."},
    {"card_number": 8, "title": "Deltoid Özellikleri", "body": "Tabanları ortak iki ikizkenar üçgenin birleşimidir. KÖŞEGENLER DİK KESİŞİR ve simetri köşegeni açıortaydır."},
    {"card_number": 9, "title": "Çokgenlerin İç Açıları Toplamı", "body": "n kenarlı bir çokgenin iç açıları toplamı (n - 2) . 180 derece formülüyle bulunur."},
    {"card_number": 10, "title": "Düzgün Beşgen ve Altıgen Açısı", "body": "Düzgün beşgenin bir iç açısı 108 derece; Düzgün altıgenin bir iç açısı 120 derecedir (Dış açı = 360 / n)."}
  ],
  "topic-geo-cember": [
    {"card_number": 1, "title": "Çember Çevresi ve Daire Alanı", "body": "Yarıçapı r olan çemberin Çevresi = 2.pi.r ; Dairenin Alanı = pi.r^2 formülü ile hesaplanır."},
    {"card_number": 2, "title": "Merkez Açı Özelliği", "body": "Köşesi çemberin merkezinde olan açıdır. Merkez açının ölçüsü gördüğü yayın derece ölçüsüne BİREBİR EŞİTTİR."},
    {"card_number": 3, "title": "Çevre Açı Özelliği", "body": "Köşesi çember üzerinde olan açıdır. Çevre açının ölçüsü gördüğü yayın derece ölçüsünün YARISINA eşittir."},
    {"card_number": 4, "title": "Çapı Gören Çevre Açı 90 Derecedir", "body": "Çemberde çapı gören çevre açının ölçüsü daima 90 derecedir (Dik açıdır)."},
    {"card_number": 5, "title": "Aynı Yayı Gören Açıların Eşitliği", "body": "Çemberde aynı yayı gören çevre açıların ölçüleri birbirine eşittir."},
    {"card_number": 6, "title": "Teğet - Yarıçap Dikliği", "body": "Çemberin merkezinden teğetin değme noktasına çizilen yarıçap teğete DAİMA DİKTİR (90 derece)."},
    {"card_number": 7, "title": "Dışarıdaki Noktadan Çizilen Teğetler", "body": "Çemberin dışındaki bir noktadan çembere çizilen iki teğet parçasının uzunlukları birbirine eşittir."},
    {"card_number": 8, "title": "Kirişler Dörtgeni Özelliği", "body": "Köşeleri çember üzerinde olan dörtgenlerde karşılıklı açıların toplamı 180 derecedir (A + C = 180)."},
    {"card_number": 9, "title": "Daire Diliminin Alanı", "body": "a derecelik açının gördüğü daire diliminin alanı = (pi . r^2) . (a / 360) formülüyle bulunur."},
    {"card_number": 10, "title": "Kirişe İnen Dikme Kuralı", "body": "Çemberin merkezinden kirişe inilen dikme, kirişi ve kirişin yayını iki eşit parçaya böler."}
  ],
  "topic-geo-kati-cisimler": [
    {"card_number": 1, "title": "Prizmalarda Hacim Genel Formülü", "body": "Bütün dik prizmaların Hacmi = Taban Alanı x Yükseklik (V = T.A . h) formülü ile hesaplanır."},
    {"card_number": 2, "title": "Dikdörtgenler Prizması", "body": "Hacim = a . b . c ; Yüzey Alanı = 2(ab + bc + ac) ; Cismin Köşegeni = kök(a^2 + b^2 + c^2)."},
    {"card_number": 3, "title": "Küp Özellikleri ve Hacmi", "body": "Tüm kenarları a olan küpün Hacmi = a^3 ; Yüzey Alanı = 6.a^2 ; Cisim Köşegeni = a.kök(3)'tür."},
    {"card_number": 4, "title": "Silindirin Hacmi ve Alanı", "body": "Yarıçapı r, yüksekliği h olan silindirin Hacmi = pi . r^2 . h ; Yanal Alanı = 2.pi.r.h dır."},
    {"card_number": 5, "title": "Piramit Hacim Formülü (1/3 Kuralı)", "body": "Piramitlerin Hacmi = (Taban Alanı x Yükseklik) / 3 (V = 1/3 . T.A . h) dır."},
    {"card_number": 6, "title": "Koninin Hacmi ve Yanal Alanı", "body": "Yarıçapı r, ana doğrusu l olan koninin Hacmi = (pi.r^2.h) / 3 ; Yanal Alanı = pi . r . l dır."},
    {"card_number": 7, "title": "Kürenin Hacmi Formülü", "body": "Yarıçapı R olan kürenin Hacmi = (4/3) . pi . R^3 formülü ile hesaplanır."},
    {"card_number": 8, "title": "Kürenin Yüzey Alanı Formülü", "body": "Yarıçapı R olan kürenin Yüzey Alanı = 4 . pi . R^2 formülü ile bulunur."},
    {"card_number": 9, "title": "Benzerlik Oranının Hacme Etkisi", "body": "İki benzer katı cismin alanları oranı benzerlik oranının karesi (k^2); HACİMLERİ ORANI ise benzerlik oranının KÜPÜDÜR (k^3)."},
    {"card_number": 10, "title": "Silindir Açınımı Yanal Yüzey", "body": "Dik silindir açıldığında yanal yüzeyi bir dikdörtgen olur. Dikdörtgenin kenarları 2.pi.r ve h'dir."}
  ]
}

def export_all_math_flashcards():
    base_dir = os.path.join("assets", "data", "topics", "matematik")
    os.makedirs(base_dir, exist_ok=True)
    
    total_cards = 0
    for topic_id, cards in math_flashcard_database.items():
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

    print(f"\n[BAŞARILI] MATEMATİK & GEOMETRİ DERSİNİN TÜM 21 ALT KONUSUNA AİT TOPLAM {total_cards} FLASHCARD ENTEGRE EDİLDİ!")

if __name__ == "__main__":
    export_all_math_flashcards()
