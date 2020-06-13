#1: Build a project which changes your keyboard layout to that of 
#another country every 15 keystrokes. You should include at 
#least 5 layouts.

import keyboard


def main():
	keyStrokeCounter = 0
	exitFlag = True
	while exitFlag:
		x = keyboard.is_pressed('a')
		if x:
			print(x)
			keyStrokeCounter += 1
			print(keyStrokeCounter)

		if keyStrokeCounter > 15:
			exitFlag = False

if __name__ == '__main__':
	main()