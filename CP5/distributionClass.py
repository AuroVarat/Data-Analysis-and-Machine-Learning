#%%
import numpy as numpy 
from scipy import integrate
import math
# # background parameters
#%%
XMIN = 0.
XMAX = 20.
intercept = 20.
slope = -1.
# signal parameters
mean = 10.
sigma = 0.5
NBINS = 100
# chose number of bins that is appropriate for the size of the statistics sample NBINS = 100
#%%

class Linear:
    def __init__(self, XMIN,XMAX,intercept,slope):
        self.mass = []
        
        self.lolimit = XMIN
        self.hilimit = XMAX
        self.intercept = intercept
        self.slope = slope
      
        
# Evaluate method (un-normalised)
    def evaluate(self, t):
        f = lambda t: self.intercept + self.slope * t
        return f(t)
    def maxval(self):
        return self.evaluate(self.hilimit)
    def next(self): 
        doLoop = True
        while(doLoop):

        # start with uniform random number in [lolimit, hilimit) 
            x = numpy.random.uniform(self.lolimit , self.hilimit)
            y1 = self.evaluate(x)
     
            y2 = numpy.random.uniform(0, self.maxval())
            if (y2 < y1):
                filtered_x = x 
                self.mass.append(filtered_x) 
                return filtered_x
#%%
class Gaussian:
    def __init__(self,mean=mean,sigma=sigma):
        self.mass = []
        
        self.mean = mean
        self.sigma = sigma
        
    def evaluate(self, t):
        
        return numpy.exp(-(t - self.mean)**2 / (2 * self.sigma**2)) # where 1 was amplitude initially
    def integrate(self):
        return integrate.quad(self.evaluate,0,10000)
    def next(self): 
        return numpy.random.normal(loc=self.mean, scale=self.sigma) 

    
#%%   
class SignalWithBackground:
    def __init__(self, mean=mean, sigma=sigma, sig_fraction=0.03, intercept=intercept, slope=slope, XMIN=XMIN, XMAX=XMAX):
        self.mass_sig = []
        self.mass_bgd = []
        self.mass = []
        
        
        self.signal = Gaussian(mean=mean,sigma=sigma)
        self.background = Linear(XMIN=XMIN,XMAX=XMAX,intercept=intercept,slope=slope)
        self.sig_fraction = sig_fraction
  

    # Draw random number form distribution
    def next(self):
        q = numpy.random.uniform() 
        if( q < self.sig_fraction):
        # if here, we will draw x from signal distribution
            filtered_x = self.signal.next()
            self.mass_sig.append(filtered_x)
        else:
            # if here, we will draw x from background distribuion
            filtered_x = self.background.next() 
            self.mass_bgd.append(filtered_x)
        self.mass.append(filtered_x) 
        return filtered_x
#%%

    
# %%

# %%
