import json
import os

# Complete Flashcard database builder for Güncel Bilgiler & Genel Kültür (5 Topics x 10 Flashcards = 50 Flashcards)
guncel_flashcard_database = {
  "topic-gun-turkiye-gundemi": [
    {"card_number": 1, "title": "Türkiye'nin İlk Astronotu", "body": "Alper Gezeravcı, Ocak 2024'te Ax-3 misyonu ile Uluslararası Uzay İstasyonu'na giderek uzaya çıkan ilk Türk astronot olmuştur."},
    {"card_number": 2, "title": "Türkiye'nin İkinci Uzay Yolcusu", "body": "Tuva Cihangir Atasever, Haziran 2024'te Virgin Galactic firmasının yörünge altı uzay uçuşuyla uzay araştırmalarında yer almıştır."},
    {"card_number": 3, "title": "Dünyanın İlk SİHA Gemisi", "body": "TCG Anadolu, Türk Deniz Kuvvetleri envanterine giren, üzerine SİHA (Bayraktar TB3, Kızılelma) inip kalkabilen ilk amfibi hücum gemisidir."},
    {"card_number": 4, "title": "Türkiye'nin İlk Yerli ve Milli Otomobili", "body": "TOGG (Türkiye'nin Otomobili Girişim Grubu), ilk doğuştan elektrikli C-SUV modelini Gemlik tesislerinde üreterek yollara çıkarmıştır."},
    {"card_number": 5, "title": "Türkiye'nin İlk Muharip Uçağı", "body": "KAAN (TUSAŞ tarafından geliştirilen), 5. nesil milli muharip savaş uçağımız olarak ilk uçuşunu başarıyla gerçekleştirmiştir."},
    {"card_number": 6, "title": "Türkiye'nin Yerli Gözlem Uydusu", "body": "İMECE, metre altı yüksek çözünürlüklü ilk yerli ve milli gözlem uydumuzdur (2023'te uzaya fırlatılmıştır)."},
    {"card_number": 7, "title": "Türkiye'nin İlk Yerli Haberleşme Uydusu", "body": "Türksat 6A, Türk mühendisler tarafından yerli imkanlarla üretilen ilk haberleşme uydumuzdur."},
    {"card_number": 8, "title": "Türkiye'nin İlk İnsansız Savaş Uçağı", "body": "Bayraktar KIZILELMA, Baykar tarafından geliştirilen jet motorlu insansız otonom savaş uçağıdır."},
    {"card_number": 9, "title": "2024 Yılı Kültür ve Turizm Başkenti", "body": "Türk Dünyası Kültür Başkenti olarak TÜRKSOY tarafından 2024 yılı için Aşkabat (Türkmenistan) şehri seçilmiştir."},
    {"card_number": 10, "title": "Türkiye'nin İlk Şehir Hastanesi", "body": "Yozgat Şehir Hastanesi, Türkiye'de kamu-özel iş birliğiyle hizmete giren ilk şehir hastanesidir."}
  ],
  "topic-gun-dunya-ve-nobel": [
    {"card_number": 1, "title": "2024 Nobel Barış Ödülü Sahibi", "body": "Japonya merkezli 'Nihon Hidankyo' örgütü, nükleer silahsızlanma çabaları nedeniyle 2024 Nobel Barış Ödülü'nü kazanmıştır."},
    {"card_number": 2, "title": "2024 Nobel Edebiyat Ödülü Sahibi", "body": "Güney Koreli yazar 'Han Kang', tarihsel travmalarla yüzleşen ve insan hayatının kırılganlığını gözler önüne seren düzyazılarıyla ödülü kazanmıştır."},
    {"card_number": 3, "title": "2023 Nobel Barış Ödülü Sahibi", "body": "İranlı insan hakları savunucusu ve aktivist 'Nergis Muhammedi', kadın hakları mücadelesi nedeniyle ödülü almıştır."},
    {"card_number": 4, "title": "Nobel Ödülü Kazanan Türkler", "body": "Orhan Pamuk (2006 Nobel Edebiyat Ödülü) ve Prof. Dr. Aziz Sancar (2015 Nobel Kimya Ödülü)."},
    {"card_number": 5, "title": "Birleşmiş Milletler (BM) Genel Sekreteri", "body": "Antonio Guterres (Portekizli diplomat), 2017'den beri BM Genel Sekreterliği görevini yürütmektedir."},
    {"card_number": 6, "title": "Avrupa Birliği (AB) Komisyonu Başkanı", "body": "Ursula von der Leyen (Alman siyasetçi), AB Komisyonu'nun ilk kadın başkanıdır."},
    {"card_number": 7, "title": "NATO'ya Katılan Son Ülkeler", "body": "Finlandiya (31. üye - 2023) ve İsveç (32. üye - 2024) NATO'ya katılan en son üye ülkelerdir."},
    {"card_number": 8, "title": "Euro Bölgesi'ne Katılan Son Ülke", "body": "Hırvatistan, 1 Ocak 2023 itibarıyla Euro para birimine ve Schengen bölgesine resmen katılmıştır."},
    {"card_number": 9, "title": "G7 ve G20 Liderler Zirvesi", "body": "G7 gelişmiş 7 ülkenin birliğidir (ABD, İngiltere, Fransa, Almanya, İtalya, Kanada, Japonya). Türkiye G20 üyesidir."},
    {"card_number": 10, "title": "Dünyanın En Kalabalık Ülkesi", "body": "Hindistan, BM verilerine göre Çin'i geride bırakarak dünyanın en kalabalık nüfusuna sahip ülkesi olmuştur."}
  ],
  "topic-gun-spor-basarilari": [
    {"card_number": 1, "title": "Okçuluk Olimpiyat ve Dünya Şampiyonu", "body": "Mete Gazoz, 2020 Tokyo Olimpiyatları'nda ve 2023 Dünya Okçuluk Şampiyonası'nda altın madalya kazanmıştır."},
    {"card_number": 2, "title": "Filenin Sultanları 2023 Şampiyonluğu", "body": "Kadın Milli Voleybol Takımımız 2023 Milletler Ligi (VNL) ve 2023 Avrupa Şampiyonası'nda altın madalya alarak Dünya 1.si olmuştur."},
    {"card_number": 3, "title": "Olimpiyatlarda Atıcılık İkonu (Yusuf Dikeç)", "body": "2024 Paris Olimpiyatları'nda teçhizatsız ve eli cebinde yaptığı atışla gümüş madalya kazanan ve dünya gündemine oturan milli atıcımızdır."},
    {"card_number": 4, "title": "Dünya ve Avrupa Şampiyonu Güreşçimiz", "body": "Taha Akgül (Serbest stil) ve Rıza Kayaalp (Grekoromen stil) ata sporumuz güreşte tarihe geçen Olimpiyat ve Dünya şampiyonlarımızdır."},
    {"card_number": 5, "title": "Boks Olimpiyat Şampiyonumuz", "body": "Busenaz Sürmeneli, 2020 Tokyo Olimpiyatları'nda kadınlar boksta Türkiye tarihinin ilk altın madalyasını kazanmıştır."},
    {"card_number": 6, "title": "Dünya Şampiyonu Milli Jimnastikçimiz", "body": "İbrahim Çolak (Halka aleti) ve Adem Asil (Erkekler genel toplam), Dünya Jimnastik Şampiyonası'nda altın madalya kazanmışlardır."},
    {"card_number": 7, "title": "Şahika Ercümen Serbest Dalış", "body": "Milli sporcumuz Şahika Ercümen, paletsiz değişken ağırlık kategorisinde yüzlerce metreye dalarak dünya rekorları kırmıştır."},
    {"card_number": 8, "title": "Dünya Ampute Futbol Şampiyonu", "body": "Ampute Futbol Milli Takımımız, 2022 Dünya Kupası ve Avrupa Şampiyonluklarında altın madalya alarak dünya zirvesine çıkmıştır."},
    {"card_number": 9, "title": "2024 EURO Avrupa Futbol Şampiyonası", "body": "2024 Avrupa Futbol Şampiyonası (EURO 2024) Almanya'nın ev sahipliğinde düzenlenmiş, şampiyon İspanya olmuştur."},
    {"card_number": 10, "title": "2032 Avrupa Futbol Şampiyonası Ev Sahibi", "body": "EURO 2032 Avrupa Futbol Şampiyonası Türkiye ve İtalya ortak ev sahipliğinde düzenlenecektir."}
  ],
  "topic-gun-kultur-sanat-unesco": [
    {"card_number": 1, "title": "Tutunamayanlar ve Oğuz Atay", "body": "Oğuz Atay'ın 'Tutunamayanlar' romanı Türk edebiyatında modernizm ve bilinç akışı tekniğinin öncü eseridir."},
    {"card_number": 2, "title": "Kaplumbağa Terbiyecisi Eseri", "body": "Dünyaca ünlü tablo Sanayi-i Nefise Mektebi kurucusu ve arkeolog Osman Hamdi Bey'e aittir."},
    {"card_number": 3, "title": "Türk Edebiyatında 'Şair-i Azam'", "body": "Abdülhak Hamit Tarhan 'Şair-i Azam' (Büyük Şair) unvanıyla tanınır; en ünlü şiiri eşinin ölümü üzerine yazdığı 'Makber'dir."},
    {"card_number": 4, "title": "İstiklal Marşı Şairi Mehmet Akif Ersoy", "body": "İstiklal Marşı 12 Mart 1921'de kabul edilmiş, Mehmet Akif şiirini Türk ordusuna ithaf etmiş ve ödülü Darülmesai'ye bağışlamıştır."},
    {"card_number": 5, "title": "Sinekli Bakkal ve Halide Edip Adıvar", "body": "Kurtuluş Savaşı romanlarıyla tanınan Halide Edip Adıvar'ın en bilinen eserlerinden biridir (Doğu-Batı sentezi)."},
    {"card_number": 6, "title": "İnce Memed ve Yaşar Kemal", "body": "Yaşar Kemal'in Çukurova insanını, ağalık düzenini ve başkaldırıyı anlattığı 4 ciltlik dünyaca ünlü epic eseridir."},
    {"card_number": 7, "title": "Türk Edebiyatında İlk Romanlar", "body": "İlk Yerli Roman: Taaşşuk-ı Talat ve Fitnat (Şemsettin Sami); İlk Çeviri Roman: Telemak (Yusuf Kamil Paşa); İlk Tarihi Roman: Cezmi (Namık Kemal)."},
    {"card_number": 8, "title": "Dünyanın En Eski Tapınağı Göbeklitepe", "body": "Şanlıurfa'da yer alan, Neolitik döneme ait M.Ö. 10.000 yıllarına tarihlenen tarihin sıfır noktası tapınak kompleksidir."},
    {"card_number": 9, "title": "Mesnevi ve Mevlana Celaleddin-i Rumi", "body": "Tasavvuf düşüncesinin abidesi olan 26 bin beyitlik 'Mesnevi' eseri Mevlana'ya aittir (Şeb-i Arus: Vuslat gecesi ölüm yıldönümü)."},
    {"card_number": 10, "title": "İstiklal Marşı Bestecisi Zeki Üngör", "body": "İstiklal Marşı'mızın günümüzde kullanılan resmi bestesi Cumhurbaşkanlığı Senfoni Orkestrası şefi Osman Zeki Üngör'e aittir."}
  ],
  "topic-gun-bilim-teknoloji": [
    {"card_number": 1, "title": "James Webb Uzay Teleskobu (JWST)", "body": "NASA, ESA ve CSA ortaklığıyla fırlatılan, Hubble'ın halefi kızılötesi uzay teleskobudur; evrenin ilk galaksilerini gözlemler."},
    {"card_number": 2, "title": "Büyük Hadron Çarpıştırıcısı (LHC)", "body": "CERN (İsviçre-Fransa sınırı) altında yer alan dünyanın en büyük parçacık hızlandırıcısıdır (Higgs Bozonu keşfedilmiştir)."},
    {"card_number": 3, "title": "CRISPR-Cas9 Gen Düzenleme", "body": "Genom üzerinde hassas kesme ve düzenleme yapmayı sağlayan moleküler makas genetik teknolojisidir (Nobel Kimya ödülü almıştır)."},
    {"card_number": 4, "title": "Mars Drone'u Ingenuity", "body": "NASA'nın Perseverance uzay aracıyla Mars'a gönderilen ve başka bir gezegende uçan ilk motorlu hava aracıdır."},
    {"card_number": 5, "title": "Yapay Zeka Turing Testi", "body": "Alan Turing tarafından önerilen, bir makinenin insan zekasından ayırt edilemeyecek şekilde yanıt verip veremediğini ölçen klasik testtir."},
    {"card_number": 6, "title": "Kuantum Bilgisayar ve Kubit", "body": "Klasik bilgisayarlardaki 0 ve 1 bitleri yerine süperpozisyon özelliğine sahip 'Kubit' (Qubit) birimini kullanan kuantum sistemleridir."},
    {"card_number": 7, "title": "Nesnelerin İnterneti (IoT)", "body": "Günlük hayattaki tüm cihazların (akıllı ev, araçlar) internet üzerinden birbirleriyle veri paylaşımı yapması teknolojisidir."},
    {"card_number": 8, "title": "Lidar Sensör Teknolojisi", "body": "Otonom (sürücüsüz) araçlarda ve haritalamada kullanılan, lazer ışınları ile 3D çevre taraması yapan sensör sistemidir."},
    {"card_number": 9, "title": "Kötü Amaçlı Yazılım (Malware)", "body": "Bilgisayar sistemlerine sızmak, zarar vermek veya veri çalmak için tasarlanmış virüs, trojan ve fidye yazılımlarının genel adıdır."},
    {"card_number": 10, "title": "Ay'a Ayak Basan İlk İnsan", "body": "Neil Armstrong, 1969 yılında Apollo 11 misyonu ile Ay yüzeyine ayak basan ilk insandır ('İnsan için küçük, insanlık için büyük bir adım')."}
  ]
}

def export_all_guncel_flashcards():
    base_dir = os.path.join("assets", "data", "topics", "guncel_bilgiler")
    os.makedirs(base_dir, exist_ok=True)
    
    total_cards = 0
    for topic_id, cards in guncel_flashcard_database.items():
        data = {
            "topic_id": topic_id,
            "flashcard_count": len(cards),
            "flashcards": cards
        }
        
        file_name = f"flashcards_{topic_id}.json"
        file_path = os.path.join(base_dir, file_name)
        
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
            
        total_cards += len(cards)
        print(f"  [OK] {topic_id} -> {len(cards)} Flashcard yazıldı: {file_path}")

    print(f"\n[BAŞARILI] GÜNCEL BİLGİLER DERSİNİN TÜM 5 ALT KONUSUNA AİT TOPLAM {total_cards} FLASHCARD ENTEGRE EDİLDİ!")

if __name__ == "__main__":
    export_all_guncel_flashcards()
