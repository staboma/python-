sorular = {
    "1. Soru": "Türkiye'nin başkenti?",
    "2. Soru": "En yüksek dağ?",
    "3. Soru": "Kim bilir?",
}

cevaplar = {
    "1. Soru": "Ankara",
    "2. Soru": "Everest",
    "3. Soru": "Yaradan bilir.",
}

puan = 0
for soru, dogru_cevap in sorular.items():
    cevap = input(soru + "\nCevabınız: ")
    if cevap.lower() == dogru_cevap.lower():
        print("Doğru!")
        puan += 10
    else:
        print("Yanlış!")

print("Toplam Puanınız:", puan)

