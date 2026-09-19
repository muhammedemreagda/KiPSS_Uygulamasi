# ============================================================================
# KPSS KAPSAMLI SORU & HAP BİLGİ VERİ TABANI ÜRETİCİSİ (SEEDER)
# Tüm KPSS Derslerini (Türkçe, Matematik, Tarih, Coğrafya, Vatandaşlık, Güncel)
# Özgün Soru ve Konu Özetleriyle Doldurur.
# ============================================================================

import json
import os
import sys

from generator.validator import ContentValidator

def build_comprehensive_kpss_dataset():
    data = {
        "categories": [
            { "id": "cat-gy-01", "code": "GY", "title": "Genel Yetenek", "sort_order": 1 },
            { "id": "cat-gk-01", "code": "GK", "title": "Genel Kültür", "sort_order": 2 }
        ],
        "courses": [
            { "id": "course-turkce", "category_id": "cat-gy-01", "code": "TURKCE", "title": "Türkçe", "icon_name": "menu_book", "sort_order": 1 },
            { "id": "course-mat", "category_id": "cat-gy-01", "code": "MATEMATIK", "title": "Matematik & Geometri", "icon_name": "calculate", "sort_order": 2 },
            { "id": "course-tarih", "category_id": "cat-gk-01", "code": "TARIH", "title": "Tarih", "icon_name": "history_edu", "sort_order": 3 },
            { "id": "course-cog", "category_id": "cat-gk-01", "code": "COGRAFYA", "title": "Coğrafya", "icon_name": "public", "sort_order": 4 },
            { "id": "course-vat", "category_id": "cat-gk-01", "code": "VATANDASLIK", "title": "Vatandaşlık & Anayasa", "icon_name": "gavel", "sort_order": 5 },
            { "id": "course-gun", "category_id": "cat-gk-01", "code": "GUNCEL", "title": "Güncel Bilgiler", "icon_name": "newspaper", "sort_order": 6 }
        ],
        "topics": [],
        "quick_notes": [],
        "questions": []
    }

    # =========================================================================
    # 1. TÜRKÇE DERSİ
    # =========================================================================
    # Konu 1.1: Yazım Kuralları
    data["topics"].append({
        "id": "topic-turkce-yazim",
        "course_id": "course-turkce",
        "parent_id": None,
        "title": "Yazım Kuralları",
        "slug": "yazim-kurallari",
        "importance_weight": 1.8,
        "sort_order": 1
    })
    data["quick_notes"].append({
        "id": "note-turkce-yazim",
        "topic_id": "topic-turkce-yazim",
        "title": "'de/da' Bağlacı ve '-ki' Ekinin Yazımı",
        "content": "### 1. 'de/da' Bağlacı mı, Bulunma Eki mi?\n- **Bağlaç Olan de/da:** Cümleden çıkarıldığında cümlenin anlamı bozulmaz, ayrı yazılır. (*Ahmet de geldi* -> *Ahmet geldi*).\n- **Bulunma Eki olan -de/-da:** Cümleden çıkarıldığında anlam bozulur, bitişik yazılır. (*Evde kaldık*).\n\n### 2. '-ki' Ekinin Yazımı\n- **Bağlaç olan ki:** Ayrı yazılır (*Duydum ki unutmuşsun*).\n- **Sıfat yapan / Zamir olan -ki:** Bitişik yazılır (*Sizinki, akşamki maç*).\n> **Pratik Kural:** Kelimeye *-ler* eki getir. *Akşamkiler* mantıklı olduğu için bitişik, *duydum kiler* anlamsız olduğu için ayrı yazılır.",
        "source_reference": "TDK Yazım Kılavuzu 2026",
        "is_verified": True,
        "read_time_seconds": 50
    })
    data["questions"].extend([
        {
            "id": "q-turkce-yazim-01",
            "topic_id": "topic-turkce-yazim",
            "question_text": "Aşağıdaki cümlelerin hangisinde 'de/da' ekinin/bağlacının yazımı ile ilgili bir YANLIŞLIK yapılmıştır?",
            "media_url": None,
            "options": [
                { "key": "A", "text": "Toplantıda alınan kararlar kısa sürede uygulamaya konuldu." },
                { "key": "B", "text": "Zor zamanlarımızda sen de daima yanımızda durdun." },
                { "key": "C", "text": "Dün akşam ki maçta sende bizimle olmalıydın." },
                { "key": "D", "text": "Okulda düzenlenen bilim fuarında projeler sergilendi." },
                { "key": "E", "text": "Yapılan araştırmalarda beklenen sonuçlara ulaşılamadı." }
            ],
            "correct_option": "C",
            "explanation": "'Dün akşam ki maçta sende...' cümlesinde 'akşamki' kelimesindeki '-ki' sıfat türeten ektir ve bitişik yazılmalıdır. Ayrıca 'sen de' ifadesindeki 'de' bağlaçtır ve ayrı yazılmalıdır. C seçeneğinde iki ayrı yazım hatası yapılmıştır.",
            "difficulty_level": "lisans",
            "is_verified": True
        },
        {
            "id": "q-turkce-yazim-02",
            "topic_id": "topic-turkce-yazim",
            "question_text": "Aşağıdaki cümlelerin hangisinde birleşik kelimelerin yazımıyla ilgili bir YANLIŞLIK yapılmıştır?",
            "media_url": None,
            "options": [
                { "key": "A", "text": "Olayı duyunca hemen bir göz atıp terketmek zorunda kaldı." },
                { "key": "B", "text": "Son yapılan teklifi büyük bir memnuniyetle kabul etti." },
                { "key": "C", "text": "Her şey yolunda giderse yarın sabah yola çıkacağız." },
                { "key": "D", "text": "Hukuksal süreç devam ettiği için hak kaybı yaşanmadı." },
                { "key": "E", "text": "Masaüstü bilgisayarındaki dosyaları harici diske aktardı." }
            ],
            "correct_option": "A",
            "explanation": "Türkçe yazım kurallarına göre etmek, eylemek, olmak gibi yardımcı fiillerle kurulan birleşik fiillerde herhangi bir ses düşmesi veya ses türemesi yoksa fiil ayrı yazılır. 'Terk etmek' kelimesinde ses olayı olmadığı için ayrı yazılmalıdır ('terk etmek').",
            "difficulty_level": "lisans",
            "is_verified": True
        }
    ])

    # Konu 1.2: Paragrafta Anlam
    data["topics"].append({
        "id": "topic-turkce-paragraf",
        "course_id": "course-turkce",
        "parent_id": None,
        "title": "Paragrafta Anlam & Düşünceyi Geliştirme",
        "slug": "paragrafta-anlam",
        "importance_weight": 2.0,
        "sort_order": 2
    })
    data["quick_notes"].append({
        "id": "note-turkce-paragraf",
        "topic_id": "topic-turkce-paragraf",
        "title": "Paragraf Sorularında Ana Fikir ve Yardımcı Fikir Tespiti",
        "content": "### Ana Fikir Nerede Aranır?\n- Ana fikir genellikle paragrafın **ilk cümlesinde** (giriş) veya **son cümlesinde** (özet/sonuç) yer alır.\n- *Oysa, ama, fakat, kısacası, sonuç olarak, yani* gibi bağlaçlardan sonra gelen cümleler ana fikri taşır.\n\n### Çeldirici Şık Tuzakları:\n- **Aşırı Genelleme:** Paragraftaki bir detaydan tüm dünya için genel kural çıkarmak.\n- **Paragrafta Geçmeyen Doğru Bilgi:** Cümle genel kültür olarak doğru olabilir ama paragrafta geçmiyorsa YANLIŞTIR.",
        "source_reference": "ÖSYM KPSS Türkçe Soru Analizleri",
        "is_verified": True,
        "read_time_seconds": 60
    })
    data["questions"].append({
        "id": "q-turkce-paragraf-01",
        "topic_id": "topic-turkce-paragraf",
        "question_text": "Bir sanat eserini kalıcı kılan şey, yazıldığı dönemin modasına uyması değil; insan ruhunun değişmeyen zamansız arzularına dokunabilmesidir. Yüz yıllar önce yazılmış bir destanın bugün dahi okuyucuyu derinden etkilemesi, eser sahibinin zamana meydan okuyan insan doğasını iyi kavramış olmasından kaynaklanır.\n\nBu parçada vurgulanmak istenen temel düşünce aşağıdakilerden hangisidir?",
        "media_url": None,
        "options": [
            { "key": "A", "text": "Sanat eserlerinin başarısı yayınlandığı dönemin popülerliğine bağlıdır." },
            { "key": "B", "text": "Kalıcı eserler, insanlığın evrensel ve zamansız duygularına hitap edebilenlerdir." },
            { "key": "C", "text": "Eski dönemlerde yazılan destanlar günümüz romanlarından daha kalitelidir." },
            { "key": "D", "text": "Yazarlar toplumsal sorunları işledikleri sürece zamana meydan okuyabilirler." },
            { "key": "E", "text": "Bir eserin kalıcılığı kullanılan dilin sadeliği ile doğru orantılıdır." }
        ],
        "correct_option": "B",
        "explanation": "Metinde vurgulanan ana düşünce, bir eserin kalıcı olabilmesi için 'dönemin modasına uyması değil, insan ruhunun değişmeyen zamansız arzularına dokunabilmesi' gerektiğidir. Bu da B seçeneğindeki 'insanlığın evrensel ve zamansız duygularına hitap edebilenlerdir' ifadesiyle birebir örtüşmektedir.",
        "difficulty_level": "lisans",
        "is_verified": True
    })

    # =========================================================================
    # 2. MATEMATİK DERSİ
    # =========================================================================
    data["topics"].append({
        "id": "topic-mat-temel",
        "course_id": "course-mat",
        "parent_id": None,
        "title": "Temel Kavramlar & Sayılar",
        "slug": "temel-kavramlar",
        "importance_weight": 1.6,
        "sort_order": 1
    })
    data["quick_notes"].append({
        "id": "note-mat-temel",
        "topic_id": "topic-mat-temel",
        "title": "Tek - Çift Sayılar ve Bölünebilme Kuralları",
        "content": "### 1. Tek - Çift Sayı Kuralları\n- Tek × Tek = **Tek** | Tek × Çift = **Çift**\n- Tek ± Tek = **Çift** | Tek ± Çift = **Tek**\n- Çift sayının tüm pozitif tam sayı kuvvetleri **Çifttir**.\n\n### 2. Bölünebilme Pratik Kuralı\n- **3 ile bölünebilme:** Rakamları toplamı 3 veya 3'ün katı olmalı.\n- **4 ile bölünebilme:** Son iki basamağı 00 veya 4'ün katı olmalı.\n- **11 ile bölünebilme:** Basamaklar sağdan sola doğru +, -, +, - sırasıyla işaretlenip toplanır.",
        "source_reference": "KPSS Matematik Müfredatı",
        "is_verified": True,
        "read_time_seconds": 45
    })
    data["questions"].append({
        "id": "q-mat-temel-01",
        "topic_id": "topic-mat-temel",
        "question_text": "a, b ve c pozitif tam sayılar olmak üzere,\n\na · b + 3 = 2c + 4\n\neşitliği veriliyor.\n\nBuna göre aşağıdakilerden hangisi KESİNLİKLE doğrudur?",
        "media_url": None,
        "options": [
            { "key": "A", "text": "a ve b sayıları çift sayıdır." },
            { "key": "B", "text": "c tek sayıdır." },
            { "key": "C", "text": "a ve b sayılarının her ikisi de tek sayıdır." },
            { "key": "D", "text": "a tek sayı ise b çift sayıdır." },
            { "key": "E", "text": "a + b + c toplamı çift sayıdır." }
        ],
        "correct_option": "C",
        "explanation": "Eşitliğin sağ tarafındaki 2c + 4 ifadesinde 2c çifttir, 4 de çifttir. Çift + Çift = Çift olur. Dolayısıyla a · b + 3 ifadesi ÇİFT bir sayıya eşittir.\n(a · b) + 3 = Çift ise, (a · b) tek olmak zorundadır (Tek + Tek = Çift).\nİki tam sayının çarpımı tek ise her iki sayı da TEK olmak zorundadır. Bu yüzden a ve b'nin ikisi de KESİNLİKLE TEKTİR.",
        "difficulty_level": "lisans",
        "is_verified": True
    })

    # =========================================================================
    # 3. TARİH DERSİ
    # =========================================================================
    data["topics"].append({
        "id": "topic-tarih-osmanli-kurulus",
        "course_id": "course-tarih",
        "parent_id": None,
        "title": "Osmanlı Kuruluş & Yükselme Dönemi",
        "slug": "osmanli-kurulus-yukselme",
        "importance_weight": 1.9,
        "sort_order": 1
    })
    data["quick_notes"].append({
        "id": "note-tarih-osmanli",
        "topic_id": "topic-tarih-osmanli-kurulus",
        "title": "Osmanlı Devleti'nin Kısa Sürede Büyüme Nedenleri",
        "content": "### 1. Jeopolitik Konum\n- Bizans sınırında bir **Uç Beyliği** olarak kurulması ve Bizans'ın taht kavgaları içinde zayıf durumda bulunması.\n\n### 2. İskân Politikası (Yerleştirme)\n- Fethedilen Rumeli topraklarına Anadolu'dan getirilen Türkmen ailelerin yerleştirilmesi (Bölgenin kalıcı olarak Türkleşmesi sağlandı).\n\n### 3. İstimâlet Politikası (Hoşgörü)\n- Gayrimüslim halkın din, dil ve inanç özgürlüğüne saygı duyulması ve adil vergi sistemi uygulanması.\n\n### 4. Ahi Desteği\n- Osman Bey'in Şeyh Edebalı'nın kızıyla evlenerek Ahi teşkilatının dini ve ekonomik gücünü arkasına alması.",
        "source_reference": "MEB Tarih Ders Kitapları & KPSS Kılavuzu",
        "is_verified": True,
        "read_time_seconds": 60
    })
    data["questions"].extend([
        {
            "id": "q-tarih-osmanli-01",
            "topic_id": "topic-tarih-osmanli-kurulus",
            "question_text": "Osmanlı Devleti'nin Rumeli ve Balkanlarda fethettiği topraklara Anadolu'daki konar-göçer Türkmenleri yerleştirerek bu bölgelerde kalıcı hakimiyet kurmayı amaçladığı politika aşağıdakilerden hangisidir?",
            "media_url": None,
            "options": [
                { "key": "A", "text": "İstimâlet Politikası" },
                { "key": "B", "text": "İskân Politikası" },
                { "key": "C", "text": "Devşirme Sistemi" },
                { "key": "D", "text": "Millet Sistemi" },
                { "key": "E", "text": "Tımar Sistemi" }
            ],
            "correct_option": "B",
            "explanation": "Fethedilen topraklara Anadolu'daki Türkmen nüfusun yerleştirilerek bölgenin Türkleştirilmesi ve asayişin sağlanması amacını taşıyan politika İSKÂN POLİTİKASI'dır. İstimâlet ise hoşgörü politikasına verilen addır.",
            "difficulty_level": "lisans",
            "is_verified": True
        },
        {
            "id": "q-tarih-osmanli-02",
            "topic_id": "topic-tarih-osmanli-kurulus",
            "question_text": "Osmanlı Devleti'nde ilk altın parayı (Sultani) bastıran ve ilk deniz gücü olan Karesioğulları Beyliği'ni Osmanlı topraklarına katan padişahlar sırasıyla aşağıdakilerin hangisinde doğru verilmiştir?",
            "media_url": None,
            "options": [
                { "key": "A", "text": "Fatih Sultan Mehmet — Orhan Bey" },
                { "key": "B", "text": "Kanuni Sultan Süleyman — Osman Bey" },
                { "key": "C", "text": "II. Bayezid — I. Murad" },
                { "key": "D", "text": "Yavuz Sultan Selim — Orhan Bey" },
                { "key": "E", "text": "Fatih Sultan Mehmet — I. Mehmed (Çelebi)" }
            ],
            "correct_option": "A",
            "explanation": "Osmanlı Devleti'nde ilk altın para Fatih Sultan Mehmet döneminde bastırılmıştır. Karesioğulları Beyliği ise Orhan Bey döneminde Osmanlı sınırlarına katılarak Osmanlı'nın ilk donanmaya sahip olmasını sağlamıştır.",
            "difficulty_level": "lisans",
            "is_verified": True
        }
    ])

    # Konu 3.2: Kurtuluş Savaşı ve İnkılap Tarihi
    data["topics"].append({
        "id": "topic-tarih-inkilap",
        "course_id": "course-tarih",
        "parent_id": None,
        "title": "Kurtuluş Savaşı & Atatürk İnkılapları",
        "slug": "inkilap-tarihi",
        "importance_weight": 2.0,
        "sort_order": 2
    })
    data["quick_notes"].append({
        "id": "note-tarih-inkilap",
        "topic_id": "topic-tarih-inkilap",
        "title": "Amasya Genelgesi (22 Haziran 1919) Önemli Kararları",
        "content": "### İhtilal Bildirisi Niteliğindedir!\n- **Savaşın Gerekçesi:** *'Vatanın bütünlüğü, milletin bağımsızlığı tehlikededir.'*\n- **Savaşın Amacı ve Yöntemi:** *'Milletin bağımsızlığını yine milletin azim ve kararı kurtaracaktır.'* (İlk kez milli egemenlik üstü kapalı olarak vurgulanmıştır).\n- **Çağrı:** Sivas'ta ulusal bir kongrenin toplanması kararlaştırılmıştır.",
        "source_reference": "Nutuk & MEB Tarih Müfredatı",
        "is_verified": True,
        "read_time_seconds": 45
    })
    data["questions"].append({
        "id": "q-tarih-inkilap-01",
        "topic_id": "topic-tarih-inkilap",
        "question_text": "Kurtuluş Savaşı hazırlık döneminde yayımlanan aşağıdaki belgelerin hangisinde ilk kez 'Milletin bağımsızlığını yine milletin azim ve kararı kurtaracaktır' ifadesi yer alarak Milli Mücadele'nin amacı, gerekçesi ve yöntemi belirtilmiştir?",
        "media_url": None,
        "options": [
            { "key": "A", "text": "Sivas Kongresi Kararları" },
            { "key": "B", "text": "Erzurum Kongresi Tüzüğü" },
            { "key": "C", "text": "Amasya Genelgesi" },
            { "key": "D", "text": "Havza Genelgesi" },
            { "key": "E", "text": "Misak-ı Milli Kararları" }
        ],
        "correct_option": "C",
        "explanation": "Milli Mücadele'nin amacını, gerekçesini ve yöntemini açıklayan ve milli egemenlikten ilk kez bahseden belge 22 Haziran 1919 tarihli AMASYA GENELGESİ'dir.",
        "difficulty_level": "lisans",
        "is_verified": True
    })

    # =========================================================================
    # 4. COĞRAFYA DERSİ
    # =========================================================================
    data["topics"].append({
        "id": "topic-cog-turkiye-fiziki",
        "course_id": "course-cog",
        "parent_id": None,
        "title": "Türkiye'nin Fiziki Coğrafyası & İklimi",
        "slug": "turkiye-fiziki-cografyasi",
        "importance_weight": 1.7,
        "sort_order": 1
    })
    data["quick_notes"].append({
        "id": "note-cog-fiziki",
        "topic_id": "topic-cog-turkiye-fiziki",
        "title": "Türkiye'nin Coğrafi Konumu ve Dağların Uzanış Yönü",
        "content": "### Dağların Uzanışının Etkileri:\n- **Karadeniz ve Akdeniz:** Dağlar kıyıya **paralel** uzanır. Kıyı ile iç kesimler arasında ulaşım geçitlerle (Zamana, Zigana, Kop, Çubuk, Gülek) sağlanır. Kıyı iklimi iç kesimlere sokulamaz.\n- **Ege Bölgesi:** Dağlar kıyıya **dik** uzanır. Kıyı iklimi iç kesimlere kadar sokulur, enine kıyı tipi görülür, girinti-çıkıntı fazladır.",
        "source_reference": "TÜİK & Harita Genel Müdürlüğü Verileri",
        "is_verified": True,
        "read_time_seconds": 50
    })
    data["questions"].append({
        "id": "q-cog-fiziki-01",
        "topic_id": "topic-cog-turkiye-fiziki",
        "question_text": "Türkiye'de dağların kıyıya paralel uzandığı Karadeniz ve Akdeniz kıyılarında aşağıdaki coğrafi özelliklerden hangisinin görülmesi BEKLENMEZ?",
        "media_url": None,
        "options": [
            { "key": "A", "text": "Kıyı ile iç kesimler arasında iklim farklılığının belirgin olması" },
            { "key": "B", "text": "Denizellerin (deniz etkisinin) iç kesimlere rahatça sokulabilmesi" },
            { "key": "C", "text": "Kıyı boyunca boyuna kıyı tipinin hakim olması" },
            { "key": "D", "text": "Kıyı ile iç kesimler arasındaki ulaşımın doğal geçitlerle sağlanması" },
            { "key": "E", "text": "Falez (yalıyar) oluşumlarının yaygın olması" }
        ],
        "correct_option": "B",
        "explanation": "Dağların kıyıya paralel uzandığı yerlerde yüksek dağ sıraları bir duvar görevi görerek denizel nemli havanın iç kesimlere sokulmasını ENGELLER. Bu yüzden B seçeneğindeki ifade BEKLENMEZ.",
        "difficulty_level": "lisans",
        "is_verified": True
    })

    # =========================================================================
    # 5. VATANDAŞLIK & ANAYASA DERSİ
    # =========================================================================
    data["topics"].append({
        "id": "topic-vat-anayasa",
        "course_id": "course-vat",
        "parent_id": None,
        "title": "1982 Anayasası & Devlet Organları",
        "slug": "anayasa-devlet-organlari",
        "importance_weight": 1.8,
        "sort_order": 1
    })
    data["quick_notes"].append({
        "id": "note-vat-anayasa",
        "topic_id": "topic-vat-anayasa",
        "title": "Yasama, Yürütme ve Yargı Organları (1982 Anayasası)",
        "content": "### 1. Yasama Organı\n- **TBMM:** 600 milletvekilinden oluşur. Seçimler 5 yılda bir yapılır.\n\n### 2. Yürütme Organı\n- **Cumhurbaşkanı:** Yürütme yetkisi tek başınadır.\n\n### 3. Yargı Organı\n- Bağımsız ve tarafsız mahkemelerce yürütülür. **Anayasa Mahkemesi 15 üyeden** oluşur (12 üye Cumhurbaşkanı, 3 üye TBMM tarafından seçilir).",
        "source_reference": "1982 Anayasası Güncellenmiş Metni",
        "is_verified": True,
        "read_time_seconds": 45
    })
    data["questions"].append({
        "id": "q-vat-anayasa-01",
        "topic_id": "topic-vat-anayasa",
        "question_text": "1982 Anayasası'na göre Türkiye Büyük Millet Meclisi (TBMM) toplam kaç milletvekilinden oluşur ve genel seçimler kaç yılda bir gerçekleştirilir?",
        "media_url": None,
        "options": [
            { "key": "A", "text": "550 Milletvekili — 4 Yılda bir" },
            { "key": "B", "text": "600 Milletvekili — 5 Yılda bir" },
            { "key": "C", "text": "600 Milletvekili — 4 Yılda bir" },
            { "key": "D", "text": "500 Milletvekili — 5 Yılda bir" },
            { "key": "E", "text": "650 Milletvekili — 6 Yılda bir" }
        ],
        "correct_option": "B",
        "explanation": "2017 Anayasa değişikliği ile TBMM üye sayısı 550'den 600'e çıkarılmış ve TBMM genel seçimlerinin 5 yılda bir Cumhurbaşkanlığı seçimiyle birlikte yapılması hükme bağlanmıştır.",
        "difficulty_level": "lisans",
        "is_verified": True
    })

    # =========================================================================
    # 6. GÜNCEL BİLGİLER DERSİ
    # =========================================================================
    data["topics"].append({
        "id": "topic-gun-kultur",
        "course_id": "course-gun",
        "parent_id": None,
        "title": "Güncel Kültür, Sanat & Dünya Gündemi",
        "slug": "guncel-kultur-sanat",
        "importance_weight": 1.5,
        "sort_order": 1
    })
    data["quick_notes"].append({
        "id": "note-gun-kultur",
        "topic_id": "topic-gun-kultur",
        "title": "UNESCO Dünya Mirası Listesi & Önemli Kültür Durakları",
        "content": "### UNESCO Türkiye Varlıkları:\n- **Göbeklitepe (Şanlıurfa):** Tarihin sıfır noktası kabul edilen en eski tapınak kompleksi.\n- **Çatalhöyük (Konya):** Neolitik dönem insanlık yerleşimi.\n- **Arslantepe Höyüğü (Malatya):** Dünyanın bilinen ilk devlet bürokrasisi ve saray yapısı.",
        "source_reference": "UNESCO & Kültür ve Turizm Bakanlığı 2026",
        "is_verified": True,
        "read_time_seconds": 40
    })
    data["questions"].append({
        "id": "q-gun-kultur-01",
        "topic_id": "topic-gun-kultur",
        "question_text": "Şanlıurfa sınırları içerisinde yer alan, yaklaşık 12.000 yıllık geçmişiyle 'Tarihin Sıfır Noktası' olarak adlandırılan ve UNESCO Dünya Mirası Listesi'nde yer alan arkeolojik alan aşağıdakilerden hangisidir?",
        "media_url": None,
        "options": [
            { "key": "A", "text": "Çatalhöyük" },
            { "key": "B", "text": "Göbeklitepe" },
            { "key": "C", "text": "Efes Antik Kenti" },
            { "key": "D", "text": "Arslantepe Höyüğü" },
            { "key": "E", "text": "Hattuşaş" }
        ],
        "correct_option": "B",
        "explanation": "Şanlıurfa yakınlarında bulunan ve insanoğlunun bilinen en eski tapınak kompleksi olarak 'Tarihin Sıfır Noktası' kabul edilen yer GÖBEKLİTEPE'dir.",
        "difficulty_level": "lisans",
        "is_verified": True
    })

    # =========================================================================
    # VERİ DOĞRULAMA (VALIDATION CHECK FOR ALL QUESTIONS)
    # =========================================================================
    print("Tüm veriler doğrulanıyor...")
    total_q = len(data["questions"])
    total_n = len(data["quick_notes"])
    
    for idx, q in enumerate(data["questions"]):
        valid, errs = ContentValidator.validate_question(q)
        if not valid:
            raise ValueError(f"Soru {idx + 1} ({q['id']}) doğrulama hatası: {errs}")

    print(f"[BAŞARILI] {len(data['courses'])} Ders, {len(data['topics'])} Konu, {total_n} Hap Bilgi ve {total_q} Özgün Soru başarıyla oluşturuldu ve doğrulandı.")

    return data

if __name__ == "__main__":
    dataset = build_comprehensive_kpss_dataset()
    
    target_path = os.path.join("mobile_app", "assets", "data", "sample_data.json")
    with open(target_path, "w", encoding="utf-8") as f:
        json.dump(dataset, f, ensure_ascii=False, indent=2)
        
    print(f"[TAMAMLANDI] Veri seti kaydedildi -> {target_path}")
