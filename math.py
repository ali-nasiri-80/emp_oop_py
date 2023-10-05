import math as m
class math:
    staticmethod
    def isOdd_even(number):
        if number % 2 == 0:
            print("\nnumber is even")
        else: print("\nnumber is ood")
        
    staticmethod
    def issquare(number):
        sq= m.sqrt(number) 
        if sq * sq == number:
            print("\nis square.")
        else: print("\nis not square.")
        
    staticmethod
    def isperfect(number):
        sum= 0
        for i in range(1,number-1):
            if number % i==0:
                sum +=i
        if sum == number:
            print("\nis perfect.")
        else:
            print("\nis not perfect.")
                   
    staticmethod
    def isprimary(number):
        count = 0
        for i in range(2,number):
            if number % i * i==0:
                count +=1
             
        if(count > 0):
            print("\nis not primary")
        else: 
            print("\nis primary.")

number = int(input("\nEnter the number:"))
math.isOdd_even(number)
math.isperfect(number)
math.issquare(number)
math.isprimary(number)


