#35: Code a function/method that takes a sentence as input and return 
#the first word with the greatest number of repeated letters. For 
#example: "Today, is the greatest day ever!" should return greatest 
#because it has 2 e's (and 2 t's) and it comes before ever which also has 
#2 e's. If there are no words with repeating letters return -1.

import string

def most_frequent_letter(in_sentence):
	#initialise output variables convert sentence to lowercase and 
	#split into an array of constituent words
	output = ""
	output_letter = ""
	greatest_repeat = 0
	temp_sentence = in_sentence.lower()
	words = in_sentence.split()
	

	for word in words:
		greatest_inner_repeat = 0 #identify most frequent letter in word
		for letter in string.ascii_lowercase:
			#loop through letters in alphabet and compare to word
			temp_repeat = 0
			for a_letter in word:
				if letter == a_letter:
					temp_repeat += 1
			#if instances of letter is greater than previously 
			#stored and letter is repeated then overwrite and store letter
			if (temp_repeat > greatest_inner_repeat and temp_repeat != 1):
				greatest_inner_repeat = temp_repeat
				output_letter = letter
		#if the most frequent letter in word is greater than previously stored
		#then store word
		if (greatest_inner_repeat > greatest_repeat and greatest_inner_repeat != 1):
			greatest_repeat = greatest_inner_repeat
			output = word
	#if no repeats print -1
	if output == "":
		print(-1)
	else:
		print("the most frequent letter is", output_letter, "in the word ", output)


test_string = "Today, is the greatest day ever!"
test_string2 = "this has no doubles"
most_frequent_letter(test_string)