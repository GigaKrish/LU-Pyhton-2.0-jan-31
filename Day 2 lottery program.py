#Day 2 Assignment by Krish Sharma, email: ksysknp@gmail.com
#Lottery program, declare winner by index value of a word


enter = [string for string in input ("Enter a phrase or a letter: ").lower()]

new = []
for i in enter:         #a block of code to remove spaces
    if (i == " " or i == ""):
        new.append(i)
        new.pop()
    else:
        new.append(i)

freq = [0] * 26         #Sir I used your code too but did some tweaks and correction
for j in new:
  freq[ord(j) - 97] += 1        # lowercase alphabets - ASCII code: 97 to 122

result = freq.index(max(freq))
#fully functional code as per question asked in assignment 

if (result == 7 or result == 4 or result == 2 or result == 14 or result == 3): #index values of h,e,c,o and d 
    print ("Congratulations you've won the lottery!!! \n\
You're a lucky winner!!")
else: 
    print ("Uh oh... Better luck next time. \n\
Thanks for your participation!")