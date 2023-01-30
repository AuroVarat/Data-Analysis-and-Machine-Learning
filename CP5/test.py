#%%
import numpy as np
import matplotlib.pyplot as plt
#%%
def eva(x):
    return -1*x+20
filtered_x = np.random.uniform(0 , 20,size=10300)
y1 = eva(filtered_x)
y2 = np.random.uniform(0, 20,size=10300)
# %%
left_filtered = np.where(~(y2<y1))[0]
print(filtered_x[~left_filtered].size)
# %%
while(len(left_filtered) != 0):
    filtered_x[left_filtered] = np.random.uniform(0 , 20,size=len(left_filtered))
    y1 = eva(filtered_x)
    y2[left_filtered] = np.random.uniform(0, 20,size=len(left_filtered))
    left_filtered = np.where(~(y2 < y1))[0]
print("Finished")
# %%
plt.hist(filtered_x,bins=100,density=True)
plt.plot(filtered_x,y1/(20*(10*-1+20)))
# %%
