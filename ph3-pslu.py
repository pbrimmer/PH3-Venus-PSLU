import numpy as np
import matplotlib.pyplot as plt
import sys
import copy
import matplotlib.patches as patches
import scipy.optimize as sop


def lineprofile(nu,nu0):                #Line profile, define as you see fit.
    funct = 0.0
    return funct

gamma0 = 0.186        #in cm-1 atm-1 (theoretical)
#gamma0 = 0.286        #in cm-1 atm-1 (ammonia analogy)

gamma = gamma0*2.9979e10     #convert cm-1 atm-1 to s-1 atm-1
nu0 = 300.0*1e9         #center of the line in s-1
Sstar = 0.0  #PH3 line strength coeff in units of cm-1/(mol cm-2) [JPL units are nm2 MHz]
muPH3 = 33.998      #mean molecular weight
nu = np.arange(200.0,400.0001,0.0001) #nu in GHz
nu *= 1e9                         #convert from GHz to s-1
I0 = np.full(len(nu),1.0)           #starting intensity, set to unity.

I = copy.copy(I0)
Iprime = copy.copy(I0)

#read in height (km), temperature (K), number density (cm-3), pressure (bar)
h,T,n,P = np.genfromtxt('pT-Venus.dat',skip_header=2,usecols=(0,1,3,4),unpack=True)

h *= 1e5            #Convert from km to cm

xPH3 = np.zeros(len(h))

for j in range(len(xPH3)):
    xPH3[j] = 0.0

for i in range(len(h)-1):
    if h[i]*1e-5 > 0.0:
        dh = h[i+1] - h[i]
        S = Sstar*n[i]*xPH3[i]*2.9979e10 #PH3 line strength in units of cm-1 s-1
        knu = lineprofile(nu,nu0)*S
        I *= np.exp(-knu*dh)


for i in range(len(nu)):
    if (nu[i]-nu0)/nu0*299792.0 >= -50.1 and (nu[i]-nu0)/nu0*299792.0 < -50.0: 
        I50 = I[i]-1.0

fig, ax = plt.subplots()
#rect = patches.Rectangle((-50.0,-3.5e-4),100.0,3.5e-4,linewidth=1, edgecolor='none', facecolor='blue',alpha=0.25)

plt.title('Pressure Broadening Coefficient = '+('%.2e' % gamma0)+' cm$^{-1}$ atm$^{-1}$',fontsize=13)
plt.ylabel('l:c ratio',fontsize=13)
plt.xlabel('Venus frame velocity (km s$^{-1}$)',fontsize=13)

#ax.add_patch(rect)

ax.set_xlim([-50.0,50.0])
ax.set_ylim([-1.5e-4,2e-5])
ax.plot((nu-nu0)/nu0*299792.0,I-1.0-I50,'k-',linewidth=1.0,label='LineShape')
plt.legend()
plt.savefig('./PH3-Test.pdf',bbox_inches='tight')
