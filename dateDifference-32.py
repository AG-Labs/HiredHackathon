#32: Write a program that returns the number of days until the date 
#entered (accept dates formatted as DD/MM/YYYY). It should be run from 
#the command line and ask the user for input
import sys
import re
import datetime 

def main():
	today = datetime.date.today()
	if len(sys.argv) != 1:
		input_value = sys.argv[1]
		reduced_str = re.sub('[/]+','', input_value)

		in_day = int(str(reduced_str)[0:2])
		in_month = str(reduced_str)[2:4]
		in_month = int(in_month.lstrip("0"))
		in_year = int(str(reduced_str)[4:])
	try:
		input_date = datetime.date(in_year,in_month,in_day)
	except:
	    print("Invalid date entered")
	delta = input_date - today

	if delta < datetime.timedelta(days = 0):
		print("the date is in the past")
	else:
		print("the date is ",delta.days, " from today")


if __name__ == '__main__': main()