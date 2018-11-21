#50: Takes in a credit card number from a card 
#vendor (Visa, MasterCard, etc) and validates it 
#to make sure that it is a valid number (look into 
#how credit cards use a checksum).

#I found the checksum maths on https://www.sapling.com/7966257/checksum-credit-card

def creditCardChecker(cardNo):
	#initialise variables for later use
	result = False
	outputCode = [0] * 15 #array of 0's length n
	mySum = 0

	inputLength = len(str(cardNo))

	if inputLength == 16:
		print("valid length")
		#split card number into check sum and first part
		firstPart = str(cardNo)[0:15]
		secondPart = str(cardNo)[15] #confused by this need to check the [] operator on strings
		for i in range(0,len(firstPart)):
			#loop through first part of string
			print("\n")
			print("loop in ", i)
			print("value is ", firstPart[i])
			
			if i%2 == 0:
				#double every 2nd entry starting from 0 and add to outputcode
				print("doubling")
				doubledDigit = int(firstPart[i]) * 2
				print("the doubled vaue is ", doubledDigit)
				#if the double value is two digits add them together to form new number
				if len(str(doubledDigit)) == 2:
					firstDigit = str(doubledDigit)[0]
					secondDigit = str(doubledDigit)[1]
					newDoubleDigit = int(firstDigit) + int(secondDigit)
					print("adding ", newDoubleDigit)
					outputCode[i] = newDoubleDigit
				else:
					outputCode[i] = int(doubledDigit)
					print("adding ", int(doubledDigit))

			else:
				print("adding ",int(firstPart[i]))
				outputCode[i] = int(firstPart[i])
		#sum the entries of the first part and add the checksum
		for j in range(0,15):
			mySum = mySum + int(outputCode[j])

		finalValue = mySum + int(secondPart)
		# if the value is an even multiple of 10 the card number is valid
		finalValue = finalValue / 10
		finalValue = finalValue%2

		if int(finalValue) == 0:
			result = True
	else:
		print("invalid length")
		result = False

	print("\n\n\n\nthis is a valid card number" if result == True else "this isnt a card number")

creditCardChecker(1000000000000000)