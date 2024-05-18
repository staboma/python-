import asyncio

async def fetch_data():
    print("Veri çekiliyor...")
    await asyncio.sleep(2)
    print("Veri çekildi.")
    return {"data": 42}

async def main():
    data = await fetch_data()
    print(f"Veri: {data}")

asyncio.run(main())
