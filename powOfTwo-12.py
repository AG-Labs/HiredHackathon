#12: Code a function/method that takes an int and returns
#true if it's a power of two. For example if the input is 16
#then your program should return the true but if the input
#is 22 then the output should be false

def main():
    testInt = 8
    testInt2 = 10.5
    testInt3 = float(10)
    testInt4 = 23457
    testInt5 = 2 ** 395

    print(powOfTwo(testInt5)) 
    
def powOfTwo(inNumber) :
    #if number is not an int check that it is a whole number
    if type (inNumber) != int:
        if int(inNumber) == inNumber:
            print("float is whole number")
            #if binary representation only has a single 1 then it is a positive power of two
            BinRep = bin(int(inNumber))
            if BinRep.count("1") == 1:
                return True
            else:
                return False
        else: 
            return False
    else:
        BinRep = bin(inNumber)
        if BinRep.count("1") == 1:
            return True
        else:
            return False

if __name__ == "__main__": main()
