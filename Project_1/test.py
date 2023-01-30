#%%
import numpy as np
# %%
np.random.normal(0,0,size=(500))
# %%
a= np.ones((100,1000))
b = np.linspace(0,99,100)
b=[1,2]
# print(a * b.T)
print(np.multiply(a, b[:, None]))
# %%
np.random.normal(0,0,size=100)
# %%
f = 1.0
print(not f == True)
# %%
import winsound

# %%
winsound.Beep(2093, 180)