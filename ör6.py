class Calisan:
    def __init__(self, calisan_id, ad, soyad, ise_baslangic_tarihi):
        self.calisan_id = calisan_id
        self.ad = ad
        self.soyad = soyad
        self.ise_baslangic_tarihi = ise_baslangic_tarihi

class CalisanListesi:
    def __init__(self):
        self.calisanlar = []

    def calisan_ekle(self, calisan):
        self.calisanlar.append(calisan)

    def calisan_sil(self, calisan_id):
        for calisan in self.calisanlar:
            if calisan.calisan_id == calisan_id:
                self.calisanlar.remove(calisan)
                print(f"{calisan.ad} {calisan.soyad} adlı çalışan silindi.")
                return
        print("Belirtilen ID'ye sahip bir çalışan bulunamadı.")

# Örnek çalışanlar oluştur
calisan1 = Calisan(101, "Ahmet", "Yılmaz", "2023-01-01")
calisan2 = Calisan(102, "Ayşe", "Kaya", "2022-06-15")

# Çalışan listesi oluştur
calisan_listesi = CalisanListesi()
calisan_listesi.calisan_ekle(calisan1)
calisan_listesi.calisan_ekle(calisan2)

# Çalışanları listele
print("İlk çalışan listesi:")
for calisan in calisan_listesi.calisanlar:
    print(f"{calisan.ad} {calisan.soyad}, ID: {calisan.calisan_id}")

# Çalışan ID'si ile silme işlemi
calisan_listesi.calisan_sil(101)

# Çalışanları listele (silme işlemi sonrası)
print("\nSilindikten sonra çalışan listesi:")
for calisan in calisan_listesi.calisanlar:
    print(f"{calisan.ad} {calisan.soyad}, ID: {calisan.calisan_id}")
