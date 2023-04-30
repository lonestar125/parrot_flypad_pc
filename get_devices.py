import asyncio
from bleak import BleakScanner

async def main():
  async with BleakScanner() as scanner:
      devices = await scanner.discover()
      for d in devices:
          print(d)

if __name__ == "__main__":
    asyncio.run(main())