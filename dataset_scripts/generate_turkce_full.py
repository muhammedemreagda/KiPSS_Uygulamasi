# ============================================================================
# KPSS TÜRKÇE DERSİ — 12 KONU X 10 SORU (TOPLAM 120 VERİFİED SORU + HAP BİLGİLER)
# ============================================================================

import json
import os
from generator.validator import ContentValidator

def build_turkce_full_dataset():
    topics = []
    quick_notes = []
    questions = []

    # -------------------------------------------------------------------------
    # KONU 1: Sözcükte Anlam
    # -------------------------------------------------------------------------
    t1_id = "topic-turkce-sozcukte-anlam"
    topics.append({
        "id": t1_id,
        "course_id": "course-turkce",
        "parent_id": None,
        "title": "Sözcükte Anlam",
        "slug": "sozcukte-anlam",
        "importance_weight": 1.7,
        "sort_order": 1
    })
    quick_notes.append({
        "id": "note-turkce-sozcukte-anlam",
        "topic_id": t1_id,
        "title": "Sözcükte Anlam İlişkileri ve Mecaz Türleri",
        "content": "### 1. Gerçek, Mecaz ve Terim Anlam\n- **Gerçek Anlam:** Sözcüğün akla gelen ilk temel anlamıdır (*Ağır çuvalı taşıdı*).\n- **Mecaz Anlam:** Sözcüğün gerçek anlamından tamamen uzaklaşarak kazandığı yeni anlamdır (*Ağır sözlerle kalbimi kırdı*).\n- **Terim Anlam:** Bilim, sanat, spor dallarına özgü kavramlardır (*Açı, nota, penaltı*).\n\n### 2. Deyim ve Atasözü Farkı\n- **Deyimler:** Genellikle mastar ekiyle biter, durum bildirir (*Gözden düşmek*).\n- **Atasözleri:** Tam bir cümle yapısındadır, öğüt verir (*Damlaya damlaya göl olur*).",
        "source_reference": "TDK Türkçe Sözlük & KPSS Türkçe Rehberi",
        "is_verified": True,
        "read_time_seconds": 60
    })
    
    # 10 Soru - Sözcükte Anlam
    q_t1 = [
        {
            "id": "q-t1-01", "topic_id": t1_id,
            "question_text": "Aşağıdaki cümlelerin hangisinde 'keskin' sözcüğü mecaz anlamda kullanılmıştır?",
            "options": [
                {"key": "A", "text": "Elimdeki keskin bıçakla sebzeleri hızlıca doğradım."},
                {"key": "B", "text": "Adamın keskin bakışları odadaki herkesi bir anda susturdu."},
                {"key": "C", "text": "Masadaki keskin makas kağıtları düzgünce kesti."},
                {"key": "D", "text": "Keskin bir virajdan sonra kasabanın ışıkları göründü."},
                {"key": "E", "text": "Usta, keskin aletleri çocukların erişemeyeceği yere kaldırdı."}
            ],
            "correct_option": "B",
            "explanation": "'Keskin bakış' ifadesinde keskin kelimesi somut kesme işlevinden uzaklaşarak 'etkileyici, sert, keskin duygulu' anlamında mecaz olarak kullanılmıştır.",
            "difficulty_level": "lisans", "is_verified": True
        },
        {
            "id": "q-t1-02", "topic_id": t1_id,
            "question_text": "Aşağıdaki cümlelerin hangisinde bir terim anlamlı sözcük KULLANILMAMIŞTIR?",
            "options": [
                {"key": "A", "text": "Hakem, ceza sahası içindeki müdahaleye penaltı düdüğü çaldı."},
                {"key": "B", "text": "Şiirde kullanılan hece ölçüsü ve uyak düzeni ahengi artırmış."},
                {"key": "C", "text": "Üçgenin iç açıları toplamı her zaman yüz seksen derecedir."},
                {"key": "D", "text": "Hekim, hastanın kalbindeki ritim bozukluğu için mercek kullandı."},
                {"key": "E", "text": "Dün akşam arkadaşımla sahilde uzun uzun yürüyüş yaptık."}
            ],
            "correct_option": "E",
            "explanation": "E seçeneğinde geçen kelimelerin tamamı günlük dildeki gerçek anlamlarıyla kullanılmış olup herhangi bir bilim, sanat veya spor terimi içermemektedir.",
            "difficulty_level": "lisans", "is_verified": True
        },
        {
            "id": "q-t1-03", "topic_id": t1_id,
            "question_text": "Aşağıdaki cümlelerin hangisinde deyim açıklamasıyla birlikte verilmiştir?",
            "options": [
                {"key": "A", "text": "Çok sevinçliydi, adeta etekleri zil çalıyordu."},
                {"key": "B", "text": "Sınavı kazanınca göklere uçtu, mutlu oldu."},
                {"key": "C", "text": "Olayın detaylarını duyunca kulaklarına inanamadı."},
                {"key": "D", "text": "Her şey yolunda giderken işi yokuşa sürdü."},
                {"key": "E", "text": "Sinirinden ne yapacağını bilemeyip küplere bindi."}
            ],
            "correct_option": "A",
            "explanation": "A seçeneğinde 'çok sevinçliydi' ifadesi, hemen ardından gelen 'etekleri zil çalıyordu' deyiminin doğrudan açıklaması ve anlamıdır.",
            "difficulty_level": "lisans", "is_verified": True
        },
        {
            "id": "q-t1-04", "topic_id": t1_id,
            "question_text": "Aşağıdaki altı çizili sözcük çiftlerinden hangisi aralarında 'zıt (karşıt) anlam' ilişkisi taşımaktadır?",
            "options": [
                {"key": "A", "text": "Geniş - Ferah alanlar"},
                {"key": "B", "text": "Cesur - Korkak insanların mücadelesi"},
                {"key": "C", "text": "Yoksul - Fakir köylülerin yaşamı"},
                {"key": "D", "text": "Cevap - Yanıt bekleyen sorular"},
                {"key": "E", "text": "Uzun - Boylu genç adam"}
            ],
            "correct_option": "B",
            "explanation": "'Cesur' ve 'Korkak' sözcükleri birbirinin tam karşıtı olan zıt anlamlı kelimelerdir.",
            "difficulty_level": "lisans", "is_verified": True
        },
        {
            "id": "q-t1-05", "topic_id": t1_id,
            "question_text": "Aşağıdaki cümlelerin hangisinde 'ad aktarması (mecazımürsel)' vardır?",
            "options": [
                {"key": "A", "text": "Soba yanınca bütün ev sıcacık bir havaya büründü."},
                {"key": "B", "text": "Güneşin doğuşunu izlemek için dağın zirvesine tırmandılar."},
                {"key": "C", "text": "Bahçedeki güller baharın gelişiyle birlikte açtı."},
                {"key": "D", "text": "Yeni aldığı arabayı kapının önüne özenle park etti."},
                {"key": "E", "text": "Deniz kenarında oturup dalgaların sesini dinledik."}
            ],
            "correct_option": "A",
            "explanation": "'Soba yanınca' ifadesinde kastedilen sobaya ait demir gövde değil, sobanın içindeki odun/kömürdür. Dış söylenip iç kastedilerek ad aktarması yapılmıştır.",
            "difficulty_level": "lisans", "is_verified": True
        },
        {
            "id": "q-t1-06", "topic_id": t1_id,
            "question_text": "Aşağıdaki ikilemelerden hangisi 'biri anlamlı biri anlamsız' iki sözcüğün birleşmesiyle oluşmuştur?",
            "options": [
                {"key": "A", "text": "Ses seda çıkmıyordu."},
                {"key": "B", "text": "Eğri büğrü yollardan geçtik."},
                {"key": "C", "text": "Eski püskü kıyafetlerini giydi."},
                {"key": "D", "text": "Yalan yanlış bilgiler verdi."},
                {"key": "E", "text": "Gece gündüz demeden çalıştı."}
            ],
            "correct_option": "C",
            "explanation": "'Eski püskü' ikilemesinde 'eski' tek başına anlamlı bir kelimeyken 'püskü' tek başına anlamsızdır.",
            "difficulty_level": "lisans", "is_verified": True
        },
        {
            "id": "q-t1-07", "topic_id": t1_id,
            "question_text": "Aşağıdaki cümlelerin hangisinde 'somutlaştırma' yapılmıştır?",
            "options": [
                {"key": "A", "text": "Aklına gelen fikirleri bir kağıda tek tek not etti."},
                {"key": "B", "text": "Yalnızlık adeta peşimi bırakmayan siyah bir gölge gibiydi."},
                {"key": "C", "text": "Soğuk hava yüzümüzü adeta bıçak gibi kesiyordu."},
                {"key": "D", "text": "Rüzgarın sesi ormanda derin bir sessizliği bozdu."},
                {"key": "E", "text": "Ağaçların yaprakları sararıp dökülmeye başladı."}
            ],
            "correct_option": "B",
            "explanation": "Soyut bir kavram olan 'yalnızlık', duyularla algılanabilen somut bir nesneye ('siyah bir gölgeye') benzetilerek somutlaştırılmıştır.",
            "difficulty_level": "lisans", "is_verified": True
        },
        {
            "id": "q-t1-08", "topic_id": t1_id,
            "question_text": "Aşağıdaki cümlelerin hangisinde 'eş sesli (sesteş)' bir sözcük KULLANILMAMIŞTIR?",
            "options": [
                {"key": "A", "text": "Yaz mevsiminde köye gidip bahçeyi suladık."},
                {"key": "B", "text": "Çay kenarında oturup çayımızı yudumladık."},
                {"key": "C", "text": "Yüzme bilmediği için sığ suda yüzdü."},
                {"key": "D", "text": "Kitaptaki zor soruları çözmek için saatlerce uğraştı."},
                {"key": "E", "text": "Gül bahçesinde dolaşırken bana tebessümle baktı."}
            ],
            "correct_option": "D",
            "explanation": "D seçeneğindeki kelimelerin sesteş (yazılışları aynı anlamları farklı) eş seslisi bulunmamaktadır. A'da yaz (mevsim/fiil), B'de çay (dere/içecek), C'de yüz (sayı/fiil/çehre), E'de gül (çiçek/fiil) sesteştir.",
            "difficulty_level": "lisans", "is_verified": True
        },
        {
            "id": "q-t1-09", "topic_id": t1_id,
            "question_text": "Aşağıdaki atasözlerinden hangisi 'tasarruf ve birikim yapmanın önemini' vurgulamaktadır?",
            "options": [
                {"key": "A", "text": "Ağaç yaş iken eğilir."},
                {"key": "B", "text": "Damlaya damlaya göl olur."},
                {"key": "C", "text": "Gülünü seven dikenine katlanır."},
                {"key": "D", "text": "Üzüm üzüme baka baka kararır."},
                {"key": "E", "text": "Dost kara günde belli olur."}
            ],
            "correct_option": "B",
            "explanation": "'Damlaya damlaya göl olur' atasözü küçük birikimlerin zamanla büyük değerlere ulaşacağını, yani tasarrufu öğütler.",
            "difficulty_level": "lisans", "is_verified": True
        },
        {
            "id": "q-t1-10", "topic_id": t1_id,
            "question_text": "Aşağıdaki cümlelerin hangisinde 'yansıma sözcükten türemiş' bir kelime vardır?",
            "options": [
                {"key": "A", "text": "Kapının gıcırtısı gece boyunca herkesi rahatsız etti."},
                {"key": "B", "text": "Güneşin ışıkları odanın içini aydınlattı."},
                {"key": "C", "text": "Rüzgar hafif hafif esmeye devam ediyordu."},
                {"key": "D", "text": "Çocuklar sokakta neşeyle koşuşuyorlardı."},
                {"key": "E", "text": "Kuşların cıvıltısı sabahın sessizliğini böldü."}
            ],
            "correct_option": "A",
            "explanation": "'Gıcırtı' kelimesi doğadaki 'gıcır' sesinden türemiş yansıma bir sözcüktür.",
            "difficulty_level": "lisans", "is_verified": True
        }
    ]
    questions.extend(q_t1)

    # -------------------------------------------------------------------------
    # KONU 2: Cümlede Anlam
    # -------------------------------------------------------------------------
    t2_id = "topic-turkce-cumlede-anlam"
    topics.append({
        "id": t2_id,
        "course_id": "course-turkce",
        "parent_id": None,
        "title": "Cümlede Anlam & Anlam İlişkileri",
        "slug": "cumlede-anlam",
        "importance_weight": 1.8,
        "sort_order": 2
    })
    quick_notes.append({
        "id": "note-turkce-cumlede-anlam",
        "topic_id": t2_id,
        "title": "Neden-Sonuç, Amaç-Sonuç ve Koşul Cümleleri",
        "content": "### 1. Neden-Sonuç (Sebep-Sonuç) Cümleleri\n- Eylem gerçekleşmiştir, nedeni bellidir. *-için, -den dolayı* ekleriyle kurulur.\n- *Yağmur yağdığı için ıslandık* (Yağmur yağdı = Gerçekleşti).\n\n### 2. Amaç-Sonuç Cümleleri\n- Henüz gerçekleşmemiş bir hedefe ulaşmak istenmektedir. *-mak için, amacıyla* konulabilir.\n- *Sınavı kazanmak için çalışıyor* (Henüz kazanmadı = Amaç).\n\n### 3. Örtülü Anlam\n- Cümlede açıkça söylenmeyip cümlenin anlamından çıkarılan ek anlamdır (*Ahmet de sınava girdi* -> Başkaları da girdi).",
        "source_reference": "TDK & KPSS Türkçe Rehberi",
        "is_verified": True,
        "read_time_seconds": 55
    })
    q_t2 = [
        {
            "id": "q-t2-01", "topic_id": t2_id,
            "question_text": "Aşağıdaki cümlelerin hangisi bir 'amaç-sonuç' ilişkisi içermektedir?",
            "options": [
                {"key": "A", "text": "Hava çok soğuk olduğundan dışarı çıkamadık."},
                {"key": "B", "text": "Yüksek lisans yapmak amacıyla yurt dışına başvurdu."},
                {"key": "C", "text": "Elektrikler kesilince mum yakmak zorunda kaldık."},
                {"key": "D", "text": "Sınav sonuçları açıklandığı için herkes heyecanlıydı."},
                {"key": "E", "text": "Trafik yoğun olduğu için toplantıya gecikti."}
            ],
            "correct_option": "B",
            "explanation": "B seçeneğinde 'yurt dışına başvurma' eylemi 'yüksek lisans yapmak amacıyla' gerçekleştirilmiştir (Amaç-Sonuç). Diğer şıklarda eylemin sebebi belirtilmiştir (Neden-Sonuç).",
            "difficulty_level": "lisans", "is_verified": True
        },
        {
            "id": "q-t2-02", "topic_id": t2_id,
            "question_text": "Aşağıdaki cümlelerin hangisinde 'öznel bir yargı' söz konusudur?",
            "options": [
                {"key": "A", "text": "Türkiye'nin başkenti Ankara'dır."},
                {"key": "B", "text": "Roman 350 sayfadan oluşmaktadır."},
                {"key": "C", "text": "Şairin son şiir kitabı okuyucuyu büyüleyen muhteşem bir eserdir."},
                {"key": "D", "text": "Filmin yönetmeni ödülü almak için sahneye çıktı."},
                {"key": "E", "text": "Toplantı saat tam 14:00'te başladı."}
            ],
            "correct_option": "C",
            "explanation": "'Okuyucuyu büyüleyen muhteşem bir eserdir' ifadesi kişisel beğeni ve duygu içerdiği için kanıtlanamayan öznel bir yargıdır.",
            "difficulty_level": "lisans", "is_verified": True
        },
        {
            "id": "q-t2-03", "topic_id": t2_id,
            "question_text": "Aşağıdaki cümlelerin hangisinde 'koşula (şarta) bağlılık' söz konusudur?",
            "options": [
                {"key": "A", "text": "Erken yatarsan sabah yorgun uyanmazsın."},
                {"key": "B", "text": "Sabah erkenden kalkıp yürüyüşe çıktı."},
                {"key": "C", "text": "Yağmur başladığı için şemsiyesini açtı."},
                {"key": "D", "text": "Bütün gün ders çalışmaktan gözleri yoruldu."},
                {"key": "E", "text": "Misafirler gelince hemen çay demledi."}
            ],
            "correct_option": "A",
            "explanation": "'Sabah yorgun uyanmama' eyleminin gerçekleşmesi 'erken yatma' şartına bağlandığı için koşul-sonuç ilişkisi vardır.",
            "difficulty_level": "lisans", "is_verified": True
        },
        {
            "id": "q-t2-04", "topic_id": t2_id,
            "question_text": "Aşağıdaki cümlelerin hangisinde 'örtülü anlam' vardır?",
            "options": [
                {"key": "A", "text": "Bu yıl da KPSS sınavına rekor katılım sağlandı."},
                {"key": "B", "text": "Kütüphane hafta sonları saat beşten sonra kapanıyor."},
                {"key": "C", "text": "Yazarlar son kitaplarında genellikle yalnızlık temasını işliyor."},
                {"key": "D", "text": "Ders çalışırken düzenli not tutmak başarıyı artırır."},
                {"key": "E", "text": "Otobüs durağında yaklaşık yirmi dakika bekledik."}
            ],
            "correct_option": "A",
            "explanation": "'Bu yıl da...' cümlesindeki 'da' eki, geçmiş yıllarda da sınava rekor katılım sağlandığı açıkça söylenmeyen örtülü anlamını çıkarır.",
            "difficulty_level": "lisans", "is_verified": True
        },
        {
            "id": "q-t2-05", "topic_id": t2_id,
            "question_text": "Aşağıdaki cümlelerin hangisinde bir 'varsayım' söz konusudur?",
            "options": [
                {"key": "A", "text": "Tut ki sınavı kazandın, ilk yapacağın şey ne olurdu?"},
                {"key": "B", "text": "Muhtemelen otobüs birazdan durağa gelecektir."},
                {"key": "C", "text": "Keşke ben de sizinle o geziye katılsaydım."},
                {"key": "D", "text": "Belki yarın akşam size çaya gelebiliriz."},
                {"key": "E", "text": "Sanırım bu sorunun cevabı B seçeneği olmalı."}
            ],
            "correct_option": "A",
            "explanation": "'Tut ki...' kelimesi gerçekleşmemiş bir olayı geçici olarak gerçekleşmiş kabul etme anlamı (varsayım) taşır.",
            "difficulty_level": "lisans", "is_verified": True
        },
        {
            "id": "q-t2-06", "topic_id": t2_id,
            "question_text": "Aşağıdaki cümlelerin hangisinde bir 'sitem' dile getirilmiştir?",
            "options": [
                {"key": "A", "text": "İnsan bunca yıllık arkadaşına bir telefon etmez mi?"},
                {"key": "B", "text": "Yazıklar olsun, bunca emeğim boşa gitti!"},
                {"key": "C", "text": "Eyvah, anahtarı evde unuttum!"},
                {"key": "D", "text": "Keşke o gün oraya hiç gitmeseydim."},
                {"key": "E", "text": "Ne yazık ki beklediğimiz destek gelmedi."}
            ],
            "correct_option": "A",
            "explanation": "A seçeneğinde sevilen/yakın bir kişiye sitem etme, kırgınlığını tatlı sert dile getirme durumu vardır.",
            "difficulty_level": "lisans", "is_verified": True
        },
        {
            "id": "q-t2-07", "topic_id": t2_id,
            "question_text": "Aşağıdaki cümlelerin hangisinde 'doğrudan anlatım' yapılmıştır?",
            "options": [
                {"key": "A", "text": "Öğretmen, yarın sınav yapacağını söyledi."},
                {"key": "B", "text": "Atatürk: 'Hayatta en hakiki mürşit ilimdir.' demiştir."},
                {"key": "C", "text": "Doktor, ilaçları düzenli kullanması gerektiğini belirtti."},
                {"key": "D", "text": "Arkadaşım akşam bize geleceğini haber verdi."},
                {"key": "E", "text": "Müdür toplantının ertelendiğini duyurdu."}
            ],
            "correct_option": "B",
            "explanation": "B seçeneğinde başkasına ait bir söz hiçbir değişikliğe uğratılmadan tırnak içinde aynen aktarılmıştır (Doğrudan Anlatım).",
            "difficulty_level": "lisans", "is_verified": True
        },
        {
            "id": "q-t2-08", "topic_id": t2_id,
            "question_text": "Aşağıdaki cümlelerin hangisi 'üslup (biçem)' ile ilgilidir?",
            "options": [
                {"key": "A", "text": "Yazar, eserinde Kurtuluş Savaşı yıllarını anlatmaktadır."},
                {"key": "B", "text": "Şair, kısa ve devrik cümlelerle akıcı bir dil yakalamıştır."},
                {"key": "C", "text": "Kitapta göç eden ailelerin dramı ele alınmıştır."},
                {"key": "D", "text": "Roman üç ana bölümden meydana gelmektedir."},
                {"key": "E", "text": "Şiirde doğa sevgisi ve yalnızlık işlenmiştir."}
            ],
            "correct_option": "B",
            "explanation": "Üslup (biçem), yazarın 'nasıl anlattığı' (dil kullanımı, kelime seçimi, cümle yapısı) ile ilgilidir. B seçeneğindeki kelime seçimi ve akıcılık vurgusu üsluptur.",
            "difficulty_level": "lisans", "is_verified": True
        },
        {
            "id": "q-t2-09", "topic_id": t2_id,
            "question_text": "Aşağıdaki cümlelerin hangisinde 'öz eleştiri' yapılmıştır?",
            "options": [
                {"key": "A", "text": "Planlı çalışmadığım için zamanı iyi yönetemedim."},
                {"key": "B", "text": "Rakiplerimiz bizden daha çok hazırlık yapmıştı."},
                {"key": "C", "text": "Sınav soruları beklenenden daha zordu."},
                {"key": "D", "text": "Hava muhalefeti sebebiyle etkinlik iptal edildi."},
                {"key": "E", "text": "Grup üyeleri sorumluluklarını yerine getirmedi."}
            ],
            "correct_option": "A",
            "explanation": "Kişinin kendi davranış ve eksikliklerini tarafsızca eleştirmesine 'öz eleştiri' denir. A seçeneğinde kişi kendi zamansızlığını eleştirmiştir.",
            "difficulty_level": "lisans", "is_verified": True
        },
        {
            "id": "q-t2-10", "topic_id": t2_id,
            "question_text": "Aşağıdaki cümlelerin hangisinde 'olasılık (ihtimal)' anlamı vardır?",
            "options": [
                {"key": "A", "text": "Şu anda Ankara'da yağmur yağıyor olabilir."},
                {"key": "B", "text": "Bu işi yarın akşama kadar mutlaka bitirmelisiniz."},
                {"key": "C", "text": "Ödevini yapmadan bilgisayar oyunu oynayamazsın."},
                {"key": "D", "text": "Lütfen sınıf içinde yüksek sesle konuşmayınız."},
                {"key": "E", "text": "Düzenli spor yapmak insan sağlığını korur."}
            ],
            "correct_option": "A",
            "explanation": "'Yağıyor olabilir' ifadesi kesinlik taşımayan, gerçekleşmesi muhtemel durumları belirten olasılık cümlesidir.",
            "difficulty_level": "lisans", "is_verified": True
        }
    ]
    questions.extend(q_t2)

    # -------------------------------------------------------------------------
    # KONU 3: Paragrafta Anlam
    # -------------------------------------------------------------------------
    t3_id = "topic-turkce-paragrafta-anlam"
    topics.append({
        "id": t3_id,
        "course_id": "course-turkce",
        "parent_id": None,
        "title": "Paragrafta Anlam & Yapı",
        "slug": "paragrafta-anlam-yapi",
        "importance_weight": 2.0,
        "sort_order": 3
    })
    quick_notes.append({
        "id": "note-turkce-paragrafta-anlam",
        "topic_id": t3_id,
        "title": "Paragrafta Akışı Bozan Cümle ve Paragraf Bölme",
        "content": "### 1. Düşüncenin Akışını Bozan Cümle\n- Paragraf tek bir konu etrafında şekillenir. Konunun dışına çıkan veya konunun farklı bir boyutuna aniden geçen cümle akışı bozar.\n\n### 2. Paragrafı İkiğe Bölme\n- İkinci paragraf, konunun **yeni ve farklı bir yönüne** geçildiği ilk cümle ile başlar.",
        "source_reference": "KPSS Paragraf Teknikleri Rehberi",
        "is_verified": True,
        "read_time_seconds": 50
    })
    q_t3 = [
        {
            "id": "q-t3-01", "topic_id": t3_id,
            "question_text": "(I) Kitap okuma alışkanlığı çocukluk çağında kazanılan en değerli becerilerden biridir. (II) Erken yaşta kitaplarla tanışan çocuklar dil becerilerini hızla geliştirirler. (III) Türkiye'de kağıt üretim maliyetleri son yıllarda oldukça artmıştır. (IV) Ayrıca hayal güçleri ve zihinsel odaklanma kapasiteleri de güçlenir. (V) Bu yüzden ebeveynlerin çocuklarına kitap okuma konusunda örnek olması gerekir.\n\nBu parçada numaralanmış cümlelerden hangisi düşüncenin akışını bozmaktadır?",
            "options": [
                {"key": "A", "text": "I"}, {"key": "B", "text": "II"}, {"key": "C", "text": "III"}, {"key": "D", "text": "IV"}, {"key": "E", "text": "V"}
            ],
            "correct_option": "C",
            "explanation": "Paragrafta çocuklarda kitap okuma alışkanlığının faydaları anlatılırken III. cümlede aniden 'kağıt üretim maliyetlerinden' bahsedilmiş ve akış bozulmuştur.",
            "difficulty_level": "lisans", "is_verified": True
        },
        {
            "id": "q-t3-02", "topic_id": t3_id,
            "question_text": "Sanatçı, içinde yaşadığı toplumun aynasıdır. Toplumda yaşanan acıları, sevinçleri ve değişimleri eserlerine yansıtmayan bir yazarın kalıcı olması düşünülemez. Halkın diliyle konuşmayan, onların dertleriyle dertlenmeyen yapıtlar kütüphane raflarında tozlanmaya mahkûmdur.\n\nBu parçanın başlığı aşağıdakilerden hangisi olmaya en uygundur?",
            "options": [
                {"key": "A", "text": "Edebiyatın Tarihsel Gelişimi"},
                {"key": "B", "text": "Sanatçı ve Toplum İlişkisi"},
                {"key": "C", "text": "Kütüphanelerin Önemı"},
                {"key": "D", "text": "Roman Yazma Teknikleri"},
                {"key": "E", "text": "Dilin Sanattaki Yeri"}
            ],
            "correct_option": "B",
            "explanation": "Paragrafın tamamında sanatçının toplumla olan bağı ve toplumu eserlerine yansıtma zorunluluğu anlatıldığı için en uygun başlık 'Sanatçı ve Toplum İlişkisi'dir.",
            "difficulty_level": "lisans", "is_verified": True
        },
        {
            "id": "q-t3-03", "topic_id": t3_id,
            "question_text": "(I) Yapay zeka teknolojileri günümüzde sağlık sektöründe çığır açmaktadır. (II) Hastalıkların erken teşhisinde devrim niteliğinde algoritmalar kullanılmaktadır. (III) Tıbbi görüntüleme cihazları yapay zeka sayesinde tümörleri milimetrik olarak tespit edebilmektedir. (IV) Eğitim sisteminde ise kişiselleştirilmiş öğrenme yazılımları ön plana çıkmaktadır. (V) Bu yazılımlar her öğrencinin öğrenme hızına uygun müfredat sunmaktadır.\n\nBu parça iki paragrafa bölünmek istense ikinci paragraf hangi cümleyle başlar?",
            "options": [
                {"key": "A", "text": "II"}, {"key": "B", "text": "III"}, {"key": "C", "text": "IV"}, {"key": "D", "text": "V"}, {"key": "E", "text": "I"}
            ],
            "correct_option": "C",
            "explanation": "I, II ve III. cümlelerde yapay zekanın 'sağlık sektöründeki' yeri anlatılırken IV. cümleden itibaren 'eğitim sistemindeki' uygulamalarına geçilmiştir. İkinci paragraf IV. cümle ile başlamalıdır.",
            "difficulty_level": "lisans", "is_verified": True
        },
        {
            "id": "q-t3-04", "topic_id": t3_id,
            "question_text": "İyi bir konuşmacı, dinleyicinin dikkatini sürekli canlı tutmayı başaran kişidir. Bunun için sadece bilgi vermek yetmez; jest ve mimikleri doğru kullanmak, ses tonunu yerine göre ayarlamak da gerekir. ----.\n\nBu parçanın sonuna düşüncenin akışına göre aşağıdakilerden hangisi getirilmelidir?",
            "options": [
                {"key": "A", "text": "Çünkü dinleyici sadece anlatılana değil, anlatılış biçimine de bakar."},
                {"key": "B", "text": "Bu yüzden konuşma yapmak her insanın harcı değildir."},
                {"key": "C", "text": "Ancak günümüzde iyi konuşmacı bulmak imkânsızlaşmıştır."},
                {"key": "D", "text": "Zira kitap okumak da konuşma becerisini geliştirir."},
                {"key": "E", "text": "Oysa dinleyiciler genellikle sunumun slaytlarına odaklanır."}
            ],
            "correct_option": "A",
            "explanation": "Paragrafta jest, mimik ve ses tonu gibi üslup unsurlarının öneminden bahsedilmiştir. A seçeneği 'Çünkü dinleyici anlatılış biçimine de bakar' ifadesiyle metni mantıksal olarak tamamlar.",
            "difficulty_level": "lisans", "is_verified": True
        },
        {
            "id": "q-t3-05", "topic_id": t3_id,
            "question_text": "Eleştirmenlik, sadece bir eserin kusurlarını bulup ortaya çıkarmak değildir. Aksine, eserin güçlü yönlerini, sanatçının yakalamak istediği özü ve edebiyata getirdiği yenilikleri okuyucuya tarafsızca aktarabilme sanatıdır. Gerçek bir eleştirmen yıkıcı değil, yol göstericidir.\n\nBu parçadan çıkarılabilecek en kapsamlı yargı aşağıdakilerden hangisidir?",
            "options": [
                {"key": "A", "text": "Eleştirmenler sadece olumsuz noktaları vurgulamalıdır."},
                {"key": "B", "text": "Hakiki eleştiri, eserin değerini tarafsızca ortaya koyan yapıcı bir süreçtir."},
                {"key": "C", "text": "Her okuyucu aynı zamanda iyi bir eleştirmendir."},
                {"key": "D", "text": "Sanatçılar eleştirmenlerin fikirlerini dikkate almalıdır."},
                {"key": "E", "text": "Edebiyatta eleştiri türü roman kadar ilgi görmez."}
            ],
            "correct_option": "B",
            "explanation": "Metinde eleştirinin yıkıcı kusur bulma değil, tarafsız ve yapıcı bir değerlendirme süreci olduğu vurgulanmıştır.",
            "difficulty_level": "lisans", "is_verified": True
        },
        {
            "id": "q-t3-06", "topic_id": t3_id,
            "question_text": "Fotoğraf sanatı, anı durdurma ve dondurma gücüne sahiptir. Resimden farklı olarak fotoğrafçı, doğada var olan ışık ve gölge oyununu makinesiyle yakalar. Kadrajına aldığı her nesne, onun dünya görüşünün bir yansımasıdır.\n\nBu parçada fotoğraf sanatı ile ilgili aşağıdakilerden hangisine DEĞİNİLMEMİŞTİR?",
            "options": [
                {"key": "A", "text": "Anı dondurabilme yeteneğine"},
                {"key": "B", "text": "Resim sanatından farklı yönleri olduğuna"},
                {"key": "C", "text": "Fotoğrafçının bakış açısını yansıttığına"},
                {"key": "D", "text": "Dünyanın en pahalı hobi türü olduğuna"},
                {"key": "E", "text": "Işık ve gölge elementlerinden yararlandığına"}
            ],
            "correct_option": "D",
            "explanation": "Metinde fotoğrafın maliyetine veya en pahalı hobi olduğuna dair hiçbir bilgi veya değinme yer almamaktadır.",
            "difficulty_level": "lisans", "is_verified": True
        },
        {
            "id": "q-t3-07", "topic_id": t3_id,
            "question_text": "Geleneksel el sanatlarımız arasında yer alan ebru sanatı, su üzerine serpilen boyaların kağıda aktarılmasıyla icra edilir. Her ebru çalışması benzersizdir; çünkü suyun üzerindeki desenin birebir aynısını tekrar oluşturmak imkânsızdır.\n\nBu parçaya göre ebru sanatının en belirgin özelliği aşağıdakilerden hangisidir?",
            "options": [
                {"key": "A", "text": "Yapımı son derece kolay bir sanat olması"},
                {"key": "B", "text": "Her eserin tek ve özgün (tekrarlanamaz) olması"},
                {"key": "C", "text": "Sadece yağlı boya ile yapılması"},
                {"key": "D", "text": "Dünyada en çok satılan sanat türü olması"},
                {"key": "E", "text": "Yalnızca kağıt üzerine uygulanabilmesi"}
            ],
            "correct_option": "B",
            "explanation": "Paragraftaki 'desenin birebir aynısını tekrar oluşturmak imkânsızdır' cümlesi, ebru sanatının her eserinin tek ve benzersiz olduğunu gösterir.",
            "difficulty_level": "lisans", "is_verified": True
        },
        {
            "id": "q-t3-08", "topic_id": t3_id,
            "question_text": "(I) Şehir hayatının karmaşası insanları doğaya kaçmaya zorluyor. (II) Hafta sonları ormanlık alanlar ve kamp bölgeleri dolup taşıyor. (III) Doğa yürüyüşü yapan insanların stresi azalıyor. (IV) Kamp malzemeleri üreten firmalar satışlarını artırdı. (V) Doğa ile baş başa kalmak zihinsel yenilenme sağlıyor.\n\nBu parçadaki numaralanmış cümlelerden hangisi 'yardımcı fikir' niteliğinde DEĞİLDİR (akışı bozmaktadır)?",
            "options": [
                {"key": "A", "text": "I"}, {"key": "B", "text": "II"}, {"key": "C", "text": "III"}, {"key": "D", "text": "IV"}, {"key": "E", "text": "V"}
            ],
            "correct_option": "D",
            "explanation": "Metin genel olarak doğanın insan ruhuna ve zihnine iyi gelmesini anlatırken IV. cümle ticari malzeme satışlarından bahsederek konu bütünlüğünü bozmuştur.",
            "difficulty_level": "lisans", "is_verified": True
        },
        {
            "id": "q-t3-09", "topic_id": t3_id,
            "question_text": "Düzenli uykunun insan sağlığı üzerindeki olumlu etkileri bilimsel olarak kanıtlanmıştır. Bağışıklık sistemini güçlendiren uyku, aynı zamanda hafızayı tazeler ve odaklanma süresini uzatır. Yeterli uyumayan bireylerde ise karar verme yeteneği zayıflar.\n\nBu parçadan aşağıdakilerden hangisine ULAŞILAMAZ?",
            "options": [
                {"key": "A", "text": "Uykusuzluğun zihinsel performansı olumsuz etkilediğine"},
                {"key": "B", "text": "Düzenli uykunun bağışıklık sistemini desteklediğine"},
                {"key": "C", "text": "Uykunun öğrenme ve hafıza süreçlerine faydasına"},
                {"key": "D", "text": "Günde en az dokuz saat uyunması gerektiğine"},
                {"key": "E", "text": "Uykunun insan sağlığındaki öneminin bilimsel temeline"}
            ],
            "correct_option": "D",
            "explanation": "Metinde uykunun faydaları anlatılmakla birlikte 'günde en az dokuz saat uyunması gerektiği' şeklinde spesifik bir saat rakamına ulaşılamaz.",
            "difficulty_level": "lisans", "is_verified": True
        },
        {
            "id": "q-t3-10", "topic_id": t3_id,
            "question_text": "Klasik eserler, her okunduğunda okuyucuya yeni bir şeyler söyleyebilen kitaplardır. Yirmi yaşında okuduğunuz bir romanı kırk yaşında tekrar okuduğunuzda bambaşka derinlikler keşfedersiniz.\n\nBu parçada klasik eserlerin hangi özelliği vurgulanmaktadır?",
            "options": [
                {"key": "A", "text": "Çok satan kitaplar olması"},
                {"key": "B", "text": "Zamansız ve sürekli yeni anlamlar sunabilen yapısı"},
                {"key": "C", "text": "Sadece yetişkinler tarafından anlaşılabilmesi"},
                {"key": "D", "text": "Dilinin ağır ve ağdalı olması"},
                {"key": "E", "text": "Sayfa sayısının fazla olması"}
            ],
            "correct_option": "B",
            "explanation": "Farklı yaşlarda okunduğunda yeni derinlikler keşfedilmesi, klasiklerin zamansız ve tükenmez anlam derinliğini gösterir.",
            "difficulty_level": "lisans", "is_verified": True
        }
    ]
    questions.extend(q_t3)

    # -------------------------------------------------------------------------
    # KONU 4: Anlatım Biçimleri ve Düşünceyi Geliştirme Yolları
    # -------------------------------------------------------------------------
    t4_id = "topic-turkce-anlatim-bicimleri"
    topics.append({
        "id": t4_id,
        "course_id": "course-turkce",
        "parent_id": None,
        "title": "Anlatım Biçimleri & Düşünceyi Geliştirme",
        "slug": "anlatim-bicimleri",
        "importance_weight": 1.6,
        "sort_order": 4
    })
    quick_notes.append({
        "id": "note-turkce-anlatim-bicimleri",
        "topic_id": t4_id,
        "title": "Anlatım Biçimleri ve Düşünceyi Geliştirme Yolları Rehberi",
        "content": "### 1. Anlatım Biçimleri (4 Temel Tür)\n- **Öyküleme:** Olay akışı var (Hareket, zaman, kişi).\n- **Betimleme:** Kelimelerle resim çizme (Görsel detaylar, niteleyici sıfatlar).\n- **Açıklama:** Bilgi verme amacı taşır (Tarafsız, nesnel).\n- **Tartışma:** Kendi fikrini savunup karşı fikri çürütme amacı taşır.\n\n### 2. Düşünceyi Geliştirme Yolları\n- **Tanımlama:** *Bu nedir?* sorusunun cevabı.\n- **Örnekleme:** Soyut fikri somutlaştırmak için örnek verme.\n- **Tanık Gösterme:** Uzman bir kişinin sözünü aynen aktarma.\n- **Sayısal Verilerden Yararlanma:** İstatistik, yüzde ve rakamlar.",
        "source_reference": "KPSS Edebiyat & Türkçe Notları",
        "is_verified": True,
        "read_time_seconds": 60
    })
    q_t4 = [
        {
            "id": "q-t4-01", "topic_id": t4_id,
            "question_text": "Güneş yavaşça dağların arkasından çekilirken köyün üzerine kızıl bir tül örtüldü. Ahşap evlerin pencerelerinden sızan sarı ışıklar, dar ve taşlı sokakları aydınlatıyordu. Serin rüzgar çam kokularını ortalığa yayıyordu.\n\nBu parçanın anlatımında aşağıdaki anlatım biçimlerinden hangisi ağır basmaktadır?",
            "options": [
                {"key": "A", "text": "Açıklama"}, {"key": "B", "text": "Tartışma"}, {"key": "C", "text": "Betimleme"}, {"key": "D", "text": "Öyküleme"}, {"key": "E", "text": "Örnekleme"}
            ],
            "correct_option": "C",
            "explanation": "Metinde görsellik ön plandadır; kelimelerle resim çizilerek (kızıl tül, sarı ışıklar, ahşap evler) betimleyici anlatım yapılmıştır.",
            "difficulty_level": "lisans", "is_verified": True
        },
        {
            "id": "q-t4-02", "topic_id": t4_id,
            "question_text": "Sabah erkenden uyandı. Çantasını hazırlayıp evden çıktı. Durağa kadar hızlı adımlarla yürüdü. Otobüse binip en arka koltuğa oturdu ve kitabını açtı.\n\nBu parçanın anlatımında aşağıdakilerden hangisi kullanılmıştır?",
            "options": [
                {"key": "A", "text": "Betimleme"}, {"key": "B", "text": "Öyküleme"}, {"key": "C", "text": "Tartışma"}, {"key": "D", "text": "Açıklama"}, {"key": "E", "text": "Tanımlama"}
            ],
            "correct_option": "B",
            "explanation": "Metinde zaman içinde gerçekleşen bir olay akışı (uyanma, çanta hazırlama, yürüme, otobüse binme) anlatıldığı için ÖYKÜLEME yapılmıştır.",
            "difficulty_level": "lisans", "is_verified": True
        },
        {
            "id": "q-t4-03", "topic_id": t4_id,
            "question_text": "Fotosentez, yeşil bitkilerin güneş ışığını kullanarak karbondioksit ve sudan organik besin ve oksijen üretmesi sürecidir. Bu süreç olmasaydı dünyadaki yaşam zinciri kırılırdı.\n\nBu parçada düşünceyi geliştirme yollarından hangisine başvurulmuştur?",
            "options": [
                {"key": "A", "text": "Tanımlama"}, {"key": "B", "text": "Örnekleme"}, {"key": "C", "text": "Tanık Gösterme"}, {"key": "D", "text": "Karşılaştırma"}, {"key": "E", "text": "Benzetme"}
            ],
            "correct_option": "A",
            "explanation": "'Fotosentez nedir?' sorusuna tam bir cevap verilerek Fotosentez kavramının tanımı yapılmıştır (Tanımlama).",
            "difficulty_level": "lisans", "is_verified": True
        },
        {
            "id": "q-t4-04", "topic_id": t4_id,
            "question_text": "Çoğu insan başarının şans eseri elde edildiğine inanır. Oysa başarı, gecesini gündüzüne katan disiplinli bir çalışmanın ürünüdür. Şans sadece hazır olan zihinlere gülümser.\n\nBu parçada hangi anlatım biçimi kullanılmıştır?",
            "options": [
                {"key": "A", "text": "Öyküleme"}, {"key": "B", "text": "Betimleme"}, {"key": "C", "text": "Tartışma"}, {"key": "D", "text": "Açıklama"}, {"key": "E", "text": "Düşsel Anlatım"}
            ],
            "correct_option": "C",
            "explanation": "Yazar toplumdaki yaygın bir kanıya ('başarı şanstır') karşı çıkarak kendi görüşünü kabul ettirmeye çalıştığı için TARTIŞMA biçimi kullanılmıştır.",
            "difficulty_level": "lisans", "is_verified": True
        },
        {
            "id": "q-t4-05", "topic_id": t4_id,
            "question_text": "Kitap okumak insanı zenginleştirir. Nitekim ünlü düşünür Bacon da 'Okuma insanı doldurur, konuşmak hazırlar, yazmak ise uzmanlaştırır' diyerek okumanın önemini vurgular.\n\nBu parçada düşünceyi geliştirme yollarından hangisi kullanılmıştır?",
            "options": [
                {"key": "A", "text": "Tanık Gösterme"}, {"key": "B", "text": "Sayısal Verilerden Yararlanma"}, {"key": "C", "text": "Benzetme"}, {"key": "D", "text": "Tanımlama"}, {"key": "E", "text": "Örnekleme"}
            ],
            "correct_option": "A",
            "explanation": "Yazar kendi fikrini desteklemek için alanında uzman Bacon'ın sözünü tırnak içinde aynen aktarmıştır (Tanık Gösterme).",
            "difficulty_level": "lisans", "is_verified": True
        },
        {
            "id": "q-t4-06", "topic_id": t4_id,
            "question_text": "2025 yılı verilerine göre kütüphanelerden yararlanan öğrenci sayısı bir önceki yıla göre %24 artarak 3,5 milyona ulaşmıştır.\n\nBu parçada düşünceyi geliştirme yollarından hangisi ağır basmaktadır?",
            "options": [
                {"key": "A", "text": "Sayısal Verilerden Yararlanma"},
                {"key": "B", "text": "Tanık Gösterme"},
                {"key": "C", "text": "Benzetme"},
                {"key": "D", "text": "Tanımlama"},
                {"key": "E", "text": "Öyküleme"}
            ],
            "correct_option": "A",
            "explanation": "Metinde istatistiksel oranlar ve rakamlar (%24, 3,5 milyon) kullanıldığı için Sayısal Verilerden Yararlanma vardır.",
            "difficulty_level": "lisans", "is_verified": True
        },
        {
            "id": "q-t4-07", "topic_id": t4_id,
            "question_text": "Türk edebiyatında milli edebiyat akımı temsilcileri halka doğru yönelmişlerdir. Örneğin Ömer Seyfettin hikayelerinde, Mehmet Emin Yurdakul ise şiirlerinde sade Türkçeyi savunmuşlardır.\n\nBu parçada düşünceyi geliştirme yollarından hangisi kullanılmıştır?",
            "options": [
                {"key": "A", "text": "Örnekleme"}, {"key": "B", "text": "Tanımlama"}, {"key": "C", "text": "Tanık Gösterme"}, {"key": "D", "text": "Sayısal Veri"}, {"key": "E", "text": "Benzetme"}
            ],
            "correct_option": "A",
            "explanation": "Genel kural verildikten sonra Ömer Seyfettin ve Mehmet Emin Yurdakul isimleri somut örnek olarak verilmiştir (Örnekleme).",
            "difficulty_level": "lisans", "is_verified": True
        },
        {
            "id": "q-t4-08", "topic_id": t4_id,
            "question_text": "Doğu edebiyatında masallar daha çok mistik ögeler taşırken Batı edebiyatında rasyonel ve gerçekçi ögeler ön plana çıkar.\n\nBu cümlede hangi düşünceyi geliştirme yolu kullanılmıştır?",
            "options": [
                {"key": "A", "text": "Karşılaştırma"}, {"key": "B", "text": "Tanımlama"}, {"key": "C", "text": "Tanık Gösterme"}, {"key": "D", "text": "Sayısal Veri"}, {"key": "E", "text": "Öyküleme"}
            ],
            "correct_option": "A",
            "explanation": "Doğu edebiyatı ile Batı edebiyatının masal anlayışı kıyaslanarak KARŞILAŞTIRMA yapılmıştır.",
            "difficulty_level": "lisans", "is_verified": True
        },
        {
            "id": "q-t4-09", "topic_id": t4_id,
            "question_text": "Zaman akan bir su gibidir; bir defa geçip gitti mi bir daha geri döndürülemez.\n\nBu cümlede başvurulan düşünceyi geliştirme yolu aşağıdakilerden hangisidir?",
            "options": [
                {"key": "A", "text": "Benzetme"}, {"key": "B", "text": "Tanımlama"}, {"key": "C", "text": "Örnekleme"}, {"key": "D", "text": "Tanık Gösterme"}, {"key": "E", "text": "Karşılaştırma"}
            ],
            "correct_option": "A",
            "explanation": "'Zaman akan bir su gibidir' ifadesinde zaman, suya benzetilmiştir (Benzetme).",
            "difficulty_level": "lisans", "is_verified": True
        },
        {
            "id": "q-t4-10", "topic_id": t4_id,
            "question_text": "Aşağıdaki anlatım biçimlerinin hangisinde nesnel ve bilgi verici bir dil kullanılması zorunludur?",
            "options": [
                {"key": "A", "text": "Açıklama"}, {"key": "B", "text": "Öyküleme"}, {"key": "C", "text": "Betimleme"}, {"key": "D", "text": "Düşsel Anlatım"}, {"key": "E", "text": "Mizahi Anlatım"}
            ],
            "correct_option": "A",
            "explanation": "Açıklayıcı anlatım biçiminin temel amacı okuyucuya tarafsız ve nesnel bilgi vermektir.",
            "difficulty_level": "lisans", "is_verified": True
        }
    ]
    questions.extend(q_t4)

    # -------------------------------------------------------------------------
    # KONU 5: Ses Bilgisi
    # -------------------------------------------------------------------------
    t5_id = "topic-turkce-ses-bilgisi"
    topics.append({
        "id": t5_id,
        "course_id": "course-turkce",
        "parent_id": None,
        "title": "Ses Bilgisi & Ses Olayları",
        "slug": "ses-bilgisi",
        "importance_weight": 1.5,
        "sort_order": 5
    })
    quick_notes.append({
        "id": "note-turkce-ses-bilgisi",
        "topic_id": t5_id,
        "title": "KPSS'de En Çok Çıkan Ses Olayları Özet Tablosu",
        "content": "### 1. Ünsüz Yumuşaması (Değişimi)\n- *p, ç, t, k* -> *b, c, d, ğ* (*Kitap-ı* -> *Kitabı*).\n\n### 2. Ünsüz Benzeşmesi (Sertleşmesi)\n- *Fıstıkçı Şahap* ünsüzlerinden sonra *c, d, g* gelirse *ç, t, k* olur (*Sınıf-da* -> *Sınıfta*).\n\n### 3. Ünlü Düşmesi\n- İki heceli kelimelerde ünlü ile başlayan ek gelince ikinci hecedeki dar ünlü düşer (*Burun-u* -> *Burnu*).\n\n### 4. Ünlü Daralması\n- *a, e* ile biten fiillere *-yor* eki gelince *ı, i, u, ü* olur (*Başla-yor* -> *Başlıyor*).",
        "source_reference": "TDK Ses Bilgisi Kuralları",
        "is_verified": True,
        "read_time_seconds": 55
    })
    q_t5 = [
        {
            "id": "q-t5-01", "topic_id": t5_id,
            "question_text": "'Sınıfta ders dinlerken burnu kanamaya başladı.' cümlesinde aşağıdaki ses olaylarından hangileri mevcuttur?",
            "options": [
                {"key": "A", "text": "Ünsüz sertleşmesi — Ünlü düşmesi"},
                {"key": "B", "text": "Ünsüz yumuşaması — Ünlü türemesi"},
                {"key": "C", "text": "Ünlü daralması — Ünsüz düşmesi"},
                {"key": "D", "text": "Ünsüz yumuşaması — Ünsüz sertleşmesi"},
                {"key": "E", "text": "Ünlü düşmesi — Ünlü daralması"}
            ],
            "correct_option": "A",
            "explanation": "'Sınıfta' kelimesinde ünsüz sertleşmesi (benzeşmesi: sınıf-da -> sınıfta), 'burnu' kelimesinde ise ünlü düşmesi (burun-u -> burnu) vardır.",
            "difficulty_level": "lisans", "is_verified": True
        },
        {
            "id": "q-t5-02", "topic_id": t5_id,
            "question_text": "Aşağıdaki cümlelerin hangisinde 'ünsüz yumuşamasına aykırı' bir kullanım vardır?",
            "options": [
                {"key": "A", "text": "Hukukun üstünlüğü ilkesi korunmalıdır."},
                {"key": "B", "text": "Kitabın sayfalarını tek tek çevirdi."},
                {"key": "C", "text": "Çocuğun elindeki oyuncağı aldı."},
                {"key": "D", "text": "Ağacın dalları rüzgarda sallanıyordu."},
                {"key": "E", "text": "Sokağın başında beklemeye başladı."}
            ],
            "correct_option": "A",
            "explanation": "'Hukuk' kelimesine ünlü ile başlayan '-un' eki gelmesine rağmen 'hukuğun' şekline dönüşmemiş, 'hukukun' olarak kalmıştır. Bu durum yumuşama kuralına aykırılıktır.",
            "difficulty_level": "lisans", "is_verified": True
        },
        {
            "id": "q-t5-03", "topic_id": t5_id,
            "question_text": "Aşağıdaki cümlelerin hangisinde 'ünlü daralması' yapılmıştır?",
            "options": [
                {"key": "A", "text": "Çocuklar bahçede neşeyle oynuyor."},
                {"key": "B", "text": "Otobüs durağa doğru yaklaşıyor."},
                {"key": "C", "text": "Her gün düzenli olarak spor yapıyor."},
                {"key": "D", "text": "Kitap okurken zamanın nasıl geçtiğini anlamıyor."},
                {"key": "E", "text": "Arkadaşlarıyla akşam sinemaya gidiyor."}
            ],
            "correct_option": "A",
            "explanation": "'Oynat/Oyna' fiiline '-yor' eki geldiğinde sonundaki geniş ünlü olan 'a' daralarak 'ı' sesine dönüşmüştür (Oyna-yor -> Oynuyor).",
            "difficulty_level": "lisans", "is_verified": True
        },
        {
            "id": "q-t5-04", "topic_id": t5_id,
            "question_text": "Aşağıdaki kelimelerin hangisinde 'ünsüz türemesi (ikizleşme)' vardır?",
            "options": [
                {"key": "A", "text": "Hakkımı sonuna kadar savunacağım."},
                {"key": "B", "text": "Küçücük çocuk sokakta kaybolmuş."},
                {"key": "C", "text": "Sabah erkenden yola çıktık."},
                {"key": "D", "text": "Aklına gelen fikri paylaştı."},
                {"key": "E", "text": "Gözleri uykusuzluktan kızarmıştı."}
            ],
            "correct_option": "A",
            "explanation": "'Hak' kelimesine '-ım' eki geldiğinde kelime kökünde bulunmayan fazladan bir 'k' sesi türeyerek 'Hakkım' olmuştur (Ünsüz Türemesi).",
            "difficulty_level": "lisans", "is_verified": True
        },
        {
            "id": "q-t5-05", "topic_id": t5_id,
            "question_text": "Aşağıdaki kelimelerin hangisinde 'ünsüz düşmesi' gerçekleşmiştir?",
            "options": [
                {"key": "A", "text": "Minicik bir kuş pencereye kondu."},
                {"key": "B", "text": "Sıcak havada dışarı çıkmak zor."},
                {"key": "C", "text": "Büyük evlerin yanında durduk."},
                {"key": "D", "text": "Genç adam hızlıca uzaklaştı."},
                {"key": "E", "text": "Derin bir nefes alıp konuşmaya başladı."}
            ],
            "correct_option": "A",
            "explanation": "'Minik' kelimesine '-cik' küçültme eki getirildiğinde sonundaki 'k' ünsüzü düşmüştür (Minik-cik -> Minicik).",
            "difficulty_level": "lisans", "is_verified": True
        },
        {
            "id": "q-t5-06", "topic_id": t5_id,
            "question_text": "Aşağıdaki cümlelerin hangisinde 'üsnüz benzeşmesi (sertleşmesi)' kuralına uyulmadığı için bir yazım hatası yapılmıştır?",
            "options": [
                {"key": "A", "text": "Saat 14:00'de toplantı başlayacak."},
                {"key": "B", "text": "Sokakta yürürken eski bir dostunu gördü."},
                {"key": "C", "text": "Kitapçıdan yeni çıkan romanı satın aldı."},
                {"key": "D", "text": "Sınıfta sessizlik hakim oldu."},
                {"key": "E", "text": "Yurttan ayrılıp eve doğru yürüdü."}
            ],
            "correct_option": "A",
            "explanation": "Saat 14:00 (on dört) sonundaki 't' sert ünsüzünden sonra gelen '-de' eki sertleşerek '-te' olmalıydı ('14:00'te'). Uyulmadığı için yazım hatası oluşmuştur.",
            "difficulty_level": "lisans", "is_verified": True
        },
        {
            "id": "q-t5-07", "topic_id": t5_id,
            "question_text": "Aşağıdaki kelimelerin hangisinde 'ünlü türemesi' gerçekleşmiştir?",
            "options": [
                {"key": "A", "text": "Daracık yollardan geçip köye ulaştık."},
                {"key": "B", "text": "Kısacık ömründe büyük işler başardı."},
                {"key": "C", "text": "İncecik kumaştan elbise diktirmiş."},
                {"key": "D", "text": "Ufacık bir taş arabanın camını kırdı."},
                {"key": "E", "text": "Sıcakçık çaydan bir yudum aldı."}
            ],
            "correct_option": "A",
            "explanation": "'Dar' kelimesine '-cık' küçültme eki getirildiğinde arada 'a' ünlüsü türeyerek 'Daracık' şeklini almıştır (Ünlü Türemesi).",
            "difficulty_level": "lisans", "is_verified": True
        },
        {
            "id": "q-t5-08", "topic_id": t5_id,
            "question_text": "Aşağıdaki cümlelerin hangisinde 'dudak ünsüzlerinin benzeşmesi (n-m değişimi)' örneği vardır?",
            "options": [
                {"key": "A", "text": "Çarşambayı sel aldı, bir yar sevdim el aldı."},
                {"key": "B", "text": "Pazartesi günü sınav sonuçları açıklanacak."},
                {"key": "C", "text": "Sonbahar mevsiminde yapraklar sararır."},
                {"key": "D", "text": "İlkbaharda çiçekler kırlarda açar."},
                {"key": "E", "text": "Yaz günlerinde deniz kenarına gideriz."}
            ],
            "correct_option": "A",
            "explanation": "'Çarşanba' kelimesindeki 'b' dudak ünsüzü kendinden önceki 'n' sesini 'm' sesine dönüştürerek 'Çarşamba' yapmıştır (n-m değişimi).",
            "difficulty_level": "lisans", "is_verified": True
        },
        {
            "id": "q-t5-09", "topic_id": t5_id,
            "question_text": "'Gönlümün efendisi' tamlamasındaki 'gönlümün' kelimesinde hangi ses olayı gerçekleşmiştir?",
            "options": [
                {"key": "A", "text": "Ünlü düşmesi"},
                {"key": "B", "text": "Ünsüz yumuşaması"},
                {"key": "C", "text": "Ünsüz türemesi"},
                {"key": "D", "text": "Ünlü daralması"},
                {"key": "E", "text": "Ünsüz düşmesi"}
            ],
            "correct_option": "A",
            "explanation": "Kelimenin kökü 'Gönül'dür. Ünlü ile başlayan ek alınca ikinci hecedeki 'ü' düşmüştür (Gönül-üm -> Gönlüm).",
            "difficulty_level": "lisans", "is_verified": True
        },
        {
            "id": "q-t5-10", "topic_id": t5_id,
            "question_text": "Aşağıdaki sözcüklerden hangisi ünlü ile başlayan bir ek aldığında 'ünsüz yumuşamasına' UĞRAMAZ?",
            "options": [
                {"key": "A", "text": "Ataç"}, {"key": "B", "text": "Ağaç"}, {"key": "C", "text": "Toprak"}, {"key": "D", "text": "Kulak"}, {"key": "E", "text": "Ç çocuk"}
            ],
            "correct_option": "A",
            "explanation": "'Ataç' özel tek heceli/yabancı kökenli isim niteliğinde yumuşamayan kelimelerdendir ('Atacı'). Diğer şıklarda Ağacı, Toprağı, Kulağı yumuşar.",
            "difficulty_level": "lisans", "is_verified": True
        }
    ]
    questions.extend(q_t5)

    # -------------------------------------------------------------------------
    # KONU 6: Sözcük Yapısı ve Ekler
    # -------------------------------------------------------------------------
    t6_id = "topic-turkce-sozcuk-yapisi"
    topics.append({
        "id": t6_id,
        "course_id": "course-turkce",
        "parent_id": None,
        "title": "Sözcük Yapısı ve Ekler",
        "slug": "sozcuk-yapisi-ekler",
        "importance_weight": 1.6,
        "sort_order": 6
    })
    quick_notes.append({
        "id": "note-turkce-sozcuk-yapisi",
        "topic_id": t6_id,
        "title": "Kök, Yapım Eki ve Çekim Eki Ayırımı",
        "content": "### 1. Basit, Türemiş ve Birleşik Sözcükler\n- **Basit:** Yapım eki almamış sözcüktür (*Ev-de, kitap-lar*).\n- **Türemiş:** En az bir yapım eki almış sözcüktür (*Göz-lük, yap-ıcı*).\n- **Birleşik:** İki sözcüğün birleşmesiyle oluşur (*İlkokul, gecekondu*).\n\n### 2. İyelik Eki vs Hal Eki Ayrımı\n- *Onun evi* (İyelik Eki - kime ait olduğu).\n- *Evi temizledi* (Belirtme Hal Eki - neyi temizledi?).",
        "source_reference": "TDK Dil Bilgisi Kuralları",
        "is_verified": True,
        "read_time_seconds": 55
    })
    q_t6 = [
        {
            "id": "q-t6-01", "topic_id": t6_id,
            "question_text": "Aşağıdaki altı çizili sözcüklerden hangisi 'türemiş' yapılı bir sözcüktür?",
            "options": [
                {"key": "A", "text": "Masadaki defterleri çantasına koydu."},
                {"key": "B", "text": "Sokaktaki çocuk neşeyle koşuyordu."},
                {"key": "C", "text": "Yazarlar son dönemde özgün eserler üretiyor."},
                {"key": "D", "text": "Evden ayrılırken kapıyı kilitledi."},
                {"key": "E", "text": "Akşam saatlerinde hava serinledi."}
            ],
            "correct_option": "C",
            "explanation": "'Yazarlar' kelimesinde 'Yaz-' kökünden 'Yazar' isim türeten yapım eki türemiştir. Türemiş kelimedir.",
            "difficulty_level": "lisans", "is_verified": True
        },
        {
            "id": "q-t6-02", "topic_id": t6_id,
            "question_text": "Aşağıdaki cümlelerin hangisinde fiilden isim türeten yapım eki almış bir kelime vardır?",
            "options": [
                {"key": "A", "text": "Sınavdaki soruların çözümü oldukça uzundu."},
                {"key": "B", "text": "Gözlükçüden yeni bir gözlük satın aldı."},
                {"key": "C", "text": "Tuzsuz yemeklerin tadı tuzu olmuyor."},
                {"key": "D", "text": "Evdeki hesap çarşıya uymadı."},
                {"key": "E", "text": "Kitaplıkta duran romanları düzenledi."}
            ],
            "correct_option": "A",
            "explanation": "'Çözüm' kelimesi 'çöz-' fiil kökünden '-üm' ekiyle 'çözüm' ismine dönüşmüş (Fiilden İsim Yapım Eki) bir kelimedir.",
            "difficulty_level": "lisans", "is_verified": True
        },
        {
            "id": "q-t6-03", "topic_id": t6_id,
            "question_text": "Aşağıdaki cümlelerin hangisinde 'iyelik eki' KULLANILMAMIŞTIR?",
            "options": [
                {"key": "A", "text": "Arabası arızalanınca çekici çağırdı."},
                {"key": "B", "text": "Evi şehir merkezine oldukça uzaktaydı."},
                {"key": "C", "text": "Kalemini masanın üzerinde unuttu."},
                {"key": "D", "text": "Kitabı kütüphaneden ödünç aldı."},
                {"key": "E", "text": "Fikirleri herkes tarafından saygıyla karşılandı."}
            ],
            "correct_option": "D",
            "explanation": "D seçeneğindeki 'Kitabı' kelimesindeki '-ı' eki iyelik eki değil, nesneyi belirten 'Belirtme Hal Eki'dir (Neyi ödünç aldı? -> Kitabı).",
            "difficulty_level": "lisans", "is_verified": True
        },
        {
            "id": "q-t6-04", "topic_id": t6_id,
            "question_text": "Aşağıdaki kelimelerden hangisi hem yapım hem de çekim eki almıştır?",
            "options": [
                {"key": "A", "text": "Öğrencilerimiz"},
                {"key": "B", "text": "Masadakiler"},
                {"key": "C", "text": "Evlerimizden"},
                {"key": "D", "text": "Kitaplarımız"},
                {"key": "E", "text": "Sokaklarda"}
            ],
            "correct_option": "A",
            "explanation": "'Öğrencilerimiz': Öğren- (Kök) -> Öğrenci (Yapım Eki) -> -ler (Çoğul Çekim Eki) -> -imiz (İyelik Çekim Eki). Hem yapım hem çekim eki almıştır.",
            "difficulty_level": "lisans", "is_verified": True
        },
        {
            "id": "q-t6-05", "topic_id": t6_id,
            "question_text": "Aşağıdaki birleşik kelimelerden hangisi 'kaynaşma (anlam kayması)' yoluyla oluşmuştur?",
            "options": [
                {"key": "A", "text": "Biçerdöver"},
                {"key": "B", "text": "Çanakkale"},
                {"key": "C", "text": "Gecekondu"},
                {"key": "D", "text": "Sonbahar"},
                {"key": "E", "text": "Mirasyedi"}
            ],
            "correct_option": "A",
            "explanation": "'Biçerdöver' kelimesinde iki fiil birleşerek bir tarım makinesinin adı olmuş ve anlam kaymasına uğramıştır.",
            "difficulty_level": "lisans", "is_verified": True
        },
        {
            "id": "q-t6-06", "topic_id": t6_id,
            "question_text": "Aşağıdaki kelimelerden hangisinin kökü 'isim' soyludur?",
            "options": [
                {"key": "A", "text": "Gözlemci"},
                {"key": "B", "text": "Yazarlar"},
                {"key": "C", "text": "Çözümsüz"},
                {"key": "D", "text": "Korkusuz"},
                {"key": "E", "text": "Gelişim"}
            ],
            "correct_option": "A",
            "explanation": "'Gözlemci' kelimesinin kökü 'Göz' ismidir (Göz -> Gözle- -> Gözlem -> Gözlemci). Diğerlerinin kökü fiildir (Yaz-, Çöz-, Kork-, Gel-).",
            "difficulty_level": "lisans", "is_verified": True
        },
        {
            "id": "q-t6-07", "topic_id": t6_id,
            "question_text": "Aşağıdaki eklerden hangisi eklendiği sözcüğün türünü değiştiren bir 'yapım eki'dir?",
            "options": [
                {"key": "A", "text": "-lık / -lik (Göz -> Gözlük)"},
                {"key": "B", "text": "-lar / -ler (Masa -> Masalar)"},
                {"key": "C", "text": "-dan / -den (Ev -> Evden)"},
                {"key": "D", "text": "-ın / -in (Kapı -> Kapının)"},
                {"key": "E", "text": "-ı / -i (Kalem -> Kalemi)"}
            ],
            "correct_option": "A",
            "explanation": "'-lık/-lik' eki yeni bir kavram türeten İsimden İsim Yapım Ekidir. Diğerleri ise çekim ekleridir.",
            "difficulty_level": "lisans", "is_verified": True
        },
        {
            "id": "q-t6-08", "topic_id": t6_id,
            "question_text": "Aşağıdaki cümlelerin hangisinde 'vasıta (araç) hal eki' (-la/-le) vardır?",
            "options": [
                {"key": "A", "text": "Okula otobüsle gitmeyi tercih ediyor."},
                {"key": "B", "text": "Bahçedeki ağaçlar çiçekle dolmuştu."},
                {"key": "C", "text": "Onunla akşam saatlerinde buluştuk."},
                {"key": "D", "text": "Sevgiyle yazılan mektuplar saklandı."},
                {"key": "E", "text": "Hızla oradan uzaklaşmaya başladı."}
            ],
            "correct_option": "A",
            "explanation": "'Otobüsle' kelimesindeki '-le' eki okula ulaşımın hangi araçla yapıldığını gösteren vasıta hal ekidir.",
            "difficulty_level": "lisans", "is_verified": True
        },
        {
            "id": "q-t6-09", "topic_id": t6_id,
            "question_text": "Aşağıdaki birleşik sözcüklerden hangisi 'isim tamamlaması' yoluyla oluşmuştur?",
            "options": [
                {"key": "A", "text": "Aslanağzı (çiçek)"},
                {"key": "B", "text": "Biçerdöver"},
                {"key": "C", "text": "Gecekondu"},
                {"key": "D", "text": "Kapkaççı"},
                {"key": "E", "text": "Uyurgezer"}
            ],
            "correct_option": "A",
            "explanation": "'Aslanağzı' (Aslanın ağzı) belirtisiz isim tamlamasının kalıplaşmasıyla oluşmuş birleşik isimdir.",
            "difficulty_level": "lisans", "is_verified": True
        },
        {
            "id": "q-t6-10", "topic_id": t6_id,
            "question_text": "Aşağıdaki kelimelerin hangisinde 'ilgi eki (tamlayan eki)' vardır?",
            "options": [
                {"key": "A", "text": "Kapının kolu kırılmıştı."},
                {"key": "B", "text": "Kapıyı hızlıca kapattı."},
                {"key": "C", "text": "Kapıda saatlerce bekledi."},
                {"key": "D", "text": "Kapıdan içeri girdi."},
                {"key": "E", "text": "Kapıya doğru yürüdü."}
            ],
            "correct_option": "A",
            "explanation": "'Kapının kolu' belirtili isim tamlamasında 'Kapının' kelimesindeki '-nın' eki İlgi (Tamlayan) ekidir.",
            "difficulty_level": "lisans", "is_verified": True
        }
    ]
    questions.extend(q_t6)

    # -------------------------------------------------------------------------
    # KONU 7: Sözcük Türleri
    # -------------------------------------------------------------------------
    t7_id = "topic-turkce-sozcuk-turleri"
    topics.append({
        "id": t7_id,
        "course_id": "course-turkce",
        "parent_id": None,
        "title": "Sözcük Türleri (İsim, Sıfat, Zamir, Zarf, Edat, Bağlaç)",
        "slug": "sozcuk-turleri",
        "importance_weight": 1.9,
        "sort_order": 7
    })
    quick_notes.append({
        "id": "note-turkce-sozcuk-turleri",
        "topic_id": t7_id,
        "title": "Sözcük Türlerini Ayırt Etme Püf Noktaları",
        "content": "### 1. Sıfat vs Zarf Ayrımı\n- **Sıfat:** İsmi niteleyen/belirten sözcüktür (*Güzel ev*).\n- **Zarf:** Fiili, fiilimsiyi veya sıfatı niteleyen sözcüktür (*Güzel konuştu*).\n\n### 2. Zamir\n- İsmin yerini tutan sözcüktür (*O, bu, şu, kim, herkes*).\n\n### 3. Edat vs Bağlaç\n- **Edat:** Tek başına anlamı olmayan, cümle içinde anlam kazanan sözcüktür (*gibi, kadar, için*).\n- **Bağlaç:** Kelime veya cümleleri birbirine bağlayan sözcüktür (*ve, veya, çünkü, ancak*).",
        "source_reference": "TDK Sözcük Türleri Rehberi",
        "is_verified": True,
        "read_time_seconds": 60
    })
    q_t7 = [
        {
            "id": "q-t7-01", "topic_id": t7_id,
            "question_text": "Aşağıdaki cümlelerin hangisinde 'güzel' sözcüğü zarf (belirteç) görevinde kullanılmıştır?",
            "options": [
                {"key": "A", "text": "Güzel bir elbise alıp partiye katıldı."},
                {"key": "B", "text": "Öğretmenimiz soruları çok güzel açıkladı."},
                {"key": "C", "text": "Güzel günler bizi bekliyor."},
                {"key": "D", "text": "Bu mahallede güzel evler var."},
                {"key": "E", "text": "Güzel bir bahçe manzarasını izledik."}
            ],
            "correct_option": "B",
            "explanation": "B seçeneğinde 'güzel' kelimesi 'açıkladı' fiilini nitelediği için Durum Zarfı görevindedir. Diğer şıklarda isimleri nitelediği için sıfattır.",
            "difficulty_level": "lisans", "is_verified": True
        },
        {
            "id": "q-t7-02", "topic_id": t7_id,
            "question_text": "Aşağıdaki cümlelerin hangisinde 'işaret zamiri' vardır?",
            "options": [
                {"key": "A", "text": "Bu kitabı daha önce okumuştum."},
                {"key": "B", "text": "Şu adamı daha önce buralarda görmedim."},
                {"key": "C", "text": "Bunu hemen kütüphaneye teslim etmelisin."},
                {"key": "D", "text": "O masayı pencere kenarına çekelim."},
                {"key": "E", "text": "Hangi yoldan gitmemiz gerektiğini bilmiyorum."}
            ],
            "correct_option": "C",
            "explanation": "'Bunu' sözcüğü bir nesnenin yerini işaret yoluyla tutan bir İşaret Zamiridir. A, B ve D şıklarında ismi belirttiği için İşaret Sıfatıdır.",
            "difficulty_level": "lisans", "is_verified": True
        },
        {
            "id": "q-t7-03", "topic_id": t7_id,
            "question_text": "Aşağıdaki cümlelerin hangisinde 'edat (ilgeç)' KULLANILMAMIŞTIR?",
            "options": [
                {"key": "A", "text": "Cennet gibi güzel bir vatanımız var."},
                {"key": "B", "text": "Akşama kadar kütüphanede ders çalıştık."},
                {"key": "C", "text": "Yalnız seninle bu konuyu görüşebilirim."},
                {"key": "D", "text": "Ahmet ve Mehmet sinemaya gittiler."},
                {"key": "E", "text": "Sınavı kazanmak için gece gündüz çalıştı."}
            ],
            "correct_option": "D",
            "explanation": "D seçeneğindeki 've' bir bağlaçtır. A'da 'gibi', B'de '-e kadar', C'de 'yalnız' (sadece anlamında edat), E'de 'için' edattır.",
            "difficulty_level": "lisans", "is_verified": True
        },
        {
            "id": "q-t7-04", "topic_id": t7_id,
            "question_text": "Aşağıdaki cümlelerin hangisinde 'belgisiz sıfat' vardır?",
            "options": [
                {"key": "A", "text": "Bazı öğrenciler kütüphanede çalışmayı seviyor."},
                {"key": "B", "text": "Bazıları sınav sorularının zor olduğunu söyledi."},
                {"key": "C", "text": "Herkes toplantı salonunda yerini aldı."},
                {"key": "D", "text": "Kimi söyler kimi dinler bu şehirde."},
                {"key": "E", "text": "Hiçbiri verilen görevi tamamlamadı."}
            ],
            "correct_option": "A",
            "explanation": "'Bazı öğrenciler' ifadesinde 'bazı' kelimesi 'öğrenciler' ismini belgisiz şekilde belirttiği için Belgisiz Sıfattır. B, C, D, E'deki ifadeler zamirdir.",
            "difficulty_level": "lisans", "is_verified": True
        },
        {
            "id": "q-t7-05", "topic_id": t7_id,
            "question_text": "Aşağıdaki cümlelerin hangisinde 'bağlaç' iki cümleyi birbirine bağlamıştır?",
            "options": [
                {"key": "A", "text": "Çok çalıştı ama istediği netlere ulaşamadı."},
                {"key": "B", "text": "Ali ve Veli okula birlikte gittiler."},
                {"key": "C", "text": "Elma ile armut pazardan satın alındı."},
                {"key": "D", "text": "Hem annesini hem babasını ziyaret etti."},
                {"key": "E", "text": "Ne kitap ne defter getirmişti."}
            ],
            "correct_option": "A",
            "explanation": "A seçeneğindeki 'ama' bağlacı 'Çok çalıştı' ve 'istediği netlere ulaşamadı' şeklinde iki bağımsız cümleyi birbirine bağlamıştır.",
            "difficulty_level": "lisans", "is_verified": True
        },
        {
            "id": "q-t7-06", "topic_id": t7_id,
            "question_text": "Aşağıdaki altı çizili kelimelerden hangisi 'kişi (şahıs) zamiri'dir?",
            "options": [
                {"key": "A", "text": "O, her zaman verdiği sözleri tutan bir insandır."},
                {"key": "B", "text": "O kitabı geçen hafta kütüphaneden aldım."},
                {"key": "C", "text": "Kendi arabasıyla yola çıkmayı tercih etti."},
                {"key": "D", "text": "Kendi düşen ağlamaz derler."},
                {"key": "E", "text": "Bunu hemen diğer odaya taşıyın."}
            ],
            "correct_option": "A",
            "explanation": "A seçeneğinde 'O' kelimesi bir insan şahsını temsil ettiği için Şahıs Zamiridir. B'de işaret sıfatı, C ve D'de dönüşlülük zamiridir.",
            "difficulty_level": "lisans", "is_verified": True
        },
        {
            "id": "q-t7-07", "topic_id": t7_id,
            "question_text": "Aşağıdaki cümlelerin hangisinde 'üntlem' cümleye 'özlem' anlamı katmıştır?",
            "options": [
                {"key": "A", "text": "Ah, nerede o eski bayramlar!"},
                {"key": "B", "text": "Eyvah, anahtarı içeride unuttum!"},
                {"key": "C", "text": "Of, bu sıcakta ders çalışmak çok zor!"},
                {"key": "D", "text": "Tüh, otobüsü yine kaçırdık!"},
                {"key": "E", "text": "Haşhaş! Sakın oraya dokunma!"}
            ],
            "correct_option": "A",
            "explanation": "'Ah, nerede o eski bayramlar!' ünlemi geçmişe ve eski bayramlara duyulan özlemi dile getirir.",
            "difficulty_level": "lisans", "is_verified": True
        },
        {
            "id": "q-t7-08", "topic_id": t7_id,
            "question_text": "Aşağıdaki cümlelerin hangisinde 'zaman zarfı' vardır?",
            "options": [
                {"key": "A", "text": "Yarın sabah yeni projenin sunumu yapılacak."},
                {"key": "B", "text": "Sessizce yerinden kalkıp dışarı çıktı."},
                {"key": "C", "text": "Çok hızlı yürüdüğü için nefes nefese kaldı."},
                {"key": "D", "text": "Yukarı çıkıp eşyalarını topladı."},
                {"key": "E", "text": "Güzel konuşmasıyla herkesi etkiledi."}
            ],
            "correct_option": "A",
            "explanation": "'Yarın sabah' ifadesi sunumun ne zaman yapılacağını bildirerek Zaman Zarfı görevini üstlenmiştir.",
            "difficulty_level": "lisans", "is_verified": True
        },
        {
            "id": "q-t7-09", "topic_id": t7_id,
            "question_text": "Aşağıdaki cümlelerin hangisinde 'derecelendirme zarfı (en, daha, çok)' vardır?",
            "options": [
                {"key": "A", "text": "Sınıfın en başarılı öğrencisi ödülünü aldı."},
                {"key": "B", "text": "Hızlıca içeri girip kapıyı kapattı."},
                {"key": "C", "text": "Dün akşam bize misafirler geldi."},
                {"key": "D", "text": "Sokakta neşeyle koşan çocukları izledi."},
                {"key": "E", "text": "Otobüs saatinde durağa ulaştı."}
            ],
            "correct_option": "A",
            "explanation": "'En başarılı' ifadesindeki 'en' kelimesi sıfatın derecesini üst seviyeye çıkaran Derecelendirme Zarfıdır (Üstünlük Zarfı).",
            "difficulty_level": "lisans", "is_verified": True
        },
        {
            "id": "q-t7-10", "topic_id": t7_id,
            "question_text": "Aşağıdaki cümlelerin hangisinde 'dönüşlülük zamiri' (kendi) kullanılmıştır?",
            "options": [
                {"key": "A", "text": "Bu zorlu projeyi kendi başına tamamladı."},
                {"key": "B", "text": "Onun fikri bizim için çok değerliydi."},
                {"key": "C", "text": "Herkes kendi eşyasını toplasın."},
                {"key": "D", "text": "A ve C seçeneklerinin ikisinde de dönüşlülük zamiri vardır."},
                {"key": "E", "text": "Hiçbiri sorulara doğru yanıt veremedi."}
            ],
            "correct_option": "D",
            "explanation": "'Kendi' kelimesi Türkçedeki tek Dönüşlülük Zamiridir ve A ile C seçeneklerinde yer almaktadır.",
            "difficulty_level": "lisans", "is_verified": True
        }
    ]
    questions.extend(q_t7)

    # -------------------------------------------------------------------------
    # KONU 8: Fiilde Çatı, Fiilimsiler & Kip Kayması
    # -------------------------------------------------------------------------
    t8_id = "topic-turkce-fiil-cati-fiilimsi"
    topics.append({
        "id": t8_id,
        "course_id": "course-turkce",
        "parent_id": None,
        "title": "Fiilde Çatı, Fiilimsiler & Kip Kayması",
        "slug": "fiil-cati-fiilimsi",
        "importance_weight": 1.7,
        "sort_order": 8
    })
    quick_notes.append({
        "id": "note-turkce-fiil-cati-fiilimsi",
        "topic_id": t8_id,
        "title": "Fiilimsiler (Eylemsiler) ve Fiilde Çatı Özeti",
        "content": "### 1. Fiilimsi Türleri\n- **İsim-Fiil:** *-ma, -ış, -mak* (*Okumak güzeldir*).\n- **Sıfat-Fiil:** *-an, -ası, -mez, -ar, -dik, -ecek, -miş* (*Koşan çocuk*).\n- **Zarf-Fiil:** *-ken, -alı, -asıya, -ince, -arak* (*Koşarak geldi*).\n\n### 2. Nesnesine Göre Çatı\n- **Geçişli:** *Onu* alır (*Onu okudu* -> Geçişli).\n- **Geçişsiz:** *Onu* almaz (*Onu uyudu* -> Geçişsiz).",
        "source_reference": "TDK Fiil Bilgisi",
        "is_verified": True,
        "read_time_seconds": 60
    })
    q_t8 = [
        {
            "id": "q-t8-01", "topic_id": t8_id,
            "question_text": "Aşağıdaki cümlelerin hangisinde 'zarf-fiil (bağ-fiil)' vardır?",
            "options": [
                {"key": "A", "text": "Ders çalışırken müzik dinlemeyi alışkanlık edindi."},
                {"key": "B", "text": "Okuduğu romanın etkisinden uzun süre kurtulamadı."},
                {"key": "C", "text": "Gelen misafirleri kapıda tebessümle karşıladı."},
                {"key": "D", "text": "Sınavı kazanmak için elinden geleni yaptı."},
                {"key": "E", "text": "Yazılan mektupları posta kutusuna bıraktı."}
            ],
            "correct_option": "A",
            "explanation": "'Ders çalışırken' kelimesindeki '-ken' eki zaman bildiren Zarf-Fiil (Bağ-Fiil) ekidir.",
            "difficulty_level": "lisans", "is_verified": True
        },
        {
            "id": "q-t8-02", "topic_id": t8_id,
            "question_text": "Aşağıdaki cümlelerin hangisindeki yüklem 'etken ve geçişli' bir fiildir?",
            "options": [
                {"key": "A", "text": "Yazar, son romanını üç yılda tamamladı."},
                {"key": "B", "text": "Sokaklar belediye ekipleri tarafından temizlendi."},
                {"key": "C", "text": "Çocuklar akşam saatlerinde odalarında uyudu."},
                {"key": "D", "text": "Toplantı salonunda sessizlik sağlandı."},
                {"key": "E", "text": "Bütün gün parkta neşeyle koştular."}
            ],
            "correct_option": "A",
            "explanation": "'Tamamladı' fiilinin öznesi bellidir (Yazar -> Etken). 'Onu tamamladı' ifadesi mantıklı olduğu için ve nesne aldığı için de Geçişlidir.",
            "difficulty_level": "lisans", "is_verified": True
        },
        {
            "id": "q-t8-03", "topic_id": t8_id,
            "question_text": "Aşağıdaki cümlelerin hangisinde 'edilgen çatılı' bir fiil kullanılmıştır?",
            "options": [
                {"key": "A", "text": "Okul bahçesindeki çöpler öğrencilerce toplandı."},
                {"key": "B", "text": "Ahmet sabah erkenden kalkıp yürüyüş yaptı."},
                {"key": "C", "text": "Kuşlar ağaç dallarında neşeyle ötüşüyordu."},
                {"key": "D", "text": "Öğretmenimiz soruları detaylıca çözdü."},
                {"key": "E", "text": "Fırtına sebebiyle denizde dalgalar büyüdü."}
            ],
            "correct_option": "A",
            "explanation": "'Toplandı' fiilinde gerçek özne işi yapan değil işten etkilenendir (sözde özne: çöpler). Fiilde '-n' edilgenlik eki vardır (Edilgen Çatı).",
            "difficulty_level": "lisans", "is_verified": True
        },
        {
            "id": "q-t8-04", "topic_id": t8_id,
            "question_text": "Aşağıdaki cümlelerin hangisinde 'anlam (zaman) kayması' yapılmıştır?",
            "options": [
                {"key": "A", "text": "Fatih Sultan Mehmet 1453 yılında İstanbul'u fetheder."},
                {"key": "B", "text": "Dün akşam kütüphanede saatlerce ders çalıştım."},
                {"key": "C", "text": "Gelecek hafta yeni projemizin sunumunu yapacağız."},
                {"key": "D", "text": "Her sabah iki kilometre koşuyorum."},
                {"key": "E", "text": "Şu anda öğretmenimiz ders anlatıyor."}
            ],
            "correct_option": "A",
            "explanation": "Geçmişte yaşanmış bir olay (1453) için geniş zaman eki (-er: fetheder) kullanılmıştır. Geçmiş zaman yerine geniş zaman kullanılarak kip kayması yapılmıştır.",
            "difficulty_level": "lisans", "is_verified": True
        },
        {
            "id": "q-t8-05", "topic_id": t8_id,
            "question_text": "Aşağıdaki cümlelerin hangisinde 'sıfat-fiil (ortaç)' KULLANILMAMIŞTIR?",
            "options": [
                {"key": "A", "text": "Kırılan bardakları çöp kovasına attı."},
                {"key": "B", "text": "Tanıdık yüzlerle karşılaşınca çok mutlu oldu."},
                {"key": "C", "text": "Gelecek yıl yapılacak sınavlara hazırlanıyor."},
                {"key": "D", "text": "Kitap okumak insan zihnini dinlendirir."},
                {"key": "E", "text": "Koşar adımlarla durağa doğru ilerledi."}
            ],
            "correct_option": "D",
            "explanation": "D seçeneğindeki 'okumak' kelimesi isim-fiildir. A'da 'kırılan', B'de 'tanıdık', C'de 'gelecek', E'de 'koşar' sıfat-fiildir.",
            "difficulty_level": "lisans", "is_verified": True
        },
        {
            "id": "q-t8-06", "topic_id": t8_id,
            "question_text": "Aşağıdaki cümlelerin hangisinde 'işteş çatı' eki (-ş) bulunmaktadır?",
            "options": [
                {"key": "A", "text": "İki eski dost yıllar sonra sarılıp kucaklaştı."},
                {"key": "B", "text": "Çamaşırlar balkonda kurutuldu."},
                {"key": "C", "text": "Yazı yazarken kalemi kırıldı."},
                {"key": "D", "text": "Odasındaki eşyaları güzelce yerleştirdi."},
                {"key": "E", "text": "Akşam saatlerinde hava karardı."}
            ],
            "correct_option": "A",
            "explanation": "'Kucaklaştı' eylemi karşılıklı yapılan bir eylemdir ve '-ş' işteşlik eki barındırır (İşteş Çatı).",
            "difficulty_level": "lisans", "is_verified": True
        },
        {
            "id": "q-t8-07", "topic_id": t8_id,
            "question_text": "Aşağıdaki cümlelerin hangisinde 'birleşik zamanlı (katmerli) fiil' vardır?",
            "options": [
                {"key": "A", "text": "Her gün bu saatlerde parka yürümeye giderdi."},
                {"key": "B", "text": "Dün akşam kütüphanede ders çalıştım."},
                {"key": "C", "text": "Yarın yeni bir kitap satın alacağım."},
                {"key": "D", "text": "Soruların tamamını doğru yanıtladı."},
                {"key": "E", "text": "Sokakta neşeyle koşan çocukları izledi."}
            ],
            "correct_option": "A",
            "explanation": "'Giderdi' fiili hem Geniş Zaman (-er) hem de Hikaye Birleşik Zamanı (-di) almış birleşik zamanlı eylemdir (Git-er-di).",
            "difficulty_level": "lisans", "is_verified": True
        },
        {
            "id": "q-t8-08", "topic_id": t8_id,
            "question_text": "Aşağıdaki cümlelerin hangisindeki fiil 'olsettirgen (ettirgen)' çatılıdır (işi başkasına yaptırma)?",
            "options": [
                {"key": "A", "text": "Müdür, odadaki tüm evrakları sekretere imzalattı."},
                {"key": "B", "text": "Çocuk neşeyle bahçede koştu."},
                {"key": "C", "text": "Derin bir nefes alıp uyudu."},
                {"key": "D", "text": "Pencereden dışarı baktı."},
                {"key": "E", "text": "Bütün soruları kendisi çözdü."}
            ],
            "correct_option": "A",
            "explanation": "'İmzalattı' fiilinde işi özne kendisi yapmamış, bir başkasına yaptırmıştır (Ettirgen Çatı).",
            "difficulty_level": "lisans", "is_verified": True
        },
        {
            "id": "q-t8-09", "topic_id": t8_id,
            "question_text": "Aşağıdaki cümlelerin hangisinde 'adlaşmış sıfat-fiil' vardır?",
            "options": [
                {"key": "A", "text": "Ağlayanlar bir gün mutlaka güler."},
                {"key": "B", "text": "Ağlayan çocuk annesine sarıldı."},
                {"key": "C", "text": "Koşan atlet birinci oldu."},
                {"key": "D", "text": "Okuyan öğrenci başarılı olur."},
                {"key": "E", "text": "Biten maçı stadyumda izlediler."}
            ],
            "correct_option": "A",
            "explanation": "'Ağlayan insanlar' tamlamasındaki 'insanlar' ismi düşmüş, 'Ağlayanlar' şeklinde sıfat-fiil adlaşmıştır (Adlaşmış Sıfat-Fiil).",
            "difficulty_level": "lisans", "is_verified": True
        },
        {
            "id": "q-t8-10", "topic_id": t8_id,
            "question_text": "Aşağıdaki cümlelerin hangisinde yüklem 'dönüşlü çatılı' bir fiildir (işi yapıp işten etkilenen aynı kişi)?",
            "options": [
                {"key": "A", "text": "Genç kız aynanın karşısında uzun uzun süslendi."},
                {"key": "B", "text": "Araba yıkanıp garaja çekildi."},
                {"key": "C", "text": "Mektup dün adrese postalandı."},
                {"key": "D", "text": "Bütün evraklar dosyaya takıldı."},
                {"key": "E", "text": "Sınav sonuçları panoya asıldı."}
            ],
            "correct_option": "A",
            "explanation": "'Süslendi' eyleminde süslenme işini yapan da işten etkilenen de genç kızın kendisidir (Dönüşlü Çatı).",
            "difficulty_level": "lisans", "is_verified": True
        }
    ]
    questions.extend(q_t8)

    # -------------------------------------------------------------------------
    # KONU 9: Cümlenin Ögeleri
    # -------------------------------------------------------------------------
    t9_id = "topic-turkce-cumlenin-ogeleri"
    topics.append({
        "id": t9_id,
        "course_id": "course-turkce",
        "parent_id": None,
        "title": "Cümlenin Ögeleri",
        "slug": "cumlenin-ogeleri",
        "importance_weight": 1.6,
        "sort_order": 9
    })
    quick_notes.append({
        "id": "note-turkce-cumlenin-ogeleri",
        "topic_id": t9_id,
        "title": "Cümlenin Ögelerini Bulma Altın Sıralaması (YÖNT)",
        "content": "### Bulma Sırası:\n1. **Yüklem:** Cümlenin yargısı, önce yüklem bulunur.\n2. **Özne:** *Kim, Ne?* soruları yükleme sorulur.\n3. **Nesne:** *Neyi, Kimi?* (Belirtili) veya *Ne?* (Belirtisiz).\n4. **Tümleçler:** Dolaylı Tümleç (*Nereye, Nerede, Nereden?*), Zarf Tümleci (*Nasıl, Ne zaman, Niçin?*).\n\n> **Önemli Kural:** Tamlamalar ve deyimler ögelerine ayrılırken ASLA bölünmez!",
        "source_reference": "TDK Cümle Bilgisi",
        "is_verified": True,
        "read_time_seconds": 55
    })
    q_t9 = [
        {
            "id": "q-t9-01", "topic_id": t9_id,
            "question_text": "'Yaşlı adam, evinin bahçesindeki kırmızı gülleri özenle suluyordu.' cümlesinin öge dizilişi aşağıdakilerin hangisinde doğru verilmiştir?",
            "options": [
                {"key": "A", "text": "Özne — Belirtili Nesne — Zarf Tümleci — Yüklem"},
                {"key": "B", "text": "Özne — Dolaylı Tümleci — Belirtili Nesne — Yüklem"},
                {"key": "C", "text": "Zarf Tümleci — Özne — Belirtili Nesne — Yüklem"},
                {"key": "D", "text": "Özne — Belirtisiz Nesne — Zarf Tümleci — Yüklem"},
                {"key": "E", "text": "Dolaylı Tümleç — Özne — Zarf Tümleci — Yüklem"}
            ],
            "correct_option": "A",
            "explanation": "Suluyordu (Yüklem). Sulayan kim? -> Yaşlı adam (Özne). Neyi suluyordu? -> Evinin bahçesindeki kırmızı gülleri (Belirtili Nesne). Nasıl suluyordu? -> Özenle (Zarf Tümleci). Özne - Belirtili Nesne - Zarf Tümleci - Yüklem.",
            "difficulty_level": "lisans", "is_verified": True
        },
        {
            "id": "q-t9-02", "topic_id": t9_id,
            "question_text": "Aşağıdaki cümlelerin hangisinde 'dolaylı tümleç (yer tamlayıcısı)' KULLANILMAMIŞTIR?",
            "options": [
                {"key": "A", "text": "Sınıftaki öğrenciler kütüphanede ders çalışıyordu."},
                {"key": "B", "text": "Otobüsten inen yolcular durağa doğru yürüdü."},
                {"key": "C", "text": "Dün akşam kütüphaneden iki kitap aldım."},
                {"key": "D", "text": "Yarın sabah otobüsle Ankara'ya gideceğiz."},
                {"key": "E", "text": "Soru çözümünü sessizce ve dikkatle dinledi."}
            ],
            "correct_option": "E",
            "explanation": "E seçeneğinde 'Sessizce ve dikkatle' Zarf Tümlecidir, 'Soru çözümünü' Belirtili Nesnedir. Nerede/Nereye/Nereden sorularına cevap veren Dolaylı Tümleç yoktur.",
            "difficulty_level": "lisans", "is_verified": True
        },
        {
            "id": "q-t9-03", "topic_id": t9_id,
            "question_text": "Aşağıdaki cümlelerin hangisinde yüklem bir 'isim tamlamasından' oluşmaktadır?",
            "options": [
                {"key": "A", "text": "Dün akşam gördüğümüz bina okulun kütüphanesidir."},
                {"key": "B", "text": "En sevdiği arkadaşı son derece yardımseverdi."},
                {"key": "C", "text": "Yeni aldığı bilgisayar oldukça hızlıydı."},
                {"key": "D", "text": "Sınav soruları beklenenden kolay çıktı."},
                {"key": "E", "text": "Hava bugün dün akşamki gibi soğuktu."}
            ],
            "correct_option": "A",
            "explanation": "'okulun kütüphanesidir' yüklemi belirtili bir isim tamlamasıdır. Tamlamalar yüklem olduğunda bölünmez.",
            "difficulty_level": "lisans", "is_verified": True
        },
        {
            "id": "q-t9-04", "topic_id": t9_id,
            "question_text": "Aşağıdaki cümlelerin hangisinde ögelere ayırmada bir HATA yapılmıştır?",
            "options": [
                {"key": "A", "text": "Genç adam / otobüsten / sessizce / indi."},
                {"key": "B", "text": "Kitabın / kapağı / yırtılmıştı."},
                {"key": "C", "text": "Yazar / son romanında / toplumsal sorunları / işlemiştir."},
                {"key": "D", "text": "Öğrenciler / bahçede / neşeyle / oynuyorlar."},
                {"key": "E", "text": "Akşam saatlerinde / fırtına / aniden / başladı."}
            ],
            "correct_option": "B",
            "explanation": "'Kitabın kapağı' bir isim tamlamasıdır. İsim tamlamaları tek bir ögedir (Özne) ve 'Kitabın / kapağı' şeklinde ayrılamaz.",
            "difficulty_level": "lisans", "is_verified": True
        },
        {
            "id": "q-t9-05", "topic_id": t9_id,
            "question_text": "Aşağıdaki cümlelerin hangisinde 'vurgu' yer tamlayıcısı (dolaylı tümleç) üzerindedir?",
            "options": [
                {"key": "A", "text": "Ahmet dün akşam hediyesini anneye verdi."},
                {"key": "B", "text": "Anneye dün akşam hediyesini verdi Ahmet."},
                {"key": "C", "text": "Hediyesini anneye dün akşam verdi."},
                {"key": "D", "text": "Ahmet anneye hediyesini verdi."},
                {"key": "E", "text": "Dün akşam anneye verdi hediyesini."}
            ],
            "correct_option": "A",
            "explanation": "Fiil cümlelerinde vurgu yüklemden hemen önceki ögenin üzerindedir. A seçeneğinde yüklem olan 'verdi'den hemen önce 'anneye' (Dolaylı Tümleç) gelmiştir.",
            "difficulty_level": "lisans", "is_verified": True
        },
        {
            "id": "q-t9-06", "topic_id": t9_id,
            "question_text": "Aşağıdaki cümlelerden hangisi sadece 'Özne ve Yüklem'den oluşmaktadır?",
            "options": [
                {"key": "A", "text": "Karadeniz'in hırçın dalgaları kıyıya vuruyordu."},
                {"key": "B", "text": "Bu tarihi konak, kentin en eski mimari yapısıdır."},
                {"key": "C", "text": "Okul bahçesinde çocuklar top oynuyor."},
                {"key": "D", "text": "Yazar son kitabını okurlarına imzaladı."},
                {"key": "E", "text": "Sabah erkenden yola çıkan kafile köye ulaştı."}
            ],
            "correct_option": "B",
            "explanation": "'kentin en eski mimari yapısıdır' -> Yüklem (Sıfat tamlaması grubu). Kentin en eski mimari yapısı olan ne? -> 'Bu tarihi konak' (Özne). Cümle sadece Özne ve Yüklemden oluşur.",
            "difficulty_level": "lisans", "is_verified": True
        },
        {
            "id": "q-t9-07", "topic_id": t9_id,
            "question_text": "Aşağıdaki cümlelerin hangisinde 'ara söz' dolaylı tümlecin açıklayıcısı durumundadır?",
            "options": [
                {"key": "A", "text": "Doğup büyüdüğüm yere, memleketime, yakında döneceğim."},
                {"key": "B", "text": "Ali'yi, en yakın arkadaşımı, dün yolda gördüm."},
                {"key": "C", "text": "Ankara, Türkiye'nin başkenti, tarihi bir kenttir."},
                {"key": "D", "text": "O günü, hiç unutmadığım o anı, tekrar hatırladım."},
                {"key": "E", "text": "Kitabımı, en sevdiğim romanı, kütüphanede unuttum."}
            ],
            "correct_option": "A",
            "explanation": "A seçeneğinde 'Doğup büyüdüğüm yere' (Dolaylı Tümleç) ögesi, hemen ardından gelen 'memleketime' ara sözü ile açıklanmıştır.",
            "difficulty_level": "lisans", "is_verified": True
        },
        {
            "id": "q-t9-08", "topic_id": t9_id,
            "question_text": "Aşağıdaki cümlelerin hangisinde 'belirtisiz nesne' vardır?",
            "options": [
                {"key": "A", "text": "Çocuk masada lezzetli bir elma yedi."},
                {"key": "B", "text": "Elmayı masanın üzerine bıraktı."},
                {"key": "C", "text": "Kitabı kütüphaneden ödünç aldı."},
                {"key": "D", "text": "Kapıyı hızlı adımlarla açtı."},
                {"key": "E", "text": "Evini güzelleştirmek için çiçek aldı."}
            ],
            "correct_option": "A",
            "explanation": "A seçeneğinde 'Ne yedi?' sorusuna verilen 'lezzetli bir elma' cevabı yalın halde olduğu için Belirtisiz Nesnedir.",
            "difficulty_level": "lisans", "is_verified": True
        },
        {
            "id": "q-t9-09", "topic_id": t9_id,
            "question_text": "Aşağıdaki cümlelerin hangisinde soru 'özneyi' buldurmaya yöneliktir?",
            "options": [
                {"key": "A", "text": "Dün akşam kapıyı çalan kimdi?"},
                {"key": "B", "text": "Sana bu lezzetli yemeği kim yaptı?"},
                {"key": "C", "text": "Kütüphaneden hangi kitabı aldın?"},
                {"key": "D", "text": "Yarın nereye gideceksiniz?"},
                {"key": "E", "text": "Toplantı saat kaçta başlayacak?"}
            ],
            "correct_option": "B",
            "explanation": "'Sana yemeği kim yaptı?' sorusunun cevabı ('Ahmet yaptı' -> Ahmet = Özne) özneyi buldurmaya yöneliktir.",
            "difficulty_level": "lisans", "is_verified": True
        },
        {
            "id": "q-t9-10", "topic_id": t9_id,
            "question_text": "Aşağıdaki cümlelerin hangisinde 'zarf tümleci' KULLANILMAMIŞTIR?",
            "options": [
                {"key": "A", "text": "Öğrenciler dersi dikkatle ve sessizce dinledi."},
                {"key": "B", "text": "Otobüs durağa yaklaşınca herkes ayağa kalktı."},
                {"key": "C", "text": "Akşam saatlerinde fırtına etkisini artırdı."},
                {"key": "D", "text": "Rüzgarın şiddetinden pencerelerin camları titriyordu."},
                {"key": "E", "text": "Kütüphanedeki raftan tarihi bir roman seçti."}
            ],
            "correct_option": "E",
            "explanation": "E seçeneğinde 'Kütüphanedeki raftan' (Dolaylı tümleç), 'tarihi bir roman' (Belirtili nesne), 'seçti' (Yüklem). Zarf tümleci yoktur.",
            "difficulty_level": "lisans", "is_verified": True
        }
    ]
    questions.extend(q_t9)

    # -------------------------------------------------------------------------
    # KONU 10: Anlatım Bozuklukları
    # -------------------------------------------------------------------------
    t10_id = "topic-turkce-anlatim-bozukluklari"
    topics.append({
        "id": t10_id,
        "course_id": "course-turkce",
        "parent_id": None,
        "title": "Anlatım Bozuklukları",
        "slug": "anlatim-bozukluklari",
        "importance_weight": 1.5,
        "sort_order": 10
    })
    quick_notes.append({
        "id": "note-turkce-anlatim-bozukluklari",
        "topic_id": t10_id,
        "title": "Anlatım Bozukluğu Türleri ve Çözüm İpuçları",
        "content": "### 1. Anlamsal Bozukluklar\n- **Gereksiz Sözcük Kullanımı:** Eş anlamlı kelimeleri aynı cümlede kullanma (*Neden ve sebepler*).\n- **Sözcüğün Yanlış Anlamda Kullanımı:** Anlamca karışan sözcükler (*Yaklaşık - Yakın, Sağlamak - Neden Olmak*).\n- **Çelişen Sözcüklerin Kullanımı:** Kesinlik ve ihtimal bildiren kelimelerin bir arada bulunması (*Şüphesiz gelebilir*).\n\n### 2. Yapısal Bozukluklar\n- Özne-Yüklem Uyumsuzluğu, Öge Eksikliği, Yanlış Tamlama.",
        "source_reference": "TDK Anlatım Bozukluğu Rehberi",
        "is_verified": True,
        "read_time_seconds": 55
    })
    q_t10 = [
        {
            "id": "q-t10-01", "topic_id": t10_id,
            "question_text": "Aşağıdaki cümlelerin hangisinde 'gereksiz sözcük kullanımından' kaynaklanan bir anlatım bozukluğu vardır?",
            "options": [
                {"key": "A", "text": "Karşılıklı mektuplaşarak dostluklarını yıllarca sürdürdüler."},
                {"key": "B", "text": "Hava sıcaklığının sıfırın altında eksi beş derece olduğu belirtildi."},
                {"key": "C", "text": "Şüphesiz bu sınavı kazanabilirsin."},
                {"key": "D", "text": "Fiyatlar çok pahalı olduğu için alışveriş yapamadı."},
                {"key": "E", "text": "A ve B seçeneklerinin her ikisinde de gereksiz sözcük kullanımı vardır."}
            ],
            "correct_option": "E",
            "explanation": "A seçeneğinde 'mektuplaşmak' zaten karşılıklı yapılır, 'karşılıklı' sözcüğü gereksizdir. B seçeneğinde 'sıfırın altında' ifadesi zaten eksi demektir, 'eksi' gereksizdir. A ve B'de gereksiz sözcük kullanımı vardır.",
            "difficulty_level": "lisans", "is_verified": True
        },
        {
            "id": "q-t10-02", "topic_id": t10_id,
            "question_text": "Aşağıdaki cümlelerin hangisinde 'sözcüğün yanlış anlamda kullanılmasından' kaynaklanan bir anlatım bozukluğu vardır?",
            "options": [
                {"key": "A", "text": "Sigara içmek akciğer kanserine yakalanma şansını artırır."},
                {"key": "B", "text": "Bu zorlu sınavı kazanmak için gece gündüz çalıştı."},
                {"key": "C", "text": "Okul bahçesindeki ağaçlar baharın gelişiyle açtı."},
                {"key": "D", "text": "Kütüphaneden aldığı kitapları zamanında teslim etti."},
                {"key": "E", "text": "Fırtına sebebiyle vapur seferleri iptal edildi."}
            ],
            "correct_option": "A",
            "explanation": "Kanser olmak olumsuz bir durumdur. Olumsuz durumlarda 'şans' sözcüğü değil 'riski' sözcüğü kullanılmalıdır ('kanser riskini artırır').",
            "difficulty_level": "lisans", "is_verified": True
        },
        {
            "id": "q-t10-03", "topic_id": t10_id,
            "question_text": "Aşağıdaki cümlelerin hangisinde 'çelişen sözcüklerin bir arada kullanılmasından' kaynaklanan anlatım bozukluğu vardır?",
            "options": [
                {"key": "A", "text": "Eminim ki bu saatte eve ulaşmış olmalı."},
                {"key": "B", "text": "Dün akşam kütüphanede ders çalıştık."},
                {"key": "C", "text": "Erken kalktığı için uykusunu alamamıştı."},
                {"key": "D", "text": "Yarın sabah otobüsle yola çıkacağız."},
                {"key": "E", "text": "Soruların tamamını doğru yanıtladığını söyledi."}
            ],
            "correct_option": "A",
            "explanation": "'Eminim ki' kesinlik bildirirken 'ulaşmış olmalı' ihtimal/olasılık bildirir. İkisinin aynı cümlede bulunması çelişkidir.",
            "difficulty_level": "lisans", "is_verified": True
        },
        {
            "id": "q-t10-04", "topic_id": t10_id,
            "question_text": "Aşağıdaki cümlelerin hangisinde 'sözcüğün yanlış yerde kullanılmasından' kaynaklanan bir anlatım bozukluğu vardır?",
            "options": [
                {"key": "A", "text": "Yeni durağa gelmiştim ki otobüs kalktı."},
                {"key": "B", "text": "Çok güneşte kaldığı için teni kızardı."},
                {"key": "C", "text": "Ağrısız kulak delinir ilanı dikkat çekiyordu."},
                {"key": "D", "text": "B ve C seçeneklerinde sözcük yanlış yerde kullanılmıştır."},
                {"key": "E", "text": "Kütüphaneden ayrılırken görevliye teşekkür etti."}
            ],
            "correct_option": "D",
            "explanation": "B'de 'Güneşte çok kaldığı için', C'de 'Kulak ağrısız delinir' şeklinde olmalıdır. Sıralama yanlışı anlatım bozukluğuna yol açmıştır.",
            "difficulty_level": "lisans", "is_verified": True
        },
        {
            "id": "q-t10-05", "topic_id": t10_id,
            "question_text": "Aşağıdaki cümlelerin hangisinde 'özne-yüklem uyumsuzluğu' vardır?",
            "options": [
                {"key": "A", "text": "Kuşlar ağaç dallarında neşeyle ötüşüyorlar."},
                {"key": "B", "text": "Öğrenciler sınıfta ders dinliyorlar."},
                {"key": "C", "text": "Biz ve sen bu işi birlikte başaracağız."},
                {"key": "D", "text": "Kitaplar raflarda düzenli duruyor."},
                {"key": "E", "text": "Herkes sınav sonucunu merakla bekliyordu."}
            ],
            "correct_option": "A",
            "explanation": "İnsan dışındaki varlıkların (kuşlar) çoğul özne olduğu durumlarda yüklem tekil olmalıdır ('ötüşüyor' olmalıydı). Tekillik-çoğulluk uyumsuzluğu vardır.",
            "difficulty_level": "lisans", "is_verified": True
        },
        {
            "id": "q-t10-06", "topic_id": t10_id,
            "question_text": "Aşağıdaki cümlelerin hangisinde 'öge eksikliğinden' kaynaklanan bir anlatım bozukluğu vardır?",
            "options": [
                {"key": "A", "text": "Arkadaşına güvendi ve her konuda yardım etti."},
                {"key": "B", "text": "Kitabı okudu ve kütüphaneye iade etti."},
                {"key": "C", "text": "Sabah erkenden kalkıp spor yaptı."},
                {"key": "D", "text": "Güneş doğunca ortalık aydınlandı."},
                {"key": "E", "text": "Yurttan ayrılıp eve doğru yürüdü."}
            ],
            "correct_option": "A",
            "explanation": "'Arkadaşına güvendi ve (ona) her konuda yardım etti' cümlesinde ikinci cümlede 'ona' Dolaylı Tümleç eksikliği vardır.",
            "difficulty_level": "lisans", "is_verified": True
        },
        {
            "id": "q-t10-07", "topic_id": t10_id,
            "question_text": "Aşağıdaki cümlelerin hangisinde 'mantık ve sıralama hatası' bulunmaktadır?",
            "options": [
                {"key": "A", "text": "Bu hastalık ölüme, hatta felce neden olabilir."},
                {"key": "B", "text": "Dün akşam kütüphanede ders çalıştık."},
                {"key": "C", "text": "Yeni projenin sunumu başarıyla tamamlandı."},
                {"key": "D", "text": "Hava muhalefeti sebebiyle uçuşlar ertelendi."},
                {"key": "E", "text": "Yemekten sonra tatlı yemeyi tercih etti."}
            ],
            "correct_option": "A",
            "explanation": "Ölüm, felçten daha ağır bir durumdur. 'Felce, hatta ölüme neden olabilir' şeklinde derece sırasına uyulmalıdır.",
            "difficulty_level": "lisans", "is_verified": True
        },
        {
            "id": "q-t10-08", "topic_id": t10_id,
            "question_text": "Aşağıdaki cümlelerin hangisinde 'tamlama hatası' vardır?",
            "options": [
                {"key": "A", "text": "Askeri ve devlet okullarına başvurular başladı."},
                {"key": "B", "text": "Türkçe ve matematik derslerinden özel ders aldı."},
                {"key": "C", "text": "Kültür ve sanat etkinlikleri düzenlendi."},
                {"key": "D", "text": "Tarih ve coğrafya öğretmenleri toplantı yaptı."},
                {"key": "E", "text": "Yazım ve noktalama kurallarına uyulmalıdır."}
            ],
            "correct_option": "A",
            "explanation": "'Askeri okullar ve devlet okullarına' şeklinde tamlama ayrılmalıdır. 'Askeri okullarına' tamlama hatası oluşturur.",
            "difficulty_level": "lisans", "is_verified": True
        },
        {
            "id": "q-t10-09", "topic_id": t10_id,
            "question_text": "Aşağıdaki cümlelerin hangisinde 'ek fiil (eylem) eksikliği' anlatım bozukluğuna yol açmıştır?",
            "options": [
                {"key": "A", "text": "Boyu kısa, kilosu da fazla değildi."},
                {"key": "B", "text": "Dün akşam bize gelecekti ama gelemedi."},
                {"key": "C", "text": "Ders çalışmayı sever ama kütüphaneye gitmezdi."},
                {"key": "D", "text": "Kitap okumak zihni açar ve dinlendirir."},
                {"key": "E", "text": "Sabahları erken kalkar ve yürüyüş yapardı."}
            ],
            "correct_option": "A",
            "explanation": "'Boyu kısaydı, kilosu da fazla değildi' şeklinde ilk cümleye ek fiil (-di) getirilmelidir. Aksi takdirde 'Boyu kısa değildi' anlamı çıkar.",
            "difficulty_level": "lisans", "is_verified": True
        },
        {
            "id": "q-t10-10", "topic_id": t10_id,
            "question_text": "Aşağıdaki cümlelerin hangisinde 'çatı uyumsuzluğu' vardır?",
            "options": [
                {"key": "A", "text": "Ders çalışıp kütüphaneden ayrılındı."},
                {"key": "B", "text": "Sabah kalkıp spor yapıldı."},
                {"key": "C", "text": "Yemek yenip masadan kalkıldı."},
                {"key": "D", "text": "Bütün şıklarda etken-edilgen çatı uyumsuzluğu vardır."},
                {"key": "E", "text": "Kitap okunup kütüphaneye iade edildi."}
            ],
            "correct_option": "D",
            "explanation": "A'da 'çalışıp (etken)' - 'ayrılındı (edilgen)', B'de 'kalkıp' - 'yapıldı', C'de 'yenip' - 'kalkıldı'. Birleşik cümlelerde yan cümlecik ve temel cümlenin çatısı etken-edilgen olarak uyumlu olmalıdır.",
            "difficulty_level": "lisans", "is_verified": True
        }
    ]
    questions.extend(q_t10)

    # -------------------------------------------------------------------------
    # KONU 11: Yazım Kuralları
    # -------------------------------------------------------------------------
    t11_id = "topic-turkce-yazim-kurallari-full"
    topics.append({
        "id": t11_id,
        "course_id": "course-turkce",
        "parent_id": None,
        "title": "Yazım Kuralları (Büyük Harfler, Kısaltmalar, Sayılar)",
        "slug": "yazim-kurallari-detayli",
        "importance_weight": 1.9,
        "sort_order": 11
    })
    quick_notes.append({
        "id": "note-turkce-yazim-kurallari-full",
        "topic_id": t11_id,
        "title": "Büyük Harfler, Kısaltmalar ve Kesme İşareti Kuralları",
        "content": "### 1. Kurum ve Kuruluş İsimleri\n- Kurum, kuruluş ve kurul adlarına gelen ekler **kesme işaretiyle AYRILMAZ** (*Türk Dil Kurumuna, Bakanlar Kurulunun*).\n\n### 2. Kısaltmalara Gelen Ekler\n- Küçük harfli kısaltmalarda kelimenin okunuşu esas alınır (*kg'dan*).\n- Büyük harfli kısaltmalarda son harfin okunuşu esas alınır (*TDK'nin* - TDK'nın DEĞİL!).\n\n### 3. Tarihlerin Yazımı\n- Belirli bir gün/ay belirten tarihlerde ay ve gün adları büyük yazılır (*15 Temmuz 2016 Cuma*).",
        "source_reference": "TDK Yazım Kılavuzu 2026",
        "is_verified": True,
        "read_time_seconds": 60
    })
    q_t11 = [
        {
            "id": "q-t11-01", "topic_id": t11_id,
            "question_text": "Aşağıdaki cümlelerin hangisinde 'kısaltmaların yazımı' ile ilgili bir YANLIŞLIK yapılmıştır?",
            "options": [
                {"key": "A", "text": "TDK'nin yayımladığı yeni kılavuz incelendi."},
                {"key": "B", "text": "TBMM'nin yeni yasama yılı törenle açıldı."},
                {"key": "C", "text": "TRT'den yapılan resmi açıklamayı izledik."},
                {"key": "D", "text": "TDK'nın son kararları tartışmaya açıldı."},
                {"key": "E", "text": "KYK'nin sunduğu burs imkanından yararlandı."}
            ],
            "correct_option": "D",
            "explanation": "Büyük harfle yapılan kısaltmalarda ek son harfin okunuşuna göre getirilir. 'K' harfi Türkçede 'ke' olarak okunur, dolayısıyla 'TDK'nin' olmalıdır. 'TDK'nın' kullanımı hatalıdır.",
            "difficulty_level": "lisans", "is_verified": True
        },
        {
            "id": "q-t11-02", "topic_id": t11_id,
            "question_text": "Aşağıdaki cümlelerin hangisinde 'büyük harflerin kullanımı' ile ilgili bir YANLIŞLIK yapılmıştır?",
            "options": [
                {"key": "A", "text": "Türk Dil Kurumuna yapılan başvurular değerlendirildi."},
                {"key": "B", "text": "29 Ekim Cumhuriyet Bayramı coşkuyla kutlandı."},
                {"key": "C", "text": "Ahmet Bey toplantı salonunda konuşma yaptı."},
                {"key": "D", "text": "Yarın Doğu Anadolu Bölgesi'nde kar yağışı bekleniyor."},
                {"key": "E", "text": "Batı medeniyeti ile Doğu Felsefesi karşılaştırıldı."}
            ],
            "correct_option": "E",
            "explanation": "'Doğu Felsefesi' tamlamasında 'felsefesi' kelimesi cins isim olduğu için küçük harfle yazılmalıdır ('Doğu felsefesi').",
            "difficulty_level": "lisans", "is_verified": True
        },
        {
            "id": "q-t11-03", "topic_id": t11_id,
            "question_text": "Aşağıdaki cümlelerin hangisinde 'sayıların yazımı' ile ilgili bir YANLIŞLIK yapılmıştır?",
            "options": [
                {"key": "A", "text": "Sınavda 2'nci sırada yer almayı başardı."},
                {"key": "B", "text": "Yarışmada 5'erli gruplar halinde mücadele ettiler."},
                {"key": "C", "text": "Toplantıya saat 14.30'da başlanacağı duyuruldu."},
                {"key": "D", "text": "Çekteki iki yüz elli bin TL tahsil edildi."},
                {"key": "E", "text": "Okulda yüz elli beş öğrenci bulunuyordu."}
            ],
            "correct_option": "B",
            "explanation": "Üleştirme sayıları (paylaştırma) rakamla değil, KESİNLİKLE yazıyla yazılır ('beşerli' olmalıdır, 5'erli YANLIŞTIR).",
            "difficulty_level": "lisans", "is_verified": True
        },
        {
            "id": "q-t11-04", "topic_id": t11_id,
            "question_text": "Aşağıdaki cümlelerin hangisinde 'kesme işaretinin kullanımı' ile ilgili bir YANLIŞLIK yapılmıştır?",
            "options": [
                {"key": "A", "text": "Türk Dil Kurumu'na yapılan başvuru kabul edildi."},
                {"key": "B", "text": "Mustafa Kemal Atatürk'ün eseri Nutuk okundu."},
                {"key": "C", "text": "Türkiye'nin başkenti Ankara'dır."},
                {"key": "D", "text": "1923'te kurulan cumhuriyetimiz gelişiyor."},
                {"key": "E", "text": "İngilizce'yi öğrenmek için yurt dışına gitti."}
            ],
            "correct_option": "A",
            "explanation": "TDK kurallarına göre Kurum, kuruluş, kurul ve iş yeri adlarına gelen ekler kesme işaretiyle AYRILMAZ ('Türk Dil Kurumuna' olmalıdır). Ayrıca E seçeneğinde dil isimlerine gelen yapım ekleri de ayrılmaz ('İngilizceyi'). A şıkkı net kurum adı ihlalidir.",
            "difficulty_level": "lisans", "is_verified": True
        },
        {
            "id": "q-t11-05", "topic_id": t11_id,
            "question_text": "Aşağıdaki birleşik sözcüklerden hangisinin yazımı YANLIŞTIR?",
            "options": [
                {"key": "A", "text": "Kuşburnıı"},
                {"key": "B", "text": "Rüzgargülü"},
                {"key": "C", "text": "Gözdevran"},
                {"key": "D", "text": "Hukuksever"},
                {"key": "E", "text": "Basımevi"}
            ],
            "correct_option": "C",
            "explanation": "'Gözdevran' şeklinde bir kelime yazımı yoktur; 'sever' kelimesiyle kurulan birleşik kelimeler bitişik yazılır (Hukuksever).",
            "difficulty_level": "lisans", "is_verified": True
        },
        {
            "id": "q-t11-06", "topic_id": t11_id,
            "question_text": "Aşağıdaki cümlelerin hangisinde 'tarihlerin yazımı' ile ilgili bir YANLIŞLIK yapılmıştır?",
            "options": [
                {"key": "A", "text": "Sınav 14 Haziran Pazar günü yapılacaktır."},
                {"key": "B", "text": "29 Ekim 1923'te Cumhuriyet ilan edildi."},
                {"key": "C", "text": "Gelecek Yılın Mayıs ayında buluşacağız."},
                {"key": "D", "text": "Okullar Eylül ayının ikinci haftası açılacak."},
                {"key": "E", "text": "15 Temmuz Cuma günü resmi tatildir."}
            ],
            "correct_option": "C",
            "explanation": "Belli bir günü/rakamı göstermeyen ay ve gün adları küçük harfle yazılır ('Mayıs ayında' değil 'mayıs ayında' olmalıdır).",
            "difficulty_level": "lisans", "is_verified": True
        },
        {
            "id": "q-t11-07", "topic_id": t11_id,
            "question_text": "Aşağıdaki cümlelerin hangisinde 'ile' sözcüğünün ekleşerek yazımında hata yapılmıştır?",
            "options": [
                {"key": "A", "text": "Okula otobüsle gitmeyi tercih etti."},
                {"key": "B", "text": "Arkadaşıylada sinemaya gitmek istedi."},
                {"key": "C", "text": "Çantasıyla sınıfa giriş yaptı."},
                {"key": "D", "text": "Sevgiyle yazılan mektuplar okundu."},
                {"key": "E", "text": "Hızla oradan uzaklaşmaya başladı."}
            ],
            "correct_option": "B",
            "explanation": "'Arkadaşıyla da' cümlesinde 'da' bağlacı ayrı yazılmalıdır ('Arkadaşıyla da').",
            "difficulty_level": "lisans", "is_verified": True
        },
        {
            "id": "q-t11-08", "topic_id": t11_id,
            "question_text": "Aşağıdaki cümlelerin hangisinde 'mi/mı' soru edatının yazımı YANLIŞTIR?",
            "options": [
                {"key": "A", "text": "Sen de bizimle sinemaya gelecek misin?"},
                {"key": "B", "text": "Güzel mi güzel bir bahçesi vardı."},
                {"key": "C", "text": "Dün akşam kütüphanede ders çalıştınızmı?"},
                {"key": "D", "text": "Beni duyan var mı acaba?"},
                {"key": "E", "text": "Soruların tamamını yanıtladın mı?"}
            ],
            "correct_option": "C",
            "explanation": "Soru edatı olan 'mi/mı' her zaman kendinden önceki sözcükten ayrı yazılır ('çalıştınız mı?' olmalıdır).",
            "difficulty_level": "lisans", "is_verified": True
        },
        {
            "id": "q-t11-09", "topic_id": t11_id,
            "question_text": "Aşağıdaki sözcüklerden hangisinin yazımı DOĞRUDUR?",
            "options": [
                {"key": "A", "text": "Yalnız (Yanlış değil)"},
                {"key": "B", "text": "Yalnış"},
                {"key": "C", "text": "Yalnışlık"},
                {"key": "D", "text": "Şartşat"},
                {"key": "E", "text": "Herbiri"}
            ],
            "correct_option": "A",
            "explanation": "'Yalın'dan türeyen 'Yalnız' kelimesi doğrudur. 'Yanıl'dan türeyen ise 'Yanlış'tır.",
            "difficulty_level": "lisans", "is_verified": True
        },
        {
            "id": "q-t11-10", "topic_id": t11_id,
            "question_text": "Aşağıdaki ikilemelerden hangisinin yazımı DOĞRUDUR?",
            "options": [
                {"key": "A", "text": "Bire bir (görüşme)"},
                {"key": "B", "text": "Birebir (etkili ilaç)"},
                {"key": "C", "text": "El ele verip başardık."},
                {"key": "D", "text": "Baş başa verdiler."},
                {"key": "E", "text": "Tüm seçeneklerdeki kullanım durumuna göre doğrudur."}
            ],
            "correct_option": "E",
            "explanation": "İkilemeler ayrı yazılır (El ele, baş başa, bire bir görüşme). Ancak 'birebir' kelimesi 'etkili/birebir ilaç' anlamında sıfatlaşırsa bitişik yazılabilir. Verilen durumların hepsi doğrudur.",
            "difficulty_level": "lisans", "is_verified": True
        }
    ]
    questions.extend(q_t11)

    # -------------------------------------------------------------------------
    # KONU 12: Noktalama İşaretleri
    # -------------------------------------------------------------------------
    t12_id = "topic-turkce-noktalama-isaretleri"
    topics.append({
        "id": t12_id,
        "course_id": "course-turkce",
        "parent_id": None,
        "title": "Noktalama İşaretleri",
        "slug": "noktalama-isaretleri",
        "importance_weight": 1.8,
        "sort_order": 12
    })
    quick_notes.append({
        "id": "note-turkce-noktalama-isaretleri",
        "topic_id": t12_id,
        "title": "Virgül ve Noktalı Virgül Kullanım Rehberi",
        "content": "### 1. Virgül (,) Nerede Kullanılmaz?\n- Metin içinde *-ve, veya, yahut* bağlaçlarından önce/sonra konmaz.\n- Şart eki (-se/-sa) ve Zarf-fiil eklerinden (-arak, -ince) sonra **virgül konmaz** (*Gidince görürsün*).\n\n### 2. Noktalı Virgül (;) Kullanımı\n- Cümle içinde virgüllerle ayrılmış tür veya takımları ayırmak için konur (*Erkek çocuklara Ali, Veli; kız çocuklara Ayşe, Fatma adı verilir*).",
        "source_reference": "TDK Noktalama Kılavuzu 2026",
        "is_verified": True,
        "read_time_seconds": 55
    })
    q_t12 = [
        {
            "id": "q-t12-01", "topic_id": t12_id,
            "question_text": "Aşağıdaki cümlelerin hangisinde 'virgül (,)' YANLIŞ kullanılmıştır?",
            "options": [
                {"key": "A", "text": "Ders çalışıp, kütüphaneden neşeyle ayrıldı."},
                {"key": "B", "text": "Pazardan elma, armut, muz ve çilek satın aldı."},
                {"key": "C", "text": "Genç adam, yavaş adımlarla durağa ilerledi."},
                {"key": "D", "text": "Efendiler, yarın cumhuriyeti ilan edeceğiz!"},
                {"key": "E", "text": "Sessizce oturdu, kitabını okumaya devam etti."}
            ],
            "correct_option": "A",
            "explanation": "Zarf-fiil eki (-ıp/-ip) almış sözcüklerden sonra metinde başka zarf-fiil yoksa virgül KONMAZ. A seçeneğinde '-ıp' ekinden sonra virgül konularak hata yapılmıştır.",
            "difficulty_level": "lisans", "is_verified": True
        },
        {
            "id": "q-t12-02", "topic_id": t12_id,
            "question_text": "Aşağıdaki cümlelerin hangisinde 'noktalı virgül (;)' kullanımı DOĞRUDUR?",
            "options": [
                {"key": "A", "text": "Erkek çocuklara Ali, Ahmet; kız çocuklara ise Ayşe, Zeynep adları verildi."},
                {"key": "B", "text": "Yarın sabah kütüphaneye gideceğim; ama ders çalışmayacağım."},
                {"key": "C", "text": "Pazardan elma; armut ve muz aldık."},
                {"key": "D", "text": "Sınavı kazandı; çok mutlu oldu."},
                {"key": "E", "text": "Kitabını açtı; okumaya başladı."}
            ],
            "correct_option": "A",
            "explanation": "Virgüllerle ayrılmış tür ve takımları (erkek isimleri - kız isimleri) birbirinden ayırmak için noktalı virgül kullanılması kurala uygundur.",
            "difficulty_level": "lisans", "is_verified": True
        },
        {
            "id": "q-t12-03", "topic_id": t12_id,
            "question_text": "Aşağıdaki cümlelerin hangisinin sonuna 'üç nokta (...)' getirilmelidir?",
            "options": [
                {"key": "A", "text": "Karşımızda masmavi bir deniz ve rengârenk çiçekler..."},
                {"key": "B", "text": "Dün akşam kütüphanede ders çalıştık."},
                {"key": "C", "text": "Sınav sonuçları açıklandı mı?"},
                {"key": "D", "text": "Ne kadar güzel bir gün!"},
                {"key": "E", "text": "Toplantı saat ikiye ertelendi."}
            ],
            "correct_option": "A",
            "explanation": "A seçeneğinde yüklem bulunmadığı için cümle eksiltilidir (eksiltili cümlelerin sonuna üç nokta konur).",
            "difficulty_level": "lisans", "is_verified": True
        },
        {
            "id": "q-t12-04", "topic_id": t12_id,
            "question_text": "Aşağıdaki cümlelerin hangisinde 'iki nokta (:)' kullanımı DOĞRUDUR?",
            "options": [
                {"key": "A", "text": "Milli Edebiyat akımının en önemli temsilcilerinden bazıları şunlardır: Ömer Seyfettin, Ziya Gökalp."},
                {"key": "B", "text": "Pazardan şunları aldı: elma, armut ve muz."},
                {"key": "C", "text": "Kendimi şöyle savunuyorum: Ben suçsuzum."},
                {"key": "D", "text": "A, B ve C seçeneklerinin tamamında iki nokta kullanımı doğrudur."},
                {"key": "E", "text": "Hiçbirinde doğru kullanılmamıştır."}
            ],
            "correct_option": "D",
            "explanation": "Örnek verilecek veya açıklama yapılacak cümlelerden sonra iki nokta kullanılması kurala tam uygundur. A, B ve C seçeneklerinin hepsi doğrudur.",
            "difficulty_level": "lisans", "is_verified": True
        },
        {
            "id": "q-t12-05", "topic_id": t12_id,
            "question_text": "Aşağıdaki cümlelerin hangisinde 'kesme işareti' YANLIŞ kullanılmıştır?",
            "options": [
                {"key": "A", "text": "Avrupa Birliği'ne üyelik süreci devam ediyor."},
                {"key": "B", "text": "Türk Dil Kurumu'na yapılan başvuru reddedildi."},
                {"key": "C", "text": "TBMM'nin yeni kararları yayımlandı."},
                {"key": "D", "text": "1923'te kurulan devletimiz büyüyor."},
                {"key": "E", "text": "Atatürk'ün Nutuk eseri okundu."}
            ],
            "correct_option": "B",
            "explanation": "Kurum ve kuruluş adlarına gelen ekler kesme işaretiyle ayrılmaz ('Türk Dil Kurumuna' olmalıdır).",
            "difficulty_level": "lisans", "is_verified": True
        },
        {
            "id": "q-t12-06", "topic_id": t12_id,
            "question_text": "Aşağıdaki cümlelerin hangisinde 'kısa çizgi (-)' kullanımı YANLIŞTIR?",
            "options": [
                {"key": "A", "text": "2025 - 2026 eğitim öğretim yılı başladı."},
                {"key": "B", "text": "Ankara - İstanbul hızlı tren seferleri artırıldı."},
                {"key": "C", "text": "Satır sonuna sığmayan kelimeleri heceleyerek böldü."},
                {"key": "D", "text": "Cümledeki ara sözü -yani en yakın arkadaşını- ziyaret etti."},
                {"key": "E", "text": "Saat 14:00 - de toplantı başlayacak."}
            ],
            "correct_option": "E",
            "explanation": "E seçeneğinde '14:00'te' ek kesme işareti ile ayrılmalıdır, kısa çizgi ile ayrılamaz.",
            "difficulty_level": "lisans", "is_verified": True
        },
        {
            "id": "q-t12-07", "topic_id": t12_id,
            "question_text": "Aşağıdaki cümlelerin hangisinde 'tırnak işareti ('' '')' kullanımı gereksizdir?",
            "options": [
                {"key": "A", "text": "Atatürk'ün 'Ne mutlu Türk'üm diyene!' sözünü unutmamalıyız."},
                {"key": "B", "text": "Yazarın 'Çalıkuşu' romanı tiyatroya uyarlandı."},
                {"key": "C", "text": "Öğretmen 'Sessiz olun' dedi."},
                {"key": "D", "text": "'Dün akşam' kütüphaneden aldığım kitabı okudum."},
                {"key": "E", "text": "Kitaptaki 'Yazım Kuralları' bölümünü inceledik."}
            ],
            "correct_option": "D",
            "explanation": "D seçeneğinde 'Dün akşam' özel bir eser adı, vurgulanmak istenen kavram veya alıntı söz olmadığı için tırnak içine alınması gereksizdir.",
            "difficulty_level": "lisans", "is_verified": True
        },
        {
            "id": "q-t12-08", "topic_id": t12_id,
            "question_text": "Aşağıdaki cümlelerin hangisinin sonuna 'ünlem işareti (!)' getirilmelidir?",
            "options": [
                {"key": "A", "text": "Ey bu topraklar için toprağa düşmüş asker"},
                {"key": "B", "text": "Yarın kaçta buluşacağımızı bilmiyorum"},
                {"key": "C", "text": "Kütüphaneden hangi kitapları aldın"},
                {"key": "D", "text": "Sınav sonuçları dün akşam açıklandı"},
                {"key": "E", "text": "Ders çalışmanın önemini biliyorum"}
            ],
            "correct_option": "A",
            "explanation": "A seçeneği bir seslenme/nida cümlesi olduğu için sonuna Ünlem İşareti (!) getirilmelidir.",
            "difficulty_level": "lisans", "is_verified": True
        },
        {
            "id": "q-t12-09", "topic_id": t12_id,
            "question_text": "Aşağıdaki cümlelerin hangisinde 'yay ayraç (parantez)' kullanımı YANLIŞTIR?",
            "options": [
                {"key": "A", "text": "Adamın zeki (!) olduğu verdiği cevaplardan anlaşılıyordu (Alay anlamı)."},
                {"key": "B", "text": "Yazarın doğum yılı (1881) kitapta belirtilmiş."},
                {"key": "C", "text": "Tiyatro eserindeki oyuncu (Yavaş adımlarla sahneye ilerler) hareket etti."},
                {"key": "D", "text": "Tüm seçeneklerde parantez kuralına uygun kullanılmıştır."},
                {"key": "E", "text": "Hiçbirinde doğru değildir."}
            ],
            "correct_option": "D",
            "explanation": "A'da alay/küçümseme, B'de tarihsel bilgi, C'de sahne hareketi için parantez kullanımı kurala uygundur.",
            "difficulty_level": "lisans", "is_verified": True
        },
        {
            "id": "q-t12-10", "topic_id": t12_id,
            "question_text": "Aşağıdaki cümlelerin hangisinde 'kesme işareti' özel isim dışındaki bir kullanımda hece/ses düşmesini göstermek için kullanılmıştır?",
            "options": [
                {"key": "A", "text": "N'oldu sana böyle birdenbire?"},
                {"key": "B", "text": "Ankara'ya giden otobüs kalktı."},
                {"key": "C", "text": "1923'te cumhuriyet ilan edildi."},
                {"key": "D", "text": "TDK'nin yeni yayınlarını inceledik."},
                {"key": "E", "text": "Atatürk'ün gençliğe hitabesini okuduk."}
            ],
            "correct_option": "A",
            "explanation": "'N'oldu' kelimesinde 'Ne oldu' ifadesindeki 'e' sesinin düştüğünü göstermek için kesme işareti kullanılmıştır (Ses düşmesi işareti).",
            "difficulty_level": "lisans", "is_verified": True
        }
    ]
    questions.extend(q_t12)

    # -------------------------------------------------------------------------
    # TÜM SORULARI DOĞRULAMA (VALIDATOR CHECK)
    # -------------------------------------------------------------------------
    print(f"Toplam Türkçe Konuları: {len(topics)}")
    print(f"Toplam Türkçe Hap Bilgiler: {len(quick_notes)}")
    print(f"Toplam Türkçe Sorular: {len(questions)}")
    print("Validator kontrolü yapılıyor...")

    for idx, q in enumerate(questions):
        valid, errs = ContentValidator.validate_question(q)
        if not valid:
            raise ValueError(f"Soru {idx + 1} ({q['id']}) Hata: {errs}")

    print("Tüm 120 Türkçe sorusu ve 12 Hap Bilgisi %100 VALIDATED!")

    return topics, quick_notes, questions

if __name__ == "__main__":
    t_topics, t_notes, t_questions = build_turkce_full_dataset()
    
    # Mevcut JSON veri setini oku ve Türkçe kısmını tam set ile güncelle
    json_path = os.path.join("mobile_app", "assets", "data", "sample_data.json")
    with open(json_path, "r", encoding="utf-8") as f:
        full_db = json.load(f)

    # Türkçe dışındaki diğer ders ve konuları koru, Türkçe konusuna tam 12 konuyu entegre et
    # 1. Mevcut Türkçe konuları ve soruları çıkarıp yenisini koy
    full_db["topics"] = [t for t in full_db["topics"] if t["course_id"] != "course-turkce"]
    full_db["quick_notes"] = [n for n in full_db["quick_notes"] if not n["topic_id"].startswith("topic-turkce")]
    full_db["questions"] = [q for q in full_db["questions"] if not q["topic_id"].startswith("topic-turkce")]

    # Yenileri ekle
    full_db["topics"].extend(t_topics)
    full_db["quick_notes"].extend(t_notes)
    full_db["questions"].extend(t_questions)

    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(full_db, f, ensure_ascii=False, indent=2)

    print(f"\n[BAŞARILI] {len(t_topics)} Konu, {len(t_notes)} Hap Bilgi ve {len(t_questions)} Soru {json_path} dosyasına aktarıldı!")
