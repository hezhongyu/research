# -*- coding: utf-8 -*-

# @Time    : 2020/10/28 20:24
# @Author  : Zhongyu
# @File    : lorenz.py

# lorenz系统生成器


import numpy as np
from scipy.integrate import odeint
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt


class Lorenz(object):
    def __init__(self,  args, t, model='lorenz63'):
        super(Lorenz, self).__init__()
        self.model_name = model
        if self.model_name == 'lorenz63':
            self.data = odeint(self._lorenz63, (0, 1, 0), t, args=args)
        elif self.model_name == 'lorenz96':
            n, f = args
            x0 = f * np.zeros(n)
            x0[0] += 0.01  # 加初始扰动，很重要
            self.data = odeint(self._lorenz96, x0, t, args=args)

    @staticmethod
    def _lorenz63(w, t, p, r, b):
        x, y, z = w
        return np.array([p * (y - x), x * (r - z) - y, x * y - b * z])

    @staticmethod
    def _lorenz96(x, t, n, f):
        d = np.zeros(n)
        for i in range(n):
            d[i] = (x[(i + 1) % n] - x[i - 2]) * x[i - 1] - x[i] + f
        return d

    def get_data(self):
        return self.data


if __name__ == '__main__':
    t = np.arange(0, 30, 0.01)
    args = (10, 28.0, 8 / 3)
    track1 = Lorenz(args, t, 'lorenz63').get_data()
    # print(type(track1))
    # print(track1.shape)

    args2 = (5, 8)
    track2 = Lorenz(args2, t, 'lorenz96').get_data()

    fig = plt.figure()
    ax = Axes3D(fig)
    # ax.plot(track1[:, 0], track1[:, 1], track1[:, 2])
    ax.plot(track2[:,0], track2[:,1], track2[:,2])
    plt.show()

