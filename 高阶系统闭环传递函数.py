from scipy import *
from control import *
from matplotlib.pyplot import *
from control.matlab import *

numerator = [45]
# denominator = [[1, 0.6, 1], [1, 3, 9], [1, 5]]
denominator = [1, 0.6, 1]
sys = tf(numerator, denominator)

T, yout = step_response(sys)
plot(T, yout)
show()

