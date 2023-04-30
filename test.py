"""
import asyncio
from bleak import BleakScanner

async def main():
    devices = await BleakScanner.discover()
    for d in devices:
        print(d)

asyncio.run(main())
"""
"""
import asyncio
from bleak import BleakClient

address = "C6:41:41:93:4B:73"
MODEL_NBR_UUID = "00002a24-0000-1000-8000-00805f9b34fb"

async def main(address):
    async with BleakClient(address) as client:
        model_number = await client.read_gatt_char(MODEL_NBR_UUID)
        print("Model Number: {0}".format("".join(map(chr, model_number))))

asyncio.run(main(address))
"""
#FLYPAD_215923
import asyncio
from bleak import BleakScanner

async def main():
  async with BleakScanner() as scanner:
      devices = await scanner.discover()
      for d in devices:
          print(d)

if __name__ == "__main__":
    asyncio.run(main())