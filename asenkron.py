import asyncio

async def uzun_islem():
    print("Uzun işlem başlıyor...")
    await asyncio.sleep(2)
    print("Uzun işlem tamamlandı!")
    return "Sonuç"

async def main():
    sonuc = await uzun_islem()
    print(sonuc)

asyncio.run(main())
