import numpy as np 
import matplotlib.pyplot as plt 



fig=plt.figure()

x=np.linspace(0,5,11)
y=x**2
z=x**3
axes=fig.add_axes([0.1,0.1,0.6,0.6])

axes.plot(x,y,color='green',linewidth=5,alpha=0.5,linestyle=':')	#alpha is to make it more transparence
axes.plot(x,z,'purple',linewidth=3,linestyle='--',marker='o',markersize=4) # marker is to highlight the location of the points
axes.set_xlim([0,3])
axes.set_ylim([10,20])
plt.tight_layout()
plt.show()