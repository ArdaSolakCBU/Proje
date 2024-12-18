import json

# Öğrencilerin bilgilerini tutmak için boş bir liste
veritabani = []

# Yeni öğrenci ekleme
def ogrenci_ekle():
    """Kullanıcıdan öğrenci bilgilerini alır ve kayıt oluşturur."""
    print("\n=== Yeni Öğrenci Kaydı ===")
    isim = input("Öğrenci Adı: ").strip().capitalize()
    soyisim = input("Öğrenci Soyadı: ").strip().capitalize()

    # Öğrenci numarası girişi ve kontrolü
    while True:
        try:
            numara = int(input("Öğrenci Numarası (3 Haneli): "))
            if 100 <= numara <= 999 and not numara_var_mi(numara):
                break
            print("Hatalı giriş! Numara benzersiz ve 3 haneli olmalı.")
        except ValueError:
            print("Lütfen geçerli bir sayı giriniz.")

    # Ders ve not girişleri
    notlar = {}
    en_az_bir_ders = False
    while True:
        ders = input("Ders adı (Çıkmak için '0' yazın): ").strip().capitalize()
        if ders == "0":
            if en_az_bir_ders:
                break
            else:
                print("En az bir ders eklemek zorundasınız.")
                continue
        elif ders:
            while True:
                try:
                    puan = int(input(f"{ders} notu (0-100): "))
                    if 0 <= puan <= 100:
                        notlar[ders] = puan
                        en_az_bir_ders = True
                        break
                    else:
                        print("Not 0 ile 100 arasında olmalıdır.")
                except ValueError:
                    print("Lütfen geçerli bir sayı giriniz.")
        else:
            print("Ders adı boş olamaz.")

    # Kayıt ekleme
    veritabani.append({"isim": isim, "soyisim": soyisim, "numara": numara, "notlar": notlar})
    print("Öğrenci başarıyla eklendi.")

# Kayıtları listeleme
def kayitlari_goster():
    """Kayıtlı öğrencilerin bilgilerini ekrana yazdırır."""
    print("\n=== Kayıtlı Öğrenciler ===")
    if not veritabani:
        print("Henüz kayıtlı öğrenci yok.")
        return
    for kayit in veritabani:
        print(f"Ad: {kayit['isim']} {kayit['soyisim']}, Numara: {kayit['numara']}")
        print("  Notlar:")
        if kayit["notlar"]:
            for ders, puan in kayit["notlar"].items():
                print(f"    {ders}: {puan}")
        else:
            print("    Not bilgisi yok.")
        print("-" * 30)

# Not istatistiklerini hesaplama
def istatistikleri_hesapla():
    """Notları analiz ederek istatistikleri ekrana yazdırır."""
    print("\n=== Not İstatistikleri ===")
    tum_notlar = []
    for kayit in veritabani:
        tum_notlar.extend(kayit["notlar"].values())
    if not tum_notlar:
        print("Henüz not bilgisi girilmemiş.")
        return

    en_yuksek = max(tum_notlar)
    en_dusuk = min(tum_notlar)
    ortalama = sum(tum_notlar) / len(tum_notlar)

    print(f"En Yüksek Not: {en_yuksek}")
    print(f"En Düşük Not: {en_dusuk}")
    print(f"Sınıf Ortalaması: {ortalama:.2f}")

# Öğrenci numarasını kontrol etme
def numara_var_mi(ogrenci_numarasi):
    """Girilen öğrenci numarasının kayıtlı olup olmadığını kontrol eder."""
    for kayit in veritabani:
        if kayit["numara"] == ogrenci_numarasi:
            return True
    return False

# Menü Gösterimi
def menu_goster():
    """Ana menüyü ekrana yazdırır."""
    print("\n==== Öğrenci Yönetim Sistemi ====")
    print("📌 1. Öğrenci Ekle")
    print("📌 2. Kayıtları Gör")
    print("📌 3. Not İstatistikleri")
    print("📌 4. Programdan Çık")

# Program Döngüsü
while True:
    menu_goster()
    secim = input("Bir seçim yapınız: ").strip()
    if secim == "1":
        ogrenci_ekle()
    elif secim == "2":
        kayitlari_goster()
    elif secim == "3":
        istatistikleri_hesapla()
    elif secim == "4":
        print("Programdan çıkılıyor...")
        break
    else:
        print("Geçersiz seçim, lütfen tekrar deneyiniz.")
