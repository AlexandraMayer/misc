import matplotlib

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

colorc = "#33ccff"
colorctext = "#0086b3"
colorp="#99e600"
colorptext = "#669900"
fig = plt.figure()
#SaveYDA Performance 
plt.subplot(2,1,1)

plt.title('Performance of SaveYDA')
#plt.xlabel('nhistograms')
plt.ylabel('time(seconds)')
plt.grid(True)

blue_patch = mpatches.Patch(color=colorc,label='yaml-cpp')
green_patch = mpatches.Patch(color=colorp,label='pyyaml')


#SaveYDA cpp Performance

x = [100,1000,10000]
y1 = [0.04341000000005,0.4276305,4.313542]
y2 = [0.4173235,3.984236,26.391431]
y3 = [4.31955,27.062256,217.617151]


cpp = plt.plot(x,y1,label="yaml-cpp")
cpp2 = plt.plot(x,y1,"o",x,y2,x,y2,"o",x,y3,x,y3,"o")
plt.setp(cpp,color=colorc,linewidth =1.5)
plt.setp(cpp2,color=colorc,linewidth =1.5)

plt.text(8000,1.6, 'xbins = 100',fontsize = 10,color=colorctext,rotation=4)
plt.text(8000,11.0, 'xbins = 1000',fontsize = 10,color=colorctext,rotation = 3)
plt.text(8000,90.9, 'xbins = 10000',fontsize = 10,color=colorctext,rotation=3.5)

#SaveYDA python Performance

y1 = [0.6042085,7.368399,76.3381485]
y2 = [6.219068,62.222895,282.40803]
y3 = [62.895356,297.1315395,2835.59174]


python = plt.plot(x,y1,label="pyyaml")
python2 = plt.plot(x,y1,"o",x,y2,x,y2,"o",x,y3,x,y3,"o")
plt.setp(python,color=colorp,linewidth =1.5)
plt.setp(python2,color=colorp,linewidth =1.5)

plt.text(4000,23.8, 'xbins = 100',fontsize = 10,color=colorptext,rotation=3.4)
plt.text(4000,130.4, 'xbins = 1000',fontsize = 10,color=colorptext,rotation=1.4)
plt.text(4000,1100, 'xbins = 10000',fontsize = 10,color=colorptext,rotation=3.4)
plt.yscale('log')
#plt.show()
plt.legend(loc=4,fontsize = 10)
#LoadYDA Performance

p2 = plt.subplot(2,1,2)

plt.title('Performance of LoadYDA')
plt.xlabel('nhistograms')
plt.ylabel('time(seconds)')
plt.grid(True)



#LoadYDA cpp Performance

x = [100,1000,2000]
y1 = [0.168317,1.519279,3.0539185]
y2 = [1.3211975,12.935343,24.369694]
y3 = [2.7367485, 29.641191,48.5328725]

cpp = plt.plot(x,y1,label="yaml-cpp")
cpp2 =plt.plot(x,y1,"o",x,y2,x,y2,"o",x,y3,x,y3,"o")
plt.setp(cpp,color=colorc,linewidth =1.5)
plt.setp(cpp2,color=colorc,linewidth =1.5)
blue_patch = mpatches.Patch(color=colorc,label='yaml-cpp')
plt.text(1500,1.5, 'xbins = 100',fontsize = 10,color=colorctext,rotation=2.4)
plt.text(1500,12.5, 'xbins = 1000',fontsize = 10,color=colorctext,rotation=2.6)
plt.text(1500,46.8, 'xbins = 10000',fontsize = 10,color=colorctext,rotation=1.6)

#LoadYDA python Performance

y1 = [1.330259, 13.5810796666667,26.8930875]
y2 = [12.1064295,129.488247333333,262.1420125]
y3 = [24.5846623333333,259.039196,526.675047]


python = plt.plot(x,y1,label="pyyaml")
python2 = plt.plot(x,y1,"o",x,y2,x,y2,"o",x,y3,x,y3,"o")
plt.setp(python,color=colorp,linewidth =1.5)
plt.setp(python2,color=colorp,linewidth =1.5)
green_patch = mpatches.Patch(color=colorp,label='pyyaml')
plt.legend(loc=4,fontsize = 10)
plt.text(600,10.0, 'xbins = 100',fontsize = 10,color=colorptext,rotation=10.6)
plt.text(600,55.4, 'xbins = 1000',fontsize = 10,color=colorptext,rotation=10.4)
plt.text(600,220.4, 'xbins = 10000',fontsize = 10,color=colorptext,rotation=11)
plt.yscale('log')
#plt.show()


fig.savefig("performancePlot.png")