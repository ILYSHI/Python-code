import matplotlib.pyplot as plt
import numpy as np

x=np.arange(0,10,1)
print(x)


y=x**2
fig=plt.figure()
axes1 = fig.add_axes([0.1,0.1,0.8,0.8])
axes1.set_xlabel('x')
axes1.plot(x,y,label="привет")
axes1.legend(loc=6)
axes2 = fig.add_axes([0.2,0.7,0.4,0.2])
axes2.set_xlabel('x')
axes2.plot(y,x,'b^')
axes2.plot(x,y,y,x,label="пока")
axes2.legend(loc=2)
fig.tight_layout()
plt.show()
