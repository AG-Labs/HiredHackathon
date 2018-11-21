#11: Code a function/method that takes an array of numbers and returns 
#the second lowest and second greatest numbers respectively, separated 
#by a space. For example: if arr contains [7, 7, 12, 98, 106] the output 
#should be 12 98

def myFunc(inArr):
	print(inArr)
	#converting to a set removes duplication, reconversion 
	#back into a list allows for sorting operation
	setConverted = set(inArr)
	shortenedList = list(setConverted)
	print(shortenedList)
	shortenedList.sort()
	print(shortenedList)

	#identify length of list to print 2nd and 2nd from last entry 
	myLength = len(shortenedList)
	print("\n\n\nthe result is ")
	print(shortenedList[1], shortenedList[myLength-2])


inputArr = [7, 7,7,100,7,7, 12, 98, 106]
myFunc(inputArr)
