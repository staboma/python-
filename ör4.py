class Calisan:
    def __init__(self, id, calisan_id, unvan, baslangic_tarihi, bitis_tarihi):
        self.id = id
        self.calisan_id = calisan_id
        self.unvan = unvan
        self.baslangic_tarihi = baslangic_tarihi
        self.bitis_tarihi = bitis_tarihi

# Örnek çalışanlar oluştur
calisan1 = Calisan(1, 101, "Yazılım Mühendisi", "2023-01-01", "2024-01-01")
calisan2 = Calisan(2, 102, "Veri Analisti", "2022-06-15", None)  # Henüz ayrılmadı

# Çalışanların bilgilerini yazdır
print("Calisan 1:")
print("ID:", calisan1.id)
print("Çalışan ID:", calisan1.calisan_id)
print("Unvan:", calisan1.unvan)
print("Başlangıç Tarihi:", calisan1.baslangic_tarihi)
print("Bitiş Tarihi:", calisan1.bitis_tarihi)

print("\nCalisan 2:")
print("ID:", calisan2.id)
print("Çalışan ID:", calisan2.calisan_id)
print("Unvan:", calisan2.unvan)
print("Başlangıç Tarihi:", calisan2.baslangic_tarihi)
print("Bitiş Tarihi:", calisan2.bitis_tarihi if calisan2.bitis_tarihi else "Hala çalışıyor")
