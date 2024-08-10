from gpiozero import DigitalInputDevice
from time import sleep

# initialize the sensor as a digital input device
rain_sensor = DigitalInputDevice(17)

while True:
	if rain_sensor.is_active: #check if it is active (no rain)
		print("No rain detected.")
	else:
		print("Rain detected!")
	sleep(1)
