from matplotlib.pyplot import *
from sympy.polys.dispersion import dispersion, dispersionset
import sympy
import numpy
import control

# 这个是一个阶跃函数信息的简单实现
# 没有拟合曲线
# 随着 T, yout 的输出密度增加而提升精度
def step_info(t, yout):
    # 超调量
    print("Mp (%): ", (yout.max() / yout[-1] - 1) * 100)
    # 峰值时间
    print("Tp: ", t[numpy.argmax(yout)])
    # 上升时间
    print("Tr: ", t[next(i for i in range(0, len(yout) - 1) if yout[i] > yout[-1])])
    # 调整时间
    offset = 0.05 # 最大误差容许范围
    print("Ts: ", t[next(len(yout) - i for i in range(2, len(yout) - 1) if abs(yout[-i] / yout[-1] - 1) > offset)])

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
print(T)
print(yout)

step_info(T, yout)

# 绘图
plot(T, yout)
title("System Step Response")
xlabel("time / sec")
ylabel("response / value")
# show()
