file_name = "example.txt"

try:
    # Dosyayı okuma modunda aç
    with open(file_name, "r") as file:
        # Satır satır oku
        for line in file:
            print(line.strip())  # strip metodu ile satır sonundaki boşlukları kaldır
except FileNotFoundError:
    print("Dosya bulunamadı.")
except Exception as e:
    print("Beklenmeyen bir hata oluştu:", e)
