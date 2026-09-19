import json
import random
import os

def shuffle_and_balance_options():
    json_path = os.path.join("mobile_app", "assets", "data", "sample_data.json")
    with open(json_path, "r", encoding="utf-8") as f:
        db = json.load(f)

    questions = db["questions"]
    random.seed(42) # Deterministic yet completely randomized shuffle

    keys = ["A", "B", "C", "D", "E"]

    for i, q in enumerate(questions):
        correct_key = q["correct_option"]
        options = q["options"]

        # Find text of correct option
        correct_text = None
        for opt in options:
            if opt["key"] == correct_key:
                correct_text = opt["text"]
                break

        if not correct_text:
            continue

        # Shuffle option texts
        option_texts = [opt["text"] for opt in options]
        random.shuffle(option_texts)

        # Assign new keys A, B, C, D, E
        new_options = []
        new_correct_key = "A"

        for idx, text in enumerate(option_texts):
            k = keys[idx]
            new_options.append({"key": k, "text": text})
            if text == correct_text:
                new_correct_key = k

        q["options"] = new_options
        q["correct_option"] = new_correct_key

    # Print distribution
    from collections import Counter
    dist = Counter(q["correct_option"] for q in questions)
    print("=== YENİ DOĞRU ŞIK DAĞILIMI ===")
    print(dist)

    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(db, f, ensure_ascii=False, indent=2)

    print("\n[ŞIKLAR DENGELENDİ] sample_data.json başarıyla güncellendi!")

if __name__ == "__main__":
    shuffle_and_balance_options()
