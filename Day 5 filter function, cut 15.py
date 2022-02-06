#Day 5 Assignment by Krish Sharma, email: ksysknp@gmail.com
#Assignment: Use filter function to filter out the elements from a list that are divisible by 3 & 5

def fun(n):
  return n % 3 == 0 and n % 5 == 0

#li = list(range(1, 101))           #script to test program in different way

li = [int(i) for i in input('Enter some numeric values (seperate with spaces): ').split()]
#list comprehension for user inputs

print ("Filtered list is: ", list(filter (fun, li)) )