# This is a complete solution to Project Euler problem 587 (https://projecteuler.net/problem=588).

from math import sin
from math import cos
from math import pi

totalArea = 1-0.25*pi # the total area of the L-section.

def f(theta):
    """
    returns the area corresponding to the angle theta.
    """
    x,y = 1-sin(theta),1-cos(theta)
    return 0.5*x*y + (1-x)*y + 0.5*(1-x)*(1-y) - 0.5*theta

def getTheta(target):
    """
    uses the bisection technique to returns an (approximate) value for theta,
    such that f(theta) is an approximately equal to target.
    """
    a,b = 0,1
    while b-a>0.1**8:
        c = 0.5*(a+b)
        if f(c)>target:
            b=c
        else:
            a=c
    return 0.5*(a+b)

def main(r):
    """
    returns the least integer n, for which the concave triangle occupies
    less than r of the total area of the L-section.
    """
    theta = getTheta(r*totalArea)
    x = 1-sin(theta)
    y = 1-cos(theta)
    return int(x/y)+1

# this simply checks that main(0.1) evaluates correctly (it should be 15).
print(main(0.1))

# Problem 587 requires us to compute main(0.001).
print(main(0.001))
