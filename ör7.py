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

    def calisan_guncelle(self, calisan_id, yeni_ad, yeni_soyad, yeni_ise_baslangic_tarihi):
        for calisan in self.calisanlar:
            if calisan.calisan_id == calisan_id:
                calisan.ad = yeni_ad
                calisan.soyad = yeni_soyad
                calisan.ise_baslangic_tarihi = yeni_ise_baslangic_tarihi
                print(f"{calisan_id} ID'li çalışanın bilgileri güncellendi.")
                return
        print("Belirtilen ID'ye sahip bir çalışan bulunamadı.")

# Örnek çalışanlar oluştur
calisan1 = Calisan(101, "Ahmet", "Yılmaz", "2023-01-01")
calisan2 = Calisan(102, "Ayşe", "Kaya", "2022-06-15")

# Çalışan listesi oluştur
calisan_listesi = CalisanListesi()
calisan_listesi.calisan_ekle(calisan1)
calisan_listesi.calisan_ekle(calisan2)

# Çalışanları listele (güncelleme işlemi öncesi)
print("İlk çalışan listesi:")
for calisan in calisan_listesi.calisanlar:
    print(f"{calisan.calisan_id}: {calisan.ad} {calisan.soyad}, İşe Başlangıç Tarihi: {calisan.ise_baslangic_tarihi}")

# Çalışan bilgilerini güncelle
calisan_listesi.calisan_guncelle(101, "Mehmet", "Demir", "2024-01-01")

# Çalışanları listele (güncelleme işlemi sonrası)
print("\nGüncellendikten sonra çalışan listesi:")
for calisan in calisan_listesi.calisanlar:
    print(f"{calisan.calisan_id}: {calisan.ad} {calisan.soyad}, İşe Başlangıç Tarihi: {calisan.ise_baslangic_tarihi}")
