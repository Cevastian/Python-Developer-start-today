# Real-time processing exercises with web-socket 008

import websockets
import asyncio

async def bithumb_ws_client():
    uri = "wss://pubwss.bithumb.com/pub/ws"
    
    async with websockets.connect(uri) as websocket:
        greeting = await websocket.recv()
        print(greeting)
        
async def main():
    await bithumb_ws_client()
    
asyncio.run(main())

f = open('C:\\Users\\chois\\Desktop\\PythonProject\\Codes\\Coding Exercise with Cryptocurrency Auto Trading\\file_write_exercise 001.txt', 'w')
f.write("Hi Sebastian!")
f.close()

with open('C:\\Users\\chois\\Desktop\\PythonProject\\Codes\\Coding Exercise with Cryptocurrency Auto Trading\\file_write_exercise 001.txt', 'w') as f
f.write("Hello, world!")
f.write("Hello Sebastian!")