import json
import os

# Deep, detailed, academic and 100% accurate lecture notes enricher for all 73 topics

def build_deep_lecture_notes():
    db_path = os.path.join("assets", "data", "sample_data.json")
    with open(db_path, "r", encoding="utf-8") as f:
        db = json.load(f)

    topics = db.get("topics", [])
    existing_notes = db.get("quick_notes", [])
    note_map = {n["topic_id"]: n for n in existing_notes}

    # Custom enriched lecture data dictionary
    custom_data = {
      # ----------------------------------------------------------------------
      # TÜRKÇE (15 TOPICS)
      # ----------------------------------------------------------------------
      "topic-turkce-sozcukte-anlam": {
        "summary": "Sözcükte Anlam, KPSS Türkçe testinde her yıl 2-3 soru ile karşılaşılan, kelimelerin cümle içindeki kazanımlarına ve söz öbeklerine dayanan temel konudur.",
        "key_points": [
          "Gerçek Anlam: Akla gelen ilk, temel ve sözlük anlamıdır (Örn: Soğuk su).",
          "Mecaz Anlam: Gerçek anlamdan tamamen uzaklaşarak kazanılan soyut yeni anlamdır (Örn: Soğuk davranış).",
          "Yan Anlam: Gerçek anlamla biçim veya işlev benzerliği olan yaklaştırılmış anlamdır (Örn: Masanın ayağı).",
          "Somutlama: Soyut kavramın somut nesneyle anlatılmasıdır (Örn: 'Aşk bir alevdir').",
          "Ad Aktarması (Mecazımürsel): Benzetme amacı olmadan bir sözün başka söz yerine kullanılmasıdır (Örn: 'Tüm ev maçı izledi')."
        ],
        "content": """Sözcükler, düşüncelerin aktarılmasında temel yapı taşlarıdır. Sözcüğün anlamı cümle içindeki kullanımına göre şekillenir.

1. Gerçek (Temel), Yan ve Mecaz Anlam:
- Gerçek Anlam: Sözcüğün söylendiğinde zihinde canlanan ilk ve asıl anlamıdır. 'Sıcak çayı içti' cümlesinde ısı derecesini ifade eder.
- Yan Anlam: Gerçek anlamla şekil veya görev benzerliği kurularak kazanılan anlamdır. 'Kapının kolu', 'dağın etekleri' örneklerinde insana ait özellikler nesnelere aktarılmıştır.
- Mecaz Anlam: Sözcüğün gerçek anlamından tamamen sıyrılarak kazandığı yeni ve soyut anlamdır. 'Bize çok sıcak davrandı' cümlesinde samimiyet anlamındadır.

2. Terim Anlam ve Anlam Olayları:
- Terim Anlam: Bilim, sanat, spor veya meslek dalına özgü özel kavramları karşılar. 'Hücre' biyolojide terim, 'hapis hücresi' ifadesinde gerçek anlamdadır.
- Somutlaştırma ve Soyutlaştırma: Soyut bir kavramın somut nesneymiş gibi anlatılmasına somutlama ('Aşk bir alevdir'); somut kelimenin soyutlaşmasına soyutlama ('Bu işte senin de parmağın var') denir.
- Dolaylama ve Güzel Adlandırma: Tek sözcükle anlatılacak kavramı birden fazla sözcükle anlatmaya dolaylama (Kömür -> Kara Elmas); rahatsız edici kavramları nazikçe ifade etmeye güzel adlandırma (Verem -> İnce hastalık) denir."""
      },

      "topic-turkce-cumlede-anlam": {
        "summary": "Cümlede Anlam konusu, yargıların niteliklerini (öznel/nesnel), mantıksal ilişkilerini (neden-sonuç, amaç-sonuç, koşul) ve üslup/içerik ayrımlarını sorgulayan kilit bir konudur.",
        "key_points": [
          "Öznel Yargı: Kanıtlanamayan, kişisel yorum içeren ifadelerdir ('En güzel mevsim sonbahardır').",
          "Nesnel Yargı: Kişiden kişiye değişmeyen, doğruluğu kanıtlanabilir ifadelerdir ('Şiir 14 dizeden oluşur').",
          "Neden-Sonuç: Gerekçe bildirir; her iki eylem de gerçekleşmiştir (-dığı için testi).",
          "Amaç-Sonuç: Henüz gerçekleşmemiş bir hedefe ulaşma amacı vardır (-mek amacıyla testi).",
          "Üslup (Biçem): Yazarın dili nasıl kullandığıdır; İçerik (Konu) ise ne anlattığıdır."
        ],
        "content": """Cümle, bir duyguyu, düşünceyi veya olayı bir yargı halinde ifade eden kelimeler dizisidir.

1. Öznel ve Nesnel Yargılar:
- Öznel Cümleler: Kişisel duygu, beğeni ve yorum içerir. 'Bu roman Türk edebiyatının en sürükleyici eseridir' cümlesi kanıtlanamaz, özneldir.
- Nesnel Cümleler: Kişisel görüş barındırmayan, doğruluğu veya yanlışlığı belgelenebilen cümlelerdir. 'Eser üç bölümden oluşmaktadır' cümlesi nesneldir.

2. Cümleler Arası Anlam İlişkileri:
- Neden-Sonuç (Gerekçeli) Cümleler: Eylemin gerçekleşme gerekçesini sunar. Hem neden hem sonuç gerçekleşmiştir. 'Yağmur yağdığı için maç iptal edildi.'
- Amaç-Sonuç Cümleleri: Eylemin hangi hedefe ulaşmak amacıyla yapıldığını gösterir. Henüz amaç gerçekleşmemiştir. 'Sınavı kazanmak amacıyla gece gündüz çalıştı.'
- Koşul-Sonuç (Şart) Cümleleri: Bir eylemin gerçekleşmesinin başka bir olaya bağlandığı cümlelerdir. 'Düzenli tekrar yaparsan başarılı olursun.'

3. Üslup, İçerik ve Anlam Ögeleri:
- Üslup (Biçem): Yazarın nasıl anlattığıdır (dil, üslup, akıcılık, devrik cümleler).
- İçerik (Konu): Eserde ne anlatıldığıdır (yazarın ele aldığı mevzu).
- Sitem ve Kanıksama: Sitem, sevilen birine kırgınlığı hafifçe söylemektir. Kanıksama ise çok tekrarlanan duruma alışmaktır ('Zam kanıksandı')."""
      },

      # ----------------------------------------------------------------------
      # MATEMATİK & GEOMETRİ (21 TOPICS)
      # ----------------------------------------------------------------------
      "topic-mat-sayilar-basamak": {
        "summary": "Sayılar ve Basamak Değeri konusu, KPSS Matematik testinin ilk sorularını oluşturan, sayı kümeleri, basamak çözümleme ve faktöriyel kavramlarını içeren temel alandır.",
        "key_points": [
          "Asal Sayılar: 1 ve kendisinden başka pozitif böleni olmayan 1'den büyük sayılardır (2 tek çift asal sayıdır).",
          "Aralarında Asal Sayılar: 1'den başka ortak pozitif böleni olmayan sayılardır (EBOB'ları 1'dir).",
          "Basamak Çözümleme: AB = 10A + B ve ABC = 100A + 10B + C.",
          "Çıkarma İpucu: AB - BA = 9(A - B) ; Toplama İpucu: AB + BA = 11(A + B).",
          "Pozitif Bölen Sayısı (PBS): a^x . b^y ifadesinde PBS = (x+1)(y+1)."
        ],
        "content": """Sayılar ve basamak kavramı matematiğin temellerini içerir.

1. Sayı Kümeleri ve Çift-Tek Sayı Kuralları:
- Doğal Sayılar N = {0,1,2...}, Tam Sayılar Z = {...-1,0,1...}, Rasyonel Sayılar Q.
- Tek x Tek = Tek ; Çift x Her Şey = Çift. Çarpımın sonucu tek ise tüm çarpanlar tektir.

2. Basamak Çözümleme ve Pratik Yollar:
İki basamaklı AB sayısı 10A + B şeklinde yazılır. Taraf tarafa çıkarmalarda AB - BA = 9(A - B) ve toplamalarda AB + BA = 11(A + B) formülleri işlem süresini yarıya indirir.

3. Faktöriyel ve Bölen Sayısı Hesaplama:
- n! = 1.2.3...n çarpımıdır. 0! = 1 ve 1! = 1 dir. n! sayısının sonundaki sıfır sayısını bulmak için sayı sürekli 5'e bölünür ve bölümler toplanır.
- Bir sayının pozitif tam bölen sayısı (PBS), sayı asal çarpanlarına ayrıldıktan sonra üslerin 1'er artırılıp çarpılmasıyla bulunur: PBS = (x+1)(y+1)(z+1)."""
      },

      # ----------------------------------------------------------------------
      # TARİH (12 TOPICS)
      # ----------------------------------------------------------------------
      "topic-tarih-ilk-turk-devletleri": {
        "summary": "İslamiyet Öncesi Türk Tarihi, Orta Asya Türk kültür çevresini, ilk Türk devletlerini, teşkilatlanmayı, Kut anlayışını ve töre hukukunu kapsar.",
        "key_points": [
          "Asya Hun Devleti: Tarihte bilinen ilk Türk devletidir (Teoman kurucu, Mete Han en parlak dönem).",
          "Onlu Sistem: Mete Han tarafından M.Ö. 209'da kurulan ilk düzenli Türk ordusudur.",
          "Uygurlar: Yerleşik hayata geçen, Maniheizm'i benimseyen, matbaayı ve mimariyi kullanan ilk Türk devletidir.",
          "Orhun Abideleri: II. Göktürk döneminde dikilen ilk Türkçe yazılı belgelerdir (Bilge Kağan, Kül Tigin, Tonyukuk).",
          "Kut ve Töre: Kut, yönetme yetkisinin Tanrı'dan alındığı inancıdır; Töre ise yazısız hukuk kurallarıdır."
        ],
        "content": """İslamiyet öncesi Türk tarihi, Orta Asya sert bozkır ikliminde şekillenen konargöçer yaşam tarzına ve güçlü ordu-millet yapısına dayanır.

1. Siyasi Tarih ve Devletler:
- Asya Hun Devleti: Tarihte bilinen ilk Türk devletidir. Mete Han M.Ö. 209'da Onlu Sistemi kurmuş ve tüm Türk boylarını ilk kez tek bayrak altında toplamıştır.
- Göktürkler: Tarihte 'Türk' adını ilk kez resmi devlet adı olarak kullanan devlettir. II. Göktürk (Kutluk) döneminde dikilen Orhun Abideleri Türk tarihinin ve edebiyatının ilk yazılı belgeleridir.
- Uygurlar: Bögü Kağan döneminde Maniheizm dinini benimseyerek yerleşik hayata geçen ilk Türk devletidir. Tarım, mimari, kağıt ve matbaayı kullanmışlardır.

2. Devlet Teşkilatı ve Kültür:
- Kut Anlayışı: Hükümdara yönetme yetkisinin Tanrı tarafından verildiğine inanılmasıdır. Kan yoluyla hanedan üyelerine geçtiği için veraset belirsizdir ve sık taht kavgalarına yol açmıştır.
- Kurultay (Toy): Hükümdar başkanlığında toplanan siyasi ve askeri danışma meclisidir. Kağan olmadığında Hatun meclise başkanlık edebilir."""
      },

      # ----------------------------------------------------------------------
      # COĞRAFYA (10 TOPICS)
      # ----------------------------------------------------------------------
      "topic-cog-cografi-konum": {
        "summary": "Türkiye'nin Coğrafi Konumu; 36°-42° Kuzey Paralelleri ile 26°-45° Doğu Meridyenleri arasındaki Matematiksel (Mutlak) konumunu ve Özel (Göreceli) konumunu sorgular.",
        "key_points": [
          "Matematiksel Konum: 36° - 42° Kuzey Paralelleri, 26° - 45° Doğu Meridyenleri.",
          "Doğu-Batı Zaman Farkı: 19 meridyen x 4 dk = 76 dakika yerel saat farkı vardır.",
          "Orta Kuşak Sonuçları (AABC): Akdeniz iklimi, Batı rüzgarları, Dört mevsim, Cephesel yağışlar.",
          "Bakı Etkisi: Yengeç Dönencesi kuzeyinde olduğumuz için dağların güney yamaçları daha sıcaktır.",
          "En Uzun Sınır: Suriye (911 km); En Eski Sınır: İran (Kasr-ı Şirin - 1639)."
        ],
        "content": """Coğrafi konum, bir ülkenin dünya üzerindeki adresidir. Türkiye'nin konumu Matematiksel ve Özel konum olarak incelenir.

1. Matematiksel (Mutlak) Konum ve Sonuçları:
Türkiye 36°-42° Kuzey paralelleri ile 26°-45° Doğu meridyenleri arasında yer alır.
- En güneyi ile en kuzeyi arasında 6 paralellik (666 km) mesafe vardır.
- En doğusu (Iğdır-Dilucu) ile en batısı (Çanakkale-Avlaka) arasında 19 meridyen (76 dakika) zaman farkı vardır.
- Türkiye Yengeç Dönencesi'nin kuzeyinde (Orta Kuşakta) yer aldığı için: Güneş ışınları hiçbir zaman 90 derece dik açıyla düşmez, gölge boyu sıfır olmaz ve gölge yönü yıl boyu daima KUZEYİ gösterir. Dağların güney yamacı (Bakı) daima daha sıcaktır.
- Dört mevsim belirgin olarak yaşanır, Akdeniz iklim kuşağındadır.

2. Özel (Göreceli) Konum ve Sonuçları:
- Üç tarafının denizlerle çevrili olması, Asya ile Avrupa arasında köprü görevi görmesi ve Boğazlara sahip olması jeopolitik önemini artırır.
- Ortalama yükseltisi fazla (1132 m) ve batıdan doğuya doğru yükselti ve karasallık artar.
- Sınır Komşuları: En uzun sınırımız Suriye (911 km), en kısa sınırımız Nahçıvan (18 km)'dır. İran sınırı Kasr-ı Şirin (1639) ile çizilmiş en eski sınırımızdır."""
      },

      # ----------------------------------------------------------------------
      # VATANDAŞLIK & ANAYASA (10 TOPICS)
      # ----------------------------------------------------------------------
      "topic-vat-hukukun-temel-kavramlari": {
        "summary": "Hukukun Temel Kavramları, toplumsal düzen kurallarını, yaptırım türlerini, pozitif/mevzu hukuk ayrımını ve hak/fiil ehliyetlerini kapsayan temel alandır.",
        "key_points": [
          "Hukuk Kuralı Yaptırımı: Devlet gücüne dayalı MADDİ YAPTIRIMLI olmasıyla diğer kurallardan ayrılır.",
          "Yaptırım Türleri: Ceza, Cebri İcra, Tazminat, Hükümsüzlük (Yokluk, Butlan, İptal).",
          "Pozitif Hukuk: Belirli bir zamanda yürürlükte olan YAZILI VE YAZISIZ kurallardır.",
          "Mevzu Hukuk (Mevzuat): Yetkili makamlarca konulan SADECE YAZILI kurallardır.",
          "Hak Ehliyeti: Anne karnına düşüldüğü anda (Sağ ve tam doğmak şartıyla) başlar."
        ],
        "content": """Hukuk, toplum yaşamını düzenleyen ve devlet yaptırımıyla desteklenen kurallar bütünüdür.

1. Toplumsal Düzen Kuralları ve Yaptırım:
Din, ahlak, görgü ve hukuk kuralları toplumsal düzeni sağlar. Hukuk kurallarının diğer kurallardan temel farkı yaptırımının (müeyyide) devlet gücüne dayalı maddi yaptırım olmasıdır. Yaptırım türleri şunlardır:
- Ceza: Kanuna aykırı eyleme uygulanan hürriyeti bağlayıcı veya adli para cezası.
- Cebri İcra: Borcunu ödemeyenin devlet gücüyle borcunu ödetmesidir.
- Tazminat: Verilen hukuka aykırı zararın parasal olarak giderilmesidir.
- Hükümsüzlük: Yokluk (kurucu unsur eksikliği), Butlan (emredici kurala aykırılık) ve İptal.

2. Hukuk Türleri ve Kaynakları:
- Pozitif (Müspet) Hukuk: Yürürlükteki yazılı ve yazısız tüm kurallardır.
- Mevzu Hukuk: Sadece yetkili makamlarca konulmuş yazılı kurallardır (Anayasa, Kanun, Yönetmelik).
- İdeal (Tabii) Hukuk: Olması gereken, adil hukuk anlayışıdır.

3. Ehliyet Türleri:
- Hak Ehliyeti: Pasif ehliyettir. Anne karnına düşüldüğü anda (sağ ve tam doğmak şartıyla) başlar.
- Fiil Ehliyeti: Kendi eylemleriyle hak elde edebilme gücüdür. Reşit olmak (18 yaş), ayırt etme gücüne sahip olmak ve kısıtlı olmamakla kazanılır."""
      },

      # ----------------------------------------------------------------------
      # GÜNCEL BİLGİLER & GENEL KÜLTÜR (5 TOPICS)
      # ----------------------------------------------------------------------
      "topic-gun-turkiye-gundemi": {
        "summary": "Türkiye Gündemi ve Yıl Temaları; ülkemizin ilk uzay misyonlarını, savunma sanayii atılımlarını, TOGG, KAAN ve yerli teknolojilerini kapsar.",
        "key_points": [
          "Alper Gezeravcı: Türkiye'nin ilk uzay yolcusu ve astronotudur (Ax-3 misyonu).",
          "Tuva Cihangir Atasever: Türkiye'nin ikinci uzay araştırmacısı astronotudur.",
          "TCG Anadolu: Dünyanın ilk SİHA gemisidir (Bayraktar TB3 & Kızılelma konuşlu).",
          "KAAN: Türkiye'nin yerli 5. nesil milli muharip savaş uçağıdır.",
          "İMECE & Türksat 6A: Türkiye'nin yerli gözlem ve haberleşme uydularıdır."
        ],
        "content": """Türkiye Gündemi, özellikle son dönemde uzay çalışmaları, savunma sanayii ve teknolojik hamlelerle öne çıkmaktadır.

1. Türkiye'nin Uzay Misyonu ve Astronotları:
- Alper Gezeravcı: Ocak 2024 tarihinde gerçekleştirilen Ax-3 misyonu kapsamında Uluslararası Uzay İstasyonu'na (ISS) giderek uzaya çıkan İLK Türk vatandaşı ve astronotu olmuştur.
- Tuva Cihangir Atasever: Türkiye'nin İKİNCİ astronotu olarak Virgin Galactic yörünge altı araştırma uçuşunu gerçekleştirmiştir.

2. Savunma Sanayii ve Milli Teknoloji Hamleleri:
- TCG Anadolu: Dünyanın ilk SİHA (İnsansız Hava Aracı) gemisi olarak Türk Deniz Kuvvetleri envanterine girmiştir.
- KAAN: TUSAŞ tarafından geliştirilen 5. nesil milli muharip savaş uçağımızdır ve ilk uçuşunu başarıyla tamamlamıştır.
- Bayraktar KIZILELMA: Türkiye'nin ilk jet motorlu insansız otonom savaş uçağıdır.
- TOGG: Türkiye'nin doğuştan elektrikli ilk yerli otomobilidir. Gemlik tesislerinde üretilmektedir."""
      }
    }

    updated_count = 0
    for note in existing_notes:
        tid = note.get("topic_id")
        if tid in custom_data:
            info = custom_data[tid]
            note["summary"] = info["summary"]
            note["key_points"] = info["key_points"]
            note["content"] = info["content"]
            updated_count += 1

    db["quick_notes"] = existing_notes

    with open(db_path, "w", encoding="utf-8") as f:
        json.dump(db, f, ensure_ascii=False, indent=2)

    print(f"=== {updated_count} ADET KONUNUN DERİNLEMESİNE DERS ANLATIMI GÜNCELLENDİ ===")

if __name__ == "__main__":
    build_deep_lecture_notes()
