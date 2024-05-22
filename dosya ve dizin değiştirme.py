import os

# Eski dosya adı
old_file_name = "old_name.txt"

# Yeni dosya adı
new_file_name = "new_name.txt"

# Eski dizin adı
old_dir_name = "old_dir"

# Yeni dizin adı
new_dir_name = "new_dir"

try:
    # Dosya adını değiştir
    os.rename(old_file_name, new_file_name)
    print(f"{old_file_name} dosyasının adı {new_file_name} olarak değiştirildi.")

    # Dizin adını değiştir
    os.rename(old_dir_name, new_dir_name)
    print(f"{old_dir_name} dizinin adı {new_dir_name} olarak değiştirildi.")
except FileNotFoundError:
    print("Dosya veya dizin bulunamadı.")
except PermissionError:
    print("Dosya veya dizin adını değiştirmek için izin yok.")
except FileExistsError:
    print("Hedef dosya veya dizin zaten var.")
except Exception as e:
    print("Beklenmeyen bir hata oluştu:", e)

