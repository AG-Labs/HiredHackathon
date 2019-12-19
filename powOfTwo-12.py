#12: Code a function/method that takes an int and returns
#true if it's a power of two. For example if the input is 16
#then your program should return the true but if the input
#is 22 then the output should be false

def main():
    test_int = 8
    test_int2 = 10.5
    test_int3 = float(10)
    test_int4 = 23457
    test_int5 = 2 ** 395

    print(pow_of_two(test_int5)) 
    
def pow_of_two(in_number) :
    #if number is not an int check that it is a whole number
    if type (in_number) != int:
        if int(in_number) == in_number:
            print("float is whole number")
            #if binary representation only has a single 1 then it is a positive power of two
            bin_rep = bin(int(in_number))
            if bin_rep.count("1") == 1:
                return True
            else:
                return False
        else: 
            return False
    else:
        bin_rep = bin(in_number)
        if bin_rep.count("1") == 1:
            return True
        else:
            return False

if __name__ == "__main__": main()
