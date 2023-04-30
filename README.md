# parrot_flypad_pc
Use the parrot flypad (BLE) as a controller for pc, using python, bleak and vgamepad

required packages:
```
pip install bleak
pip install vgamepad
```
(note: installing vgamepad will also install the ViGEm drivers)

# Usage
Turn on flypad and run get_devices.py, this will output a list of BLE devices, once you have found your flypad in the list, copy its address and paste it at the bottom of the read_inputs.py file ```address = "XX:XX:XX:XX:XX:XX```. Make sure the flypad is on and that the LED is blinking green, run read_inputs.py, once connected the flypad LED will turn a solid green and everything should be working.

So far, it seems that all flypads share the same service and characteristics ids, though if that is not the case you can use the get_device_info.py with your flypad address in order to get a list of services and their characteristics.

# Not Implemented:
bumpers, triggers, stick press button, middle flight button
These have not been implemented as I do not have a purpose for them. 
Implementing should be fairly straightforward as it's mainly just figuring out the required bytes and mapping.
