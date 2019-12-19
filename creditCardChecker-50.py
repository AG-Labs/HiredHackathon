#50: Takes in a credit card number from a card 
#vendor (Visa, MasterCard, etc) and validates it 
#to make sure that it is a valid number (look into 
#how credit cards use a checksum).

#I found the checksum maths on https://www.sapling.com/7966257/checksum-credit-card

def credit_card_checker(card_no):
	#initialise variables for later use
	result = False
	output_code = [0] * 15 #array of 0's length n
	my_sum = 0

	input_length = len(str(card_no))

	if input_length == 16:
		print("valid length")
		#split card number into check sum and first part
		first_part = str(card_no)[0:15]
		second_part = str(card_no)[15] #confused by this need to check the [] operator on strings
		for i in range(0,len(first_part)):
			#loop through first part of string
			print("\n")
			print("loop in ", i)
			print("value is ", first_part[i])
			
			if i%2 == 0:
				#double every 2nd entry starting from 0 and add to outputcode
				print("doubling")
				doubled_digit = int(first_part[i]) * 2
				print("the doubled vaue is ", doubled_digit)
				#if the double value is two digits add them together to form new number
				if len(str(doubled_digit)) == 2:
					first_digit = str(doubled_digit)[0]
					second_digit = str(doubled_digit)[1]
					new_double_digit = int(first_digit) + int(second_digit)
					print("adding ", new_double_digit)
					output_code[i] = new_double_digit
				else:
					output_code[i] = int(doubled_digit)
					print("adding ", int(doubled_digit))
			else:
				print("adding ",int(first_part[i]))
				output_code[i] = int(first_part[i])
		#sum the entries of the first part and add the checksum
		for j in range(0,15):
			my_sum = my_sum + int(output_code[j])

		final_value = my_sum + int(second_part)
		# if the value is an even multiple of 10 the card number is valid
		final_value = final_value / 10
		final_value = final_value%2

		if int(final_value) == 0:
			result = True
	else:
		print("invalid length")
		result = False

	print("\n\n\n\nthis is a valid card number" if result == True else "this isnt a card number")

credit_card_checker(1000000000000000)