from sympy.solvers import solve
from sympy import symbols

x, y = symbols('x, y')
result = solve(x**3 - y, x)
print(result)
