from gpiozero import DistanceSensor
from time import sleep

sensor = DistanceSensor(23, 24)

try:

	while True:
		print("Distance to nearest object is", sensor.distance, "m")
		sleep(1)

except KeyboardInterrupt:
	print(" Ta ta for now!")
