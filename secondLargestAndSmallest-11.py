#11: Code a function/method that takes an array of numbers and returns 
#the second lowest and second greatest numbers respectively, separated 
#by a space. For example: if arr contains [7, 7, 12, 98, 106] the output 
#should be 12 98

def my_func(in_arr):
	print(in_arr)
	#converting to a set removes duplication, reconversion 
	#back into a list allows for sorting operation
	set_converted = set(in_arr)
	shortened_list = list(set_converted)
	print(shortened_list)
	shortened_list.sort()
	print(shortened_list)

	#identify length of list to print 2nd and 2nd from last entry 
	my_length = len(shortened_list)
	print("\n\n\nthe result is ")
	print(shortened_list[1], shortened_list[my_length-2])


input_arr = [7, 7,7,100,7,7, 12, 98, 106]
my_func(input_arr)
