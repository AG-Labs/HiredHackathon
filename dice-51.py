#51: Build a project which simulates throwing a number of different dice 
#n times and provides the outcome

import random
def rollDiceX(diceThrows):
	output = []

	for count in range(0, diceThrows):
		diceThrow = random.randint(0, 5)
		diceThrow += 1
		output.append(diceThrow)
	return output

result = rollDiceX(10)

print("your results are ", result)


