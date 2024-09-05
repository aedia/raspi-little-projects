from gpiozero import DigitalInputDevice
from gpiozero import Button
from gpiozero import LED
from time import sleep

rain_power_fake_led = LED(18)
# initialize the sensor as a digital input device
rain_sensor = DigitalInputDevice(17)
button = Button(22)
q2_beepy_fake_led = LED(27)
detection_count = 0

def makebeeps():
	q2_beepy_fake_led.on()
	sleep(1)
	q2_beepy_fake_led.off()

try:

	while True:
		rain_power_fake_led.on()
		if rain_sensor.is_active: #check if it is active (no rain)
			print("No rain detected.")
			detection_count = 0
		else:
			print("Rain detected!")
			#if rain was not detected recently then make a beep
			#the first time we detect it again
			if detection_count == 0:  
				makebeeps()
			if button.is_pressed:
				print("Beep beep! It's raining!")
				#also make the snap circuit beep
				makebeeps()
			detection_count += 1

		sleep(1)
		print("Hi! You can press CTRL+C to stop.")
		print("Hold the button to hear a beep if it's raining!")
		#print("Press the button to check the rain again.")
		#button.wait_for_press()
		#if  button.is_pressed:
		#	print("Yay, button was pressed!")
		#else:
		#	print("Aw, you were not pressing the button when I checked.")

except KeyboardInterrupt:
	print("See ya later!")
