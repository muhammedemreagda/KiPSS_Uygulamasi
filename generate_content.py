#!/usr/bin/env python3
"""
KPSS İçerik Üretim Aracı — KıPSS şemasına uyumlu
==================================================
KıPSS uygulamasının gerçek veri modeline (QuickNoteModel, FlashcardItem,
QuestionModel) birebir uyumlu JSON üretir. Üç mod var:

  note        -> Yeni bir konu için tam QuickNote (özet+içerik+key_points
                 +flashcard'lar) VE soru seti üretir (henüz hiç işlenmemiş
                 bir alt konu için).
  flashcards  -> Var olan bir konuya EK flashcard üretir (mevcut kartlarla
                 tekrara düşmeden), "Hızlı Okuma Kartları" eksikliğini
                 kapatmak için.
  questions   -> Var olan bir konuya EK soru üretir (10 sorudan 25-30'a
                 çıkarmak için), numaralandırmayı otomatik devam ettirir.
"""

import argparse
import json
import os
import sys
import urllib.request
import urllib.error

API_URL = "https://api.anthropic.com/v1/messages"
MODEL = "claude-3-5-sonnet-20241022"
MAX_TOKENS = 8000

BASE_RULES = """Sen KıPSS adlı bir KPSS (Türkiye Kamu Personeli Seçme Sınavı) hazırlık
uygulaması için içerik üreten bir editörsün.

KATI KURALLAR:
1. Kaynak metin verilirse ASLA birebir kopyalama; kuralı kendi cümlelerinle,
   öğretici bir üslupla, ÖZGÜN olarak anlat.
2. Sorular tamamen ÖZGÜN olmalı — gerçek ÖSYM veya yayınevi sorularını
   kopyalama/parafraz etme, sadece format/kalıp referans al.
3. Bilgi hatası içermemeli; emin olmadığın detayı ekleme.
4. Şıkların (A-E) dağılımı dengeli olsun, doğru cevap hep aynı harfte
   toplanmasın.
5. Açıklamalar kuralı TEKRAR öğretecek şekilde detaylı yazılmalı.
6. SADECE istenen JSON'u ver — markdown fence, önsöz, sonsöz YOK.
"""


def call_claude(api_key, system_prompt, user_prompt):
    payload = {
        "model": MODEL,
        "max_tokens": MAX_TOKENS,
        "system": system_prompt,
        "messages": [{"role": "user", "content": user_prompt}],
    }
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        API_URL, data=data,
        headers={
            "Content-Type": "application/json",
            "x-api-key": api_key,
            "anthropic-version": "2023-06-01",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=180) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        print(f"API hatası ({e.code}): {e.read().decode('utf-8', errors='replace')}", file=sys.stderr)
        sys.exit(1)
    except urllib.error.URLError as e:
        print(f"Bağlantı hatası: {e}", file=sys.stderr)
        sys.exit(1)


def extract_text(resp):
    return "\n".join(b["text"] for b in resp.get("content", []) if b.get("type") == "text").strip()


def parse_json(raw):
    cleaned = raw.strip()
    if cleaned.startswith("```"):
        cleaned = cleaned.strip("`")
        if cleaned.lower().startswith("json"):
            cleaned = cleaned[4:]
    try:
        return json.loads(cleaned)
    except json.JSONDecodeError as e:
        print(f"UYARI: JSON parse edilemedi: {e}", file=sys.stderr)
        with open("ham_cikti_hata.txt", "w", encoding="utf-8") as f:
            f.write(raw)
        print("Ham çıktı 'ham_cikti_hata.txt' dosyasına yazıldı.", file=sys.stderr)
        sys.exit(1)


def load_output(path):
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                pass
    return {"quick_notes": [], "questions": []}


def save_output(path, data):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def cmd_note(args, api_key):
    kaynak = ""
    if args.kaynak_dosya:
        with open(args.kaynak_dosya, "r", encoding="utf-8") as f:
            kaynak = f.read()

    user_prompt = f"""Ders: {args.ders}
Konu başlığı: {args.title}
Konu ID (topic_id): {args.topic_id}
İstenen soru sayısı: {args.soru_sayisi}
İstenen flashcard sayısı: {args.flashcard_sayisi} (8-12 arası ideal)
{"Kaynak notlar (kopyalamayın, sadece referans alın): " + kaynak if kaynak else ""}

Tam olarak şu JSON şemasında çıktı ver:

{{
  "quick_note": {{
    "id": "note-{args.topic_id}",
    "topic_id": "{args.topic_id}",
    "title": "{args.title}",
    "summary": "ÖSYM'de bu konunun soru değerini özetleyen 1-2 cümle",
    "content": "Markdown destekli, ### başlıklarla bölümlenmiş detaylı ders anlatımı",
    "key_points": ["emoji ile başlayan 2-4 adet ÖSYM püf noktası / akrostiş"],
    "flashcards": [
      {{"card_number": 1, "title": "kısa başlık", "body": "1-2 cümlelik hatırlatıcı"}}
    ],
    "source_reference": "kullanılan kaynağın adı (örn. TDK Yazım Kılavuzu, Anayasa metni)"
  }},
  "questions": [
    {{
      "id": "q-{args.topic_id}-1",
      "topic_id": "{args.topic_id}",
      "question_text": "...",
      "options": [
        {{"key": "A", "text": "..."}}, {{"key": "B", "text": "..."}},
        {{"key": "C", "text": "..."}}, {{"key": "D", "text": "..."}},
        {{"key": "E", "text": "..."}}
      ],
      "correct_option": "A",
      "explanation": "...",
      "difficulty_level": 3
    }}
  ]
}}

questions dizisinde id'leri q-{args.topic_id}-1'den {args.soru_sayisi}'e kadar sırayla numaralandır.
flashcards dizisinde card_number 1'den {args.flashcard_sayisi}'e kadar sırayla olsun."""

    resp = call_claude(api_key, BASE_RULES, user_prompt)
    parsed = parse_json(extract_text(resp))

    note = parsed.get("quick_note", {})
    note["is_verified"] = False
    note.setdefault("read_time_seconds", 180)

    questions = parsed.get("questions", [])

    data = load_output(args.cikti)
    data["quick_notes"].append(note)
    data["questions"].extend(questions)
    save_output(args.cikti, data)

    print(f"[+] '{args.title}' için 1 quick_note + {len(questions)} soru üretildi -> {args.cikti}")
    _print_review_reminder()


def cmd_flashcards(args, api_key):
    mevcut_kartlar = []
    baslangic_no = 1
    if args.mevcut_kartlar and os.path.exists(args.mevcut_kartlar):
        with open(args.mevcut_kartlar, "r", encoding="utf-8") as f:
            mevcut_kartlar = json.load(f)
        if mevcut_kartlar:
            baslangic_no = max(c.get("card_number", 0) for c in mevcut_kartlar) + 1

    eksik_sayi = args.hedef_sayi - len(mevcut_kartlar)
    if eksik_sayi <= 0:
        print(f"[i] Bu konuda zaten {len(mevcut_kartlar)} kart var, hedef {args.hedef_sayi}'e ulaşılmış. Üretim yapılmadı.")
        return

    mevcut_metin = "\n".join(f"- {c.get('title','')}: {c.get('body','')}" for c in mevcut_kartlar)
    user_prompt = f"""Konu başlığı: {args.title}
Konu özeti: {args.mevcut_ozet}

Bu konu için ZATEN VAR OLAN flashcard'lar (bunları TEKRARLAMA, farklı açılardan
yeni kartlar üret):
{mevcut_metin if mevcut_metin else "(henüz kart yok)"}

{eksik_sayi} adet YENİ flashcard üret. Her biri farklı bir alt-detay, istisna,
ya da sık yapılan hata üzerine olsun (mevcut kartlarla çakışmasın).

Tam olarak şu JSON şemasında çıktı ver:
{{
  "flashcards": [
    {{"card_number": {baslangic_no}, "title": "...", "body": "..."}}
  ]
}}
card_number'ları {baslangic_no}'dan başlayıp sırayla artır."""

    resp = call_claude(api_key, BASE_RULES, user_prompt)
    parsed = parse_json(extract_text(resp))
    yeni_kartlar = parsed.get("flashcards", [])

    data = load_output(args.cikti)
    note = next((n for n in data["quick_notes"] if n.get("topic_id") == args.topic_id), None)
    if note is None:
        note = {"topic_id": args.topic_id, "title": args.title, "flashcards": [], "is_verified": False}
        data["quick_notes"].append(note)
    note.setdefault("flashcards", [])
    note["flashcards"].extend(yeni_kartlar)
    note["is_verified"] = False
    save_output(args.cikti, data)

    print(f"[+] '{args.title}' için {len(yeni_kartlar)} yeni flashcard üretildi -> {args.cikti}")
    _print_review_reminder()


def cmd_questions(args, api_key):
    user_prompt = f"""Konu başlığı: {args.title}
Konu ID: {args.topic_id}

Bu konu için {args.soru_sayisi} adet YENİ, ÖZGÜN soru üret. Zorluk seviyesi
1-5 arası (KPSS Lisans için ağırlıklı olarak 3-4) dağıtılmış olsun.

Tam olarak şu JSON şemasında çıktı ver:
{{
  "questions": [
    {{
      "id": "q-{args.topic_id}-{args.baslangic_no}",
      "topic_id": "{args.topic_id}",
      "question_text": "...",
      "options": [
        {{"key": "A", "text": "..."}}, {{"key": "B", "text": "..."}},
        {{"key": "C", "text": "..."}}, {{"key": "D", "text": "..."}},
        {{"key": "E", "text": "..."}}
      ],
      "correct_option": "A",
      "explanation": "...",
      "difficulty_level": 3
    }}
  ]
}}
id'leri q-{args.topic_id}-{args.baslangic_no}'dan başlayıp {args.soru_sayisi} adet
sırayla numaralandır. Şık dağılımını dengeli tut (doğru cevap hep aynı harfte
olmasın)."""

    resp = call_claude(api_key, BASE_RULES, user_prompt)
    parsed = parse_json(extract_text(resp))
    yeni_sorular = parsed.get("questions", [])

    data = load_output(args.cikti)
    data["questions"].extend(yeni_sorular)
    save_output(args.cikti, data)

    print(f"[+] '{args.title}' için {len(yeni_sorular)} yeni soru üretildi -> {args.cikti}")
    _print_review_reminder()


def _print_review_reminder():
    print("[!] HATIRLATMA: Üretilen içerik TASLAKTIR (is_verified: false).")
    print("    Yayınlamadan/uygulamaya işlemeden önce:")
    print("    - Bilgi doğruluğunu kontrol edin")
    print("    - Şık dağılımının dengeli olduğunu doğrulayın (özellikle C şıkkı fazla kullanılmasın)")
    print("    - Onayladıktan sonra is_verified alanını elle 'true' yapın")


def get_api_key():
    key = os.environ.get("ANTHROPIC_API_KEY")
    if not key:
        print("HATA: ANTHROPIC_API_KEY ortam değişkeni bulunamadı.", file=sys.stderr)
        print('export ANTHROPIC_API_KEY="sk-ant-..."', file=sys.stderr)
        sys.exit(1)
    return key


def main():
    ap = argparse.ArgumentParser(description="KıPSS şemasına uyumlu içerik üretici")
    sub = ap.add_subparsers(dest="mod", required=True)

    p_note = sub.add_parser("note", help="Yeni konu için tam QuickNote + soru seti üret")
    p_note.add_argument("--topic_id", required=True)
    p_note.add_argument("--title", required=True)
    p_note.add_argument("--ders", required=True)
    p_note.add_argument("--soru_sayisi", type=int, default=25)
    p_note.add_argument("--flashcard_sayisi", type=int, default=10)
    p_note.add_argument("--kaynak_dosya", default=None)
    p_note.add_argument("--cikti", default="kpss_yeni_icerik.json")

    p_fc = sub.add_parser("flashcards", help="Mevcut konuya ek flashcard üret")
    p_fc.add_argument("--topic_id", required=True)
    p_fc.add_argument("--title", required=True)
    p_fc.add_argument("--mevcut_ozet", required=True)
    p_fc.add_argument("--mevcut_kartlar", default=None, help="Mevcut flashcard'ları içeren JSON dosyası (liste)")
    p_fc.add_argument("--hedef_sayi", type=int, default=10)
    p_fc.add_argument("--cikti", default="kpss_yeni_icerik.json")

    p_q = sub.add_parser("questions", help="Mevcut konuya ek soru üret")
    p_q.add_argument("--topic_id", required=True)
    p_q.add_argument("--title", required=True)
    p_q.add_argument("--soru_sayisi", type=int, default=15)
    p_q.add_argument("--baslangic_no", type=int, default=11, help="Yeni soruların başlayacağı numara (10 soru varsa 11'den başlar)")
    p_q.add_argument("--cikti", default="kpss_yeni_icerik.json")

    args = ap.parse_args()
    api_key = get_api_key()

    if args.mod == "note":
        cmd_note(args, api_key)
    elif args.mod == "flashcards":
        cmd_flashcards(args, api_key)
    elif args.mod == "questions":
        cmd_questions(args, api_key)


if __name__ == "__main__":
    main()
