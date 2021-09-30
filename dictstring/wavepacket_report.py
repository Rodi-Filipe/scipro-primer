# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 21:55:30 2021

@author: rodin
"""

import matplotlib.pyplot as plt
import numpy as np

def write_html():
    
    outfile=open('c:/users/rodin/Documents/Python_Scripts/wavepacket_report.html','w')
    
    
    str_var = """\
<html>
<body>
<h1> Explnation 1</h1>
This is the code used to create the gif file wavepacket.gif
<h1>Code</h1>
<pre>
import matplotlib.pyplot as plt
from matplotlib import animation
import numpy as np

import glob, os
# Remove old plot files
for filename in glob.glob('tmp_*.png'): os.remove(filename)


def init():
    
    lines[0].set_data([],[])
    plt.xlabel('x values')
    plt.ylabel('y values')
    plt.title('wave packet function')
    plt.axis([-6,6,-1.5,1.5])
    
    return lines

def frames(args):
    
    x, t, lines = args
    y=np.exp(-1*(x-3*t)**2)*np.sin(3*np.pi*(x-t))
    
    lines[0].set_data(x,y)
    
    return lines

fig=plt.figure()
lines=plt.plot([],[])
all_args=[(np.linspace(-6,6,10000),i, lines) for i in np.linspace(-1,1,100)]

anim=animation.FuncAnimation(fig,frames,all_args,init_func=init,interval=150,blit=True)

anim.save('mymovie0.gif',fps=6)</pre>
<h1>Results 1</h1>
<img src="c:/users/rodin/Documents/Python_Scripts/mymovie0.gif">
<h1>Explanation 2</h1>
The function below plots the wave packet at 3 different <em>t</em> values
<h1>Code 2</h1>
<pre>
def graph_wavepacket():
    
    t = [-1,0,1]
    fig, ax = plt.subplots(1,3,constrained_layout=True)
    
    
    for k in range(len(ax)):
        x = np.linspace(-6,6,10000)
        y = np.exp(-1*(x-3*t[k])**2)*np.sin(3*np.pi*(x-t[k]))
        ax[k].plot(x,y,'--')
        
        ax[k].set_xlabel('x values')
        ax[k].set_ylabel('y values')
        ax[k].set_title('wavepacket function')
        
    plt.savefig('c:/users/rodin/Documents/Python_Scripts/wavepacket_image')</pre>
The results are shown below
<h1>Results 2</h1>
<img src="c:/users/rodin/Documents/Python_Scripts/wavepacket_image.png">
</body>
</html>"""

    print(str_var,file=outfile)
    
    outfile.close()

def graph_wavepacket():
    
    t = [-1,0,1]
    fig, ax = plt.subplots(1,3,constrained_layout=True)
    
    
    for k in range(len(ax)):
        x = np.linspace(-6,6,10000)
        y = np.exp(-1*(x-3*t[k])**2)*np.sin(3*np.pi*(x-t[k]))
        ax[k].plot(x,y,'--')
        
        ax[k].set_xlabel('x values')
        ax[k].set_ylabel('y values')
        ax[k].set_title('wavepacket function')
        
    plt.savefig('c:/users/rodin/Documents/Python_Scripts/wavepacket_image') 
        
graph_wavepacket()

write_html()
