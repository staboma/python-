def sınavı_başlat(sorular):
    puan = 0
    for soru_id, (soru, dogru_cevap) in sorular.items():
        print(soru)
        cevap = input("Cevabınızı girin: ").strip().lower()
        if cevap == dogru_cevap:
            puan += 1
    return puan

def main():
    sorular = {
        1: ("Hangi renk trafik lambasının anlamı durdur? ", "kırmızı"),
        2: ("Kaç tane gün vardır?", "7"),
        
    }

    print("Sınav başlıyor!")
    puan = sınavı_başlat(sorular)
    print(f"Sınavı bitirdiniz! Aldığınız puan: {puan}/{len(sorular)}")

if __name__ == "__main__":
    main()
