sorularVeDogruCevaplari = {
    "1. Soru: Türkiye'nin başkenti hangi ildir?": "Ankara",
    "2. Soru: En yüksek dağın adı nedir?": "Everest",
    "3. Soru: Kim bilir": "Yaradan bilir"
}

puan = 0

for soru, dogru_cevap in sorularVeDogruCevaplari.items():
    cevap = input(soru + "\nCevabınız: ")
    if dogru_cevap.lower() in cevap.lower():
        print("Doğru!")
        puan += 10
    else:
        print("Yanlış!")

print("Toplam Puanınız: ", puan)

