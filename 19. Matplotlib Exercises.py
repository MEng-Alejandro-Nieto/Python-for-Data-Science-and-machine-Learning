import numpy as np 
import matplotlib.pyplot as plt 

x=np.linspace(0,10,10)
y=x*2
z=x**2


# Create a figure object called fig 
# set the axes to fill the entire figure
# plot x,y and set the lables and titles
'''
fig=plt.figure()
axes=fig.add_axes([0.1,0.1,0.8,0.8])
axes.plot(x,y)
axes.set_xlabel('X')
axes.set_ylabel('Y')
axes.set_title('TITLE')
plt.tight_layout()
plt.show()
'''


# Create a figure and put two axes on it, located at [0,0,1,1] and
# [0.2,0.5,0.2,0.2]
#


fig=plt.figure()
axes1=fig.add_axes([0.1,0.1,.8,0.8])
axes2=fig.add_axes([.2,.5,.2,.2])
axes1.plot(x,y)
axes2.plot(x,z)
axes1.set_xlabel('X')
axes1.set_ylabel('Y')

plt.tight_layout()
plt.show()

