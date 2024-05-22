metin = "Bu bir örnek metin. Ayrıca, metinde gereksiz boşluklar ve noktalama işaretleri var!"

# Metindeki gereksiz boşlukları kaldırma
temiz_metin = " ".join(metin.split())

# Metindeki noktalama işaretlerini kaldırma
temiz_metin = "".join(c for c in metin if c not in ("!", ".", ",", ";", ":"))
