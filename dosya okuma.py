file_name = "example.txt"

try:
    # Dosyayı okuma modunda aç
    with open(file_name, "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("Dosya bulunamadı.")
except Exception as e:
    print("Beklenmeyen bir hata oluştu:", e)
