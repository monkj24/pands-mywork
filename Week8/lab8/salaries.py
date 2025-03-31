# Program makes a list
# has a 10 random numbers (20000-80000)

import numpy as np
# it is a good idea to have your absolute values set into variables 
# at the begining of your program

minSalary= 20000
maxSalary = 80000
numberOfEntries = 10

np.random.seed(1)
salaries = np.random.randint(minSalary, maxSalary, numberOfEntries)
salariesPlus = salaries + 5000 # this will add 5000 to each value

salariesMult = salaries * 1.05  # add 5% by multiplying by 1.05
print(salariesMult)
# This is a float array, here I conver it to an int array (it does a floor)
newSalaries = salariesMult.astype(int)
print(newSalaries)

'''
print (salaries)
print(salariesPlus)'
'''