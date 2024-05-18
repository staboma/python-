with open("veriler.txt", "r") as dosya:
    veriler = dosya.readlines()

for veri in veriler:
    print(veri.strip())  # Satır sonundaki boşlukları kaldırır
