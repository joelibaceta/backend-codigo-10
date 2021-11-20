from asyncio.streams import start_server
import websockets
import asyncio

col_sockets = []

async def handler(websocket):

    col_sockets.append(websocket)

    async for message in websocket: 
        reply = f"Data recibida: {message}"
        #await websocket.send(reply)
        websockets.broadcast(col_sockets, reply)

async def main():
    async with websockets.serve(handler, "localhost", 7000):
        await asyncio.Future()

asyncio.run(main())