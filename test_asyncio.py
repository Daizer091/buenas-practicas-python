import asyncio

async def fetch_data():
    print("Inicio")
    await asyncio.sleep(2)
    print("Fin")

async def main():
    await asyncio.gather(fetch_data(), fetch_data())

asyncio.run(main())