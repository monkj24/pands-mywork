# messing with histogram

import numpy as np
import matplotlib.pyplot as plt
'''
np.random.seed(1)   #for see the same random data, 
#without that code  histogram when runing again and again will be different

normData = np.random.normal(size=10000)

plt.hist(normData)
plt.show()
'''

fruit = np.array(['Apples', 'Orange', 'Bannana'])
numbers = np.array([23,77,500])

plt.pie(numbers, labels = fruit)
plt.legend()
plt.show()
