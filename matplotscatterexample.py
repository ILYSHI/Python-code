
import matplotlib.pyplot as plt
import numpy as np
data = {"a":np.arange(150),
        'c':np.random.randint(0,50,150),
        'd':np.random.randn(150)}
data['b']=data['a']+100*np.random.rand(150)
data['d']=np.abs(data['d'])*100
plt.scatter('a','b',c='a',s='a',data=data)
plt.xlabel('entry a')
plt.ylabel('entry b')
plt.show()

