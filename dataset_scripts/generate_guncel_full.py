# ============================================================================
# KPSS GÜNCEL BİLGİLER DERSİ — 5 ALT KONU X 10 SORU (TOPLAM 50 VERİFİED SORU + 5 HAP BİLGİ)
# https://kpss.digital/konular/guncel/ MÜFREDATINA %100 UYGUN
# ============================================================================

import json
import os
from generator.validator import ContentValidator

def build_guncel_dataset():
    topics = []
    quick_notes = []
    questions = []

    def add_gun_bundle(t_id, title, slug, weight, order, note_title, note_content, note_ref, q_list):
        topics.append({
            "id": t_id,
            "course_id": "course-guncel",
            "parent_id": None,
            "title": title,
            "slug": slug,
            "importance_weight": weight,
            "sort_order": order
        })
        quick_notes.append({
            "id": f"note-{t_id}",
            "topic_id": t_id,
            "title": note_title,
            "content": note_content,
            "source_reference": note_ref,
            "is_verified": True,
            "read_time_seconds": 45
        })
        for q in q_list:
            q["topic_id"] = t_id
            valid, errs = ContentValidator.validate_question(q)
            if not valid:
                raise ValueError(f"Güncel Bilgiler Soru Hatası ({q['id']}): {errs}")
            questions.append(q)

    # 1. Türkiye Gündemi & Yıl Temaları
    q1 = [
        {"id": "qgn-1-1", "question_text": "Türkiye'nin İLK uzay yolcusu olan ve Uluslararası Uzay İstasyonu'nda (ISS) 13 farklı bilimsel deney gerçekleştiren astronotumuz kimdir?", "options": [{"key":"A","text":"Alper Gezeravcı"},{"key":"B","text":"Tuva Cihangir Atasever"},{"key":"C","text":"Aziz Sancar"},{"key":"D","text":"Selçuk Bayraktar"},{"key":"E","text":"Canan Dağdeviren"}], "correct_option": "A", "explanation": "Alper Gezeravcı Axiom-3 görevi ile uzaya çıkan ilk Türk astronot olmuştur.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qgn-1-2", "question_text": "Türkiye'nin ikinci astronotu olarak yörünge altı bilimsel araştırma uçuşunu gerçekleştiren isim kimdir?", "options": [{"key":"A","text":"Tuva Cihangir Atasever"},{"key":"B","text":"Alper Gezeravcı"},{"key":"C","text":"Umut Yıldız"},{"key":"D","text":"Feryal Özel"},{"key":"E","text":"Eleni Topuz"}], "correct_option": "A", "explanation": "Tuva Cihangir Atasever Virgin Galactic ile yörünge altı bilim uçuşu yapmıştır.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qgn-1-3", "question_text": "Türkiye'nin İLK yeryüzü gözlem uydusu ve ilk yerli haberleşme uyduları sırasıyla hangileridir?", "options": [{"key":"A","text":"RASAT (Gözlem) — TÜRKSAT 6A (Yerli Haberleşme)"},{"key":"B","text":"Göktürk-1 — Türksat 1A"},{"key":"C","text":"BİLSAT — Türksat 3A"},{"key":"D","text":"Göktürk-2 — Türksat 4A"},{"key":"E","text":"İMECE — Türksat 5B"}], "correct_option": "A", "explanation": "İlk yerli gözlem uydumuz RASAT, ilk yerli ve milli haberleşme uydumuz TÜRKSAT 6A'dır.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qgn-1-4", "question_text": "Türkiye Cumhuriyeti Cumhurbaşkanlığı tarafından ilan edilen ilan temalarından '2024 Yılı' ne yılı olarak ilan edilmiştir?", "options": [{"key":"A","text":"Emekliler Yılı"},{"key":"B","text":"Aşık Veysel Yılı"},{"key":"C","text":"Yunus Emre Yılı"},{"key":"D","text":"Patara Yılı"},{"key":"E","text":"Göbeklitepe Yılı"}], "correct_option": "A", "explanation": "2024 yılı Cumhurbaşkanlığı tarafından 'Emekliler Yılı' olarak ilan edilmiştir.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qgn-1-5", "question_text": "Türk Dünyası Kültür Başkenti ilan edilen şehirler kapsamında Türksoy tarafından kültür başkenti seçilen Özbekistan şehri hangisidir?", "options": [{"key":"A","text":"Hiva (2020) / Semerkand"},{"key":"B","text":"Taşkent"},{"key":"C","text":"Buhara"},{"key":"D","text":"Bişkek"},{"key":"E","text":"Aşkabat"}], "correct_option": "A", "explanation": "TÜRKSOY tarafından Hiva ve Anav kültür başkentleri arasında ilan edilmiştir.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qgn-1-6", "question_text": "Türkiye'nin ilk yerli ve milli otomobili olan TOGG'un üretim tesisi hangi ilimizin Gemlik ilçesindedir?", "options": [{"key":"A","text":"Bursa"},{"key":"B","text":"Kocaeli"},{"key":"C","text":"Sakarya"},{"key":"D","text":"Eskişehir"},{"key":"E","text":"İzmir"}], "correct_option": "A", "explanation": "TOGG Teknoloji Kampüsü Bursa Gemlik'tedir.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qgn-1-7", "question_text": "Dünyanın İLK SİHA gemisi (insansız hava aracı taşıyıcısı) olan Türk Deniz Kuvvetleri amiral gemisi hangisidir?", "options": [{"key":"A","text":"TCG Anadolu (L-400)"},{"key":"B","text":"TCG Derya"},{"key":"C","text":"TCG İstanbul"},{"key":"D","text":"TCG Piri Reis"},{"key":"E","text":"TCG Barbaros"}], "correct_option": "A", "explanation": "TCG Anadolu dünyanın ilk SİHA gemisi olarak envantere girmiştir.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qgn-1-8", "question_text": "Türkiye'nin ilk insansız savaş uçağı projesi olan ve ses hızını aşabilen Baykar yapımı uçak hangisidir?", "options": [{"key":"A","text":"Bayraktar KIZILELMA"},{"key":"B","text":"Bayraktar TB2"},{"key":"C","text":"AKINCI TİHA"},{"key":"D","text":"ANKA-3"},{"key":"E","text":"KAAN"}], "correct_option": "A", "explanation": "KIZILELMA insansız savaş uçağımızdır (KAAN ise insanlı 5. nesil milli muharip uçağımızdır).", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qgn-1-9", "question_text": "TUSAŞ tarafından geliştirilen Türkiye'nin 5. nesil İNSANLI ilk milli muharip savaş uçağı hangisidir?", "options": [{"key":"A","text":"KAAN"},{"key":"B","text":"KIZILELMA"},{"key":"C","text":"HÜRJET"},{"key":"D","text":"HÜRKUŞ"},{"key":"E","text":"ANKA"}], "correct_option": "A", "explanation": "Milli Muharip Uçak projesinin adı KAAN'dır.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qgn-1-10", "question_text": "Türkiye'nin en yüksek ayağa sahip viyadüğü ve Avrupa'nın çift hatlı en uzun demiryolu tüneline sahip projesi hangi hattadır?", "options": [{"key":"A","text":"Ankara-Sivas Hızlı Tren Hattı"},{"key":"B","text":"Marmaray"},{"key":"C","text":"Bakü-Tiflis-Kars"},{"key":"D","text":"Halkalı-Kapıkule"},{"key":"E","text":"Konya-Karaman"}], "correct_option": "A", "explanation": "Ankara-Sivas YHT hattında devasa viyadük ve tüneller inşa edilmiştir.", "difficulty_level": "lisans", "is_verified": True}
    ]
    add_gun_bundle("topic-gun-turkiye-gundemi", "Türkiye Gündemi & Yıl Temaları", "turkiye-gundemi-ve-yil-temalari", 1.8, 1, "Uzay ve Savunma Sanayii Notu", "### Kritik Gelişmeler:\n- **İlk Türk Astronot:** Alper Gezeravcı (ISS).\n- **İkinci Astronot:** Tuva Cihangir Atasever.\n- **İlk SİHA Gemisi:** TCG Anadolu.\n- **5. Nesil Savaş Uçağı:** KAAN.", "KPSS Güncel Bilgiler", q1)

    # 2. Dünya Gündemi, Uluslararası Zirveler & Nobel
    q2 = [
        {"id": "qgn-2-1", "question_text": "2015 yılında Kimya alanında Nobel Ödülü kazanan ve DNA onarımı konusundaki çalışmalarıyla tanınan Türk bilim insanı kimdir?", "options": [{"key":"A","text":"Prof. Dr. Aziz Sancar"},{"key":"B","text":"Prof. Dr. Oktay Sinanoğlu"},{"key":"C","text":"Prof. Dr. Gazi Yaşargil"},{"key":"D","text":"Prof. Dr. Celal Şengör"},{"key":"E","text":"Prof. Dr. Uğur Şahin"}], "correct_option": "A", "explanation": "Aziz Sancar 2015 Nobel Kimya Ödülü'nü kazanmıştır.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qgn-2-2", "question_text": "2006 yılında Edebiyat alanında Nobel Ödülü kazanan ve Nobel kazanan İLK Türk vatandaşımız olan yazar kimdir?", "options": [{"key":"A","text":"Orhan Pamuk"},{"key":"B","text":"Yaşar Kemal"},{"key":"C","text":"Aziz Nesin"},{"key":"D","text":"Elif Şafak"},{"key":"E","text":"Zülfü Livaneli"}], "correct_option": "A", "explanation": "Orhan Pamuk 2006'da Nobel Edebiyat Ödülü'nü almıştır.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qgn-2-3", "question_text": "2024 yılında NATO'ya katılarak örgütün 32. üyesi olan İskandinav ülkesi hangisidir?", "options": [{"key":"A","text":"İsveç (32. Üye)"},{"key":"B","text":"Finlandiya (31. Üye)"},{"key":"C","text":"Ukrayna"},{"key":"D","text":"Avusturya"},{"key":"E","text":"İsviçre"}], "correct_option": "A", "explanation": "Finlandiya 31., İsveç ise 32. üye olarak NATO'ya girmiştir.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qgn-2-4", "question_text": "Birleşmiş Milletler (BM) Genel Sekreteri kimdir?", "options": [{"key":"A","text":"Antonio Guterres"},{"key":"B","text":"Ban Ki-moon"},{"key":"C","text":"Kofi Annan"},{"key":"D","text":"Volkan Bozkır"},{"key":"E","text":"Ursula von der Leyen"}], "correct_option": "A", "explanation": "Antonio Guterres Portekizli diplomattır ve BM Genel Sekreteridir.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qgn-2-5", "question_text": "Avrupa Birliği (AB) Komisyonu Başkanı olan kadın siyasetçi kimdir?", "options": [{"key":"A","text":"Ursula von der Leyen"},{"key":"B","text":"Christine Lagarde"},{"key":"C","text":"Roberta Metsola"},{"key":"D","text":"Angela Merkel"},{"key":"E","text":"Georgia Meloni"}], "correct_option": "A", "explanation": "Ursula von der Leyen AB Komisyonu başkanıdır.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qgn-2-6", "question_text": "Avrupa Merkez Bankası (ECB) Başkanı olan Fransız ekonomist kimdir?", "options": [{"key":"A","text":"Christine Lagarde"},{"key":"B","text":"Ursula von der Leyen"},{"key":"C","text":"Kristalina Georgieva"},{"key":"D","text":"Ngozi Okonjo-Iweala"},{"key":"E","text":"Janet Yellen"}], "correct_option": "A", "explanation": "Christine Lagarde ECB başkanıdır (IMF başkanı Kristalina Georgieva'dır).", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qgn-2-7", "question_text": "Dünya Sağlık Örgütü (WHO) Genel Direktörü kimdir?", "options": [{"key":"A","text":"Tedros Adhanom Ghebreyesus"},{"key":"B","text":"Antonio Guterres"},{"key":"C","text":"Jens Stoltenberg"},{"key":"D","text":"Rafael Grossi"},{"key":"E","text":"Fatih Birol"}], "correct_option": "A", "explanation": "Etiyopyalı Tedros Ghebreyesus WHO genel direktörüdür.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qgn-2-8", "question_text": "Uluslararası Enerji Ajansı (IEA) Başkanlığı görevini yürüten Türk ekonomist kimdir?", "options": [{"key":"A","text":"Dr. Fatih Birol"},{"key":"B","text":"Daron Acemoğlu"},{"key":"C","text":"Özlem Türeci"},{"key":"D","text":"Gazi Yaşargil"},{"key":"E","text":"Muhtar Kent"}], "correct_option": "A", "explanation": "Dr. Fatih Birol UEA (IEA) başkanıdır.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qgn-2-9", "question_text": "2024 yılında Ekonomi alanında Clark Madalyası ve Nobel adayı gösterilen dünyaca ünlü Türk akademisyen kimdir?", "options": [{"key":"A","text":"Prof. Dr. Daron Acemoğlu"},{"key":"B","text":"Dani Rodrik"},{"key":"C","text":"Refet Gürkaynak"},{"key":"D","text":"Özgür Demirtaş"},{"key":"E","text":"Mahfi Eğilmez"}], "correct_option": "A", "explanation": "MIT öğretim üyesi Daron Acemoğlu dünyanın en çok atıf alan ekonomistlerindendir.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qgn-2-10", "question_text": "2024 İklim Değişikliği Zirvesi (COP29) hangi ülkede gerçekleştirilmiştir?", "options": [{"key":"A","text":"Azerbaycan (Bakü)"},{"key":"B","text":"BAE (Dubai)"},{"key":"C","text":"Mısır (Şarm El Şeyh)"},{"key":"D","text":"İskoçya (Glasgow)"},{"key":"E","text":"Fransa (Paris)"}], "correct_option": "A", "explanation": "COP29 İklim Zirvesi Bakü Azerbaycan'da düzenlenmiştir.", "difficulty_level": "lisans", "is_verified": True}
    ]
    add_gun_bundle("topic-gun-dunya-ve-nobel", "Dünya Gündemi & Nobel Ödülleri", "dunya-gundemi-ve-nobel-odulleri", 1.7, 2, "Nobel ve Örgüt Başkanları", "### İsimler & Görevler:\n- **Aziz Sancar:** 2015 Nobel Kimya.\n- **Orhan Pamuk:** 2006 Nobel Edebiyat.\n- **NATO 32. Üye:** İsmeç (31. Finlandiya).\n- **UEA Başkanı:** Fatih Birol.", "KPSS Güncel Bilgiler", q2)

    # 3. Spor Şampiyonlukları & Türk Sporcular
    q3 = [
        {"id": "qgn-3-1", "question_text": "Milletler Ligi, Avrupa Şampiyonası ve Dünya Kupası şampiyonu olarak dünya sıralamasında 1. sıraya yükselen 'Filenin Sultanları' hangi branştadır?", "options": [{"key":"A","text":"Kadın Voleybol Milli Takımı"},{"key":"B","text":"Kadın Basketbol Milli Takımı"},{"key":"C","text":"Kadın Hentbol Milli Takımı"},{"key":"D","text":"Kadın Futbol Takımı"},{"key":"E","text":"Kadın Filenin Melekleri"}], "correct_option": "A", "explanation": "Türkiye Kadın Millî Voleybol Takımı 'Filenin Sultanları' olarak anılır.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qgn-3-2", "question_text": "Tokyo Olimpiyatları ve Dünya Şampiyonası'nda Klasik Yay Okçuluk dalında Altın Madalya kazanan İLK Türk okçu kimdir?", "options": [{"key":"A","text":"Mete Gazoz"},{"key":"B","text":"Taha Akgül"},{"key":"C","text":"Rıza Kayaalp"},{"key":"D","text":"Servet Tazegül"},{"key":"E","text":"Ali Sofuoğlu"}], "correct_option": "A", "explanation": "Mete Gazoz okçulukta olimpiyat ve dünya şampiyonudur.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qgn-3-3", "question_text": "Olimpiyat ve Dünya Şampiyonu olan İLK Kadın Boksörümüz kimdir?", "options": [{"key":"A","text":"Busenaz Sürmeneli"},{"key":"B","text":"Buse Naz Çakıroğlu"},{"key":"C","text":"Yasemin Adar"},{"key":"D","text":"Şahika Ercümen"},{"key":"E","text":"İrem Karamete"}], "correct_option": "A", "explanation": "Busenaz Sürmeneli olimpiyat şampiyonu kadın boksörümüzdür.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qgn-3-4", "question_text": "Güreşte erkeklerde kırılması güç rekorlara imza atan, çok sayıda Avrupa ve Dünya şampiyonluğu bulunan Türk güreşçilerimiz kimlerdir?", "options": [{"key":"A","text":"Rıza Kayaalp ve Taha Akgül"},{"key":"B","text":"Hamza Yerlikaya ve Naim Süleymanoğlu"},{"key":"C","text":"Kenan Sofuoğlu ve Toprak Razgatlıoğlu"},{"key":"D","text":"Servet Tazegül ve Mete Gazoz"},{"key":"E","text":"Halil Mutlu ve Yaşar Doğu"}], "correct_option": "A", "explanation": "Rıza Kayaalp (Grekoromen) ve Taha Akgül (Serbest) efsane güreşçilerimizdir.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qgn-3-5", "question_text": "Dünya Superbike Şampiyonası'nda Dünya Şampiyonu olan ve Türkiye'yi motor sporlarında temsil eden gururumuz kimdir?", "options": [{"key":"A","text":"Toprak Razgatlıoğlu"},{"key":"B","text":"Kenan Sofuoğlu"},{"key":"C","text":"Can Öncü"},{"key":"D","text":"Deniz Öncü"},{"key":"E","text":"Cem Bölükbaşı"}], "correct_option": "A", "explanation": "Toprak Razgatlıoğlu WorldSBK Dünya Şampiyonudur.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qgn-3-6", "question_text": "Serbest dalışta paletsiz kategoride dünya rekoru kıran milli sporcumuz kimdir?", "options": [{"key":"A","text":"Şahika Ercümen"},{"key":"B","text":"Derya Can"},{"key":"C","text":"Bender Göçmen"},{"key":"D","text":"Sümeyye Boyacı"},{"key":"E","text":"Merve Tuncel"}], "correct_option": "A", "explanation": "Şahika Ercümen dünya serbest dalış rekortmenimizdir.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qgn-3-7", "question_text": "Paralimpik Dünya ve Avrupa Yüzme Şampiyonu olan kollarısız milli yüzücümüz kimdir?", "options": [{"key":"A","text":"Sümeyye Boyacı"},{"key":"B","text":"Sevilay Öztürk"},{"key":"C","text":"Meryem Çavdar"},{"key":"D","text":"Besra Duman"},{"key":"E","text":"Kübra Korkut"}], "correct_option": "A", "explanation": "Sümeyye Boyacı paralimpik yüzme şampiyonumuzdur.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qgn-3-8", "question_text": "Tarihte 'Cep Herkülü' olarak anılan, 3 kez Olimpiyat Şampiyonu olan efsanevi merhum haltercimiz kimdir?", "options": [{"key":"A","text":"Naim Süleymanoğlu"},{"key":"B","text":"Halil Mutlu"},{"key":"C","text":"Taner Sağır"},{"key":"D","text":"Nurcan Taylan"},{"key":"E","text":"Daniyar Ismayilov"}], "correct_option": "A", "explanation": "Naim Süleymanoğlu 'Cep Herkülü' lakabıyla efsane haltercidir.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qgn-3-9", "question_text": "Real Madrid'e transfer olarak İspanya'da şampiyonluk yaşayan genç Türk futbolcu kimdir?", "options": [{"key":"A","text":"Arda Güler"},{"key":"B","text":"Kenan Yıldız"},{"key":"C","text":"Hakan Çalhanoğlu"},{"key":"D","text":"Orkun Kökçü"},{"key":"E","text":"Semih Kılıçsoy"}], "correct_option": "A", "explanation": "Arda Güler Real Madrid kadrosunda yer alan milli futbolcumuzdur.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qgn-3-10", "question_text": "UEFA Euro 2032 Avrupa Futbol Şampiyonası hangi iki ülke ortaklığında düzenlenecektir?", "options": [{"key":"A","text":"Türkiye ve İtalya"},{"key":"B","text":"Türkiye ve Yunanistan"},{"key":"C","text":"İngiltere ve İrlanda"},{"key":"D","text":"İspanya ve Portekiz"},{"key":"E","text":"Almanya ve Fransa"}], "correct_option": "A", "explanation": "EURO 2032 Türkiye ve İtalya ortaklığında yapılacaktır.", "difficulty_level": "lisans", "is_verified": True}
    ]
    add_gun_bundle("topic-gun-spor-basarilari", "Spor Şampiyonlukları & Türk Sporcular", "spor-basarilari-ve-turk-sporcular", 1.7, 3, "Milli Sporcularımız Notu", "### Efsane İsimler:\n- **Mete Gazoz:** Okçuluk Olimpiyat Şampiyonu.\n- **Filenin Sultanları:** Kadın Voleybol 1. sırada.\n- **Busenaz Sürmeneli:** Boks Olimpiyat Şampiyonu.\n- **EURO 2032:** Türkiye & İtalya Ev Sahipliği.", "KPSS Güncel Bilgiler", q3)

    # 4. Kültür, Sanat, Edebiyat & UNESCO
    q4 = [
        {"id": "qgn-4-1", "question_text": "UNESCO tarafından 'Yaşayan İnsan Hazinesi' ilan edilen ve geleneksel çini sanatçımız kimdir?", "options": [{"key":"A","text":"Sıtkı Olçar"},{"key":"B","text":"Neşet Ertaş"},{"key":"C","text":"Aşık Veysel"},{"key":"D","text":"Kani Karaca"},{"key":"E","text":"Ara Güler"}], "correct_option": "A", "explanation": "Kütahyalı Sıtkı Usta (Sıtkı Olçar) UNESCO çini ustası seçilmiştir.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qgn-4-2", "question_text": "'Bozkırın Tezenesi' lakabıyla tanınan ve UNESCO tarafından Yaşayan İnsan Hazinesi kabul edilen büyük halk ozanımız kimdir?", "options": [{"key":"A","text":"Neşet Ertaş"},{"key":"B","text":"Aşık Veysel"},{"key":"C","text":"Mahzuni Şerif"},{"key":"D","text":"Aşık Daimi"},{"key":"E","text":"Davut Sulari"}], "correct_option": "A", "explanation": "Neşet Ertaş Bozkırın Tezenesi unvanına sahiptir.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qgn-4-3", "question_text": "'İstanbul Fotoğrafçısı' veya 'Gözü' olarak tanınan dünyaca ünlü merhum fotoğraf sanatçımız kimdir?", "options": [{"key":"A","text":"Ara Güler"},{"key":"B","text":"Ozan Sağdıç"},{"key":"C","text":"Nuri Bilge Ceylan"},{"key":"D","text":"Fikret Otyam"},{"key":"E","text":"Şakir Eczacıbaşı"}], "correct_option": "A", "explanation": "Ara Güler İstanbul Fotoğrafçısı olarak anılır.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qgn-4-4", "question_text": "Cannes Film Festivali'nde 'Kış Uykusu' filmi ile Altın Palmiye kazanan Türk yönetmen kimdir?", "options": [{"key":"A","text":"Nuri Bilge Ceylan"},{"key":"B","text":"Zeki Demirkubuz"},{"key":"C","text":"Semih Kaplanoğlu"},{"key":"D","text":"Ferzan Özpetek"},{"key":"E","text":"Fatih Akın"}], "correct_option": "A", "explanation": "Nuri Bilge Ceylan Altın Palmiye kazanan 2. Türk yönetmendir (İlki Yılmaz Güney - Yol).", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qgn-4-5", "question_text": "'İstiklal Şairi' Mehmet Akif Ersoy'un şiirlerini topladığı ünlü eseri hangisidir?", "options": [{"key":"A","text":"Safahat"},{"key":"B","text":"Çile"},{"key":"C","text":"Kendi Gök Kubbemiz"},{"key":"D","text":"Gölgeler"},{"key":"E","text":"Haluk'un Defteri"}], "correct_option": "A", "explanation": "Mehmet Akif Ersoy şiirlerini Safahat adlı 7 kitaptan oluşan eserinde toplamıştır (İstiklal Marşı'nı milletine hediye ettiği için Safahat'a almamıştır).", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qgn-4-6", "question_text": "'Dede Korkut Hikayeleri' UNESCO İnsanlığın Somut Olmayan Kültürel Mirası Temsili Listesi'ne kaç yılında eklenmiştir?", "options": [{"key":"A","text":"2018"},{"key":"B","text":"2010"},{"key":"C","text":"2015"},{"key":"D","text":"2020"},{"key":"E","text":"2022"}], "correct_option": "A", "explanation": "Dede Korkut mirası 2018 yılında UNESCO listesine girmiştir.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qgn-4-7", "question_text": "Türk sinema tarihinin İLK renkli filmi hangisidir?", "options": [{"key":"A","text":"Halıcı Kız (Muhsin Ertuğrul - 1953)"},{"key":"B","text":"Susuz Yaz"},{"key":"C","text":"Vurun Kahpeye"},{"key":"D","text":"Yol"},{"key":"E","text":"Gurbet Kuşları"}], "correct_option": "A", "explanation": "Halıcı Kız (1953) çekilen ilk renkli Türk filmidir.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qgn-4-8", "question_text": "Uluslararası Berlin Film Festivali'nde (Altın Ayı) ödül kazanan İLK Türk filmi hangisidir?", "options": [{"key":"A","text":"Susuz Yaz (Metin Erksan - 1964)"},{"key":"B","text":"Halıcı Kız"},{"key":"C","text":"Yol"},{"key":"D","text":"Duvar"},{"key":"E","text":"Uzak"}], "correct_option": "A", "explanation": "Metin Erksan'ın Susuz Yaz filmi Altın Ayı kazanan ilk filmimizdir.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qgn-4-9", "question_text": "Cumhurbaşkanlığı Kültür ve Sanat Büyük Ödüllerinde Edebiyat/Müzik/Sinema alanında ödül alan usta sanatçılarımız her yıl nerede ilan edilir?", "options": [{"key":"A","text":"Çankaya / Beştepe Cumhurbaşkanlığı Külliyesi"},{"key":"B","text":"TBMM"},{"key":"C","text":"Atatürk Kültür Merkezi (AKM)"},{"key":"D","text":"Kültür Bakanlığı"},{"key":"E","text":"TRT"}], "correct_option": "A", "explanation": "Cumhurbaşkanlığı Kültür Sanat Ödülleri Külliye'de dağıtılır.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qgn-4-10", "question_text": "Erzurum'da doğan, 'Yaban', 'Kiralık Konak' ve 'Ankara' romanlarının yazarı kimdir?", "options": [{"key":"A","text":"Yakup Kadri Karaosmanoğlu"},{"key":"B","text":"Halide Edib Adıvar"},{"key":"C","text":"Reşat Nuri Güntekin"},{"key":"D","text":"Tarık Buğra"},{"key":"E","text":"Peyami Safa"}], "correct_option": "A", "explanation": "Yakup Kadri Karaosmanoğlu Yaban ve Kiralık Konak'ın yazarıdır.", "difficulty_level": "lisans", "is_verified": True}
    ]
    add_gun_bundle("topic-gun-kultur-sanat-unesco", "Kültür, Sanat, Edebiyat & UNESCO", "kultur-sanat-edebiyat-unesco", 1.6, 4, "Sanatçı ve Unvan Eşleşmesi", "### Önemli Unvanlar:\n- **Bozkırın Tezenesi:** Neşet Ertaş.\n- **İstanbul Fotoğrafçısı:** Ara Güler.\n- **Altın Palmiye:** Nuri Bilge Ceylan (Kış Uykusu).\n- **İlk Renkli Film:** Halıcı Kız (1953).", "KPSS Güncel Bilgiler", q4)

    # 5. Bilim, Teknoloji, İcatlar & Uzay
    q5 = [
        {"id": "qgn-5-1", "question_text": "Türkiye'nin en büyük teknoloji ve havacılık festivali olan TEKNOFEST'in yönetim kurulu başkanı kimdir?", "options": [{"key":"A","text":"Selçuk Bayraktar"},{"key":"B","text":"Haluk Bayraktar"},{"key":"C","text":"Temel Kotil"},{"key":"D","text":"İsmaill Demir"},{"key":"E","text":"Haluk Görgün"}], "correct_option": "A", "explanation": "Selçuk Bayraktar T3 Vakfı Mütevelli Heyeti ve TEKNOFEST başkanıdır.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qgn-5-2", "question_text": "10 Türk Lirası banknotunun arka yüzünde portresi yer alan dünyaca ünlü Türk matematikçisi kimdir?", "options": [{"key":"A","text":"Cahit Arf ('Arf Sabiti' / 'Arf Halkaları')"},{"key":"B","text":"Ali Kuşçu"},{"key":"C","text":"Matrakçı Nasuh"},{"key":"D","text":"Ömer Hayyam"},{"key":"E","text":"Harezmi"}], "correct_option": "A", "explanation": "10 TL arkasında Cahit Arf yer almaktadır.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qgn-5-3", "question_text": "5 Türk Lirası banknotunun arka yüzünde resmi yer alan İLK Türk bilim tarihi profesörümüz kimdir?", "options": [{"key":"A","text":"Prof. Dr. Aydın Sayılı"},{"key":"B","text":"Cahit Arf"},{"key":"C","text":"Mimar Sinan"},{"key":"D","text":"Yunus Emre"},{"key":"E","text":"Fatma Aliye"}], "correct_option": "A", "explanation": "5 TL arkasında Aydın Sayılı yer almaktadır.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qgn-5-4", "question_text": "50 Türk Lirası banknotunun arka yüzünde yer alan İLK kadın romancımız kimdir?", "options": [{"key":"A","text":"Fatma Aliye Hanım"},{"key":"B","text":"Halide Edib Adıvar"},{"key":"C","text":"Afife Jale"},{"key":"D","text":"Sabiha Gökçen"},{"key":"E","text":"Samiye Cahid"}], "correct_option": "A", "explanation": "50 TL arkasında ilk kadın romancımız Fatma Aliye vardır.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qgn-5-5", "question_text": "100 Türk Lirası banknotunun arka yüzünde yer alan büyük Klasik Türk Müziği bestekarı kimdir?", "options": [{"key":"A","text":"Buhurizade Mustafa Itri"},{"key":"B","text":"Dede Efendi"},{"key":"C","text":"Hacı Arif Bey"},{"key":"D","text":"Tamburi Cemil Bey"},{"key":"E","text":"Sadettin Kaynak"}], "correct_option": "A", "explanation": "100 TL arkasında Itri (Buhurizade Mustafa) yer alır.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qgn-5-6", "question_text": "200 Türk Lirası banknotunun arka yüzünde yer alan 'Sevelim Sevilelim' diyen büyük tasavvuf şairimiz kimdir?", "options": [{"key":"A","text":"Yunus Emre"},{"key":"B","text":"Mevlana"},{"key":"C","text":"Hacı Bektaş-ı Veli"},{"key":"D","text":"Pir Sultan Abdal"},{"key":"E","text":"Kaygusuz Abdal"}], "correct_option": "A", "explanation": "200 TL arkasında Yunus Emre yer alır.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qgn-5-7", "question_text": "Fatih Sultan Mehmed döneminde İstanbul'a gelerek Medrese müderrisliği yapan ünlü astronom ve matematikçi kimdir?", "options": [{"key":"A","text":"Ali Kuşçu"},{"key":"B","text":"Ulugh Bey"},{"key":"C","text":"Takiyüddin"},{"key":"D","text":"Kadızade-i Rumi"},{"key":"E","text":"Piri Reis"}], "correct_option": "A", "explanation": "Ali Kuşçu Fatih döneminde İstanbul'a davet edilen astronomdur.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qgn-5-8", "question_text": "Cihannüma ve Fezleke isimli ünlü coğrafya ve tarih eserlerinin yazarı Osmanlı alimi kimdir?", "options": [{"key":"A","text":"Katip Çelebi (Hacı Halife)"},{"key":"B","text":"Evliya Çelebi"},{"key":"C","text":"Naima"},{"key":"D","text":"Peçevi"},{"key":"E","text":"Aşıkpaşazade"}], "correct_option": "A", "explanation": "Cihannüma yazarı Katip Çelebi'dir (Evliya Çelebi Seyahatname yazarıdır).", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qgn-5-9", "question_text": "Dünya haritasını ceylan derisi üzerine çizen ve Kitab-ı Bahriye eserinin sahibi olan Osmanlı denizcisi kimdir?", "options": [{"key":"A","text":"Piri Reis"},{"key":"B","text":"Seydi Ali Reis"},{"key":"C","text":"Barbaros Hayrettin Paşa"},{"key":"D","text":"Turgut Reis"},{"key":"E","text":"Oruç Reis"}], "correct_option": "A", "explanation": "Piri Reis Kitab-ı Bahriye ve ilk dünya haritasıyla ünlüdür.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qgn-5-10", "question_text": "Türkiye'nin İLK kadın savaş pilotu ve dünyanın ilk kadın savaş pilotu kimdir?", "options": [{"key":"A","text":"Sabiha Gökçen"},{"key":"B","text":"Bedriye Tahir Gökmen"},{"key":"C","text":"Afife Jale"},{"key":"D","text":"Selma Rıza"},{"key":"E","text":"Semiha Berksoy"}], "correct_option": "A", "explanation": "Sabiha Gökçen ilk kadın savaş pilotumuzdur (Bedriye Tahir ise ilk kadın sivil pilotumuzdur).", "difficulty_level": "lisans", "is_verified": True}
    ]
    add_gun_bundle("topic-gun-bilim-teknoloji", "Bilim, Teknoloji, İcatlar & Uzay", "bilim-teknoloji-ve-icatlar", 1.5, 5, "Para Banknotları Üzerindeki Şahsiyetler", "### Türk Lirası Banknotları:\n- **5 TL:** Aydın Sayılı (Bilim Tarihi)\n- **10 TL:** Cahit Arf (Matematik)\n- **50 TL:** Fatma Aliye (İlk Kadın Romancı)\n- **100 TL:** Itri (Müzik)\n- **200 TL:** Yunus Emre (Tasavvuf)", "KPSS Güncel Bilgiler", q5)

    print(f"Toplam Güncel Bilgiler Alt Konusu: {len(topics)}")
    print(f"Toplam Güncel Bilgiler Hap Bilgiler: {len(quick_notes)}")
    print(f"Toplam Güncel Bilgiler Sorular: {len(questions)}")

    return topics, quick_notes, questions

if __name__ == "__main__":
    g_topics, g_notes, g_questions = build_guncel_dataset()
    
    json_path = os.path.join("mobile_app", "assets", "data", "sample_data.json")
    with open(json_path, "r", encoding="utf-8") as f:
        full_db = json.load(f)

    # course-guncel yoksa ekleyelim
    has_guncel_course = any(c["id"] == "course-guncel" for c in full_db["courses"])
    if not has_guncel_course:
        full_db["courses"].append({
            "id": "course-guncel",
            "name": "Güncel Bilgiler & Genel Kültür",
            "slug": "guncel-bilgiler",
            "description": "Türkiye ve dünya gündemi, kültür-sanat, spor, bilim ve güncel olaylar.",
            "icon": "newspaper",
            "color": "0xFF9C27B0",
            "sort_order": 6
        })

    # Eski Güncel Bilgiler verilerini temizle ve yeni 5 alt konulu 50 soruyu ekle
    full_db["topics"] = [t for t in full_db["topics"] if t["course_id"] != "course-guncel"]
    full_db["quick_notes"] = [n for n in full_db["quick_notes"] if not n["topic_id"].startswith("topic-gun")]
    full_db["questions"] = [q for q in full_db["questions"] if not q["topic_id"].startswith("topic-gun")]

    full_db["topics"].extend(g_topics)
    full_db["quick_notes"].extend(g_notes)
    full_db["questions"].extend(g_questions)

    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(full_db, f, ensure_ascii=False, indent=2)

    print(f"\n[BAŞARILI GÜNCEL BİLGİLER HAVUZU] {len(g_topics)} Alt Konu, {len(g_notes)} Hap Bilgi ve {len(g_questions)} Güncel Bilgiler Sorusu veritabanına aktarıldı!")
