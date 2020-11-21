import matplotlib.pyplot as plt
import numpy as np
n=50/3*np.random.randn(10000)+50
fig, axes = plt.subplots(1,2, figsize=(12,4))
axes[0].hist(n)
axes[0].set_title('Default histogram')
axes[0].set_xlim((min(n),max(n)))
axes[1].hist(n,cumulative=True,bins=50)
axes[1].set_title('Cumulative')
axes[1].set_xlim((min(n),max(n)))

plt.show()
