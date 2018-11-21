#10: Code a function/method that takes a str parameter/argument 
#and return true if there is an equal number of e's and o's, otherwise 
#return false. Ex: input = method output = true (1 o & 1 e)import string

import re #import regex

def eando(inSentence):
	tempSentence = inSentence.lower()
	#regex for character matches negated set and match one or more instances
	es = re.sub('[^e]+', '', tempSentence)
	os = re.sub('[^o]+', '', tempSentence)

	print("equal numbers of e's and o's" if len(es) == len(os) else "unequal numbers of e's and o's")

testString = "this has 5 e and 5 o eeee oooo"
testString2 = "this is unequal"

eando(testString)