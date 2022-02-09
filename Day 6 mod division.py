#Day 7 Assignment by Krish Sharma, email: ksysknp@gmail.com


def mod_div(fun):
	def deno(a, b):
		if a < b :
			a, b = b, a
		return fun(a, b)
	return deno
	
@mod_div
def div(a, b):
	return  a // b
    
a, b = (int(i) for i in input("Enter any two Numbers: ").split())
print ("the answer is:", div(a, b))