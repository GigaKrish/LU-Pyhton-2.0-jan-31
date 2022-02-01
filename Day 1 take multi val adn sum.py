#Day 1 (jan 31) Assignment:Take different input values and print thier sum
print ("Enter different numeric values, seprate them with space adn get the sum of it!")
full = [int(i) for i in input('Enter numeric values: ').split()]    #list comprehension to take feed values 
print (f"The sum of given values is : {sum(full)}")   #f string to display data 

#Assignment by Krish Sharma 
#email: ksysknp@gmail.com
