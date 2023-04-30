import asyncio
import sys
from bleak import BleakClient

INPUT_ID = "9e35fa01-4344-44d4-a2e2-0c7f6046878b"

def print_data(handle, data):
    #converted = bytes(data)
    name = bytearray.decode(data, 'windows-1252')


    print(name)

async def main(address):
  async with BleakClient(address) as client:
    if (not client.is_connected):
      raise "client not connected"

    services = await client.get_services()
    #name_bytes = await client.read_gatt_char(FIRST_NAME_ID)
    #name = bytearray.decode(name_bytes)
    #print('name', name)

    #test = None
    await client.start_notify(INPUT_ID, print_data)
    await asyncio.sleep(10)
    await client.stop_notify(INPUT_ID)

#C6:41:41:93:4B:73: FLYPAD_215923
#data: 9e35fa01-4344-44d4-a2e2-0c7f6046878b, 9e35fa01-4344-44d4-a2e2-0c7f6046878b

if __name__ == "__main__":
  address = "C6:41:41:93:4B:73"
  print('address:', address)
  asyncio.run(main(address))