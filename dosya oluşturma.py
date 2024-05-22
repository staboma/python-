# Dosya adı
file_name = "example.txt"

# Dosyayı yazma modunda aç
with open(file_name, "w") as file:
    file.write("Bu bir örnek dosyadır.\n")
    file.write("İkinci satır.\n")
    file.write("Üçüncü satır.\n")
