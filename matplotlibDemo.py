import matplotlib.pyplot as mpl
import numpy as np

x = np.linspace(1,20,100) # create list of evenly-spaced numbers over the range

mpl.plot(x, np.sin(x)) # Plot the sine of each  point

mpl.show()
