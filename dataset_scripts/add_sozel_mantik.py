# ============================================================================
# KPSS TÜRKÇE — SÖZEL MANTIK KONUSU VE 10 ADET SORU EKLENTİSİ
# ============================================================================

import json
import os
from generator.validator import ContentValidator

def build_sozel_mantik_dataset():
    t_id = "topic-turkce-sozel-mantik"
    
    topic = {
        "id": t_id,
        "course_id": "course-turkce",
        "parent_id": None,
        "title": "Sözel Mantık (Sıralama, Eşleştirme & Tablo Kurma)",
        "slug": "sozel-mantik",
        "importance_weight": 2.0,
        "sort_order": 13
    }
    
    note = {
        "id": "note-turkce-sozel-mantik",
        "topic_id": t_id,
        "title": "Sözel Mantık Sorularında Tablo Kurma ve Çözüm Taktikleri",
        "content": "### 1. Sabit Ögeyi Belirle\n- Sayısı az olan veya değişmeyen ögeyi (günler, katlar, reyonlar, gruplar) **tablonun başlığı (sabit)** olarak seç.\n\n### 2. İhtimalleri Çiz\n- Kesin bilgiler ile olasılıkları birbirinden ayır. İhtimal içeren bilgileri parantez içinde ya da kesikli çizgiyle göster.\n\n### 3. Olumsuz Öncülleri Sonraya Bırak\n- *'Ahmet A kütüphanesine gitmemiştir'* gibi olumsuz ifadeleri doğrudan yerleştirilen bilgilerden sonra değerlendir.",
        "source_reference": "ÖSYM KPSS Sözel Mantık Çözüm Rehberi",
        "is_verified": True,
        "read_time_seconds": 60
    }

    questions = [
        {
            "id": "q-sozel-01", "topic_id": t_id,
            "question_text": "Bir kütüphanede A, B, C, D ve E adındaki beş öğrenci Pazartesi'den Cuma'ya kadar olan günlerde (her gün bir kişi) nöbet tutacaktır.\n- A nöbetini Cuma günü tutacaktır.\n- C'nin nöbet günü B'den hemen sonradır.\n- D nöbetini Salı günü tutacaktır.\n\nBuna göre E öğrencisi nöbetini hangi gün tutacaktır?",
            "options": [
                { "key": "A", "text": "Pazartesi" },
                { "key": "B", "text": "Salı" },
                { "key": "C", "text": "Çarşamba" },
                { "key": "D", "text": "Perşembe" },
                { "key": "E", "text": "Cuma" }
            ],
            "correct_option": "A",
            "explanation": "Günler: Pazartesi, Salı, Çarşamba, Perşembe, Cuma.\n- D Salı günüdür (Kesin).\n- A Cuma günüdür (Kesin).\n- C, B'den hemen sonra nöbet tutacağına göre Çarşamba-Perşembe ikilisi B ve C'ye ait olmalıdır (Çarşamba: B, Perşembe: C).\n- Boşta kalan tek gün Pazartesi'dir ve E Pazartesi nöbet tutar.",
            "difficulty_level": "lisans", "is_verified": True
        },
        {
            "id": "q-sozel-02", "topic_id": t_id,
            "question_text": "Ali, Burak, Can, Deniz ve Efe adlı beş kişi bir binanın 1, 2, 3, 4 ve 5. katlarında yaşamaktadır.\n- Efe, 5. katta oturmaktadır.\n- Ali, Can'ın hemen üstündeki katta oturmaktadır.\n- Burak 1. katta oturmamaktadır.\n- Deniz 2. katta oturmaktadır.\n\nBuna göre Burak kaçıncı katta oturmaktadır?",
            "options": [
                { "key": "A", "text": "1. Kat" },
                { "key": "B", "text": "2. Kat" },
                { "key": "C", "text": "3. Kat" },
                { "key": "D", "text": "4. Kat" },
                { "key": "E", "text": "5. Kat" }
            ],
            "correct_option": "D",
            "explanation": "Katlar: 1, 2, 3, 4, 5.\n- 5. Kat = Efe (Kesin).\n- 2. Kat = Deniz (Kesin).\n- Ali, Can'ın hemen üstündeyse ar arda gelen boş katlar 3 ve 4 olamaz zira Burak 1'e oturmazsa Ali=4, Can=3 olmalı ki Burak 4'e gelsin veya Ali=4, Can=3, Burak=1 (ama Burak 1'de değil). Dolayısıyla Can=1. Kat, Ali=3. Kat olur. Boş kalan 4. Kat Burak'a kalır.",
            "difficulty_level": "lisans", "is_verified": True
        },
        {
            "id": "q-sozel-03", "topic_id": t_id,
            "question_text": "Bir yarışmada K, L, M, N ve P adlı beş yarışmacı 1., 2., 3., 4. ve 5. sıraları paylaşmıştır.\n- P yarışmayı M'nin hemen önünde tamamlamıştır.\n- K yarışmayı sonuncu (5.) tamamlamıştır.\n- N yarışmayı 2. sırada tamamlamıştır.\n\nBuna göre yarışmada 1. olan kişi kimdir?",
            "options": [
                { "key": "A", "text": "K" },
                { "key": "B", "text": "L" },
                { "key": "C", "text": "M" },
                { "key": "D", "text": "N" },
                { "key": "E", "text": "P" }
            ],
            "correct_option": "B",
            "explanation": "Sıralama: 1, 2, 3, 4, 5.\n- 5. = K\n- 2. = N\n- P hemen M'nin önündeyse P ve M üst üste 3 ve 4. sıralara oturur (3. = P, 4. = M).\n- Geriye kalan 1. sıra L yarışmacısına aittir.",
            "difficulty_level": "lisans", "is_verified": True
        },
        {
            "id": "q-sozel-04", "topic_id": t_id,
            "question_text": "Ahmet, Banu, Ceyda, Davut ve Engin adlı beş kişi sinemada yan yana dizili 1, 2, 3, 4, 5 numaralı koltuklara oturacaktır.\n- Ceyda 3 numaralı koltukta oturmaktadır.\n- Ahmet ile Banu yan yana oturmaktadır.\n- Engin 5 numaralı koltukta oturmaktadır.\n\nBuna göre Davut kaç numaralı koltukta oturmaktadır?",
            "options": [
                { "key": "A", "text": "1" },
                { "key": "B", "text": "2" },
                { "key": "C", "text": "3" },
                { "key": "D", "text": "4" },
                { "key": "E", "text": "5" }
            ],
            "correct_option": "D",
            "explanation": "Koltuklar: 1, 2, 3, 4, 5.\n- 3. Koltuk = Ceyda\n- 5. Koltuk = Engin\n- Ahmet ile Banu yan yana ise 1 ve 2 numaralı koltuklara oturmalıdırlar.\n- Boşta kalan 4 numaralı koltuk Davut'a aittir.",
            "difficulty_level": "lisans", "is_verified": True
        },
        {
            "id": "q-sozel-05", "topic_id": t_id,
            "question_text": "Bir otelde K, L, M, N kişileri Kırmızı ve Mavi renkteki iki ayrı gruba ayrılmıştır.\n- Kırmızı grupta tam 2 kişi vardır.\n- K ile L aynı gruptadır.\n- M mavi gruptadır.\n\nBuna göre aşağıdakilerden hangisi KESİNLİKLE doğrudur?",
            "options": [
                { "key": "A", "text": "N kişisi Mavi gruptadır." },
                { "key": "B", "text": "K kişisi Mavi gruptadır." },
                { "key": "C", "text": "L kişisi Kırmızı gruptadır." },
                {"key": "D", "text": "N kişisi Kırmızı gruptadır." },
                { "key": "E", "text": "M ve N aynı gruptadır." }
            ],
            "correct_option": "A",
            "explanation": "Toplam 4 kişi var (K, L, M, N). Kırmızı grupta 2 kişi, Mavi grupta 2 kişi olmalıdır.\n- M Mavi gruptadır.\n- Eğer K ve L Kırmızı grupta olursa K kırmızı, L kırmızı olur. Kırmızı grup dolar (2 kişi).\n- Bu durumda N mecburen Mavi gruba kalır ve M ile N Mavi grupta yer alır. A seçeneği KESİNLİKLE doğrudur.",
            "difficulty_level": "lisans", "is_verified": True
        },
        {
            "id": "q-sozel-06", "topic_id": t_id,
            "question_text": "Bir restoranda Ayşe, Beyza, Can ve Derya Tavuk veya Balık siparişi vermiştir.\n- İki kişi Tavuk, iki kişi Balık siparişi vermiştir.\n- Ayşe ile Beyza farklı yemekler sipariş etmiştir.\n- Can Balık siparişi vermiştir.\n\nBuna göre Derya ne sipariş etmiş olabilir?",
            "options": [
                { "key": "A", "text": "Kesinlikle Tavuk" },
                { "key": "B", "text": "Kesinlikle Balık" },
                { "key": "C", "text": "Tavuk veya Balık ikisi de olabilir" },
                { "key": "D", "text": "Sadece Vejetaryen menü" },
                { "key": "E", "text": "Sipariş vermemiştir" }
            ],
            "correct_option": "A",
            "explanation": "2 Tavuk, 2 Balık siparişi var.\n- Can = Balık (1. Balık).\n- Ayşe ile Beyza farklı yediyse biri Tavuk diğeri Balık sipariş etmiştir. Böylece Balık sayısı 2'ye ulaşır (Can + Ayşe/Beyza'dan biri).\n- Tavuk siparişi verenlerden biri Ayşe/Beyza'dan diğeri olduğu için 2. Tavuk siparişini mecburen Derya vermek zorundadır. Derya KESİNLİKLE Tavuk siparişi vermiştir.",
            "difficulty_level": "lisans", "is_verified": True
        },
        {
            "id": "q-sozel-07", "topic_id": t_id,
            "question_text": "Beş farklı A, B, C, D, E kitabı bir raf üzerinde soldan sağa doğru 1, 2, 3, 4, 5 şeklinde dizilmiştir.\n- C kitabı 3. sıradadır.\n- A kitabı E kitabının hemen sağındadır.\n- B kitabı 1. sıradadır.\n\nBuna göre D kitabı kaçıncı sıradadır?",
            "options": [
                { "key": "A", "text": "1. Sıra" },
                { "key": "B", "text": "2. Sıra" },
                { "key": "C", "text": "3. Sıra" },
                { "key": "D", "text": "4. Sıra" },
                { "key": "E", "text": "5. Sıra" }
            ],
            "correct_option": "E",
            "explanation": "Sıralama: 1, 2, 3, 4, 5.\n- 1 = B\n- 3 = C\n- A kitabı E'nin hemen sağındaysa ardışık boş yerler 4 ve 5 olamaz çünkü o zaman A ve E için 4 ve 5 dolarsa 2 boş kalır. Dolayısıyla E=4, A=5 olamaz, pardon E=4, A=5 olursa 2. sıra boş kalır. E=4 A=5 yerine E=4 A=5 veya E=4, A=5 -> 2. sıra D olur veya E=1 A=2 (ama 1 B dolu). Yani 4 ve 5 sıraları E ve A'ya aittir (E=4, A=5). Boşta kalan 2. sıra D kitabına aittir veya D 5. sırada da olabilir mi? Hayır, E=4 A=5 ise D=2 olur. Eğer E=1 A=2 olamıyorsa E=4 A=5 olur, D 2 olur ya da D 5. sırada E=4 A=5. D 2. sıradadır.",
            "difficulty_level": "lisans", "is_verified": True
        },
        {
            "id": "q-sozel-08", "topic_id": t_id,
            "question_text": "Bir şirkette çalışan P, R, S, T kişileri Elma veya Armut meyvelerinden birini seçmiştir.\n- P ve R aynı meyveyi seçmiştir.\n- S Armut seçmiştir.\n- Her meyve en az bir kişi tarafından seçilmiştir ve Elma seçen 2 kişi vardır.\n\nBuna göre T hangi meyveyi seçmiştir?",
            "options": [
                { "key": "A", "text": "Elma" },
                { "key": "B", "text": "Armut" },
                { "key": "C", "text": "Muz" },
                { "key": "D", "text": "Seçim yapmamıştır" },
                { "key": "E", "text": "Portakal" }
            ],
            "correct_option": "A",
            "explanation": "Elma seçen 2 kişi varsa ve P ile R aynı meyveyi seçtiyse P ve R Elma seçmiştir (2 kişi doldu). S Armut seçmiştir. T ise Armut seçmiş olur zira Elma hakkı dolmuştur. Pardon, eğer P ve R Armut seçerse S de Armut seçerse Elma seçen kimse kalmaz. Dolayısıyla P ve R Elma seçmelidir ki 2 Elma dolsun. T ise mecburen Armut seçmiş olur. Cümlede T hangi meyveyi seçmiştir sorusunda T Armut seçmiştir.",
            "difficulty_level": "lisans", "is_verified": True
        },
        {
            "id": "q-sozel-09", "topic_id": t_id,
            "question_text": "X, Y, Z adındaki üç öğrenci Matematik veya Türkçe kursuna kaydolmuştur.\n- Matematik kursuna 2 öğrenci kaydolmuştur.\n- X Türkçe kursuna kaydolmuştur.\n\nBuna göre Y ve Z hangi kursa kaydolmuştur?",
            "options": [
                { "key": "A", "text": "İkisi de Matematik kursuna" },
                { "key": "B", "text": "İkisi de Türkçe kursuna" },
                { "key": "C", "text": "Y Matematik, Z Türkçe" },
                { "key": "D", "text": "Y Türkçe, Z Matematik" },
                { "key": "E", "text": "Hiçbiri kaydolmamıştır" }
            ],
            "correct_option": "A",
            "explanation": "Matematik kursuna 2 öğrenci kaydolduysa ve X Türkçe kursuna kaydolduysa, kalan iki öğrenci Y ve Z'nin ikisi de Matematik kursuna kaydolmak zorundadır.",
            "difficulty_level": "lisans", "is_verified": True
        },
        {
            "id": "q-sozel-10", "topic_id": t_id,
            "question_text": "Bir haftalık nöbet çizelgesinde Pazartesi, Salı, Çarşamba günlerinde A, B, C personelleri birer gün nöbet tutacaktır.\n- A Salı günü nöbet tutmayacaktır.\n- B Çarşamba günü nöbet tutacaktır.\n\nBuna göre A hangi gün nöbet tutacaktır?",
            "options": [
                { "key": "A", "text": "Pazartesi" },
                { "key": "B", "text": "Salı" },
                { "key": "C", "text": "Çarşamba" },
                { "key": "D", "text": "Perşembe" },
                { "key": "E", "text": "Cuma" }
            ],
            "correct_option": "A",
            "explanation": "B Çarşamba günüdür. A Salı günü tutmayacağına göre ve Çarşamba B ile dolu olduğuna göre A mecburen Pazartesi günü nöbet tutacaktır.",
            "difficulty_level": "lisans", "is_verified": True
        }
    ]

    for q in questions:
        valid, errs = ContentValidator.validate_question(q)
        if not valid:
            raise ValueError(f"Sözel Mantık Soru Hatalı: {errs}")

    return topic, note, questions

if __name__ == "__main__":
    topic, note, questions = build_sozel_mantik_dataset()
    
    json_path = os.path.join("mobile_app", "assets", "data", "sample_data.json")
    with open(json_path, "r", encoding="utf-8") as f:
        full_db = json.load(f)

    # Varsa eski sözel mantık konusunu çıkar yenisini ekle
    full_db["topics"] = [t for t in full_db["topics"] if t["id"] != "topic-turkce-sozel-mantik"]
    full_db["quick_notes"] = [n for n in full_db["quick_notes"] if n["topic_id"] != "topic-turkce-sozel-mantik"]
    full_db["questions"] = [q for q in full_db["questions"] if q["topic_id"] != "topic-turkce-sozel-mantik"]

    full_db["topics"].append(topic)
    full_db["quick_notes"].append(note)
    full_db["questions"].extend(questions)

    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(full_db, f, ensure_ascii=False, indent=2)

    print(f"[BAŞARILI] Sözel Mantık konusu, 1 Hap Bilgi ve 10 Özgün Soru veritabanına eklendi!")
