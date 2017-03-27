import matplotlib

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
#import numpy as np


#SaveYDA cpp Performance

x = [0,100,1000,10000]
y1 = [0,0.04341000000005,0.4276305,4.313542]
y2 = [0,0.4173235,3.984236,26.391431]
y3 = [0,4.31955,27.062256,217.617151]


plt.title('Performance of SaveYDA')
plt.xlabel('nhistograms')
plt.ylabel('time(seconds)')
cpp = plt.plot(x,y1,"b",x,y1,"oc",x,y2,"b",x,y2,"or",x,y3,"b",x,y3,"oy")
blue_patch = mpatches.Patch(color='blue',label='yaml-cpp')
plt.legend(handles = [blue_patch])
plt.text(8500,6.5, 'xbins = 100',fontsize = 8)
plt.text(8000,29.8, 'xbins = 1000',fontsize = 9)
plt.text(8000,190.4, 'xbins = 10000',fontsize = 10)
#plt.show()
plt.grid(True)
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#SaveYDA python Performance

y1 = [0,0.6042085,7.368399,76.3381485]
y2 = [0,6.219068,62.222895,282.40803]
y3 = [0,62.895356,297.1315395,2835.59174]
plt.axis([-1.9,10001,-1.9,600])
plt.plot(x,y1,"g",x,y1,"oc",x,y2,"g",x,y2,"or",x,y3,"g",x,y3,"oy")
green_patch = mpatches.Patch(color='green',label='pyyaml')
plt.legend(handles = [blue_patch,green_patch])
plt.text(4000,40.4, 'xbins = 100',fontsize = 10)
plt.text(4000,165.4, 'xbins = 1000',fontsize = 10)
plt.text(500,200.4, 'xbins = 10000',fontsize = 10)
plt.show()
#plt.plot(x,y1)
#plt.plot(x,y2)
#plt.plot(x,y3)
#plt.show()