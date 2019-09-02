import matplotlib.pyplot as plt
import numpy as np

#%matplotlib inline

x=np.linspace(0,5,11)
y=x**2
print(x)
print(y)
# ----------------FUNCTIONAL METHOD---------------------------
'''
plt.plot(x,y,'b--')
plt.xlabel('X Label')
plt.ylabel('Y Label')
plt.title('Title')
plt.show()
'''
#Sub Plot-----------------plt.subplot(#rows, #Columns, plot # of reference)
'''
plt.subplot(2,2,1)
plt.plot(x,y,'r')

plt.subplot(2,2,2)
plt.plot(x,y,'b')
plt.show()
'''
#--------------OBJECT ORIENTED API METHOD
'''
fig=plt.figure()		# creates object
axes=fig.add_axes([0.5,0.5,0.5,0.4])	# apply a method(this one is add_axes())
axes.set_xlabel('X LABEL')
axes.set_ylabel('Y LABEL')
axes.set_title('TITLE')

axes.plot(x,y)		# show the plot
plt.show()
'''
#---------------------------------------------------
fig=plt.figure()
axes1=fig.add_axes([0.1,0.1,0.8,0.8])
axes2=fig.add_axes([0.2,0.5,0.4,0.3])

axes1.plot(x,y)
axes2.plot(y,x,'r--')

axes1.set_xlabel('x label of 1')
axes2.set_xlabel('x label of 2')
plt.show()
