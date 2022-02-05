#Day 3 Assignment by Krish Sharma, email: ksysknp@gmail.com
#Day 3 Assignment
#From a dictionary, print the Key whose Value is maximum in the dictionary.

string = str(input ("Enter a phrase or a letter: "))
newStr = string.lower()

nDct = {}

for i in newStr:
  nDct[i] = nDct.get(i, 0) + 1

result = max(nDct, key = nDct.get)
print(f'Maximum occurence is of the letter  {result}  here.')