# PHSX815_Week6

## Numerical_Integration.py

Code evaluates the integral of the function x*exp(-x)

Defaults to interval [0,40] with 10 evaluation points

Change the interval using -Xmin and -Xmax as [Xmin,Xmax]

Change the number of steps using -Steps

Prints out the numerical evaluation using Gauss-Laguerre quadrature and midpoint methods

Prints out comparison to analytic solution over the interval

## Results

Printed output using default settings 

Integral using midpoint method: 0.9700433248804851

Integral using Gauss-Laguerre quadrature: 1.0000000000000000000

Integral using analytic solution: 0.9595723180054871

Difference between midpoint method and analytic: 0.010471006874997912

Difference between Gauss-Laguerre quadrature and analytic: 0.040427681994512854045

## Additional Thoughts

Gauss-Laguerre quadrature takes the integral from [0,infinity], so it is less effective for intervals with a lower Xmax

Gauss-Laguerre method extremely close to actual integral over the default interval, it is a good reference for the actual error of the midpoint method
