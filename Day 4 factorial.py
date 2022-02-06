#Day 4 Assignment by Krish Sharma, email: ksysknp@gmail.com
##Assignment : Factorial of a number by defing a function to call for it 

n = int(input("Input a number to get it's factiorial : "))
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
print (f"Factorial of {n} is {factorial(n)}")