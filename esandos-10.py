#10: Code a function/method that takes a str parameter/argument 
#and return true if there is an equal number of e's and o's, otherwise 
#return false. Ex: input = method output = true (1 o & 1 e)import string

#import regex
import re 

def eando(in_sentence):
	temp_sentence = in_sentence.lower()
	#regex for character matches negated set and match one or more instances
	es = re.sub('[^e]+', '', temp_sentence)
	os = re.sub('[^o]+', '', temp_sentence)

	print("equal numbers of e's and o's" if len(es) == len(os) else "unequal numbers of e's and o's")

test_string = "this has 5 e and 5 o eeee oooo"
test_string2 = "this is unequal"

eando(test_string)