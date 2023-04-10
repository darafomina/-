import numpy as np
import matplotlib.pyplot as plt
y = np.arange(-200, 200.01, 0.01)


def func(x):
    function = -12*x**4*np.sin(np.cos(x)) - 18*x**3 + 5*x**2 + 10*x - 30
    return function


plt.plot(y, func(y), 'b',  label="Корней бесконечное множество.")
plt.legend()
plt.show()