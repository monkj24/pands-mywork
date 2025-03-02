# generate random 10 numbers from 0 to 100
# pronts them out and prints out the top three

import random
howMany = 10
topHowMany = 3
rangeFrom = 0
rangeTo = 100

numbers = []

for i in range(0,howMany):
    numbers.append(random.randint(rangeFrom,rangeTo))
print (f"{howMany} random numbers\t {numbers}")

#I am keeping the original list maybe I don`t need to 
topOnes = numbers.copy()

topOnes.sort(reverse = True)
print ("The top {topHowMany} are \t\t {topOnes[0:topHowMany]}")