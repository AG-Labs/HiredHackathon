#17: Insert dashes ('-') between each two odd numbers in str. For 
#example: if str is 454793 the output should be 4547-9-3.

import re

def main():
	testString = "454793"
	insertOddDash(testString)


def insertOddDash(inString):
	('[13579]')
	print(inString)
	reducedString = re.sub([13579][13579], '\10', inString)
	print(reducedString)




if __name__ == '__main__': main()