import time

def zaman_olc(fonksiyon):
    def sarmal(*args, **kwargs):
        baslangic = time.time()
        sonuc = fonksiyon(*args, **kwargs)
        bitis = time.time()
        print(f"Fonksiyon {fonksiyon.__name__} {bitis - baslangic:.4f} saniyede çalıştı.")
        return sonuc
    return sarmal

@zaman_olc
def uzun_islem():
    time.sleep(2)
    return "İşlem tamamlandı!"

print(uzun_islem())
