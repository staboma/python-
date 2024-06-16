class Calisan:
    def __init__(self, ad, soyad, ise_baslangic_tarihi):
        self.ad = ad
        self.soyad = soyad
        self.ise_baslangic_tarihi = ise_baslangic_tarihi

# Örnek çalışanlar oluştur
calisan1 = Calisan("Ahmet", "Yılmaz", "2023-01-01")
calisan2 = Calisan("Ayşe", "Kaya", "2022-06-15")

# Çalışanların bilgilerini yazdır
print("Çalışan 1:")
print("Adı:", calisan1.ad)
print("Soyadı:", calisan1.soyad)
print("İşe Başlangıç Tarihi:", calisan1.ise_baslangic_tarihi)

print("\nÇalışan 2:")
print("Adı:", calisan2.ad)
print("Soyadı:", calisan2.soyad)
print("İşe Başlangıç Tarihi:", calisan2.ise_baslangic_tarihi)
