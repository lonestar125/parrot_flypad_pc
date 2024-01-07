import asyncio
import vgamepad as vg #pip isntall vgamepad
from bleak import BleakClient #pip install bleak

INPUT_ID = "9e35fa01-4344-44d4-a2e2-0c7f6046878b" #this is the id of the characteristic that we want to read the inputs from

def print_data(handle, data):
	global current_state
	converted = bytes(data)
	#name = bytearray.decode(data, 'utf-16')
	button = bytes(data[1:2])
	extrabutton = bytes(data[2:3])
	#print(button)

	# Print the raw data
	# print("Raw Data:", converted)

    # Print the button value
	# print("Button Value:", extrabutton)

	if button == b'\x02':
		#print('button 1')
		current_state["1"] = True
		gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_X)
		#gamepad.update()

	elif button == b'\x04':
		#print('button 2')
		current_state["2"] = True
		gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_Y)
		#gamepad.update()

	elif button == b'\x08':
		#print('button B')
		current_state["b"] = True
		gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_B)
		#gamepad.update()

	elif button == b'\x10':
		#print('button A')
		current_state["a"] = True
		gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
		#gamepad.update()
    
	elif button == b'\x20':
		# print('R1')
		current_state["r1"] = True
		gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_SHOULDER)

	elif button == b'\x40':
		# print('R2')
		current_state["r2"] = True
		gamepad.right_trigger(value=255)
		gamepad.update()

	elif button == b'\x80':
		# print('L1')
		current_state["l1"] = True
		gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_SHOULDER)

	elif button == b'\x01':
		# print('take off')
		current_state["takeoff"] = True
		gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_START)

	elif extrabutton == b'\x02':
		# print('L3')
		current_state["l3"] = True
		gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_THUMB)

	elif extrabutton == b'\x01':
		# print('L2')
		current_state["l2"] = True
		gamepad.left_trigger(value=255)

	elif extrabutton == b'\x04':
		# print('R3')
		current_state["r3"] = True
		gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_THUMB)

	elif button == b'\x00':
		if current_state["a"] == True:
			current_state["a"] = False
			#print("release A")
			gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
			#gamepad.update()
		elif current_state["b"] == True:
			current_state["b"] = False
			#print("release B")
			gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_B)
			#gamepad.update()
		elif current_state["1"] == True:
			current_state["1"] = False
			#print("release 1")
			gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_X)
			#gamepad.update()
		elif current_state["2"] == True:
			current_state["2"] = False
			#print("release 2")
			gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_Y)
			#gamepad.update()
		elif current_state["l3"]:
			current_state["l3"] = False
			gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_THUMB)
		elif current_state["r3"]:
			current_state["r3"] = False
			gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_THUMB)
		elif current_state["l2"]:
			current_state["l2"] = False
			gamepad.left_trigger(value=0)
		elif current_state["r2"]:
			current_state["r2"] = False
			gamepad.right_trigger(value=0)
			gamepad.update()
		elif current_state["l1"]:
			current_state["l1"] = False
			gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_SHOULDER)
		elif current_state["r1"]:
			current_state["r1"] = False
			gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_SHOULDER)
		elif current_state["takeoff"]:
			current_state["takeoff"] = False
			gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_START)
	
	right_x = bytes(data[3:4])
	right_y = bytes(data[4:5])
	left_x = bytes(data[5:6])
	left_y = bytes(data[6:7])

	f_rx = (ord(right_x)-128)/128
	f_ry = -(ord(right_y)-128)/128
	f_lx = (ord(left_x)-128)/128
	"""
	if ord(left_y) >= 120:
		f_ly = float(1.0) # 0 throttle
	else:
		f_ly = (ord(left_y)-128)/64 + 1 # maps top part of stick to throttle between 1 and -1 
	"""
	f_ly = -(ord(left_y)-128)/128
	


	gamepad.left_joystick_float(x_value_float=f_lx, y_value_float=f_ly)  # value between 0 and 255
	gamepad.right_joystick_float(x_value_float=f_rx, y_value_float=f_ry)  # value between 0 and 255
	gamepad.update()
	#print(f"ly: {f_ly}, left_y: {ord(left_y)}")

	#print(button)
	#print(data)

async def main(address):
	async with BleakClient(address) as client:
		if (not client.is_connected):
			raise "client not connected"
		
		services = await client.get_services()

		await client.start_notify(INPUT_ID, print_data)
		await asyncio.sleep(1000000000000) #31688 years, 8 months, 25 days, 1 hour, 46 minutes, 40 seconds
		await client.stop_notify(INPUT_ID)

#C6:41:41:93:4B:73: FLYPAD_215923
#data: 9e35fa01-4344-44d4-a2e2-0c7f6046878b, 9e35fa01-4344-44d4-a2e2-0c7f6046878b

if __name__ == "__main__":
	address = "C6:41:41:93:4B:73" #this is the address of my specific flypad
	global gamepad
	gamepad = vg.VX360Gamepad()
	global current_state
	current_state = {"a": False, "b": False, "1": False, "2": False, "left_x": 0, "left_y": 0, "right_x": 0, "right_y": 0, "l3": False, "r3": False, "l2": 0, "r2": 0, "l1": False, "r1": False, "takeoff": False}
	print('address:', address)
	asyncio.run(main(address))