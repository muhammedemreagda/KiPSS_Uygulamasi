import json
import os

def fix_and_normalize_database():
    json_path = os.path.join("mobile_app", "assets", "data", "sample_data.json")
    with open(json_path, "r", encoding="utf-8") as f:
        db = json.load(f)

    # 1. Clean & Standardize Courses (6 Canonical Courses)
    canonical_courses = [
        {
            "id": "course-turkce",
            "category_id": "cat-gy-01",
            "code": "TURKCE",
            "title": "Türkçe",
            "icon_name": "menu_book",
            "sort_order": 1
        },
        {
            "id": "course-matematik",
            "category_id": "cat-gy-01",
            "code": "MATEMATIK",
            "title": "Matematik & Geometri",
            "icon_name": "calculate",
            "sort_order": 2
        },
        {
            "id": "course-tarih",
            "category_id": "cat-gk-01",
            "code": "TARIH",
            "title": "Tarih",
            "icon_name": "history_edu",
            "sort_order": 3
        },
        {
            "id": "course-cografya",
            "category_id": "cat-gk-01",
            "code": "COGRAFYA",
            "title": "Coğrafya",
            "icon_name": "public",
            "sort_order": 4
        },
        {
            "id": "course-vatandaslik",
            "category_id": "cat-gk-01",
            "code": "VATANDASLIK",
            "title": "Vatandaşlık & Anayasa",
            "icon_name": "gavel",
            "sort_order": 5
        },
        {
            "id": "course-guncel",
            "category_id": "cat-gk-01",
            "code": "GUNCEL",
            "title": "Güncel Bilgiler & Genel Kültür",
            "icon_name": "newspaper",
            "sort_order": 6
        }
    ]

    db["courses"] = canonical_courses

    # Course ID Mapping table
    id_map = {
        "course-mat": "course-matematik",
        "course-cog": "course-cografya",
        "course-vat": "course-vatandaslik",
        "course-gun": "course-guncel",
    }

    # 2. Normalize Topics course_id
    for topic in db["topics"]:
        cid = topic.get("course_id", "")
        if cid in id_map:
            topic["course_id"] = id_map[cid]

    # Verify counts per course
    print("=== DERS BAZLI ALT KONU VE SORU SAYILARI ===")
    for course in canonical_courses:
        cid = course["id"]
        c_topics = [t for t in db["topics"] if t["course_id"] == cid]
        topic_ids = set(t["id"] for t in c_topics)
        c_questions = [q for q in db["questions"] if q["topic_id"] in topic_ids]
        c_notes = [n for n in db["quick_notes"] if n["topic_id"] in topic_ids]
        print(f"[{course['title']}] ({cid}): {len(c_topics)} Alt Konu | {len(c_questions)} Soru | {len(c_notes)} Hap Bilgi")

    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(db, f, ensure_ascii=False, indent=2)

    print("\n[VERİTABANI TEMİZLENDİ] sample_data.json başarıyla güncellendi!")

if __name__ == "__main__":
    fix_and_normalize_database()
