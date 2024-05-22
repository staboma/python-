# Metin dosyasının adı
file_name = "metin_dosyasi.txt"

# Metin dosyasını okuma modunda aç
with open(file_name, "r") as file:
    # Dosyanın her satırını oku ve ekrana yazdır
    for line in file:
        print(line.strip())  # strip metodu ile satır sonundaki boşlukları kaldır
