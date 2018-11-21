#35: Code a function/method that takes a sentence as input and return 
#the first word with the greatest number of repeated letters. For 
#example: "Today, is the greatest day ever!" should return greatest 
#because it has 2 e's (and 2 t's) and it comes before ever which also has 
#2 e's. If there are no words with repeating letters return -1.

import string

def mostFrequentLetter(inSentence):
	#initialise output variables convert sentence to lowercase and 
	#split into an array of constituent words
	output = ""
	outputletter = ""
	greatestRepeat = 0
	tempSentence = inSentence.lower()
	words = inSentence.split()
	

	for word in words:
		greatestInnerRepeat = 0 #identify most frequent letter in word
		for letter in string.ascii_lowercase:
			#loop through letters in alphabet and compare to word
			tempRepeat = 0
			for aLetter in word:
				if letter == aLetter:
					tempRepeat += 1
			#if instances of letter is greater than previously 
			#stored and letter is repeated then overwrite and store letter
			if (tempRepeat > greatestInnerRepeat and tempRepeat != 1):
				greatestInnerRepeat = tempRepeat
				outputletter = letter
		#if the most frequent letter in word is greater than previously stored
		#then store word
		if (greatestInnerRepeat > greatestRepeat and greatestInnerRepeat != 1):
			greatestRepeat = greatestInnerRepeat
			output = word
	#if no repeats print -1
	if output == "":
		print(-1)
	else:
		print("the most frequent letter is", outputletter, "in the word ", output)


testString = "Today, is the greatest day ever!"
testString2 = "this has no doubles"
mostFrequentLetter(testString)