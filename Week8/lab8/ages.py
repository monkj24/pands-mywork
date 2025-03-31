# Makes a list called ages that has the same number random
# values as salaries (range :21 to 65)
# Make scatter plot

import numpy as np
import matplotlib.pyplot as plt

minSalary = 20000
maxSalary = 80000
numberOfEntries = 100

np.random.seed(1)
salaries = np.random.randint(minSalary, maxSalary, numberOfEntries)
ages = np.random.randint(low = 21, high= 65, size = numberOfEntries)
# Prefer absolute values set at the top (?)

plt.scatter(ages, salaries, label = "Salaries") # this will be a random
#plt.show()

# add x squared
xpoints = np.sort(ages)
ypoints = xpoints * xpoints  # multiply each entry by itself

plt.plot(xpoints, ypoints, color='r', label = "x squared")

plt.title("random plot") 
plt.xlabel("Age") 
plt.ylabel("Salary") 
plt.legend() 

#plt.show()

plt.savefig('prettier-plot.png')