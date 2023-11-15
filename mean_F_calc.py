"""
Calculate total amount of partial melting acording to thickness of oceanic crust

@time: 2023-11-13
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def F_mean_cal_A08_FA1(hc):
    """
    The preferred model from Afonso et al., (2008)
    hc: thickness of oceanic crust (km)
    Detail see Figure A1 by Afonso et al., (2008)
    """
    print("The parameter refers to Afonso et al., (2008)") 

    rho_crust=2880 # density of oceanic crust in kg/m3
    g=9.8   # accelration due to gravity
    Po=2.5 # pressure at which melting starts (GPa)
    Pf=0.2  # pressure at which melting stops (GPa)
    F_mean= (hc*rho_crust*g)/((Po-Pf)*10**4)
    print("The thickness of oceanic crust (km):",hc) 
    print("The mean fraction of melting (%):",F_mean)
    print("")
    return F_mean

def F_mean_cal_A08_ex(hc):
    """
    hc: thickness of oceanic crust (km)
    This is from an example by Afonso et al., (2008)
    For typical values of [Asimow et al., 1999, 2001] F 7.2%, Po 2.75 GPa, Pf 0.2 GPa, and rc = 2880 kg m3, equation (A9) gives hc  6.5 km.
    """
    print("The parameter refers to Asimow et al., 1999, 2001") 
    rho_crust=2880 # density of oceanic crust in kg/m3
    g=9.8   # accelration due to gravity
    Po=2.75 # pressure at which melting starts (GPa)
    Pf=0.2  # pressure at which melting stops (GPa)
    F_mean= (hc*rho_crust*g)/((Po-Pf)*10**4)
    print("The thickness of oceanic crust (km):",hc) 
    print("The mean fraction of melting (%):",F_mean)
    print("")
    return F_mean


# # plt.savefig(figname)

if __name__ == '__main__':
    F_mean = F_mean_cal_A08_FA1(6.5)
    F_mean = F_mean_cal_A08_FA1(6.14)

    F_mean = F_mean_cal_A08_ex(6.5)
    
    #%% plotting
    hc = np.arange(11)
    F1 = F_mean_cal_A08_FA1(hc)
    F2 = F_mean_cal_A08_ex(hc)
    plt.figure()
    plt.plot(hc,F1,label='Afonso et al., 2008')
    plt.plot(hc,F2,label='Asimow et al., 2001')
    plt.grid('on')
    plt.legend()
    plt.xlabel('hc/km')
    plt.ylabel('The mean fraction of melting (%)')
    
    plt.savefig("F_VS_hc.png")
