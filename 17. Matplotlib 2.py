import numpy as np 
import matplotlib.pyplot as plt 

x=np.linspace(1,4,20)
y=x**2
z=x**3
#----------------------------------------------------
'''
fig,axes=plt.subplots()
axes.plot(x,y)

plt. show()
'''
#----------------------------------------------------
'''
fig,axes=plt.subplots(1,2)

for position in axes:
	position.plot(x,y)

axes[0].set_ylabel('Y label in 1')
axes[1].set_ylabel('Y label in 2')
axes[0].set_xlabel('X label in 1')
axes[1].set_xlabel('X label in 2')
axes[0].set_title('title 1')
axes[1].set_title('title 2')

plt.tight_layout()
plt.show()
'''
#----------------------------------------------------
#FIGURE SIZE AND DPI
'''
fig=plt.figure(figsize=(8,2))
axes=fig.add_axes([0,0,1,1])

plt.tight_layout()
plt.show()
'''
#-----------------------------------------------------
'''
fig,axes=plt.subplots(nrows=2,ncols=1,figsize=(8,3))
axes[0].plot(x,y)
axes[1].plot(y,x)

plt.tight_layout()
plt.show()
'''
#-----------------------------------------------------

fig=plt.figure()

axes=fig.add_axes([0.2,0.2,0.6,0.6])
axes.plot(x,y,label='Y vs X')
axes.plot(x,z,label='X CUBE')
axes.legend(loc=0)# loc = 0 will allow matplotib to chose the best potition to fit the legend
plt.tight_layout()
plt.show()























