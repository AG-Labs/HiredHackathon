#34: Code a function/method that takes an array of numbers and return the 
#number that appears most frequently (the mode). For example: if arr contains 
#[10, 4, 5, 2, 4] the output should be 4. If there is more than one mode return 
#the one that appeared in the array first (ie. [5, 10, 10, 6, 5] should 
#return 5 because it appeared first). If the array is empty return -1.

def main():
	testInt = [10, 4, 5, 2, 4]
	testInt2 = [5, 10, 10, 10, 6, 5]
	findMode(testInt2)

def findMode(inInteger):
	print(inInteger)
	greatestRepeat = 0
	greatestRepeated = ''
	for entry in inInteger:
		temparyNumber = entry
		counter = 0
		for entry in inInteger:
			if entry == temparyNumber:
				counter += 1
		if counter > greatestRepeat:
			greatestRepeat = counter
			greatestRepeated = str(temparyNumber)
	print("the greatest repeated value is ", greatestRepeated, " repeated ", greatestRepeat, " times")

if __name__ == '__main__': main()