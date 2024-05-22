import os

# Dosya adı
file_name = "example.txt"

# Dizin adı
dir_name = "example_dir"

try:
    # Dosya var mı?
    if os.path.exists(file_name):
        print(f"{file_name} dosyası mevcut.")
    else:
        print(f"{file_name} dosyası mevcut değil.")

    # Dizin var mı?
    if os.path.exists(dir_name):
        print(f"{dir_name} dizini mevcut.")
    else:
        print(f"{dir_name} dizini mevcut değil.")
except Exception as e:
    print("Beklenmeyen bir hata oluştu:", e)

