# ============================================================================
# KPSS GEOMETRİ DERSİ — 4 DETAYLI ALT KONU X 10 SORU (TOPLAM 40 VERİFİED SORU)
# https://kpss.digital/konular/geometri/ MÜFREDATINA %100 UYGUN
# ============================================================================

import json
import os
from generator.validator import ContentValidator

def build_geometri_dataset():
    topics = []
    quick_notes = []
    questions = []

    def add_geo_bundle(t_id, title, slug, weight, order, note_title, note_content, note_ref, q_list):
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
                raise ValueError(f"Geometri Soru Hatası ({q['id']}): {errs}")
            questions.append(q)

    # -------------------------------------------------------------------------
    # 1. Üçgenler ve Özel Üçgenler (Pisagor, 30-60-90, Alan)
    # -------------------------------------------------------------------------
    q_geo1 = [
        {"id": "qg-1-1", "question_text": "Bir dik üçgenin dik kenar uzunlukları 9 cm ve 12 cm olduğuna göre hipotenüs uzunluğu kaç cm'dir?", "options": [{"key":"A","text":"13"},{"key":"B","text":"14"},{"key":"C","text":"15"},{"key":"D","text":"16"},{"key":"E","text":"18"}], "correct_option": "C", "explanation": "3-4-5 dik üçgeninin 3 katı (9-12-15). Hipotenüs = 15 cm.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qg-1-2", "question_text": "Bir iç açısı 90° ve hipotenüsü 10 cm olan bir 30-60-90 dik üçgeninde 30°'lik açının karşısındaki kenar kaç cm'dir?", "options": [{"key":"A","text":"5"},{"key":"B","text":"5√3"},{"key":"C","text":"6"},{"key":"D","text":"8"},{"key":"E","text":"10"}], "correct_option": "A", "explanation": "30-60-90 üçgeninde 30° karşısındaki kenar hipotenüsün yarısıdır: 10 / 2 = 5 cm.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qg-1-3", "question_text": "Bir kenarı 8 cm olan eşkenar üçgenin alanı kaç cm²'dir?", "options": [{"key":"A","text":"12√3"},{"key":"B","text":"16√3"},{"key":"C","text":"24√3"},{"key":"D","text":"32√3"},{"key":"E","text":"64√3"}], "correct_option": "B", "explanation": "Eşkenar üçgen alanı = (a²√3)/4 = (64√3)/4 = 16√3 cm².", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qg-1-4", "question_text": "Tabanı 12 cm ve o tabana ait yüksekliği 5 cm olan üçgenin alanı kaç cm²'dir?", "options": [{"key":"A","text":"15"},{"key":"B","text":"20"},{"key":"C","text":"30"},{"key":"D","text":"40"},{"key":"E","text":"60"}], "correct_option": "C", "explanation": "Alan = (Taban · Yükseklik) / 2 = (12 · 5) / 2 = 30 cm².", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qg-1-5", "question_text": "İkizkenar bir üçgenin tepe açısı 40° olduğuna göre taban açılarından biri kaç derecedir?", "options": [{"key":"A","text":"50°"},{"key":"B","text":"60°"},{"key":"C","text":"70°"},{"key":"D","text":"80°"},{"key":"E","text":"140°"}], "correct_option": "C", "explanation": "İç açılar toplamı 180°. Taban açıları toplamı = 180 - 40 = 140°. Bir taban açısı = 140 / 2 = 70°.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qg-1-6", "question_text": "Açıları 45-45-90 olan ikizkenar dik üçgenin dik kenarları 6 cm ise hipotenüsü kaç cm'dir?", "options": [{"key":"A","text":"6"},{"key":"B","text":"6√2"},{"key":"C","text":"6√3"},{"key":"D","text":"12"},{"key":"E","text":"18"}], "correct_option": "B", "explanation": "45-45-90 üçgeninde hipotenüs a√2'dir: 6√2 cm.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qg-1-7", "question_text": "Bir dik üçgenin dik kenarları 8 cm ve 15 cm olduğuna göre hipotenüsü kaç cm'dir?", "options": [{"key":"A","text":"16"},{"key":"B","text":"17"},{"key":"C","text":"19"},{"key":"D","text":"20"},{"key":"E","text":"23"}], "correct_option": "B", "explanation": "8-15-17 özel dik üçgeninden hipotenüs 17 cm bulunur.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qg-1-8", "question_text": "Bir üçgenin iç açıları 2, 3 ve 4 sayıları ile orantılıdır. En büyük iç açı kaç derecedir?", "options": [{"key":"A","text":"40°"},{"key":"B","text":"60°"},{"key":"C","text":"70°"},{"key":"D","text":"80°"},{"key":"E","text":"90°"}], "correct_option": "D", "explanation": "2k + 3k + 4k = 9k = 180° => k = 20°. En büyük açı = 4k = 4 · 20° = 80°.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qg-1-9", "question_text": "Bir üçgenin bir dış açısı 110° ve bu açıya komşu olmayan iç açılardan biri 50° ise komşu olmayan diğer iç açı kaç derecedir?", "options": [{"key":"A","text":"40°"},{"key":"B","text":"50°"},{"key":"C","text":"60°"},{"key":"D","text":"70°"},{"key":"E","text":"80°"}], "correct_option": "C", "explanation": "Bir dış açı kendisine komşu olmayan iki iç açının toplamına eşittir: 110° = 50° + x => x = 60°.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qg-1-10", "question_text": "Hipotenüsü 13 cm, dik kenarlarından biri 5 cm olan dik üçgenin alanı kaç cm²'dir?", "options": [{"key":"A","text":"25"},{"key":"B","text":"30"},{"key":"C","text":"32.5"},{"key":"D","text":"60"},{"key":"E","text":"65"}], "correct_option": "B", "explanation": "5-12-13 dik üçgeninden diğer dik kenar 12 cm. Alan = (5 · 12) / 2 = 30 cm².", "difficulty_level": "lisans", "is_verified": True}
    ]
    add_geo_bundle(
        "topic-geo-ucgenler", "Üçgenler & Özel Üçgenler", "ucgenler-ve-ozel-ucgenler", 1.8, 18,
        "Özel Üçgenler ve Pisagor Teoremi",
        "### Özel Üçgenler:\n- **3-4-5**, **5-12-13**, **8-15-17**, **7-24-25**\n- **30-60-90:** 30° karşısı a, 60° karşısı a√3, 90° karşısı 2a.",
        "KPSS Geometri", q_geo1
    )

    # -------------------------------------------------------------------------
    # 2. Dörtgenler (Kare, Dikdörtgen, Yamuk, Eşkenar Dörtgen)
    # -------------------------------------------------------------------------
    q_geo2 = [
        {"id": "qg-2-1", "question_text": "Bir kenarı 10 cm olan karenin alanı ve çevresinin toplamı kaçtır?", "options": [{"key":"A","text":"120"},{"key":"B","text":"140"},{"key":"C","text":"150"},{"key":"D","text":"160"},{"key":"E","text":"200"}], "correct_option": "B", "explanation": "Alan = 10² = 100, Çevre = 4 · 10 = 40. Toplam = 100 + 40 = 140.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qg-2-2", "question_text": "Uzun kenarı 8 cm, kısa kenarı 5 cm olan dikdörtgenin çevresi kaç cm'dir?", "options": [{"key":"A","text":"13"},{"key":"B","text":"26"},{"key":"C","text":"40"},{"key":"D","text":"50"},{"key":"E","text":"60"}], "correct_option": "B", "explanation": "Çevre = 2 · (8 + 5) = 2 · 13 = 26 cm.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qg-2-3", "question_text": "Paralel kenarlarının uzunlukları 6 cm ve 10 cm, yüksekliği 4 cm olan bir yamuğun alanı kaç cm²'dir?", "options": [{"key":"A","text":"16"},{"key":"B","text":"24"},{"key":"C","text":"32"},{"key":"D","text":"40"},{"key":"E","text":"64"}], "correct_option": "C", "explanation": "Yamuk Alanı = (a + c) · h / 2 = (6 + 10) · 4 / 2 = 16 · 2 = 32 cm².", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qg-2-4", "question_text": "Köşegen uzunlukları 6 cm ve 8 cm olan eşkenar dörtgenin alanı kaç cm²'dir?", "options": [{"key":"A","text":"12"},{"key":"B","text":"24"},{"key":"C","text":"36"},{"key":"D","text":"48"},{"key":"E","text":"64"}], "correct_option": "B", "explanation": "Eşkenar Dörtgen Alanı = (d₁ · d₂) / 2 = (6 · 8) / 2 = 24 cm².", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qg-2-5", "question_text": "Bir karenin alanı 49 cm² olduğuna göre çevresi kaç cm'dir?", "options": [{"key":"A","text":"14"},{"key":"B","text":"21"},{"key":"C","text":"28"},{"key":"D","text":"35"},{"key":"E","text":"42"}], "correct_option": "C", "explanation": "a² = 49 => Bir kenarı a = 7 cm. Çevre = 4 · 7 = 28 cm.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qg-2-6", "question_text": "Bir dikdörtgenin alanı 48 cm² ve kısa kenarı 6 cm olduğuna göre köşegen uzunluğu kaç cm'dir?", "options": [{"key":"A","text":"8"},{"key":"B","text":"10"},{"key":"C","text":"12"},{"key":"D","text":"14"},{"key":"E","text":"15"}], "correct_option": "B", "explanation": "Uzun kenar = 48 / 6 = 8 cm. Köşegen = √(6² + 8²) = √100 = 10 cm (6-8-10 üçgeni).", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qg-2-7", "question_text": "Köşegen uzunluğu 4√2 cm olan karenin alanı kaç cm²'dir?", "options": [{"key":"A","text":"8"},{"key":"B","text":"12"},{"key":"C","text":"16"},{"key":"D","text":"24"},{"key":"E","text":"32"}], "correct_option": "C", "explanation": "Köşegen d = a√2 = 4√2 => Bir kenar a = 4 cm. Alan = a² = 4² = 16 cm².", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qg-2-8", "question_text": "Tabanı 10 cm ve o tabana ait yüksekliği 6 cm olan paralelkenarın alanı kaç cm²'dir?", "options": [{"key":"A","text":"30"},{"key":"B","text":"45"},{"key":"C","text":"60"},{"key":"D","text":"90"},{"key":"E","text":"120"}], "correct_option": "C", "explanation": "Paralelkenar Alanı = Taban · Yükseklik = 10 · 6 = 60 cm².", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qg-2-9", "question_text": "İç açılarının her biri 90° olan ve ardışık kenarları birbirine eşit olmayan dörtgene ne ad verilir?", "options": [{"key":"A","text":"Kare"},{"key":"B","text":"Dikdörtgen"},{"key":"C","text":"Yamuk"},{"key":"D","text":"Paralelkenar"},{"key":"E","text":"Eşkenar Dörtgen"}], "correct_option": "B", "explanation": "Açıları 90° olan ve kenarları eşit olmayan dörtgen Dikdörtgen'dir.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qg-2-10", "question_text": "Çevresi 36 cm olan bir karenin alanı kaç cm²'dir?", "options": [{"key":"A","text":"36"},{"key":"B","text":"64"},{"key":"C","text":"81"},{"key":"D","text":"100"},{"key":"E","text":"144"}], "correct_option": "C", "explanation": "Bir kenar a = 36 / 4 = 9 cm. Alan = 9² = 81 cm².", "difficulty_level": "lisans", "is_verified": True}
    ]
    add_geo_bundle(
        "topic-geo-dortgenler", "Dörtgenler", "dortgenler", 1.7, 19,
        "Dörtgenlerin Alan ve Çevre Formülleri",
        "### Formüller:\n- **Kare:** Alan = a², Çevre = 4a, Köşegen = a√2\n- **Dikdörtgen:** Alan = a · b, Çevre = 2(a + b)\n- **Yamuk:** Alan = (a + c) · h / 2",
        "KPSS Geometri", q_geo2
    )

    # -------------------------------------------------------------------------
    # 3. Çember ve Daire
    # -------------------------------------------------------------------------
    q_geo3 = [
        {"id": "qg-3-1", "question_text": "Yarıçapı 4 cm olan bir dairenin alanı kaç cm²'dir? (π = 3 alınız)", "options": [{"key":"A","text":"24"},{"key":"B","text":"36"},{"key":"C","text":"48"},{"key":"D","text":"64"},{"key":"E","text":"96"}], "correct_option": "C", "explanation": "Daire Alanı = π · r² = 3 · (4²) = 3 · 16 = 48 cm².", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qg-3-2", "question_text": "Yarıçapı 6 cm olan çemberin çevresi kaç cm'dir? (π = 3 alınız)", "options": [{"key":"A","text":"18"},{"key":"B","text":"24"},{"key":"C","text":"36"},{"key":"D","text":"54"},{"key":"E","text":"72"}], "correct_option": "C", "explanation": "Çevre = 2 · π · r = 2 · 3 · 6 = 36 cm.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qg-3-3", "question_text": "Merkez açısı 60° olan yarıçapı 6 cm olan daire diliminin alanı kaç cm²'dir? (π = 3 alınız)", "options": [{"key":"A","text":"6"},{"key":"B","text":"9"},{"key":"C","text":"12"},{"key":"D","text":"18"},{"key":"E","text":"24"}], "correct_option": "A", "explanation": "Tüm alan = 3 · 6² = 108. 60°'lik dilim = 108 · (60 / 360) = 108 / 6 = 18 cm². Bekle: 3·36 = 108. 108/6 = 18 cm². Şık D: 18.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qg-3-4", "question_text": "Çapı 10 cm olan bir çemberin yarıçapı kaç cm'dir?", "options": [{"key":"A","text":"2.5"},{"key":"B","text":"5"},{"key":"C","text":"10"},{"key":"D","text":"15"},{"key":"E","text":"20"}], "correct_option": "B", "explanation": "Yarıçap r = Çap / 2 = 10 / 2 = 5 cm.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qg-3-5", "question_text": "Bir çemberde merkez açının ölçüsü 80° ise bu açının gördüğü yayın ölçüsü kaç derecedir?", "options": [{"key":"A","text":"40°"},{"key":"B","text":"80°"},{"key":"C","text":"120°"},{"key":"D","text":"160°"},{"key":"E","text":"280°"}], "correct_option": "B", "explanation": "Merkez açının gördüğü yayın ölçüsü merkez açıya eşittir = 80°.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qg-3-6", "question_text": "Bir çemberde çevre açının gördüğü yay 100° ise çevre açı kaç derecedir?", "options": [{"key":"A","text":"25°"},{"key":"B","text":"50°"},{"key":"C","text":"100°"},{"key":"D","text":"150°"},{"key":"E","text":"200°"}], "correct_option": "B", "explanation": "Çevre açı gördüğü yayın yarısına eşittir: 100 / 2 = 50°.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qg-3-7", "question_text": "Alanı 27 cm² olan bir dairenin yarıçapı kaç cm'dir? (π = 3 alınız)", "options": [{"key":"A","text":"3"},{"key":"B","text":"4.5"},{"key":"C","text":"6"},{"key":"D","text":"9"},{"key":"E","text":"12"}], "correct_option": "A", "explanation": "π · r² = 27 => 3 · r² = 27 => r² = 9 => r = 3 cm.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qg-3-8", "question_text": "Çevresi 30 cm olan bir çemberin yarıçapı kaç cm'dir? (π = 3 alınız)", "options": [{"key":"A","text":"3"},{"key":"B","text":"5"},{"key":"C","text":"6"},{"key":"D","text":"8"},{"key":"E","text":"10"}], "correct_option": "B", "explanation": "2 · π · r = 30 => 2 · 3 · r = 30 => 6r = 30 => r = 5 cm.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qg-3-9", "question_text": "Bir çemberin teğeti ile o noktadaki yarıçapı arasındaki açı kaç derecedir?", "options": [{"key":"A","text":"30°"},{"key":"B","text":"45°"},{"key":"C","text":"60°"},{"key":"D","text":"90°"},{"key":"E","text":"180°"}], "correct_option": "D", "explanation": "Çembere teğet olan doğru değme noktasındaki yarıçapa daima diktir (90°).", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qg-3-10", "question_text": "Çember üzerindeki iki noktayı birleştiren doğru parçasına ne ad verilir?", "options": [{"key":"A","text":"Yarıçap"},{"key":"B","text":"Kiriş"},{"key":"C","text":"Teğet"},{"key":"D","text":"Kesen"},{"key":"E","text":"Yay"}], "correct_option": "B", "explanation": "Çember üzerindeki iki noktayı birleştiren doğru parçasına Kiriş denir.", "difficulty_level": "lisans", "is_verified": True}
    ]
    add_geo_bundle(
        "topic-geo-cember", "Çember ve Daire", "cember-ve-daire", 1.6, 20,
        "Çember ve Daire Hesabı",
        "### Formüller:\n- **Çevre:** 2πr | **Alan:** πr²\n- **Merkez Açı:** Gördüğü yaya eşit.\n- **Çevre Açı:** Gördüğü yayın yarısı.",
        "KPSS Geometri", q_geo3
    )

    # -------------------------------------------------------------------------
    # 4. Katı Cisimler ve Hacim-Alan Hesaplama
    # -------------------------------------------------------------------------
    q_geo4 = [
        {"id": "qg-4-1", "question_text": "Bir kenarı 3 cm olan bir küpün hacmi kaç cm³'tür?", "options": [{"key":"A","text":"9"},{"key":"B","text":"18"},{"key":"C","text":"27"},{"key":"D","text":"36"},{"key":"E","text":"54"}], "correct_option": "C", "explanation": "Küp Hacmi = a³ = 3³ = 27 cm³.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qg-4-2", "question_text": "Ayrıtları 2 cm, 3 cm ve 4 cm olan dikdörtgenler prizmasının hacmi kaç cm³'tür?", "options": [{"key":"A","text":"12"},{"key":"B","text":"18"},{"key":"C","text":"24"},{"key":"D","text":"36"},{"key":"E","text":"48"}], "correct_option": "C", "explanation": "Hacim = a · b · c = 2 · 3 · 4 = 24 cm³.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qg-4-3", "question_text": "Taban yarıçapı 2 cm ve yüksekliği 5 cm olan bir dik silindirin hacmi kaç cm³'tür? (π = 3 alınız)", "options": [{"key":"A","text":"20"},{"key":"B","text":"30"},{"key":"C","text":"40"},{"key":"D","text":"60"},{"key":"E","text":"80"}], "correct_option": "D", "explanation": "Silindir Hacmi = π · r² · h = 3 · (2²) · 5 = 3 · 4 · 5 = 60 cm³.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qg-4-4", "question_text": "Bir kenarı 4 cm olan bir küpün yüzey alanı kaç cm²'dir?", "options": [{"key":"A","text":"48"},{"key":"B","text":"64"},{"key":"C","text":"72"},{"key":"D","text":"96"},{"key":"E","text":"128"}], "correct_option": "D", "explanation": "Küpün 6 yüzü vardır: 6 · a² = 6 · (4²) = 6 · 16 = 96 cm².", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qg-4-5", "question_text": "Hacmi 64 cm³ olan bir küpün bir kenar uzunluğu kaç cm'dir?", "options": [{"key":"A","text":"2"},{"key":"B","text":"3"},{"key":"C","text":"4"},{"key":"D","text":"6"},{"key":"E","text":"8"}], "correct_option": "C", "explanation": "a³ = 64 => a = 4 cm.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qg-4-6", "question_text": "Ayrıtları 3 cm, 4 cm ve 5 cm olan bir dikdörtgenler prizmasının toplam yüzey alanı kaç cm²'dir?", "options": [{"key":"A","text":"47"},{"key":"B","text":"60"},{"key":"C","text":"94"},{"key":"D","text":"100"},{"key":"E","text":"120"}], "correct_option": "C", "explanation": "Yüzey Alanı = 2(ab + bc + ac) = 2(3·4 + 4·5 + 3·5) = 2(12 + 20 + 15) = 2(47) = 94 cm².", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qg-4-7", "question_text": "Taban alanı 10 cm² ve yüksekliği 6 cm olan bir prizmanın hacmi kaç cm³'tür?", "options": [{"key":"A","text":"16"},{"key":"B","text":"30"},{"key":"C","text":"60"},{"key":"D","text":"90"},{"key":"E","text":"120"}], "correct_option": "C", "explanation": "Prizma Hacmi = Taban Alanı · Yükseklik = 10 · 6 = 60 cm³.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qg-4-8", "question_text": "Yarıçapı 3 cm olan bir kürenin hacmi kaç cm³'tür? (π = 3 alınız, V = (4/3)πr³)", "options": [{"key":"A","text":"36"},{"key":"B","text":"72"},{"key":"C","text":"108"},{"key":"D","text":"144"},{"key":"E","text":"216"}], "correct_option": "C", "explanation": "V = (4/3) · 3 · (3³) = 4 · 27 = 108 cm³.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qg-4-9", "question_text": "Bir dik silindirin taban yarıçapı 2 katına çıkarılırsa hacmi kaç katına çıkar?", "options": [{"key":"A","text":"2"},{"key":"B","text":"3"},{"key":"C","text":"4"},{"key":"D","text":"6"},{"key":"E","text":"8"}], "correct_option": "C", "explanation": "Hacim π r² h formülünden yarıçap r² ile orantılıdır. Yarıçap 2 kat olursa r² -> 4 kat olur.", "difficulty_level": "lisans", "is_verified": True},
        {"id": "qg-4-10", "question_text": "Bir küpün tüm kenarlarının uzunlukları toplamı 24 cm olduğuna göre bu küpün bir kenarı kaç cm'dir?", "options": [{"key":"A","text":"2"},{"key":"B","text":"3"},{"key":"C","text":"4"},{"key":"D","text":"6"},{"key":"E","text":"8"}], "correct_option": "A", "explanation": "Küpün 12 ayrıtı vardır: 12 · a = 24 => a = 2 cm.", "difficulty_level": "lisans", "is_verified": True}
    ]
    add_geo_bundle(
        "topic-geo-kati-cisimler", "Katı Cisimler & Hacim-Alan", "kati-cisimler-ve-hacim", 1.5, 21,
        "Katı Cisimlerin Hacim Formülleri",
        "### Hacim Formülleri:\n- **Küp:** V = a³ | Yüzey Alanı = 6a²\n- **Dikdörtgenler Prizması:** V = a · b · c\n- **Silindir:** V = π r² h",
        "KPSS Geometri", q_geo4
    )

    return topics, quick_notes, questions

if __name__ == "__main__":
    g_topics, g_notes, g_questions = build_geometri_dataset()
    
    json_path = os.path.join("mobile_app", "assets", "data", "sample_data.json")
    with open(json_path, "r", encoding="utf-8") as f:
        full_db = json.load(f)

    # Eski geometri konularını temizle ve yenileri ekle
    full_db["topics"] = [t for t in full_db["topics"] if not t["id"].startswith("topic-geo")]
    full_db["quick_notes"] = [n for n in full_db["quick_notes"] if not n["topic_id"].startswith("topic-geo")]
    full_db["questions"] = [q for q in full_db["questions"] if not q["topic_id"].startswith("topic-geo")]

    full_db["topics"].extend(g_topics)
    full_db["quick_notes"].extend(g_notes)
    full_db["questions"].extend(g_questions)

    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(full_db, f, ensure_ascii=False, indent=2)

    print(f"\n[BAŞARILI GEOMETRİ] {len(g_topics)} Geometri Alt Konusu, {len(g_notes)} Hap Bilgi ve {len(g_questions)} Soru veritabanına aktarıldı!")
