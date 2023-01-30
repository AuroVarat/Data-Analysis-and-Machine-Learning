#%%
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.optimize import curve_fit
rng = np.random.default_rng(1245)
#%%
rno =rng.exponential(2.2,size=1000)

while np.any(rno > 20):
    rno[rno > 20] = rng.exponential(2.2,size=len(rno[rno > 10]))
plt.hist(rno,bins=50)
plt.show()

print(np.mean(rno))

# %%
def mean_t_run():
    rno =rng.exponential(2.2,size=1000)

    while np.any(rno > 20):
        rno[rno > 20] = rng.exponential(2.2,size=len(rno[rno > 20]))
    return np.mean(rno)
#%%
t_values = np.zeros(500)

for i in range(500):
    t_values[i] = mean_t_run()
    
#%%
ns, bins,_ = plt.hist(t_values,bins=50)
# %%
from scipy.optimize import curve_fit
# Let's create a function to model and create data
def func(x, a, x0, sigma):
    return a*np.exp(-(x-x0)**2/(2*sigma**2))

# %%
bins = bins[:-1]
# Executing curve_fit on noisy data
popt, pcov = curve_fit(func, bins, ns)
  
#popt returns the best fit values for parameters of the given model (func)
print (popt)
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(bins, ns, c='k', label='Function')
ax.scatter(bins, ns)
ym = func(bins, popt[0], popt[1], popt[2])
ax.plot(bins, ym, c='r', label='Best fit')
ax.legend()
fig.savefig('model_fit.png')
# %%
