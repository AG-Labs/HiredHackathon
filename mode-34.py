#34: Code a function/method that takes an array of numbers and return the 
#number that appears most frequently (the mode). For example: if arr contains 
#[10, 4, 5, 2, 4] the output should be 4. If there is more than one mode return 
#the one that appeared in the array first (ie. [5, 10, 10, 6, 5] should 
#return 5 because it appeared first). If the array is empty return -1.

def main():
	test_int = [10, 4, 5, 2, 4]
	test_int2 = [5, 10, 10, 10, 6, 5]
	findMode(test_int2)

def findMode(in_integer):
	print(in_integer)
	greatest_repeat = 0
	greatest_repeated = ''
	for entry in in_integer:
		tempary_number = entry
		counter = 0
		for entry in in_integer:
			if entry == tempary_number:
				counter += 1
		if counter > greatest_repeat:
			greatest_repeat = counter
			greatest_repeated = str(tempary_number)
	print("the greatest repeated value is ", greatest_repeated, " repeated ", greatest_repeat, " times")

if __name__ == '__main__': main()