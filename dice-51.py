#51: Build a project which simulates throwing a number of different dice 
#n times and provides the outcome

import random
def roll_dice_x(dice_throws):
	output = []

	for count in range(0, dice_throws):
		dice_throw = random.randint(0, 5)
		dice_throw += 1
		output.append(dice_throw)
	return output

result = roll_dice_x(10)

print("your results are ", result)


