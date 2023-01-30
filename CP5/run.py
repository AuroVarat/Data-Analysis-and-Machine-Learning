#%%
from distributionClass import Linear,Gaussian,SignalWithBackground
import matplotlib.pyplot as plt

# Main code to generate and plot a single experiment


XMIN = 0.
XMAX = 20.
intercept = 20.
slope = -1.
# signal parameters
mean = 10.
sigma = 0.5
NBINS = 100
# chose number of bins that is appropriate for the size of the statistics sample NBINS = 100

def singleToy(nevents_sig = 300, nevents_bgd = 10000):
    sig_fraction = nevents_sig/(nevents_bgd + nevents_sig)
#   Create the pdf
    pdf = SignalWithBackground(mean, sigma, sig_fraction, intercept, slope, XMIN, XMAX ) 
    for i in range( nevents_sig + nevents_bgd ): pdf.next()
    # retrieve the mass values for signal, background and their sum
    data = pdf.mass 
    sig_data = pdf.mass_sig 
    bgd_data = pdf.mass_bgd
    # plot things on same page
    myRange = (XMIN, XMAX)
    fig, axs = plt.subplots(3,1, sharex='col')
    axs[0].set_title("Signal distribution (" + str(len(sig_data)) + " entries)") 
    axs[1].set_title("Background distribution (" + str(len(bgd_data)) + " entries)") 
    axs[2].set_title("Total distribution (" + str(len(data)) + " entries)") 
    axs[2].set_xlabel('X')
    axs[0].hist(sig_data, bins=NBINS, range=myRange) 
    axs[1].hist(bgd_data, bins = NBINS) 
    axs[2].hist(data, bins = NBINS) 
    fig.tight_layout()
    plt.savefig('Example1.pdf')

    
singleToy()
# %%
from distributionClass import Linear,Gaussian,SignalWithBackground
from scipy.special import erfinv
import numpy as np
bg1 = Gaussian(mean=10000,sigma=100)
bg2 = Gaussian(mean=10300,sigma=100)

p_value = bg2.integrate()[0]/bg1.integrate()[0]
print(p_value)
n_sigmas = erfinv(1 - p_value) * np.sqrt(2)
print(n_sigmas)

# %%
