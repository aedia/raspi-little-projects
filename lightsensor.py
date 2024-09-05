from gpiozero import LED
from time import sleep

q2_fake_led = LED(27) 

try:
	while True:
		q2_fake_led.on()
		sleep(10)
		q2_fake_led.off()
		sleep(2)
		print("Hello! I'm turning on the q2 for 10 seconds, then pausing for two. You can press CTRL+C to exit.")

except KeyboardInterrupt:
	print("Bye bye for now!")
