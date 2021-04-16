import math

def divisor(number):

    for i in range (1, int(math.sqrt(number)+1)):
        if (number % i == 0):
            if number / i != i:
                    print(i)
                    print(number / i)
            else:
                print(i)
   

divisor(36)   
