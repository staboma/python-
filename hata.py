try:
    sayi = int(input("Bir sayı girin: "))
    kare = sayi ** 2
    print("Sayının karesi:", kare)
except ValueError:
    print("Hatalı giriş! Bir sayı girilmelidir.")
