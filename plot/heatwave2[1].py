# -*- coding: utf-8 -*-
"""
Created on Sat Jul 31 23:38:00 2021

@author: rodin
"""
from math import sqrt, log
import numpy as np
import matplotlib.pyplot as plt
import glob
import os
# Remove frames
for filename in glob.glob('tmp_*.png'):
    os.remove(filename)
    
    
def animate(tmax, dt, x, function, ymin, ymax, t0=0,
            xlabel='x', ylabel='y', filename='tmp_'):
    t = t0
    counter = 0
    while t <= tmax:
        y = function(x, t)
        lines[0].set_data(x, y)
        plt.axis([x[0], x[-1], ymin, ymax])
        plt.title('time-%4.2f yr' % (t / 60. / 60 / 365 / 24))
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.savefig(filename + '%04d.png' % counter)
        t += dt
        counter += 1


def T(z, t):
    # T0, A, k, and omega are global variables
    return T0 + A1 * np.exp(-a1 * z) * np.sin(omega1 * t - a1 * z) + \
        A2 * np.exp(-a2 * z) * np.sin(omega2 * t - a2 * z)

k = 1E-6            # thermal diffusivity (in m**2/s)

A1 = 15             # amplitude of the daily temperature variations (in C)
P1 = 24 * 60 * 60 * 365.     # oscillation period of 24 h (in seconds)
omega1 = 2 *np. pi / P1   # angular freq of daily temp variations (in rad/s)
a1 = np.sqrt(omega1 / (2 * k))

A2 = 7                    # amplitude of yearly temperature variations (in C)
P2 = 24 * 60 * 60.  # oscillation period of 1 yr (in seconds)
omega2 = 2 * np.pi / P2      # angular freq of yearly temp variations (in rad/s)
a2 = np.sqrt(omega2 / (2 * k))

dt = P2 / 20            # time lag: 0.1 yr
tmax = 3 * P2               # 3 year simulation
T0 = 10                 # mean surface temperature in Celsius
D = -(1 / a1) * log(0.001)  # max depth
n = 501                 # no of points in the z direction

# set T0, A, k, omega, D, n, tmax, dt
z = np.linspace(0, D, n)

lines=plt.plot([],[])
animate(tmax, dt, z, T, T0 - A2 - A1, T0 + A2 + A1, 0, 'z', 'T')

os.system('ffmpeg -i tmp_%04d.png -r 5 -vcodec flv mymovie3.flv')