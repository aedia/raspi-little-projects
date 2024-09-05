from gpiozero import DigitalInputDevice
from gpiozero import Button
from gpiozero import LED
from time import sleep

# initialize the sensor as a digital input device
sound_sensor = DigitalInputDevice(16)
q2_fake_led = LED(20)

try:

	while True:
		if sound_sensor.is_active: #check if it is active (yes sound)
			print("Sound detected!")
			q2_fake_led.on()
			sleep(1)
			q2_fake_led.off()
			print("Tubbs Radio time!")
			sleep(25)
		else:
			print("Nope, no sound detected!")
		sleep(1)
		print("Hi! You can press CTRL+C to stop.")

except KeyboardInterrupt:
	print(" Later, alligator!")
