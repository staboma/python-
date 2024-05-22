import os
import shutil

# Dosya adı
file_name = "example.txt"

# Dizin adı
dir_name = "example_dir"

try:
    # Dosyayı sil
    os.remove(file_name)
    print(f"{file_name} dosyası başarıyla silindi.")

    # Dizini sil
    shutil.rmtree(dir_name)
    print(f"{dir_name} dizini başarıyla silindi.")
except FileNotFoundError:
    print("Dosya veya dizin bulunamadı.")
except PermissionError:
    print("Dosya veya dizin silme izni yok.")
except Exception as e:
    print("Beklenmeyen bir hata oluştu:", e)

