from matplotlib.pyplot import *
from sympy.polys.dispersion import dispersion, dispersionset
import sympy
import control

# 化简分母
S = sympy.symbols('S')
denominator = (S**2 + 0.6*S + 1) * (S**2 + 3*S + 9) * (S + 5)
denominator = denominator.expand() # 化简表达式
denominator = sympy.poly(denominator, S).all_coeffs() # 转成多项式 list
denominator = list(map(float, denominator)) # convert sympy.core.numbers.Float to float

numerator = [45.]
sys = control.matlab.tf(numerator, denominator)

# 阶跃
T, yout = control.step_response(sys)

# 绘图
plot(T, yout)
title("System Step Response")
xlabel("time / sec")
ylabel("response / value")
show()
