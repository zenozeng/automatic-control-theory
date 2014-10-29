import matplotlib.pyplot as pyplot
import control
import sympy
import numpy

S = sympy.symbols('S')
denominator = (S**2) * (S + 2)
denominator = denominator.expand()
denominator = sympy.poly(denominator, S).all_coeffs()
denominator = list(map(float, denominator))

numerator = [1.]
sys = control.matlab.tf(numerator, denominator)
r, k = control.matlab.rlocus(sys)
pyplot.plot(k, r)
pyplot.grid()
pyplot.axis([-20, 20, -20, 20])
pyplot.show()
