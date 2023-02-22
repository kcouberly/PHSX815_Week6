import numpy as np
import sys
import matplotlib.pyplot as plt
from sympy import *

sys.path.append(".")

#default interval
xmin = 0
xmax = 40
#default number of steps
steps = 10

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

#function that obtains the x_i, w_i values for a Gauss-Laguerre quadrature with n points
def lag_weights_roots(n):
    x = Symbol("x")
    roots = Poly(laguerre(n, x)).all_roots()
    x_i = [rt.evalf(20) for rt in roots]
    w_i = [(rt / ((n + 1) * laguerre(n + 1, rt)) ** 2).evalf(20) for rt in roots]
    return x_i, w_i

roots = lag_weights_roots(steps)

#numerical approximation using Gauss-Laguerre quadrature
gauss_integral = 0
for y in range(steps):
    #weight w_i * g(x_i) summed where g(x)=x non exponential term
    gauss_integral += roots[1][y] * roots[0][y]

#step size (midpoint method)
stepsize = (xmax-xmin)/steps

#midpoint method numerical approximation
midpt_integral = 0
x_value = xmin
for x in range(steps):
    x_value += stepsize/2
    y_value = f(x_value)
    area = y_value * stepsize
    x_value += stepsize/2
    midpt_integral += area

#analytic solution
actual_integral = integral_f(xmax)-integral_f(xmin)
    
print('Integral using midpoint method:',midpt_integral)
print('')
print('Integral using Gauss-Laguerre quadrature:',gauss_integral)
print('')
print('Integral using analytic solution:',actual_integral)
print('')

#difference between numerical integrals and analytic
print('Difference between midpoint method and analytic:',midpt_integral-actual_integral)
print('')
print('Difference between Gauss-Laguerre quadrature and analytic:',gauss_integral-actual_integral)
    