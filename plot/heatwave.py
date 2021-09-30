
from numpy import *
from matplotlib.pyplot import *

def animate(tmax, dt, x, function, ymin, ymax, t0=0,
            xlabel1='x', ylabel1='y', filename='tmp_'):
    t = t0
    counter = 0
    while t <= tmax:
        y = function(x, t)
        plot(x, y, 'b-')
        axis([x[0], x[-1], ymin, ymax])
        title('time=%2d h' % (t/3600.0))
        xlabel(xlabel1) 
        ylabel(ylabel1)
        savefig('tmp_%04d.png' % counter)
        clf()
        t += dt
        counter += 1

def T(z, t):
    # T0, A, k, and omega are global variables
    a = sqrt(omega/(2*k))
    return T0 + A*exp(-a*z)*cos(omega*t - a*z)

import glob, os
# Remove old plot files
for filename in glob.glob('tmp_*.png'): os.remove(filename)

k = 1E-6     # thermal diffusivity (in m**2/s)
P = 24*60*60.# oscillation period of 24 h (in seconds)
omega = 2*pi/P
dt = P/24    # time lag: 1 h
tmax = 3*P   # 3 day/night simulations
T0 = 10      # mean surface temperature in Celsius
A = 10       # amplitude of the temperature variations (in C)
a = sqrt(omega/(2*k))
D = -(1/a)*log(0.001) # max depth
n = 501      # no of points in the z direction

z = linspace(0, D, n)
animate(tmax, 2, z, T, T0-A, T0+A, 0, 'z', 'T')
# Make movie files
os.system('ffmpeg -i tmp_%04d.png -r 5 -vcodec flv movie.flv')
# Can use ffmpeg instead of avconv