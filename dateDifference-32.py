#32: Write a program that returns the number of days until the date 
#entered (accept dates formatted as DD/MM/YYYY). It should be run from 
#the command line and ask the user for input
import sys
import re
import datetime 

def main():
	today = datetime.date.today()
	if len(sys.argv) != 1:
		inputValue = sys.argv[1]
		reducedStr = re.sub('[/]+','', inputValue)

		inDay = int(str(reducedStr)[0:2])
		inMonth = str(reducedStr)[2:4]
		inMonth = int(inMonth.lstrip("0"))
		inYear = int(str(reducedStr)[4:])
	try:
		inputDate = datetime.date(inYear,inMonth,inDay)
	except:
	    print("Invalid date entered")
	delta = inputDate - today

	if delta < datetime.timedelta(days = 0):
		print("the date is in the past")
	else:
		print("the date is ",delta.days, " from today")


if __name__ == '__main__': main()