import numpy as np
import matplotlib.pyplot as plt
import scipy
from scipy.stats import norm
from fitting_functions import *

data = np.loadtxt("marshmellow_data.csv", delimiter=",", dtype=str)

print(data)

x = data[1:, 0].astype(np.float32)
y = data[1:, 1].astype(np.float32)

print("y = ", y)
print("x = ", x)


params, params_cov = scipy.optimize.curve_fit(linear, x, y)
slope = params[0]
intercept = params[1]


### Exercise 1

print_equation(slope, intercept, "g", "mm")

### The equation of the line is: y =  -0.05261904761904779 mm/g x +  58.21428571428577 mm 



