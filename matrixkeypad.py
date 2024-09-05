import time
import digitalio
import board
import adafruit_matrixkeypad

cols = [digitalio.DigitalInOut(x) for x in (board.D13, board.D19, board.D26)]
rows = [digitalio.DigitalInOut(x) for x in (board.D4, board.D27, board.D5, board.D6)]
keys = ((1, 2, 3),
	(4, 5, 6),
	(7, 8, 9),
	('*', 0, '#'))
keypad = adafruit_matrixkeypad.Matrix_Keypad(rows, cols, keys)

try:
	print("Welcome to keypad pressing time!")
	print("You can press CTRL + C to exit any time.")
	print("Try pressing a key on the keypad!")
	while True:
		keys = keypad.pressed_keys
		if keys:
			print("Pressed: ", keys)
		time.sleep(0.1)

except KeyboardInterrupt:
	print(" See ya later, alligator!")
