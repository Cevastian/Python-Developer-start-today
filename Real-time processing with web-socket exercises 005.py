# Real-time processing exercises with web-socket 005

import asyncio

async def make_americano():
    print("Americano making start!")
    await asyncio.sleep(3)
    print("Americano is made!")
    return "Americano"

async def make_cafelatte():
    print("Cafe Latte making start!")
    await asyncio.sleep(5)
    print("Cafe Latte is made!")
    return "Cafe Latte"

async def main():
    coroute1 = make_americano()
    coroute2 = make_cafelatte()
    result = await asyncio.gather(
        coroute1,
        coroute2
    )
    print(result)
    
print("Main start!")
asyncio.run(main())
print("Main end!")