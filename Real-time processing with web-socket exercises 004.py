# Real-time processing exercises with web-socket 004

import asyncio

async def make_americano():
    print("Americano making start!")
    await asyncio.sleep(3)
    print("Americano is made!")

async def make_cafelatte():
    print("Cafe Latte making start!")
    await asyncio.sleep(5)
    print("Cafe Latte is made!")

async def main():
    coroute1 = make_americano()
    coroute2 = make_cafelatte()
    await asyncio.gather(
        coroute1,
        coroute2
    )

print ("Main function start!")
asyncio.run(main())
print("Main function end!")