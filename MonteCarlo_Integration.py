import numpy as np
import sys
import matplotlib.pyplot as plt
from Random import Random 

random = Random()

sys.path.append(".")

#default interval
xmin = 0
xmax = 40
#default number of steps
steps = 10000

if __name__ == "__main__":
    
    if '-Xmin' in sys.argv:
        p = sys.argv.index('-Xmin')
        xmin = float(sys.argv[p+1])
    if '-Xmax' in sys.argv:
        p = sys.argv.index('-Xmax')
        xmax = float(sys.argv[p+1])
    if '-Steps' in sys.argv:
        p = sys.argv.index('-Steps')
        steps = int(sys.argv[p+1])
        
#function to be integrated
def f(x):
    return(x*np.exp(-x))

#analytically integrated version of the function
def integral_f(x):
    return(-np.exp(-x)-x*np.exp(-x))

#counts the number of random selections inside the integral
inside = 0
count = 0
for i in range(steps):
    x = xmax * random.rand()
    y = xmax * random.rand()
    if f(x) >= y:
        inside += 1
    count += 1
#fraction inside integral
frac = inside/count
print(frac)
#calculated area
monte_int = frac * xmax**2

print('monte carlo integral:',monte_int)

#analytic solution
actual_integral = integral_f(xmax)-integral_f(xmin)

print('actual integral:',actual_integral)

