# Ürünler ve fiyatları
urunler = {
    "Telefon": 1500,
    "Laptop": 3000,
    "Tablet": 1200,
    "Televizyon": 2500
}

# En düşük fiyatı ve ürünü bulma
en_dusuk_fiyat = min(urunler.values())
en_uygun_urun = [urun for urun, fiyat in urunler.items() if fiyat == en_dusuk_fiyat]

# Sonuçları yazdırma
print(f"En uygun ürün: {en_uygun_urun}, Fiyat: {en_dusuk_fiyat}")
