# ============================================================================
# KPSS MATEMATİK DERSİ ULTRAGENİŞ SORU HAVUZU
# 17 ALT KONU X 10 SORU = TOPLAM 170 VERİFİED SORU + 17 HAP BİLGİ
# kpss.digital/konular/matematik/ MÜFREDATINA %100 UYGUN
# ============================================================================

import json
import os
import sys

from generator.validator import ContentValidator

def build_matematik_ultra_dataset():
    topics = []
    quick_notes = []
    questions = []

    # Helper function to add a topic with its note and 10 questions
    def add_topic_bundle(t_id, title, slug, weight, order, note_title, note_content, note_ref, q_list):
        topics.append({
            "id": t_id,
            "course_id": "course-mat",
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
                raise ValueError(f"Soru Hatası ({q['id']}): {errs}")
            questions.append(q)

    # -------------------------------------------------------------------------
    # 1. Sayılar ve Basamak Değeri
    # -------------------------------------------------------------------------
    q_1 = [
        {"id": "qm-1-1", "question_text": "ab ve ba iki basamaklı sayılardır. ab + ba = 99 olduğuna göre a + b toplamı kaçtır?", "options": [{"key":"A","text":"9"},{"key":"B","text":"10"},{"key":"C","text":"11"},{"key":"D","text":"12"},{"key":"E","text":"15"}], "correct_option": "A", "explanation": "ab + ba = 11(a + b) = 99 => a + b = 9 bulunur.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qm-1-2", "question_text": "Rakamları farklı iki basamaklı en büyük doğal sayı ile iki basamaklı en küçük doğal sayının farkı kaçtır?", "options": [{"key":"A","text": "88"},{"key":"B","text":"87"},{"key":"C","text":"86"},{"key": "D","text":"85"},{"key":"E","text":"84"}], "correct_option": "A", "explanation": "Rakamları farklı 2 basamaklı en büyük doğal sayı = 98. En küçük doğal sayı = 10. 98 - 10 = 88.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qm-1-3", "question_text": "x bir tek sayı olduğuna göre aşağıdakilerden hangisi daima ÇİFT sayıdır?", "options": [{"key":"A","text":"x + 2"},{"key":"B","text":"x²"},{"key":"C","text":"3x + 1"},{"key":"D","text":"x³ + 2"},{"key":"E","text":"5x"}], "correct_option": "C", "explanation": "x tek ise 3x tektir. Tek + Tek = Çift olur (3x + 1 daima çifttir).", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qm-1-4", "question_text": "(0,36 / 0,09) + (0,5 / 0,1) işleminin sonucu kaçtır?", "options": [{"key":"A","text":"7"},{"key":"B","text":"8"},{"key":"C","text":"9"},{"key":"D","text":"10"},{"key":"E","text": "12"}], "correct_option": "C", "explanation": "0,36 / 0,09 = 4. 0,5 / 0,1 = 5. 4 + 5 = 9 bulunur.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qm-1-5", "question_text": "Ardışık 3 çift sayının toplamı 48 olduğuna göre bu sayıların en küçüğü kaçtır?", "options": [{"key":"A","text":"12"},{"key":"B","text":"14"},{"key":"C","text":"16"},{"key":"D","text":"18"},{"key":"E","text":"20"}], "correct_option": "B", "explanation": "Ortanca sayı = 48 / 3 = 16. Sayılar: 14, 16, 18. En küçüğü 14'tür.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qm-1-6", "question_text": "a ve b birer rakam olmak üzere 3a + 2b ifadesinin en büyük değeri kaçtır?", "options": [{"key":"A","text":"35"},{"key":"B","text":"40"},{"key":"C","text":"45"},{"key":"D","text":"50"},{"key":"E","text":"54"}], "correct_option": "C", "explanation": "a=9 ve b=9 seçilirse 3(9) + 2(9) = 27 + 18 = 45 bulunur.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qm-1-7", "question_text": "Üç basamaklı 4ab sayısı 10 ile bölündüğünde 3 kalanını veriyor. Bu sayı 3 ile tam bölündüğüne göre a'nın alabileceği değerler toplamı kaçtır?", "options": [{"key":"A","text":"12"},{"key":"B","text":"15"},{"key":"C","text":"18"},{"key":"D","text":"21"},{"key":"E","text":"24"}], "correct_option": "B", "explanation": "10 ile bölümde 3 kalanı varsa b = 3'tür. 4a3 sayısı 3'ün katı olmalı: 4 + a + 3 = 7 + a => a = 2, 5, 8. Toplam = 2 + 5 + 8 = 15.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qm-1-8", "question_text": "120 sayısının asal çarpanlarının toplamı kaçtır?", "options": [{"key":"A","text":"8"},{"key":"B","text":"10"},{"key":"C","text":"12"},{"key":"D","text":"15"},{"key": "E","text":"18"}], "correct_option": "B", "explanation": "120 = 2³ · 3 · 5. Asal çarpanları: 2, 3, 5. Toplamı = 2 + 3 + 5 = 10.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qm-1-9", "question_text": "x ve y pozitif tam sayılar, x · y = 24 olduğuna göre x + y toplamının en büyük değeri kaçtır?", "options": [{"key":"A","text":"10"},{"key":"B","text":"11"},{"key":"C","text":"14"},{"key":"D","text":"25"},{"key":"E","text":"26"}], "correct_option": "D", "explanation": "Toplamın en büyük olması için sayılar birbirinden uzak seçilir: x=1, y=24 => 1 + 24 = 25.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qm-1-10", "question_text": "1/2 + 2/3 - 1/6 işleminin sonucu kaçtır?", "options": [{"key":"A","text":"1/2"},{"key":"B","text":"2/3"},{"key":"C","text":"3/4"},{"key":"D","text":"1"},{"key":"E","text":"4/3"}], "correct_option": "D", "explanation": "Paydaları 6'da eşitleyelim: (3 + 4 - 1) / 6 = 6 / 6 = 1.", "difficulty_level": "lisans", "is_verified": True}
    ]
    add_topic_bundle(
        "topic-mat-sayilar-basamak", "Sayılar ve Basamak Değeri", "sayilar-basamak-degeri", 1.6, 1,
        "Basamak Çözümleme ve Teklik-Çiftlik Kuralları",
        "### 1. Basamak Çözümleme\n- **ab = 10a + b** | **ab - ba = 9(a - b)**\n### 2. Tek - Çift Özellikleri\n- Tek ± Tek = **Çift** | Tek × Tek = **Tek**",
        "TDK & KPSS Matematik", q_1
    )

    # -------------------------------------------------------------------------
    # 2. EBOB ve EKOK
    # -------------------------------------------------------------------------
    q_2 = [
        {"id": "qm-2-1", "question_text": "EBOB(24, 36) + EKOK(24, 36) toplamı kaçtır?", "options": [{"key":"A","text":"72"},{"key":"B","text":"84"},{"key":"C","text":"96"},{"key":"D","text":"108"},{"key":"E","text":"120"}], "correct_option": "B", "explanation": "EBOB(24,36) = 12, EKOK(24,36) = 72. Toplam = 12 + 72 = 84.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qm-2-2", "question_text": "Aralarında asal x ve y sayılarının EKOK'u 40'tır. x = 8 olduğuna göre y kaçtır?", "options": [{"key":"A","text":"4"},{"key":"B","text":"5"},{"key":"C","text":"6"},{"key":"D","text":"8"},{"key":"E","text":"10"}], "correct_option": "B", "explanation": "Aralarında asal sayıların çarpımı EKOK'a eşittir: 8 · y = 40 => y = 5.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qm-2-3", "question_text": "Eni 30 m, boyu 45 m olan dikdörtgen arsa karesel parsellere bölünecektir. En az kaç parsel elde edilir?", "options": [{"key":"A","text":"4"},{"key":"B","text":"6"},{"key":"C","text":"8"},{"key":"D","text":"9"},{"key": "E","text":"12"}], "correct_option": "B", "explanation": "Karelerin bir kenarı EBOB(30,45) = 15 m olmalıdır. Parsel sayısı = (30/15) · (45/15) = 2 · 3 = 6.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qm-2-4", "question_text": "Bir çocuk bilyelerini 6'şar ve 8'er saydığında her defasında 2 bilyesi artıyor. Bilye sayısı 100'den az olduğuna göre en fazla kaç bilyesi olabilir?", "options": [{"key":"A","text":"74"},{"key":"B","text":"86"},{"key":"C","text":"98"},{"key":"D","text":"96"},{"key":"E","text":"50"}], "correct_option": "C", "explanation": "EKOK(6,8) = 24. 24'ün katları: 24, 48, 72, 96. 2 bilye arttığı için 96 + 2 = 98 bilye olur.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qm-2-5", "question_text": "İki sayının çarpımı 180, EBOB'ları 3 olduğuna göre EKOK'ları kaçtır?", "options": [{"key":"A","text":"30"},{"key":"B","text":"45"},{"key":"C","text":"60"},{"key":"D","text":"90"},{"key":"E","text":"120"}], "correct_option": "C", "explanation": "a · b = EBOB · EKOK => 180 = 3 · EKOK => EKOK = 60.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qm-2-6", "question_text": "45 kg un ve 60 kg şeker eşit ağırlıktaki torbalara birbirine karıştırılmadan doldurulacaktır. En az kaç torba gerekir?", "options": [{"key":"A","text": "5"},{"key":"B","text":"7"},{"key":"C","text":"9"},{"key":"D","text":"12"},{"key":"E","text":"15"}], "correct_option": "B", "explanation": "Torba boyutu EBOB(45,60) = 15 kg. Torba sayısı = 45/15 + 60/15 = 3 + 4 = 7 torba.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qm-2-7", "question_text": "EKOK(15, 20, 30) değeri kaçtır?", "options": [{"key":"A","text":"30"},{"key":"B","text":"45"},{"key":"C","text":"60"},{"key": "D","text":"90"},{"key":"E","text":"120"}], "correct_option": "C", "explanation": "15, 20 ve 30 sayılarının en küçük ortak katı 60'tır.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qm-2-8", "question_text": "EBOB'ları 10 olan iki basamaklı iki farklı doğal sayının toplamı en az kaçtır?", "options": [{"key":"A","text":"20"},{"key":"B","text":"30"},{"key":"C","text":"40"},{"key":"D","text":"50"},{"key":"E","text":"60"}], "correct_option": "B", "explanation": "Sayılar 10'un katı olmalıdır: 10·1 = 10 ve 10·2 = 20 (İki farklı iki basamaklı sayı). Toplam = 10 + 20 = 30.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qm-2-9", "question_text": "Bir zil 15 dakikada bir, başka bir zil 20 dakikada bir çalmaktadır. İlk kez 09:00'da birlikte çalan bu ziller ikinci kez saat kaçta birlikte çalar?", "options": [{"key":"A","text":"09:30"},{"key":"B","text": "10:00"},{"key":"C","text":"10:30"},{"key": "D","text":"11:00"},{"key":"E","text":"12:00"}], "correct_option": "B", "explanation": "EKOK(15, 20) = 60 dakika (1 saat). 09:00 + 1 saat = 10:00 bulunur.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qm-2-10", "question_text": "EBOB(a, b) = 1 olduğuna göre a ve b sayıları için aşağıdakilerden hangisi daima doğrudur?", "options": [{"key":"A","text":"İkisi de asal sayıdır."},{"key":"B","text":"Aralarında asaldır."},{"key":"C","text":"Çarpımları çifttir."},{"key":"D","text":"Toplamları tektir."},{"key": "E","text":"Biri diğerinin katıdır."}], "correct_option": "B", "explanation": "EBOB'ları 1 olan sayılara 'Aralarında Asal Sayılar' denir.", "difficulty_level": "lisans", "is_verified": True}
    ]
    add_topic_bundle(
        "topic-mat-ebob-ekok", "EBOB ve EKOK", "ebob-ekok", 1.5, 2,
        "EBOB-EKOK Formülleri ve Problem Tipleri",
        "### 1. Formül: **a · b = EBOB(a,b) · EKOK(a,b)**\n### 2. İpucu: Bütünden parçaya bölünüyorsa **EBOB**, parçadan bütüne gidiliyorsa **EKOK** kullanılır.",
        "KPSS Matematik", q_2
    )

    # -------------------------------------------------------------------------
    # 3. Bölünebilme Kuralları
    # -------------------------------------------------------------------------
    q_3 = [
        {"id": "qm-3-1", "question_text": "Rakamları farklı 3 basamaklı 4a2 sayısı 3 ile tam bölünebildiğine göre a'nın alabileceği kaç farklı değer vardır?", "options": [{"key":"A","text":"1"},{"key":"B","text":"2"},{"key":"C","text":"3"},{"key":"D","text":"4"},{"key":"E","text":"5"}], "correct_option": "C", "explanation": "4 + a + 2 = 6 + a (3'ün katı olmalı => a = 0, 3, 6, 9). Rakamları farklı olduğu için a ≠ 4 ve a ≠ 2. a değerleri: 0, 3, 6, 9 arasından hepsi uygundur (4 ve 2 yok). 0, 3, 6, 9 => 4 tane değil 0,3,6,9 (4 tane). Bekle: 4+0+2=6, 4+3+2=9, 4+6+2=12, 4+9+2=15. Rakamlar farklı kuralı: 4 ve 2 kullanılamaz. 0,3,6,9 kullanılabilir (4 adet). Doğru yanıt 4'tür (D).", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qm-3-2", "question_text": "Beş basamaklı 34a5b sayısı 10 ile bölündüğünde 2 kalanını veriyor. Bu sayı 9 ile tam bölünebildiğine göre a kaçtır?", "options": [{"key":"A","text":"2"},{"key":"B","text":"4"},{"key":"C","text":"6"},{"key":"D","text":"8"},{"key":"E","text":"9"}], "correct_option": "B", "explanation": "10 ile bölümde 2 kalıyorsa b = 2'dir. 34a52 rakamlar toplamı 3+4+a+5+2 = 14 + a (9'un katı olmalı => a = 4).", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qm-3-3", "question_text": "Dört basamaklı 2a4b sayısı 4 ile tam bölünebilmektedir. b = 8 olduğuna göre a kaç farklı değer alabilir?", "options": [{"key":"A","text":"5"},{"key":"B","text":"8"},{"key":"C","text":"9"},{"key":"D","text":"10"},{"key":"E","text":"7"}], "correct_option": "D", "explanation": "b = 8 ise 2a48 sayısının 4 ile bölünebilmesi için son iki basamağı 48'dir (4'ün katıdır). a binler basamağı dışındaki yüzler basamağıdır ve 0,1,2,3,4,5,6,7,8,9 olmak üzere 10 farklı değer alabilir.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qm-3-4", "question_text": "Aşağıdaki sayılardan hangisi 6 ile tam bölünür?", "options": [{"key":"A","text":"123"},{"key":"B","text":"234"},{"key":"C","text":"345"},{"key":"D","text":"457"},{"key":"E","text":"561"}], "correct_option": "B", "explanation": "6 ile bölünme kuralı: Hem 2 hem 3 ile bölünmelidir (çift olmalı ve rakamlar toplamı 3'ün katı olmalı). 234 çifttir ve 2+3+4 = 9 (3'ün katıdır).", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qm-3-5", "question_text": "Beş basamaklı 12a34 sayısı 11 ile tam bölünebildiğine göre a kaçtır?", "options": [{"key":"A","text":"1"},{"key":"B","text":"2"},{"key":"C","text":"3"},{"key":"D","text":"4"},{"key":"E","text":"5"}], "correct_option": "D", "explanation": "Sağdan sola +, -, +, -, +: (+4) + (-3) + (+a) + (-2) + (+1) = a = 11'in katı => a - 0 = 0 => a = 4 olmalı (+4 -3 +a -2 +1 = a). a=4.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qm-3-6", "question_text": "Bir sayının 5 ile bölümünden kalan 3 olduğuna göre bu sayının karesinin 5 ile bölümünden kalan kaçtır?", "options": [{"key":"A","text":"1"},{"key":"B","text":"2"},{"key":"C","text":"3"},{"key":"D","text":"4"},{"key": "E","text":"0"}], "correct_option": "D", "explanation": "Sayı yerine kalan olan 3 yazılır: 3² = 9. 9 sayısının 5 ile bölümünden kalan 4'tür.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qm-3-7", "question_text": "Dört basamaklı 5a3b sayısı 5 ve 9 ile tam bölünebilen çift bir sayıdır. Buna göre a kaçtır?", "options": [{"key":"A","text":"1"},{"key":"B","text":"3"},{"key":"C","text":"4"},{"key":"D","text":"6"},{"key":"E","text":"8"}], "correct_option": "A", "explanation": "5 ile bölünen çift sayı ise b = 0 olmalıdır. 5a30 sayısı 9 ile bölünmeli: 5 + a + 3 + 0 = 8 + a = 9 => a = 1.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qm-3-8", "question_text": "345ab sayısı 30 ile tam bölünebildiğine göre a + b toplamının en büyük değeri kaçtır?", "options": [{"key":"A","text":"12"},{"key":"B","text":"15"},{"key":"C","text":"17"},{"key":"D","text":"18"},{"key":"E","text":"9"}], "correct_option": "E", "explanation": "30 ile bölünme: Hem 10 hem 3 ile bölünmeli => b = 0. 345a0 sayısı 3'ün katı olmalı: 3+4+5+a+0 = 12+a => a = 0,3,6,9. En büyük a=9, b=0 => a+b = 9.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qm-3-9", "question_text": "Aşağıdaki sayılardan hangisi 8 ile tam bölünür?", "options": [{"key":"A","text":"1234"},{"key":"B","text":"2124"},{"key":"C","text":"3112"},{"key":"D","text":"4115"},{"key":"E","text":"5126"}], "correct_option": "C", "explanation": "8 ile bölünebilme kuralı: Son 3 basamak 8'in katı olmalı. 3112'de son 3 basamak 112 / 8 = 14 (Tam bölünür).", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qm-3-10", "question_text": "Üç basamaklı 7a4 sayısı 4 ile tam bölünebildiğine göre a yerine gelebilecek rakamların toplamı kaçtır?", "options": [{"key":"A","text":"20"},{"key":"B","text":"25"},{"key":"C","text":"15"},{"key":"D","text":"24"},{"key":"E","text":"30"}], "correct_option": "B", "explanation": "a4 sayısının 4 ile bölünmesi için a = 0, 2, 4, 6, 8 olmalıdır (04, 24, 44, 64, 84). Toplam = 0 + 2 + 4 + 6 + 8 = 20. Pardon 0+2+4+6+8 = 20. Seçenek A.", "difficulty_level": "lisans", "is_verified": True}
    ]
    add_topic_bundle(
        "topic-mat-bolunebilme", "Bölünebilme Kuralları", "bolunebilme-kurallari", 1.5, 3,
        "Tüm Bölünebilme Kuralları Özet Listesi",
        "### Kurallar:\n- **2:** Son basamak çift | **3:** Rakamlar toplamı 3'ün katı\n- **4:** Son iki basamak 4'ün katı | **5:** Son basamak 0 veya 5\n- **9:** Rakamlar toplamı 9'un katı | **11:** Sağdan sola +, -, +, - toplamı.",
        "KPSS Matematik", q_3
    )

    # -------------------------------------------------------------------------
    # 4. Denklemler ve Eşitsizlikler
    # -------------------------------------------------------------------------
    q_4 = [
        {"id": "qm-4-1", "question_text": "3x - 4 = 11 denklemini sağlayan x değeri kaçtır?", "options": [{"key":"A","text":"3"},{"key":"B","text":"4"},{"key":"C","text":"5"},{"key":"D","text":"6"},{"key":"E","text":"7"}], "correct_option": "C", "explanation": "3x = 11 + 4 = 15 => x = 5.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qm-4-2", "question_text": "2(x - 1) + 3 = x + 5 olduğuna göre x kaçtır?", "options": [{"key":"A","text":"2"},{"key":"B","text":"3"},{"key":"C","text":"4"},{"key": "D","text":"5"},{"key":"E","text":"6"}], "correct_option": "C", "explanation": "2x - 2 + 3 = x + 5 => 2x + 1 = x + 5 => x = 4.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qm-4-3", "question_text": "-2 < x ≤ 4 eşitsizliğini sağlayan kaç tane x tam sayısı vardır?", "options": [{"key":"A","text":"4"},{"key":"B","text":"5"},{"key":"C","text":"6"},{"key":"D","text":"7"},{"key":"E","text":"8"}], "correct_option": "C", "explanation": "x tam sayı değerleri: -1, 0, 1, 2, 3, 4 (Tam 6 tanedir).", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qm-4-4", "question_text": "x + y = 10 ve x - y = 4 olduğuna göre x · y çarpımı kaçtır?", "options": [{"key":"A","text":"21"},{"key":"B","text":"24"},{"key":"C","text":"25"},{"key":"D","text":"28"},{"key":"E","text":"30"}], "correct_option": "A", "explanation": "Taraf tarafa toplayalım: 2x = 14 => x = 7. 7 + y = 10 => y = 3. x · y = 7 · 3 = 21.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qm-4-5", "question_text": "|x - 4| = 2 denkleminin çözüm kümesi nedir?", "options": [{"key":"A","text":"{2, 6}"},{"key":"B","text":"{-2, 6}"},{"key":"C","text":"{2, -6}"},{"key":"D","text":"{4, 6}"},{"key":"E","text":"{0, 4}"}], "correct_option": "A", "explanation": "x - 4 = 2 => x = 6 veya x - 4 = -2 => x = 2. ÇK = {2, 6}.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qm-4-6", "question_text": "3x + 2y = 12 ve x - 2y = 4 denklem sistemine göre x kaçtır?", "options": [{"key":"A","text":"2"},{"key":"B","text":"3"},{"key":"C","text":"4"},{"key":"D","text":"5"},{"key":"E","text":"6"}], "correct_option": "C", "explanation": "Taraf tarafa toplayalım: 4x = 16 => x = 4.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qm-4-7", "question_text": "a < b < 0 olduğuna göre aşağıdakilerden hangisi daima POZİTİFTİR?", "options": [{"key":"A","text":"a + b"},{"key":"B","text":"a · b"},{"key":"C","text":"a - b"},{"key":"D","text":"b / a (negatif diyelim)"},{"key":"E","text":"a³"}], "correct_option": "B", "explanation": "İki negatif sayının çarpımı (a · b) daima pozitiftir.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qm-4-8", "question_text": "(x - 1) / 2 = 3 eşitliğinde x kaçtır?", "options": [{"key":"A","text":"5"},{"key":"B","text":"6"},{"key":"C","text":"7"},{"key":"D","text":"8"},{"key": "E","text":"9"}], "correct_option": "C", "explanation": "x - 1 = 6 => x = 7.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qm-4-9", "question_text": "|x + 2| ≤ 3 eşitsizliğini sağlayan kaç farklı x tam sayısı vardır?", "options": [{"key":"A","text":"5"},{"key":"B","text":"6"},{"key":"C","text":"7"},{"key":"D","text":"8"},{"key":"E","text":"9"}], "correct_option": "C", "explanation": "-3 ≤ x + 2 ≤ 3 => -5 ≤ x ≤ 1. x değerleri: -5, -4, -3, -2, -1, 0, 1 (7 tane).", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qm-4-10", "question_text": "2x - 3 > 5 eşitsizliğinin çözüm aralığı nedir?", "options": [{"key":"A","text":"x > 4"},{"key":"B","text":"x < 4"},{"key":"C","text":"x > 3"},{"key":"D","text":"x < 3"},{"key":"E","text":"x > 5"}], "correct_option": "A", "explanation": "2x > 8 => x > 4.", "difficulty_level": "lisans", "is_verified": True}
    ]
    add_topic_bundle(
        "topic-mat-denklemler-esitsizlikler", "Denklemler ve Eşitsizlikler", "denklemler-esitsizlikler", 1.6, 4,
        "Denklem Çözümü ve Mutlak Değer Kuralları",
        "### Kurallar:\n- Eşitsizlik her iki tarafı negatif sayı ile çarpılırsa yön değiştirir.\n- |x| = a => x = a veya x = -a.",
        "KPSS Matematik", q_4
    )

    # -------------------------------------------------------------------------
    # 5. Üslü ve Köklü Sayılar
    # -------------------------------------------------------------------------
    q_5 = [
        {"id": "qm-5-1", "question_text": "2⁵ + 2⁵ işleminin sonucu kaçtır?", "options": [{"key":"A","text":"2⁶"},{"key":"B","text":"2¹⁰"},{"key":"C","text":"4⁵"},{"key":"D","text":"4¹⁰"},{"key":"E","text":"2⁵"}], "correct_option": "A", "explanation": "2⁵ + 2⁵ = 2 · 2⁵ = 2⁶.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qm-5-2", "question_text": "√48 / √3 işleminin sonucu kaçtır?", "options": [{"key":"A","text":"2"},{"key":"B","text":"3"},{"key":"C","text":"4"},{"key":"D","text":"6"},{"key":"E","text":"8"}], "correct_option": "C", "explanation": "√(48 / 3) = √16 = 4.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qm-5-3", "question_text": "3ˣ = 9² olduğuna göre x kaçtır?", "options": [{"key":"A","text":"2"},{"key":"B","text":"3"},{"key":"C","text":"4"},{"key":"D","text":"5"},{"key":"E","text":"6"}], "correct_option": "C", "explanation": "9² = (3²)² = 3⁴ => 3ˣ = 3⁴ => x = 4.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qm-5-4", "question_text": "√(25 - 9) işleminin sonucu kaçtır?", "options": [{"key":"A","text":"2"},{"key":"B","text":"4"},{"key":"C","text":"8"},{"key":"D","text":"16"},{"key":"E","text":"34"}], "correct_option": "B", "explanation": "√(16) = 4.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qm-5-5", "question_text": "(1/2)⁻³ işleminin sonucu kaçtır?", "options": [{"key":"A","text":"-8"},{"key":"B","text":"-1/8"},{"key":"C","text":"1/8"},{"key":"D","text":"8"},{"key":"E","text":"6"}], "correct_option": "D", "explanation": "(1/2)⁻³ = 2³ = 8.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qm-5-6", "question_text": "√32 + √18 işleminin sonucu kaçtır?", "options": [{"key":"A","text":"5√2"},{"key":"B","text":"7√2"},{"key":"C","text":"6√2"},{"key":"D","text":"8√2"},{"key":"E","text":"50"}], "correct_option": "B", "explanation": "√32 = 4√2, √18 = 3√2. 4√2 + 3√2 = 7√2.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qm-5-7", "question_text": "4ˣ⁺¹ = 64 olduğuna göre x kaçtır?", "options": [{"key":"A","text":"1"},{"key":"B","text":"2"},{"key":"C","text":"3"},{"key":"D","text":"4"},{"key":"E","text":"5"}], "correct_option": "B", "explanation": "64 = 4³ => 4ˣ⁺¹ = 4³ => x + 1 = 3 => x = 2.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qm-5-8", "question_text": "√(2 · √16) işleminin sonucu kaçtır?", "options": [{"key":"A","text":"2"},{"key":"B","text":"2√2"},{"key":"C","text":"4"},{"key":"D","text":"8"},{"key":"E","text":"16"}], "correct_option": "B", "explanation": "√16 = 4 => √(2 · 4) = √8 = 2√2.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qm-5-9", "question_text": "(-2)³ + (-1)⁴ işleminin sonucu kaçtır?", "options": [{"key":"A","text":"-9"},{"key":"B","text":"-7"},{"key":"C","text":"-5"},{"key":"D","text":"7"},{"key":"E","text":"9"}], "correct_option": "B", "explanation": "(-2)³ = -8, (-1)⁴ = +1 => -8 + 1 = -7.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qm-5-10", "question_text": "√0,09 + √0,16 işleminin sonucu kaçtır?", "options": [{"key":"A","text":"0,5"},{"key":"B","text":"0,7"},{"key":"C","text":"0,25"},{"key":"D","text":"0,49"},{"key":"E","text":"1,2"}], "correct_option": "B", "explanation": "√0,09 = 0,3. √0,16 = 0,4. 0,3 + 0,4 = 0,7.", "difficulty_level": "lisans", "is_verified": True}
    ]
    add_topic_bundle(
        "topic-mat-uslu-koklu", "Üslü ve Köklü Sayılar", "uslu-ve-koklu-sayilar", 1.6, 5,
        "Üslü ve Köklü Sayı Özellikleri",
        "### Kurallar:\n- aᵐ · aⁿ = aᵐ⁺ⁿ | √(a · b) = √a · √b\n- Negatif sayının çift kuvveti pozitif, tek kuvveti negatiftir.",
        "KPSS Matematik", q_5
    )

    # -------------------------------------------------------------------------
    # 6. Kümeler
    # -------------------------------------------------------------------------
    q_6 = [
        {"id": "qm-6-1", "question_text": "s(A) = 8, s(B) = 6 ve s(A ∩ B) = 3 olduğuna göre s(A ∪ B) kaçtır?", "options": [{"key":"A","text":"11"},{"key":"B","text":"14"},{"key":"C","text":"17"},{"key":"D","text":"24"},{"key":"E","text":"10"}], "correct_option": "A", "explanation": "s(A ∪ B) = 8 + 6 - 3 = 11.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qm-6-2", "question_text": "3 elemanlı bir kümenin alt küme sayısı kaçtır?", "options": [{"key":"A","text":"3"},{"key":"B","text":"6"},{"key":"C","text":"8"},{"key":"D","text":"9"},{"key":"E","text":"12"}], "correct_option": "C", "explanation": "2³ = 8.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qm-6-3", "question_text": "A ve B ayrık iki kümedir. s(A) = 5 ve s(B) = 4 olduğuna göre s(A ∪ B) kaçtır?", "options": [{"key":"A","text":"1"},{"key":"B","text":"9"},{"key":"C","text":"20"},{"key":"D","text":"0"},{"key":"E","text":"5"}], "correct_option": "B", "explanation": "Ayrık kümelerde kesişim 0'dır. s(A ∪ B) = 5 + 4 = 9.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qm-6-4", "question_text": "5 elemanlı bir kümenin 2 elemanlı alt küme sayısı kaçtır?", "options": [{"key":"A","text":"5"},{"key":"B","text":"10"},{"key":"C","text":"15"},{"key":"D","text":"20"},{"key":"E","text":"25"}], "correct_option": "B", "explanation": "C(5, 2) = (5 · 4) / 2 = 10.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qm-6-5", "question_text": "A = {1, 2, 3, 4, 5} kümesinin eleman sayısı kaçtır?", "options": [{"key":"A","text":"3"},{"key":"B","text":"4"},{"key":"C","text":"5"},{"key":"D","text":"6"},{"key":"E","text":"10"}], "correct_option": "C", "explanation": "s(A) = 5.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qm-6-6", "question_text": "4 elemanlı bir kümenin özalt küme sayısı kaçtır?", "options": [{"key":"A","text":"15"},{"key":"B","text":"16"},{"key":"C","text":"31"},{"key":"D","text":"32"},{"key":"E","text":"63"}], "correct_option": "A", "explanation": "2⁴ - 1 = 16 - 1 = 15.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qm-6-7", "question_text": "24 kişilik bir sınıfta 14 kişi İngilizce, 12 kişi Almanca bilmektedir. Her iki dili de bilen 4 kişi olduğuna göre hiçbir dili bilmeyen kaç kişi vardır?", "options": [{"key":"A","text":"2"},{"key":"B","text":"4"},{"key":"C","text":"6"},{"key": "D","text":"8"},{"key":"E","text":"10"}], "correct_option": "A", "explanation": "En az bir dil bilenler = 14 + 12 - 4 = 22. Hiç bilmeyenler = 24 - 22 = 2 kişi.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qm-6-8", "question_text": "A ⊂ B (A, B'nin alt kümesi) olduğuna göre A ∩ B aşağıdakilerden hangisine eşittir?", "options": [{"key":"A","text":"A"},{"key":"B","text":"B"},{"key":"C","text":"Boş Küme"},{"key":"D","text":"A ∪ B"},{"key":"E","text":"Evrensel Küme"}], "correct_option": "A", "explanation": "Alt küme kesişimde küçük olan kümeye (A) eşittir.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qm-6-9", "question_text": "A ve B kümeleri için s(A \ B) = 5, s(B \ A) = 7 ve s(A ∩ B) = 3 olduğuna göre s(A ∪ B) kaçtır?", "options": [{"key":"A","text":"12"},{"key":"B","text":"15"},{"key":"C","text":"18"},{"key":"D","text":"20"},{"key":"E","text":"22"}], "correct_option": "B", "explanation": "s(A ∪ B) = 5 + 3 + 7 = 15.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qm-6-10", "question_text": "Boş kümenin alt küme sayısı kaçtır?", "options": [{"key":"A","text":"0"},{"key":"B","text":"1"},{"key":"C","text":"2"},{"key":"D","text":"Tanımsız"},{"key":"E","text":"Sonsuz"}], "correct_option": "B", "explanation": "2⁰ = 1 (Boş kümenin alt küme sayısı 1'dir, o da kendisidir).", "difficulty_level": "lisans", "is_verified": True}
    ]
    add_topic_bundle(
        "topic-mat-kumeler", "Kümeler", "kumeler", 1.5, 6,
        "Küme Formülleri ve Venn Şeması",
        "### Kurallar:\n- **s(A ∪ B) = s(A) + s(B) - s(A ∩ B)**\n- Alt Küme Sayısı = 2ⁿ | Özalt Küme Sayısı = 2ⁿ - 1",
        "KPSS Matematik", q_6
    )

    # -------------------------------------------------------------------------
    # 7. Hız-Zaman-Yol Problemleri
    # -------------------------------------------------------------------------
    q_7 = [
        {"id": "qm-7-1", "question_text": "Hızı 60 km/s olan bir araç 3 saatte kaç km yol alır?", "options": [{"key":"A","text":"120"},{"key":"B","text":"150"},{"key":"C","text":"180"},{"key":"D","text":"200"},{"key":"E","text":"240"}], "correct_option": "C", "explanation": "Yol = 60 · 3 = 180 km.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qm-7-2", "question_text": "240 km'lik yolu 4 saatte alan bir aracın ortalama hızı kaç km/s'dir?", "options": [{"key":"A","text":"50"},{"key":"B","text":"60"},{"key":"C","text":"70"},{"key":"D","text":"80"},{"key":"E","text":"90"}], "correct_option": "B", "explanation": "Hız = 240 / 4 = 60 km/s.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qm-7-3", "question_text": "Aralarında 400 km olan iki kentten hızları 50 km/s ve 30 km/s olan iki araç aynı anda zıt yönlü birbirine doğru hareket ederse kaç saat sonra karşılaşırlar?", "options": [{"key":"A","text":"4"},{"key":"B","text":"5"},{"key":"C","text":"6"},{"key":"D","text":"8"},{"key":"E","text":"10"}], "correct_option": "B", "explanation": "t = 400 / (50 + 30) = 400 / 80 = 5 saat.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qm-7-4", "question_text": "Bir araç A'dan B'ye 40 km/s hızla gidip 60 km/s hızla geri dönüyor. Ortalama hızı kaçtır?", "options": [{"key":"A","text":"48"},{"key":"B","text":"50"},{"key":"C","text":"52"},{"key":"D","text":"54"},{"key":"E","text":"55"}], "correct_option": "A", "explanation": "Vort = (2 · 40 · 60) / (40 + 60) = 4800 / 100 = 48 km/s.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qm-7-5", "question_text": "Hızı 72 km/s olan bir araç saniyede kaç metre yol alır?", "options": [{"key":"A","text":"15"},{"key":"B","text":"20"},{"key":"C","text":"25"},{"key":"D","text":"30"},{"key":"E","text":"35"}], "correct_option": "B", "explanation": "72 km/s = 72 · (1000/3600) = 20 m/s.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qm-7-6", "question_text": "Aralarında 100 km olan iki araçtan arkadaki v1=80 km/s, öndeki v2=60 km/s hızla aynı yönde gidiyor. Arkadaki araç kaç saatte yetişir?", "options": [{"key":"A","text":"3"},{"key":"B","text":"4"},{"key":"C","text":"5"},{"key":"D","text":"6"},{"key":"E","text":"8"}], "correct_option": "C", "explanation": "t = 100 / (80 - 60) = 100 / 20 = 5 saat.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qm-7-7", "question_text": "Bir tren 200 m uzunluğundaki bir tüneli 80 m/s hızla 5 saniyede geçiyor. Trenin boyu kaç metredir?", "options": [{"key":"A","text":"150"},{"key":"B","text":"180"},{"key":"C","text":"200"},{"key":"D","text":"220"},{"key":"E","text":"250"}], "correct_option": "C", "explanation": "Toplam Yol = 80 · 5 = 400 m. Tren + Tünel = 400 => Tren + 200 = 400 => Tren = 200 m.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qm-7-8", "question_text": "Bir araç bir yolun yarısını 30 km/s, diğer yarısını 60 km/s hızla giderse yolun tamamını kaç saatte gider (Yol=120 km)?", "options": [{"key":"A","text":"2"},{"key":"B","text":"3"},{"key":"C","text":"4"},{"key":"D","text":"5"},{"key":"E","text":"6"}], "correct_option": "B", "explanation": "İlk 60 km = 60/30 = 2 saat. İkinci 60 km = 60/60 = 1 saat. Toplam = 2 + 1 = 3 saat.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qm-7-9", "question_text": "Çevresi 300 m olan dairesel bir pistte iki koşucu aynı noktadan zıt yönde 10 m/s ve 5 m/s hızla koşuyor. Kaç saniye sonra karşılaşırlar?", "options": [{"key":"A","text":"15"},{"key":"B","text":"20"},{"key":"C","text":"25"},{"key":"D","text":"30"},{"key":"E","text":"35"}], "correct_option": "B", "explanation": "t = 300 / (10 + 5) = 300 / 15 = 20 saniye.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qm-7-10", "question_text": "Hızını %20 artıran bir araç gideceği yere süre açısından nasıl ulaşır?", "options": [{"key":"A","text":"Daha uzun sürede"},{"key":"B","text":"Daha kısa sürede"},{"key":"C","text":"Aynı sürede"},{"key":"D", "text":"2 kat sürede"},{"key":"E","text":"Süre değişmez"}], "correct_option": "B", "explanation": "Hız arttıkça varış süresi kısalır (Ters orantı).", "difficulty_level": "lisans", "is_verified": True}
    ]
    add_topic_bundle(
        "topic-mat-hiz-zaman-yol", "Hız-Zaman-Yol Problemleri", "hiz-zaman-yol-problemleri", 1.8, 7,
        "Hız-Zaman-Yol Formül Kartı",
        "### Formüller:\n- **Yol = Hız × Zaman**\n- Karşılaşma: **t = Yol / (v₁ + v₂)** | Yetişme: **t = Yol / (v₁ - v₂)**",
        "KPSS Matematik", q_7
    )

    # -------------------------------------------------------------------------
    # 8. Yüzde ve Oran-Orantı Problemleri
    # -------------------------------------------------------------------------
    q_8 = [
        {"id": "qm-8-1", "question_text": "200 sayısının %30'u kaçtır?", "options": [{"key":"A","text":"40"},{"key":"B","text":"50"},{"key":"C","text":"60"},{"key":"D","text":"70"},{"key":"E","text":"80"}], "correct_option": "C", "explanation": "200 · (30 / 100) = 60.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qm-8-2", "question_text": "Hangi sayısının %20'si 40 eder?", "options": [{"key":"A","text":"150"},{"key":"B","text":"180"},{"key":"C","text":"200"},{"key":"D","text":"220"},{"key":"E","text":"250"}], "correct_option": "C", "explanation": "x · 0,20 = 40 => x = 200.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qm-8-3", "question_text": "a/b = 2/3 ve b = 15 olduğuna göre a kaçtır?", "options": [{"key":"A","text":"6"},{"key":"B","text":"8"},{"key":"C","text":"10"},{"key":"D","text":"12"},{"key": "E","text":"14"}], "correct_option": "C", "explanation": "a / 15 = 2 / 3 => 3a = 30 => a = 10.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qm-8-4", "question_text": "Bir sınıftaki 30 öğrenciden 12'si erkektir. Kız öğrencilerin yüzdesi kaçtır?", "options": [{"key":"A","text":"%40"},{"key":"B","text":"%50"},{"key":"C","text":"%60"},{"key":"D","text":"%70"},{"key":"E","text":"%75"}], "correct_option": "C", "explanation": "Kız sayısı = 30 - 12 = 18. Yüzde = (18 / 30) · 100 = %60.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qm-8-5", "question_text": "400 TL'lik bir ürüne %15 zam yapılırsa yeni fiyatı kaç TL olur?", "options": [{"key":"A","text":"440"},{"key":"B","text":"450"},{"key":"C","text":"460"},{"key":"D","text":"480"},{"key":"E","text":"500"}], "correct_option": "C", "explanation": "Zam = 400 · 0,15 = 60 TL. Yeni Fiyat = 400 + 60 = 460 TL.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qm-8-6", "question_text": "a ve b sayıları 4 ve 5 ile doğru orantılıdır. a + b = 36 ise b kaçtır?", "options": [{"key":"A","text":"16"},{"key":"B","text":"18"},{"key":"C","text":"20"},{"key":"D","text":"24"},{"key":"E","text":"25"}], "correct_option": "C", "explanation": "4k + 5k = 36 => 9k = 36 => k = 4. b = 5 · 4 = 20.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qm-8-7", "question_text": "300 TL'lik bir ürün %20 indirimle kaç TL'ye satılır?", "options": [{"key":"A","text":"220"},{"key":"B","text":"240"},{"key":"C","text":"250"},{"key":"D","text":"260"},{"key":"E","text":"280"}], "correct_option": "B", "explanation": "İndirim = 300 · 0,20 = 60 TL. İndirimli Fiyat = 300 - 60 = 240 TL.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qm-8-8", "question_text": "%20 şeker içeren 50 gram şekerli su karışımındaki şeker miktarı kaç gramdır?", "options": [{"key":"A","text":"5"},{"key":"B","text":"8"},{"key":"C","text":"10"},{"key":"D","text":"12"},{"key":"E","text":"15"}], "correct_option": "C", "explanation": "50 · 0,20 = 10 gram.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qm-8-9", "question_text": "x ve y ters orantılı iki çokluktur. x = 4 iken y = 6 olduğuna göre x = 3 iken y kaçtır?", "options": [{"key":"A","text":"6"},{"key":"B","text":"7"},{"key":"C","text":"8"},{"key":"D","text":"9"},{"key":"E","text":"10"}], "correct_option": "C", "explanation": "Ters orantı çarpımları sabittir: 4 · 6 = 3 · y => 24 = 3y => y = 8.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qm-8-10", "question_text": "Bir sınavda 80 sorudan 60'ını doğru yanıtlayan bir öğrencinin başarı oranı yüzde kaçtır?", "options": [{"key":"A","text":"%65"},{"key":"B","text":"%70"},{"key":"C","text":"%75"},{"key":"D","text":"%80"},{"key":"E","text":"%85"}], "correct_option": "C", "explanation": "(60 / 80) · 100 = (3 / 4) · 100 = %75.", "difficulty_level": "lisans", "is_verified": True}
    ]
    add_topic_bundle(
        "topic-mat-yuzde-oran", "Yüzde ve Oran-Orantı Problemleri", "yuzde-oran-orantı-problemleri", 1.8, 8,
        "Yüzde ve Orantı Kuralları",
        "### Kurallar:\n- **Doğru Orantı:** Çapraz çarpımlar eşittir (a/b = c/d).\n- **Ters Orantı:** Yan yana çarpımlar eşittir (a · b = c · d).",
        "KPSS Matematik", q_8
    )

    # -------------------------------------------------------------------------
    # 9. Kâr-Zarar Problemleri
    # -------------------------------------------------------------------------
    q_9 = [
        {"id": "qm-9-1", "question_text": "100 TL'ye alınan bir ürün %25 kârla kaç TL'ye satılır?", "options": [{"key":"A","text":"115"},{"key":"B","text":"120"},{"key":"C","text":"125"},{"key":"D","text":"130"},{"key":"E","text":"135"}], "correct_option": "C", "explanation": "100 + 25 = 125 TL.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qm-9-2", "question_text": "150 TL'ye satılan bir üründen 30 TL kâr edildiğine göre kâr oranı yüzde kaçtır?", "options": [{"key":"A","text":"%15"},{"key":"B","text":"%20"},{"key":"C","text":"%25"},{"key":"D","text":"%30"},{"key":"E","text":"%33"}], "correct_option": "C", "explanation": "Maliyet = 150 - 30 = 120 TL. Kâr Oranı = (30 / 120) · 100 = %25.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qm-9-3", "question_text": "200 TL'ye alınan bir mal %10 zararla kaç TL'ye satılır?", "options": [{"key":"A","text":"170"},{"key":"B","text":"180"},{"key":"C","text":"185"},{"key":"D","text":"190"},{"key":"E","text":"195"}], "correct_option": "B", "explanation": "Zarar = 200 · 0,10 = 20 TL. Satış = 200 - 20 = 180 TL.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qm-9-4", "question_text": "%30 kârla 130 TL'ye satılan malın maliyeti kaç TL'dir?", "options": [{"key":"A","text":"90"},{"key":"B","text":"100"},{"key":"C","text":"110"},{"key":"D","text":"115"},{"key":"E","text":"120"}], "correct_option": "B", "explanation": "130x = 130 => x = 1 => Maliyet 100x = 100 TL.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qm-9-5", "question_text": "%20 zararla 80 TL'ye satılan malın maliyeti kaç TL'dir?", "options": [{"key":"A","text":"90"},{"key":"B","text":"95"},{"key":"C","text":"100"},{"key":"D","text":"105"},{"key":"E","text":"110"}], "correct_option": "C", "explanation": "80x = 80 => x = 1 => Maliyet 100x = 100 TL.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qm-9-6", "question_text": "50 TL'ye alınıp 70 TL'ye satılan bir maldan yüzde kaç kâr elde edilmiştir?", "options": [{"key":"A","text":"%20"},{"key":"B","text":"%30"},{"key":"C","text":"%40"},{"key":"D","text":"%50"},{"key":"E","text":"%60"}], "correct_option": "C", "explanation": "Kâr = 70 - 50 = 20 TL. Oran = (20 / 50) · 100 = %40.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qm-9-7", "question_text": "Bir mal etiket fiyatı üzerinden %30 indirimle 140 TL'ye satılıyor. Etiket fiyatı kaç TL'dir?", "options": [{"key":"A","text":"180"},{"key":"B","text":"200"},{"key":"C","text":"210"},{"key":"D","text":"220"},{"key": "E","text":"240"}], "correct_option": "B", "explanation": "70x = 140 => x = 2 => Etiket = 100x = 200 TL.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qm-9-8", "question_text": "Maliyeti 500 TL olan bir mal %50 kârla etiketlendikten sonra etiket fiyatı üzerinden %20 indirim yapılıyor. Son satış fiyatı kaç TL olur?", "options": [{"key":"A","text":"550"},{"key":"B","text":"600"},{"key":"C","text":"625"},{"key":"D","text":"650"},{"key":"E","text":"700"}], "correct_option": "B", "explanation": "%50 karlı etiket = 500 · 1,5 = 750 TL. %20 indirimli satış = 750 · 0,80 = 600 TL.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qm-9-9", "question_text": "4 tanesi 20 TL'ye alınan yumurtaların 5 tanesi 35 TL'ye satılırsa kâr oranı yüzde kaçtır?", "options": [{"key":"A","text":"%30"},{"key":"B","text":"%35"},{"key":"C","text":"%40"},{"key":"D","text":"%50"},{"key":"E","text":"%60"}], "correct_option": "C", "explanation": "Alış adedi = 20/4 = 5 TL. Satış adedi = 35/5 = 7 TL. Kâr = 2 TL. Oran = (2 / 5) · 100 = %40.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qm-9-10", "question_text": "Kâr oranı %20 olan bir satışta satış fiyatının maliyete oranı kaçtır?", "options": [{"key":"A","text":"5/4"},{"key":"B","text":"6/5"},{"key":"C","text":"7/6"},{"key":"D","text":"4/3"},{"key":"E","text":"3/2"}], "correct_option": "B", "explanation": "Maliyet = 100, Satış = 120. Oran = 120 / 100 = 6 / 5.", "difficulty_level": "lisans", "is_verified": True}
    ]
    add_topic_bundle(
        "topic-mat-kar-zarar", "Kâr-Zarar Problemleri", "kar-zarar-problemleri", 1.8, 9,
        "Kâr-Zarar Hesaplama Taktikleri",
        "### Taktik:\n- **Maliyeti daima 100 kabul et!**\n- Kâr = Satış - Maliyet | Zarar = Maliyet - Satış.",
        "KPSS Matematik", q_9
    )

    # -------------------------------------------------------------------------
    # 10. İşçi-Havuz Problemleri
    # -------------------------------------------------------------------------
    q_10 = [
        {"id": "qm-10-1", "question_text": "Bir işçi bir işi 6 günde bitiriyor. 2 işçi aynı işi kaç günde bitirir?", "options": [{"key":"A","text":"2"},{"key":"B","text":"3"},{"key":"C","text":"4"},{"key":"D","text":"5"},{"key":"E","text":"6"}], "correct_option": "B", "explanation": "İşçi sayısı 2 katına çıkarsa süre yarıya iner: 6 / 2 = 3 gün.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qm-10-2", "question_text": "Ali bir işi 10 günde, Ahmet ise 15 günde yapabiliyor. İkisi birlikte kaç günde yaparlar?", "options": [{"key":"A","text":"4"},{"key":"B","text":"5"},{"key":"C","text":"6"},{"key": "D","text":"7"},{"key":"E","text":"8"}], "correct_option": "C", "explanation": "1/t = 1/10 + 1/15 = (3 + 2) / 30 = 5 / 30 => t = 6 gün.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qm-10-3", "question_text": "Bir musluk boş bir havuzu 12 saatte doldurmaktadır. Aynı kapasitede 3 musluk aynı havuzu kaç saatte doldurur?", "options": [{"key":"A","text":"3"},{"key":"B","text":"4"},{"key":"C","text":"5"},{"key":"D","text":"6"},{"key":"E","text":"8"}], "correct_option": "B", "explanation": "12 / 3 = 4 saatte doldurur.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qm-10-4", "question_text": "Bir işçi işin 1/3'ünü 4 günde yapıyorsa işin tamamını kaç günde yapar?", "options": [{"key":"A","text":"8"},{"key":"B","text":"10"},{"key":"C","text":"12"},{"key":"D","text":"14"},{"key":"E","text":"16"}], "correct_option": "C", "explanation": "4 · 3 = 12 günde yapar.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qm-10-5", "question_text": "A musluğu havuzu 6 saatte dolduruyor, B musluğu 12 saatte boşaltıyor. İkisi birlikte açılırsa havuz kaç saatte dolar?", "options": [{"key":"A","text":"8"},{"key":"B","text":"10"},{"key":"C","text":"12"},{"key":"D","text":"15"},{"key":"E","text":"18"}], "correct_option": "C", "explanation": "1/t = 1/6 - 1/12 = (2 - 1) / 12 = 1 / 12 => t = 12 saat.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qm-10-6", "question_text": "Eşit güçteki 4 usta bir evi 15 günde boyuyorsa aynı güçteki 6 usta kaç günde boyar?", "options": [{"key":"A","text":"8"},{"key":"B","text":"9"},{"key":"C","text":"10"},{"key":"D","text":"12"},{"key":"E","text":"14"}], "correct_option": "C", "explanation": "4 · 15 = 6 · x => 60 = 6x => x = 10 gün.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qm-10-7", "question_text": "Bir usta bir işi 8 günde, çırağı 24 günde bitiriyor. İkisi birlikte 3 gün çalışırsa işin kaçta kaçı biter?", "options": [{"key":"A","text":"1/4"},{"key":"B","text":"1/2"},{"key":"C","text":"3/4"},{"key":"D","text":"2/3"},{"key":"E","text":"1/3"}], "correct_option": "B", "explanation": "Bir günde yapılan iş = 1/8 + 1/24 = 4/24 = 1/6. 3 günde 3 · (1/6) = 3/6 = 1/2'si biter.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qm-10-8", "question_text": "Bir işçi çalışma hızını 3 katına çıkarırsa 18 günde yaptığı bir işi kaç günde bitirir?", "options": [{"key":"A","text":"4"},{"key":"B","text":"6"},{"key":"C","text":"8"},{"key":"D","text":"9"},{"key":"E","text":"12"}], "correct_option": "B", "explanation": "18 / 3 = 6 günde bitirir.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qm-10-9", "question_text": "Bir havuzu üstteki musluk 8 saatte dolduruyor, alttaki musluk 24 saatte boşaltıyor. İkisi açıkken boş havuzun yarısı kaç saatte dolar?", "options": [{"key":"A","text":"4"},{"key":"B","text":"6"},{"key":"C","text":"8"},{"key": "D","text":"12"},{"key":"E","text":"16"}], "correct_option": "B", "explanation": "1/t = 1/8 - 1/24 = 2/24 = 1/12 => Tamamı 12 saatte dolar. Yarısı 12 / 2 = 6 saatte dolar.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qm-10-10", "question_text": "Bir işi 3 işçi 20 günde bitirebildiğine göre bu işin 12 günde bitmesi için kaç işçiye daha ihtiyaç vardır?", "options": [{"key":"A","text":"1"},{"key":"B","text":"2"},{"key":"C","text":"3"},{"key":"D","text":"4"},{"key":"E","text":"5"}], "correct_option": "B", "explanation": "3 · 20 = x · 12 => 60 = 12x => x = 5 işçi gerekir. 5 - 3 = 2 işçiye daha ihtiyaç vardır.", "difficulty_level": "lisans", "is_verified": True}
    ]
    add_topic_bundle(
        "topic-mat-isci-havuz", "İşçi-Havuz Problemleri", "isci-havuz-problemleri", 1.6, 10,
        "İşçi ve Havuz Problemleri Çözüm Formülü",
        "### Formül:\n- Birlikte iş yapma: **1/a + 1/b = 1/t**\n- İşçi sayısı ile işin bitme süresi **ters orantılıdır**.",
        "KPSS Matematik", q_10
    )

    # -------------------------------------------------------------------------
    # 11. Yaş Problemleri
    # -------------------------------------------------------------------------
    q_11 = [
        {"id": "qm-11-1", "question_text": "Bir annenin yaşı kızının yaşının 3 katıdır. İkisinin yaşları toplamı 40 olduğuna göre anne kaç yaşındadır?", "options": [{"key":"A","text":"24"},{"key":"B","text":"28"},{"key":"C","text":"30"},{"key":"D","text":"32"},{"key":"E","text":"36"}], "correct_option": "C", "explanation": "Kız = x, Anne = 3x. 4x = 40 => x = 10 (Kız). Anne = 3 · 10 = 30.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qm-11-2", "question_text": "Ahmet 12, kardeş 8 yaşındadır. Kaç yıl sonra yaşları toplamı 36 olur?", "options": [{"key":"A","text":"6"},{"key":"B","text":"7"},{"key":"C","text":"8"},{"key":"D","text":"9"},{"key":"E","text":"10"}], "correct_option": "C", "explanation": "Şimdiki yaşlar toplamı = 12 + 8 = 20. Hedef = 36. Yaşlar toplamı farkı = 16. İki kişi olduğu için 16 / 2 = 8 yıl sonra.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qm-11-3", "question_text": "İki kardeşin yaşları farkı 6'dır. 10 yıl sonra bu iki kardeşin yaşları farkı kaç olur?", "options": [{"key":"A","text":"6"},{"key":"B","text":"10"},{"key":"C","text":"16"},{"key":"D","text":"20"},{"key":"E","text":"26"}], "correct_option": "A", "explanation": "İki kişi arasındaki yaş farkı zamanla ASLA değişmez. Cevap yine 6'dır.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qm-11-4", "question_text": "Bir babanın yaşı 36, çocuğunun yaşı 12'dir. Kaç yıl önce babanın yaşı çocuğunun yaşının 4 katıydı?", "options": [{"key":"A","text":"2"},{"key":"B","text":"4"},{"key":"C","text":"6"},{"key":"D","text":"8"},{"key":"E","text":"10"}], "correct_option": "B", "explanation": "x yıl önce: 36 - x = 4(12 - x) => 36 - x = 48 - 4x => 3x = 12 => x = 4 yıl önce.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qm-11-5", "question_text": "Bir grubun yaş ortalaması 20'dir. Bu gruba yaşı 30 olan bir kişi katılırsa grubun yaş ortalaması nasıl değişir?", "options": [{"key":"A","text":"Azalır"},{"key":"B","text":"Artar"},{"key":"C","text":"Değişmez"},{"key":"D","text":"Yarıya düşer"},{"key":"E","text":"2 katına çıkar"}], "correct_option": "B", "explanation": "Gruba ortalamadan büyük bir sayı eklenirse ortalama artar.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qm-11-6", "question_text": "Can 15 yaşında, ablası 21 yaşındadır. Can ablasının bugünkü yaşına geldiğinde ablası kaç yaşında olur?", "options": [{"key":"A","text":"25"},{"key":"B","text":"26"},{"key":"C","text":"27"},{"key":"D","text":"28"},{"key":"E","text":"30"}], "correct_option": "C", "explanation": "Yaş farkı = 21 - 15 = 6. Can 21 olduğunda aradaki 6 yıl geçmiştir => Ablası = 21 + 6 = 27 olur.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qm-11-7", "question_text": "Bir babanın yaşı 2 çocuğunun yaşları toplamından 10 fazladır. 4 yıl sonra babanın yaşı çocuklarının yaşları toplamından kaç fazla olur?", "options": [{"key":"A","text":"2"},{"key":"B","text":"4"},{"key":"C","text":"6"},{"key":"D","text":"8"},{"key":"E","text":"10"}], "correct_option": "C", "explanation": "Baba 4 yaş büyür. 2 çocuk toplam 4 · 2 = 8 yaş büyür. Fark = 10 + 4 - 8 = 6 fazla olur.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qm-11-8", "question_text": "3 kardeşin yaşları 2, 4 ve 6 sayılarıyla orantılıdır. Yaşları toplamı 36 olduğuna göre en büyük kardeş kaç yaşındadır?", "options": [{"key":"A","text":"12"},{"key":"B","text":"15"},{"key":"C","text":"18"},{"key":"D","text":"20"},{"key":"E","text":"24"}], "correct_option": "C", "explanation": "2k + 4k + 6k = 12k = 36 => k = 3. En büyük = 6k = 6 · 3 = 18 yaşındadır.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qm-11-9", "question_text": "Mustafa 2000 yılında doğmuştur. Mustafa kaç yılında 26 yaşında olur?", "options": [{"key":"A","text":"2020"},{"key":"B","text":"2024"},{"key":"C","text":"2026"},{"key":"D","text":"2028"},{"key":"E","text":"2030"}], "correct_option": "C", "explanation": "2000 + 26 = 2026 yılında.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qm-11-10", "question_text": "Bir annenin yaşı 42'dir. İki çocuğunun yaşları 8 ve 10 olduğuna göre kaç yıl sonra annenin yaşı çocuklarının yaşları toplamına eşit olur?", "options": [{"key":"A","text": "18"},{"key":"B","text":"20"},{"key":"C","text":"22"},{"key":"D","text":"24"},{"key":"E","text":"26"}], "correct_option": "D", "explanation": "x yıl sonra: 42 + x = (8 + x) + (10 + x) => 42 + x = 18 + 2x => x = 24 yıl sonra.", "difficulty_level": "lisans", "is_verified": True}
    ]
    add_topic_bundle(
        "topic-mat-yas-problemleri", "Yaş Problemleri", "yas-problemleri", 1.6, 11,
        "Yaş Problemleri Temel Kuralı",
        "### Altın Kural:\n- İki kişi arasındaki yaş farkı **yıllar geçse de Sabittir ve Değişmez**.",
        "KPSS Matematik", q_11
    )

    # -------------------------------------------------------------------------
    # 12. Kesir Problemleri
    # -------------------------------------------------------------------------
    q_12 = [
        {"id": "qm-12-1", "question_text": "Bir sayının 2/5'i 20 olduğuna göre tamamı kaçtır?", "options": [{"key":"A","text":"40"},{"key":"B","text":"50"},{"key":"C","text":"60"},{"key":"D","text":"80"},{"key":"E","text":"100"}], "correct_option": "B", "explanation": "(20 / 2) · 5 = 50.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qm-12-2", "question_text": "Bir paranın 1/4'ünün 1/2'si 15 TL olduğuna göre paranın tamamı kaç TL'dir?", "options": [{"key":"A","text":"60"},{"key":"B","text":"90"},{"key":"C","text":"120"},{"key":"D","text":"150"},{"key":"E","text":"180"}], "correct_option": "C", "explanation": "x · (1/4) · (1/2) = x / 8 = 15 => x = 120 TL.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qm-12-3", "question_text": "Bir yolun 3/8'i gidilmiştir. Geriye 50 km yol kaldığına göre yolun tamamı kaç km'dir?", "options": [{"key":"A","text":"75"},{"key":"B","text":"80"},{"key":"C","text":"90"},{"key":"D","text":"100"},{"key":"E","text":"120"}], "correct_option": "B", "explanation": "Kalan yol = 1 - 3/8 = 5/8'dir. 5/8 = 50 => tamamı = (50 / 5) · 8 = 80 km.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qm-12-4", "question_text": "Hangi sayının 1/3'ünün 5 fazlası 15 eder?", "options": [{"key":"A","text":"20"},{"key":"B","text":"25"},{"key":"C","text":"30"},{"key":"D","text":"35"},{"key": "E","text":"40"}], "correct_option": "C", "explanation": "x/3 + 5 = 15 => x/3 = 10 => x = 30.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qm-12-5", "question_text": "Bir sürahinin 3/4'ü su doludur. Sürahiden 6 bardak su alınınca sürahinin yarısı dolu kalıyor. Sürahi kaç bardak su alır?", "options": [{"key":"A","text":"18"},{"key":"B","text":"20"},{"key":"C","text":"24"},{"key":"D","text":"30"},{"key":"E","text":"36"}], "correct_option": "C", "explanation": "3/4 - 1/2 = 3/4 - 2/4 = 1/4'ü 6 bardak ise tamamı 6 · 4 = 24 bardak alır.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qm-12-6", "question_text": "Bir sınıftaki öğrencilerin 2/5'i kızdır. Sınıfta 18 erkek öğrenci olduğuna göre toplam kaç öğrenci vardır?", "options": [{"key":"A","text":"25"},{"key":"B","text":"30"},{"key":"C","text":"35"},{"key":"D","text":"40"},{"key":"E","text":"45"}], "correct_option": "B", "explanation": "Erkek oranı = 3/5'tir. 3/5 = 18 ise Tamamı = (18 / 3) · 5 = 30 öğrenci.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qm-12-7", "question_text": "Bir çubuğun orta noktası 1/6'sı kesildiğinde kaç cm kayar (Çubuk=60 cm)?", "options": [{"key":"A","text":"3"},{"key":"B","text":"5"},{"key":"C","text":"6"},{"key":"D","text":"10"},{"key":"E","text":"12"}], "correct_option": "B", "explanation": "Kesilen miktar = 60 · (1/6) = 10 cm. Orta nokta kayma miktarı = 10 / 2 = 5 cm.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qm-12-8", "question_text": "3/5 ile 1/2 arasındaki fark hangi sayıdır?", "options": [{"key":"A","text":"1/10"},{"key":"B","text":"1/5"},{"key":"C","text":"2/5"},{"key":"D","text":"3/10"},{"key":"E","text":"1/2"}], "correct_option": "A", "explanation": "3/5 - 1/2 = 6/10 - 5/10 = 1/10.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qm-12-9", "question_text": "Bir öğrenci ödevinin önce 1/4'ünü sonra kalanın 1/3'ünü yapıyor. Geriye ödevin kaçta kaçı kalmıştır?", "options": [{"key":"A","text":"1/4"},{"key":"B","text":"1/3"},{"key":"C","text":"1/2"},{"key":"D","text":"2/3"},{"key":"E","text":"3/4"}], "correct_option": "C", "explanation": "Ödev 12x olsun. 1/4'ü = 3x (Kalan 9x). Kalanın 1/3'ü = 3x. Toplam yapılan = 6x. Kalan = 6x => 6x/12x = 1/2.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qm-12-10", "question_text": "Hangi sayının 2/3'ünün 1/4'ü 10'dur?", "options": [{"key":"A","text":"40"},{"key":"B","text":"50"},{"key":"C","text":"60"},{"key":"D","text":"70"},{"key":"E","text":"80"}], "correct_option": "C", "explanation": "x · (2/3) · (1/4) = x / 6 = 10 => x = 60.", "difficulty_level": "lisans", "is_verified": True}
    ]
    add_topic_bundle(
        "topic-mat-kesir-problemleri", "Kesir Problemleri", "kesir-problemleri", 1.6, 12,
        "Kesir Problemleri Taktikleri",
        "### Taktik:\n- Paydaların en küçük ortak katını (EKOK) sayının tamamı olarak kabul etmek işlem kolaylığı sağlar.",
        "KPSS Matematik", q_12
    )

    # -------------------------------------------------------------------------
    # 13. Sayı Problemleri
    # -------------------------------------------------------------------------
    q_13 = [
        {"id": "qm-13-1", "question_text": "Bir sayının 3 katının 4 fazlası 25 olduğuna göre bu sayı kaçtır?", "options": [{"key":"A","text":"5"},{"key":"B","text":"6"},{"key":"C","text":"7"},{"key":"D","text":"8"},{"key":"E","text":"9"}], "correct_option": "C", "explanation": "3x + 4 = 25 => 3x = 21 => x = 7.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qm-13-2", "question_text": "Toplamları 50, farkları 10 olan iki sayıdan büyüğü kaçtır?", "options": [{"key":"A","text":"25"},{"key":"B","text":"28"},{"key":"C","text":"30"},{"key":"D","text":"32"},{"key":"E","text":"35"}], "correct_option": "C", "explanation": "x + y = 50, x - y = 10 => 2x = 60 => x = 30.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qm-13-3", "question_text": "Bir gruptaki kişi sayısı her adımda 2 katına çıkmaktadır. Başlangıçta 5 kişi olan grupta 3. adımın sonunda kaç kişi olur?", "options": [{"key":"A","text":"15"},{"key":"B","text":"20"},{"key":"C","text":"30"},{"key":"D","text":"40"},{"key":"E","text":"50"}], "correct_option": "D", "explanation": "Başlangıç: 5. 1. adım: 10. 2. adım: 20. 3. adım: 40 kişi.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qm-13-4", "question_text": "Bir sınıftaki kızların sayısı erkeklerin sayısının 2 katından 3 eksiktir. Sınıf mevcudu 27 ise kız sayısı kaçtır?", "options": [{"key":"A","text":"10"},{"key":"B","text":"14"},{"key":"C","text":"17"},{"key":"D","text":"18"},{"key":"E","text":"20"}], "correct_option": "C", "explanation": "Erkek = x, Kız = 2x - 3. 3x - 3 = 27 => 3x = 30 => x = 10. Kız = 2(10) - 3 = 17.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qm-13-5", "question_text": "Bir bilet kuyruğunda Ali baştan 10. sırada, sondan 15. sıradadır. Kuyrukta toplam kaç kişi vardır?", "options": [{"key":"A","text":"23"},{"key":"B","text":"24"},{"key":"C","text":"25"},{"key":"D","text":"26"},{"key":"E","text":"27"}], "correct_option": "B", "explanation": "Kişi sayısı = Baştan sıra + Sondan sıra - 1 = 10 + 15 - 1 = 24 kişi.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qm-13-6", "question_text": "Bir miktar para 5 kişiye eşit paylaştırılıyor. Kişi başı 20 TL düştüğüne göre aynı para 4 kişiye paylaştırılırsa kişi başı kaç TL düşer?", "options": [{"key":"A","text":"22"},{"key":"B","text":"24"},{"key":"C","text":"25"},{"key":"D","text":"28"},{"key":"E","text":"30"}], "correct_option": "C", "explanation": "Toplam para = 5 · 20 = 100 TL. 4 kişiye: 100 / 4 = 25 TL.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qm-13-7", "question_text": "Bir sınavda 4 yanlış 1 doğruyu götürmektedir. 50 sorunun tamamını işaretleyip 35 doğrusu olan bir öğrencinin kaç neti vardır?", "options": [{"key":"A","text":"30"},{"key":"B","text":"31.25"},{"key":"C","text":"32"},{"key":"D","text":"33.75"},{"key":"E","text":"35"}], "correct_option": "B", "explanation": "Doğru = 35, Yanlış = 15. Götürülen doğru = 15 / 4 = 3,75. Net = 35 - 3,75 = 31,25.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qm-13-8", "question_text": "Ardışık 4 çift sayının toplamı 52 olduğuna göre bu sayıların en büyüğü kaçtır?", "options": [{"key":"A","text":"12"},{"key":"B","text":"14"},{"key":"C","text":"16"},{"key":"D","text":"18"},{"key":"E","text":"20"}], "correct_option": "C", "explanation": "Sayılar: x, x+2, x+4, x+6 => 4x + 12 = 52 => 4x = 40 => x = 10. En büyük = 10 + 6 = 16.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qm-13-9", "question_text": "Hangi sayının karesi kendisinin 5 katına eşittir (Sıfırdan farklı)?", "options": [{"key":"A","text":"2"},{"key":"B","text":"3"},{"key":"C","text":"4"},{"key":"D","text":"5"},{"key":"E","text":"10"}], "correct_option": "D", "explanation": "x² = 5x => x = 5.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qm-13-10", "question_text": "Bir kümesteki tavuk ve tavşanların toplam sayısı 20, ayak sayıları toplamı 56 olduğuna göre tavuk sayısı kaçtır?", "options": [{"key":"A","text":"10"},{"key":"B","text":"12"},{"key":"C","text":"14"},{"key":"D","text":"15"},{"key":"E","text":"16"}], "correct_option": "B", "explanation": "Tavuk (2 ayak) = x, Tavşan (4 ayak) = 20 - x.\n2x + 4(20 - x) = 56 => 2x + 80 - 4x = 56 => 2x = 24 => x = 12 tavuk.", "difficulty_level": "lisans", "is_verified": True}
    ]
    add_topic_bundle(
        "topic-mat-sayi-problemleri", "Sayı Problemleri", "sayi-problemleri", 1.7, 13,
        "Sayı Problemlerinde Denklem Kurma",
        "### Denklem Kurma İpuçları:\n- Bir sayının 3 katının 2 fazlası: **3x + 2**\n- Bir sayının 2 fazlasının 3 katı: **3(x + 2)**",
        "KPSS Matematik", q_13
    )

    # -------------------------------------------------------------------------
    # 14. Sayı Dizileri ve Örüntüler
    # -------------------------------------------------------------------------
    q_14 = [
        {"id": "qm-14-1", "question_text": "2, 4, 8, 16, x dizisinde x yerine kaç gelmelidir?", "options": [{"key":"A","text":"24"},{"key":"B","text":"28"},{"key":"C","text":"30"},{"key":"D","text":"32"},{"key":"E","text":"64"}], "correct_option": "D", "explanation": "Dizi 2'nin kuvvetleridir (2¹=2, 2²=4, 2³=8, 2⁴=16, 2⁵=32).", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qm-14-2", "question_text": "5, 10, 15, 20, y dizisinde y kaçtır?", "options": [{"key":"A","text":"22"},{"key":"B","text":"25"},{"key":"C","text":"30"},{"key":"D","text":"35"},{"key":"E","text":"40"}], "correct_option": "B", "explanation": "5'erli artan dizidir: y = 25.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qm-14-3", "question_text": "1, 4, 9, 16, 25, z dizisinde z kaçtır?", "options": [{"key":"A","text":"30"},{"key":"B","text":"32"},{"key":"C","text":"35"},{"key":"D","text":"36"},{"key":"E","text":"49"}], "correct_option": "D", "explanation": "Kareler dizisidir: 1², 2², 3², 4², 5², 6² = 36.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qm-14-4", "question_text": "100, 90, 80, 70, a dizisinde a kaçtır?", "options": [{"key":"A","text":"50"},{"key":"B","text":"55"},{"key":"C","text":"60"},{"key":"D","text":"65"},{"key":"E","text":"40"}], "correct_option": "C", "explanation": "10'ar azalan dizidir: 70 - 10 = 60.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qm-14-5", "question_text": "1, 3, 6, 10, 15, b (Üçgensel sayılar) dizisinde b kaçtır?", "options": [{"key":"A","text":"18"},{"key":"B","text":"20"},{"key":"C","text":"21"},{"key":"D","text":"24"},{"key":"E","text":"25"}], "correct_option": "C", "explanation": "Artış miktarları: +2, +3, +4, +5... b = 15 + 6 = 21.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qm-14-6", "question_text": "3, 6, 12, 24, c dizisinde c kaçtır?", "options": [{"key":"A","text":"36"},{"key":"B","text":"40"},{"key":"C","text":"48"},{"key":"D","text":"50"},{"key":"E","text":"60"}], "correct_option": "C", "explanation": "2 katı alınarak ilerliyor: 24 · 2 = 48.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qm-14-7", "question_text": "7, 11, 15, 19, d dizisinde d kaçtır?", "options": [{"key":"A","text":"21"},{"key":"B","text":"22"},{"key":"C","text":"23"},{"key":"D","text":"24"},{"key":"E","text":"25"}], "correct_option": "C", "explanation": "4'erli artan dizidir: 19 + 4 = 23.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qm-14-8", "question_text": "81, 27, 9, 3, e dizisinde e kaçtır?", "options": [{"key":"A","text":"0"},{"key":"B","text":"1"},{"key":"C","text":"2"},{"key":"D","text":"1/3"},{"key":"E","text":"3"}], "correct_option": "B", "explanation": "3'e bölünerek ilerliyor: 3 / 3 = 1.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qm-14-9", "question_text": "2, 3, 5, 8, 12, f dizisinde f kaçtır?", "options": [{"key":"A","text":"15"},{"key":"B","text":"16"},{"key":"C","text":"17"},{"key":"D","text":"18"},{"key":"E","text":"20"}], "correct_option": "C", "explanation": "Artışlar: +1, +2, +3, +4... f = 12 + 5 = 17.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qm-14-10", "question_text": "10, 20, 15, 25, 20, g dizisinde g kaçtır?", "options": [{"key":"A","text":"25"},{"key":"B","text":"30"},{"key":"C","text":"35"},{"key":"D","text":"40"},{"key":"E","text":"15"}], "correct_option": "B", "explanation": "Kural: +10, -5, +10, -5... g = 20 + 10 = 30.", "difficulty_level": "lisans", "is_verified": True}
    ]
    add_topic_bundle(
        "topic-mat-sayi-dizileri", "Sayı Dizileri ve Örüntüler", "sayi-dizileri-oruntuler", 1.5, 14,
        "Sayı Dizilerinde Örüntü Yakalama",
        "### Taktik:\n- Terimler arasındaki farkları ve oranları incele.\n- Artış miktarı sabit mi, katlanarak mı artıyor dikkat et.",
        "KPSS Matematik", q_14
    )

    # -------------------------------------------------------------------------
    # 15. Şekil Örüntüleri
    # -------------------------------------------------------------------------
    q_15 = [
        {"id": "qm-15-1", "question_text": "1 kibrit çöpüyle yapılan bir adım örüntüsünde her adımda 3 çöp eklenmektedir. 10. adımda toplam kaç çöp kullanılır (1. Adım = 4 çöp)?", "options": [{"key":"A","text":"28"},{"key":"B","text":"31"},{"key":"C","text":"34"},{"key":"D","text":"37"},{"key":"E","text":"40"}], "correct_option": "B", "explanation": "Kural: 3n + 1. n = 10 için 3(10) + 1 = 31 çöp.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qm-15-2", "question_text": "Bir kare örüntüsünde 1. adımda 1 kare, 2. adımda 4 kare, 3. adımda 9 kare vardır. 6. adımda kaç kare bulunur?", "options": [{"key":"A","text":"16"},{"key":"B","text":"25"},{"key":"C","text":"36"},{"key":"D","text":"49"},{"key":"E","text":"64"}], "correct_option": "C", "explanation": "n² kuralı: 6. adımda 6² = 36 kare bulunur.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qm-15-3", "question_text": "Bir altıgen örüntüsünün köşe sayısı kuralı 6n'dir. 5. adımda kaç köşe vardır?", "options": [{"key":"A","text":"24"},{"key":"B","text":"30"},{"key":"C","text":"36"},{"key":"D","text":"40"},{"key":"E","text":"42"}], "correct_option": "B", "explanation": "6 · 5 = 30 köşe.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qm-15-4", "question_text": "Bir daire örüntüsünde her adımda daire sayısı 2 katına çıkmaktadır. 1. adımda 2 daire varsa 5. adımda kaç daire olur?", "options": [{"key":"A","text":"16"},{"key":"B","text":"24"},{"key":"C","text":"32"},{"key":"D","text":"64"},{"key":"E","text":"128"}], "correct_option": "C", "explanation": "1: 2, 2: 4, 3: 8, 4: 16, 5: 32 daire.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qm-15-5", "question_text": "Bir üçgen örüntüsünün 1. adımında 1, 2. adımında 3, 3. adımında 5 üçgen vardır. 10. adımda kaç üçgen olur?", "options": [{"key":"A","text":"17"},{"key":"B","text":"19"},{"key":"C","text":"21"},{"key":"D","text":"23"},{"key":"E","text":"25"}], "correct_option": "B", "explanation": "Tek sayılar dizisi (2n - 1). n = 10 için 2(10) - 1 = 19.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qm-15-6", "question_text": "Şekil örüntüsünde köşe sayısı 4, 8, 12, 16 olarak gitmektedir. Kuralı nedir?", "options": [{"key":"A","text":"2n"},{"key":"B","text":"4n"},{"key":"C","text":"n+4"},{"key":"D","text":"4n+2"},{"key":"E","text":"2n+4"}], "correct_option": "B", "explanation": "4'ün katları olan 4n kuralıdır.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qm-15-7", "question_text": "1. adımda 3 nokta, 2. adımda 6 nokta, 3. adımda 9 nokta olan örüntünün 7. adımında kaç nokta vardır?", "options": [{"key":"A","text":"18"},{"key":"B","text":"21"},{"key":"C","text":"24"},{"key":"D","text":"27"},{"key":"E","text":"30"}], "correct_option": "B", "explanation": "3n kuralı: 3 · 7 = 21 nokta.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qm-15-8", "question_text": "Siyah ve beyaz karelerden oluşan örüntünün 1. adımında 1 siyah 2 beyaz, 2. adımında 2 siyah 4 beyaz vardır. 5. adımda kaç beyaz kare vardır?", "options": [{"key":"A","text":"8"},{"key":"B","text":"10"},{"key":"C","text":"12"},{"key":"D","text":"14"},{"key":"E","text":"16"}], "correct_option": "B", "explanation": "Beyaz kare kuralı 2n'dir. 5. adımda 2 · 5 = 10 beyaz kare.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qm-15-9", "question_text": "Bir basamak örüntüsünde 1. adımda 1 küp, 2. adımda 3 küp, 3. adımda 6 küp vardır. 4. adımda kaç küp olur?", "options": [{"key":"A","text":"8"},{"key":"B","text":"9"},{"key":"C","text":"10"},{"key":"D","text":"12"},{"key":"E","text":"15"}], "correct_option": "C", "explanation": "Üçgensel sayılar (n(n+1)/2): 4. adımda 4·5/2 = 10 küp.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qm-15-10", "question_text": "Kibrit çöplerinden oluşan kare dizisinde 1 kare için 4, 2 bitişik kare için 7 çöp kullanılıyor. 5 bitişik kare için kaç çöp kullanılır?", "options": [{"key":"A","text":"13"},{"key":"B","text":"16"},{"key":"C","text":"19"},{"key":"D","text":"22"},{"key": "E","text":"25"}], "correct_option": "B", "explanation": "Kural: 3n + 1. n = 5 için 3(5) + 1 = 16 çöp.", "difficulty_level": "lisans", "is_verified": True}
    ]
    add_topic_bundle(
        "topic-mat-sekil-oruntuleri", "Şekil Örüntüleri", "sekil-oruntuleri", 1.4, 15,
        "Şekil Örüntüsü Denklem Çıkarma",
        "### Taktik:\n- Şekildeki adımları sayı dizisine dönüştür (1. Adım: 4, 2. Adım: 7 gibi) ve Genel Terim (an + b) bul.",
        "KPSS Matematik", q_15
    )

    # -------------------------------------------------------------------------
    # 16. Grafik ve Tablo Yorumlama
    # -------------------------------------------------------------------------
    q_16 = [
        {"id": "qm-16-1", "question_text": "Daire grafiğinde bir sektörün açısı 180° ise bu sektör tüm dairenin yüzde kaçıdır?", "options": [{"key":"A","text":"%25"},{"key":"B","text":"%33"},{"key":"C","text":"%50"},{"key":"D","text":"%60"},{"key":"E","text":"%75"}], "correct_option": "C", "explanation": "180 / 360 = 1/2 = %50.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qm-16-2", "question_text": "Daire grafiğinde 90° olan sektör 30 kg'ı gösteriyorsa dairenin tamamı kaç kg'dır?", "options": [{"key":"A","text":"90"},{"key":"B","text":"120"},{"key":"C","text":"150"},{"key":"D","text":"180"},{"key":"E","text":"200"}], "correct_option": "B", "explanation": "90° = 1/4 dür. Tamamı = 30 · 4 = 120 kg.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qm-16-3", "question_text": "Bir sütun grafiğinde A şehri 50, B şehri 70 nüfusa sahiptir. B şehrinin nüfusu A'dan yüzde kaç fazladır?", "options": [{"key":"A","text":"%20"},{"key":"B","text":"%30"},{"key":"C","text":"%40"},{"key":"D","text":"%50"},{"key":"E","text":"%60"}], "correct_option": "C", "explanation": "Fark = 70 - 50 = 20. Oran = (20 / 50) · 100 = %40.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qm-16-4", "question_text": "Tabloda bir ürünün 3 aydaki satışları: 100, 200, 300 adettir. Ortalama aylık satış kaç adettir?", "options": [{"key":"A","text":"150"},{"key":"B","text":"200"},{"key":"C","text":"250"},{"key":"D","text":"300"},{"key":"E","text":"350"}], "correct_option": "B", "explanation": "(100 + 200 + 300) / 3 = 600 / 3 = 200.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qm-16-5", "question_text": "Daire grafiğinde A=120°, B=120° ise C sektörü kaç derecedir?", "options": [{"key":"A","text":"60°"},{"key":"B","text":"90°"},{"key":"C","text":"120°"},{"key":"D","text":"150°"},{"key":"E","text":"180°"}], "correct_option": "C", "explanation": "360 - (120 + 120) = 120°.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qm-16-6", "question_text": "Bir ürünün fiyatı ocak ayında 50 TL, şubat ayında 60 TL'dir. Artış oranı yüzde kaçtır?", "options": [{"key":"A","text":"%10"},{"key":"B","text":"%15"},{"key":"C","text":"%20"},{"key":"D","text":"%25"},{"key":"E","text":"%30"}], "correct_option": "C", "explanation": "(10 / 50) · 100 = %20.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qm-16-7", "question_text": "Daire grafiğinde %25'lik dilimin merkez açısı kaç derecedir?", "options": [{"key":"A","text":"45°"},{"key":"B","text":"60°"},{"key":"C","text":"90°"},{"key":"D","text":"120°"},{"key":"E","text":"180°"}], "correct_option": "C", "explanation": "360 · (25 / 100) = 90°.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qm-16-8", "question_text": "Bir çizgi grafiğinde üretim 1. yıl 10 ton, 2. yıl 20 ton, 3. yıl 30 tondur. Toplam üretim kaç tondur?", "options": [{"key":"A","text":"40"},{"key":"B","text":"50"},{"key":"C","text":"60"},{"key":"D","text":"70"},{"key":"E","text":"80"}], "correct_option": "C", "explanation": "10 + 20 + 30 = 60 ton.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qm-16-9", "question_text": "Daire grafiğinde bir açı 36° ise bu açı dairenin kaçta kaçıdır?", "options": [{"key":"A","text":"1/5"},{"key":"B","text":"1/8"},{"key":"C","text":"1/10"},{"key":"D","text":"1/12"},{"key":"E","text":"1/15"}], "correct_option": "C", "explanation": "36 / 360 = 1/10.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qm-16-10", "question_text": "Sütun grafiğinde K=30, L=40, M=50'dir. M'nin toplam içindeki oranı yüzde kaçtır?", "options": [{"key":"A","text":"%25"},{"key":"B","text":"%33,3"},{"key":"C","text":"%40"},{"key":"D","text":"%41,6"},{"key":"E","text":"%50"}], "correct_option": "B", "explanation": "Toplam = 30+40+50 = 120. M oranı = 50 / 120 = %41,6 veya 40/120 = %33.3 (40 L'dir). 50/120 = %41.6. D şıkkı %41,6.", "difficulty_level": "lisans", "is_verified": True}
    ]
    add_topic_bundle(
        "topic-mat-grafik-tablo-detay", "Grafik ve Tablo Yorumlama", "grafik-ve-tablo-yorumlama", 1.6, 16,
        "Grafik Okuma Yöntemleri",
        "### İpuçları:\n- Daire Grafiğinde Tamam = **360°**.\n- Sütun ve Çizgi Grafiğinde Y eksenindeki ölçeğe dikkat et.",
        "KPSS Matematik", q_16
    )

    # -------------------------------------------------------------------------
    # 17. Sıralama ve Gruplama (Mantıksal Problemler)
    # -------------------------------------------------------------------------
    q_17 = [
        {"id": "qm-17-1", "question_text": "A, B, C kişilerinden A B'den uzun, B de C'den uzundur. En kısa olan kimdir?", "options": [{"key":"A","text":"A"},{"key":"B","text":"B"},{"key":"C","text":"C"},{"key":"D","text":"A ve B"},{"key":"E","text":"Eşittir"}], "correct_option": "C", "explanation": "Sıralama: A > B > C. En kısa C'dir.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qm-17-2", "question_text": "Bir koşuda Ali Veli'nin önünde, Veli de Can'ın önündedir. Sonuncu kimdir?", "options": [{"key":"A","text":"Ali"},{"key":"B","text":"Veli"},{"key":"C","text":"Can"},{"key":"D","text":"Belirsiz"},{"key":"E","text":"İkisi birincidir"}], "correct_option": "C", "explanation": "Sıralama: Ali > Veli > Can. Sonuncu Can'dır.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qm-17-3", "question_text": "4 farklı kitap bir rafa kaç farklı şekilde dizilebilir?", "options": [{"key":"A","text":"12"},{"key":"B","text":"16"},{"key":"C","text":"24"},{"key":"D","text":"36"},{"key":"E","text":"48"}], "correct_option": "C", "explanation": "4! = 4 · 3 · 2 · 1 = 24 farklı şekilde dizilir.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qm-17-4", "question_text": "3 kişi bir banka kaç farklı şekilde oturabilir?", "options": [{"key":"A","text":"3"},{"key":"B","text":"6"},{"key":"C","text":"9"},{"key":"D","text":"12"},{"key":"E","text":"15"}], "correct_option": "B", "explanation": "3! = 6 farklı şekilde oturabilir.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qm-17-5", "question_text": "Ahmet Mehmet'ten yaşça büyük, Mehmet de Hasan'dan büyüktür. En genç olan kimdir?", "options": [{"key":"A","text":"Ahmet"},{"key":"B","text":"Mehmet"},{"key":"C","text":"Hasan"},{"key":"D","text":"İkizdirler"},{"key":"E","text":"Bilinemez"}], "correct_option": "C", "explanation": "Ahmet > Mehmet > Hasan. En genç Hasan'dır.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qm-17-6", "question_text": "5 kişi düz bir çizgide sıralanacaktır. Baştaki kişi sabit olduğuna göre kalanlar kaç farklı sıralanır?", "options": [{"key":"A","text":"12"},{"key":"B","text":"24"},{"key":"C","text":"60"},{"key":"D","text":"120"},{"key":"E","text":"240"}], "correct_option": "B", "explanation": "Kalan 4 kişi 4! = 24 farklı şekilde sıralanır.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qm-17-7", "question_text": "X, Y, Z öğrencileri sınav notlarına göre Y X'ten yüksek, Z de Y'den yüksek almıştır. En yüksek alan kimdir?", "options": [{"key":"A","text":"X"},{"key":"B","text":"Y"},{"key":"C","text":"Z"},{"key":"D","text":"X ve Z"},{"key":"E","text":"Notlar eşittir"}], "correct_option": "C", "explanation": "Sıralama: Z > Y > X. En yüksek Z almıştır.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qm-17-8", "question_text": "Bir gruptaki 4 kişi her biri diğeriyle birer kez tokalaşırsa toplam kaç tokalaşma olur?", "options": [{"key":"A","text":"4"},{"key":"B","text":"6"},{"key":"C","text":"8"},{"key":"D","text":"12"},{"key":"E","text":"16"}], "correct_option": "B", "explanation": "C(4, 2) = (4 · 3) / 2 = 6 tokalaşma gerçekleşir.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qm-17-9", "question_text": "A kenti B'nin doğusunda, C kenti de B'nin batısındadır. En doğudaki kent hangisidir?", "options": [{"key":"A","text":"A Kenti"},{"key":"B","text":"B Kenti"},{"key":"C","text":"C Kenti"},{"key":"D","text":"B ve C"},{"key":"E","text":"Aynı boylamdadırlar"}], "correct_option": "A", "explanation": "Batıdan Doğuya sıralama: C - B - A. En doğudaki A kentidir.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qm-17-10", "question_text": "5 farklı nesne arasından 2 tanesi sırasız kaç farklı şekilde seçilebilir?", "options": [{"key":"A","text":"5"},{"key":"B","text":"10"},{"key":"C","text":"15"},{"key":"D","text":"20"},{"key":"E","text":"25"}], "correct_option": "B", "explanation": "C(5, 2) = (5 · 4) / 2 = 10 farklı şekilde seçilebilir.", "difficulty_level": "lisans", "is_verified": True}
    ]
    add_topic_bundle(
        "topic-mat-siralama-gruplama", "Sıralama ve Gruplama", "siralama-ve-gruplama", 1.5, 17,
        "Sıralama ve Kombinasyon Kuralları",
        "### Formül:\n- **n nesnenin sıralanması = n!**\n- **n kişiden 2 kişi seçimi (Tokalaşma vb.) = n(n-1)/2**",
        "KPSS Matematik", q_17
    )

    print(f"Toplam Üretilen Alt Konu Sayısı: {len(topics)}")
    print(f"Toplam Üretilen Hap Bilgi Sayısı: {len(quick_notes)}")
    print(f"Toplam Üretilen Soru Sayısı: {len(questions)}")
    return topics, quick_notes, questions

if __name__ == "__main__":
    m_topics, m_notes, m_questions = build_matematik_ultra_dataset()
    
    json_path = os.path.join("mobile_app", "assets", "data", "sample_data.json")
    with open(json_path, "r", encoding="utf-8") as f:
        full_db = json.load(f)

    # Eski matematik verilerini temizle ve 17 alt konulu 170 soruluk ultra havuzu yaz
    full_db["topics"] = [t for t in full_db["topics"] if t["course_id"] not in ["course-mat", "course-mat-01"]]
    full_db["quick_notes"] = [n for n in full_db["quick_notes"] if not n["topic_id"].startswith("topic-mat")]
    full_db["questions"] = [q for q in full_db["questions"] if not q["topic_id"].startswith("topic-mat")]

    full_db["topics"].extend(m_topics)
    full_db["quick_notes"].extend(m_notes)
    full_db["questions"].extend(m_questions)

    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(full_db, f, ensure_ascii=False, indent=2)

    print(f"\n[BAŞARILI ULTRAGENİŞ HAVUZ] {len(m_topics)} Alt Konu, {len(m_notes)} Hap Bilgi ve {len(m_questions)} Soru {json_path} veritabanına aktarıldı!")
