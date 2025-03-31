# the function that plots a function y=x2

import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array(range(1,101))
ypoints = xpoints * xpoints # multiply each entry by itself

plt.plot(xpoints, ypoints)
plt.show()

# add x squared
xpoints = np.array(range(1,101))
ypoints = xpoints * xpoints  # multiply each entry by itself

plt.plot(xpoints, ypoints, color='r')
plt.show()