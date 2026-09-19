import json
import os

db_path = os.path.join("assets", "data", "sample_data.json")
with open(db_path, "r", encoding="utf-8") as f:
    db = json.load(f)

questions = db.get("questions", [])
courses = db.get("courses", [])
topics = db.get("topics", [])
quick_notes = db.get("quick_notes", [])
note_map = {n["topic_id"]: n for n in quick_notes}

base_dir = os.path.join("assets", "data", "topics")

course_folder_map = {
    "course-turkce": "turkce",
    "course-matematik": "matematik",
    "course-tarih": "tarih",
    "course-cografya": "cografya",
    "course-vatandaslik": "vatandaslik",
    "course-guncel": "guncel_bilgiler"
}

for course in courses:
    cid = course["id"]
    ctitle = course["title"]
    cfolder = course_folder_map.get(cid, cid)
    cdir = os.path.join(base_dir, cfolder)
    os.makedirs(cdir, exist_ok=True)
    
    ctopics = [t for t in topics if t.get("course_id") == cid]
    c_questions = [q for q in questions if any(q.get("topic_id") == t["id"] for t in ctopics)]
    
    for t in ctopics:
        tid = t["id"]
        t_questions = [q for q in questions if q.get("topic_id") == tid]
        t_note = note_map.get(tid, {})
        
        topic_data = {
            "topic_id": tid,
            "title": t["title"],
            "course_id": cid,
            "question_count": len(t_questions),
            "quick_note": t_note,
            "questions": t_questions
        }
        
        t_filename = f"{tid}.json"
        t_filepath = os.path.join(cdir, t_filename)
        with open(t_filepath, "w", encoding="utf-8") as f_out:
            json.dump(topic_data, f_out, ensure_ascii=False, indent=2)
            
    master_data = {
        "course_id": cid,
        "course_title": ctitle,
        "total_topics": len(ctopics),
        "total_questions": len(c_questions),
        "topics": ctopics,
        "questions": c_questions
    }
    master_filename = f"{cfolder}_tum_konular.json"
    master_filepath = os.path.join(cdir, master_filename)
    with open(master_filepath, "w", encoding="utf-8") as f_out:
        json.dump(master_data, f_out, ensure_ascii=False, indent=2)

print("=== TÜM SENKRONİZASYON TAMAMLANDI ===")
