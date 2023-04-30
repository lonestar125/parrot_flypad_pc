import asyncio
import sys
from bleak import BleakClient

async def main(address):
  async with BleakClient(address) as client:
    if (not client.is_connected):
      raise "client not connected"

    services = await client.get_services()

    for service in services:
      print('\nservice', service.handle, service.uuid, service.description)

      characteristics = service.characteristics

      for char in characteristics:
        print('  characteristic', char.handle, char.uuid, char.description, char.properties)

        descriptors = char.descriptors

        for desc in descriptors:
          print('    descriptor', desc)

#FLYPAD_215923, C6:41:41:93:4B:73: FLYPAD_215923
#data: 9e35fa01-4344-44d4-a2e2-0c7f6046878b

if __name__ == "__main__":
  address = "C6:41:41:93:4B:73"
  print('address:', address)
  asyncio.run(main(address))