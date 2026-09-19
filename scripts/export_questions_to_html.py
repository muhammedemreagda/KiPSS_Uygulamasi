import json
import os

def export_to_html():
    json_path = os.path.join("assets", "data", "sample_data.json")
    with open(json_path, "r", encoding="utf-8") as f:
        db = json.load(f)

    questions = db.get("questions", [])
    topics = {t["id"]: t for t in db.get("topics", [])}
    courses = {c["id"]: c["title"] for c in db.get("courses", [])}

    html_content = f"""<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>KıPSS — Full Soru Bankası Arşivi ({len(questions)} Soru)</title>
    <style>
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: #0F172A;
            color: #F8FAFC;
            margin: 0;
            padding: 20px;
        }}
        .header {{
            background: linear-gradient(135deg, #00CEC9, #0984E3);
            color: #0F172A;
            padding: 24px;
            border-radius: 16px;
            margin-bottom: 24px;
            box-shadow: 0 10px 25px rgba(0,206,201,0.3);
        }}
        .header h1 {{ margin: 0 0 8px 0; font-size: 28px; }}
        .header p {{ margin: 0; font-weight: 600; opacity: 0.9; }}
        .controls {{
            display: flex;
            gap: 12px;
            margin-bottom: 24px;
            flex-wrap: wrap;
        }}
        input, select {{
            padding: 12px 16px;
            border-radius: 10px;
            border: 1px solid #334155;
            background-color: #1E293B;
            color: white;
            font-size: 14px;
            outline: none;
        }}
        input {{ flex: 1; min-width: 250px; }}
        .question-card {{
            background-color: #1E293B;
            border: 1px solid #334155;
            border-radius: 14px;
            padding: 20px;
            margin-bottom: 16px;
        }}
        .tag {{
            display: inline-block;
            padding: 4px 10px;
            background-color: rgba(0,206,201,0.15);
            color: #00CEC9;
            border: 1px solid #00CEC9;
            border-radius: 8px;
            font-size: 12px;
            font-weight: bold;
            margin-bottom: 12px;
        }}
        .q-text {{
            font-size: 16px;
            font-weight: 600;
            margin-bottom: 14px;
            line-height: 1.5;
        }}
        .options {{
            display: grid;
            gap: 8px;
            margin-bottom: 14px;
        }}
        .option {{
            padding: 10px 14px;
            background-color: #0F172A;
            border-radius: 8px;
            font-size: 14px;
        }}
        .option.correct {{
            background-color: rgba(0,184,148,0.2);
            border: 1px solid #00B894;
            color: #55E6C1;
            font-weight: bold;
        }}
        .exp {{
            background-color: rgba(9,132,227,0.1);
            border-left: 4px solid #0984E3;
            padding: 12px;
            border-radius: 6px;
            font-size: 13px;
            color: #99AAFF;
        }}
    </style>
</head>
<body>
    <div class="header">
        <h1>KıPSS — Soru Bankası ({len(questions)} Soru)</h1>
        <p>Tüm KPSS Türkçe, Matematik, Tarih, Coğrafya, Vatandaşlık ve Güncel Bilgiler Soruları</p>
    </div>

    <div class="controls">
        <input type="text" id="searchInput" placeholder="Soru metni veya alt konu ara..." onkeyup="filterQuestions()">
        <select id="courseFilter" onchange="filterQuestions()">
            <option value="">Tüm Dersler</option>
            <option value="Türkçe">Türkçe</option>
            <option value="Matematik">Matematik & Geometri</option>
            <option value="Tarih">Tarih</option>
            <option value="Coğrafya">Coğrafya</option>
            <option value="Vatandaşlık">Vatandaşlık</option>
            <option value="Güncel">Güncel Bilgiler</option>
        </select>
    </div>

    <div id="questionContainer">
"""

    for idx, q in enumerate(questions, 1):
        topic_info = topics.get(q["topic_id"], {})
        course_name = courses.get(topic_info.get("course_id", ""), "Genel")
        topic_title = topic_info.get("title", "Konu")
        correct_opt = q.get("correct_option", "A")

        html_content += f"""
        <div class="question-card" data-course="{course_name}" data-text="{q['question_text'].lower()} {topic_title.lower()}">
            <span class="tag">Soru #{idx} • {course_name} ➔ {topic_title}</span>
            <div class="q-text">{q['question_text']}</div>
            <div class="options">
        """

        for opt in q.get("options", []):
            is_correct = opt["key"] == correct_opt
            correct_class = "correct" if is_correct else ""
            badge = " ✓ (Doğru Cevap)" if is_correct else ""
            html_content += f'<div class="option {correct_class}"><b>{opt["key"]})</b> {opt["text"]}{badge}</div>'

        html_content += f"""
            </div>
            <div class="exp"><b>💡 ÖSYM Çözüm Açıklaması:</b> {q.get('explanation', '')}</div>
        </div>
        """

    html_content += """
    </div>

    <script>
        function filterQuestions() {
            var input = document.getElementById("searchInput").value.toLowerCase();
            var course = document.getElementById("courseFilter").value;
            var cards = document.getElementsByClassName("question-card");

            for (var i = 0; i < cards.length; i++) {
                var card = cards[i];
                var text = card.getAttribute("data-text");
                var cName = card.getAttribute("data-course");

                var matchesText = text.includes(input);
                var matchesCourse = course === "" || cName.includes(course);

                if (matchesText && matchesCourse) {
                    card.style.display = "block";
                } else {
                    card.style.display = "none";
                }
            }
        }
    </script>
</body>
</html>
"""

    out_path = os.path.join("KPSS_Soru_Bankasi.html")
    with open(out_path, "w", encoding="utf-8") as out_f:
        out_f.write(html_content)

    print(f"HTML Soru Bankası güncellendi: {out_path}")

if __name__ == "__main__":
    export_to_html()
