from numba import jit
import monomer_model.take_step
from monomer_model.run_simulation import run_simulation
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
from mpl_toolkits import mplot3d
from general_functions.line_to_array import line_to_array
import seaborn
from data.data_Ke_et_al import get_me_data
import data.nadarajah_data as nadarajah_data
import time as tme

# @jit
def make_plot_final(n, time, deltas):
    start_time = tme.time()
    # first set our parameters
    k = 1.380649 * (10 ** (-23))
    T = 290
    Epb = [1*k*T, 2*k*T, 3*k*T]
    deltaMu = [x*k*T for x in range(0, deltas)]
    growth_rate = [[], [], []]
    errorbars = [[], [], []]
    def phi(Epb):
        return [2*Epb, 3*Epb, 4*Epb, 5*Epb]
    j=0
    ke_data = get_me_data()
    figure, axis = plt.subplots(1, 3, figsize=(15,7))
    figure.tight_layout(pad=5.0)
    for h in range(3):
        for i in phi(Epb[h]):
            for x in deltaMu:
                growth_rate[h].append(run_simulation(n, x, i, Epb[h], T, time)[0])
                j += 1
                print(j)
    colours = ['mediumvioletred', 'lightskyblue', 'forestgreen', 'gold']
    intermediate = min(growth_rate[0]+growth_rate[1]+growth_rate[2])
    intermediate2 = max(growth_rate[0]+growth_rate[1]+growth_rate[2])
    for y in range(0,4):
        [xmin, xmax, ymin, ymax] = [0, deltas-1, 0, intermediate2]
        axis[0].plot(range(0,deltas), growth_rate[0][deltas * y:deltas * (y+1)], marker='.', label=r"$\phi$ = "+str(y+2)+r"$E_{pb}$", color=colours[y])
        #axis[0].plot(range(0,deltas), ke_data[0][13 * y:deltas * (y+1)], colours[-y-1])
        axis[0].set_title(r'$E_{pb}=kT$')
        axis[0].set(xlabel=r'$\Delta$$\mu$ in multiples of $kT$', ylabel='Growth Rate')
        axis[0].set_xlim(xmin, xmax)
        axis[0].set_ylim(ymin, ymax*1.05)        
        axis[0].legend()
        #axis[1].plot(range(0,deltas), ke_data[1][deltas * y:deltas * (y+1)], colours[-y-1])
        [xmin, xmax, ymin, ymax] = [0, deltas-1, 0, intermediate2]        
        axis[1].plot(range(0,deltas), growth_rate[1][deltas * y:deltas * (y+1)], marker='.', label=r"$\phi$ = "+str(y+2)+r"$E_{pb}$", color=colours[y])
        axis[1].set_title(r'$E_{pb}=2kT$')
        axis[1].set(xlabel='$\Delta$$\mu$ in multiples of $kT$', ylabel='Growth  Rate')
        axis[1].set_xlim(xmin, xmax)
        axis[1].set_ylim(ymin, ymax*1.05)           
        axis[1].legend()
        #axis[2].plot(range(0,deltas), ke_data[2][deltas * y:deltas * (y+1)], colours[-y-1])
        [xmin, xmax, ymin, ymax] = [0, deltas-1, 0, intermediate2]        
        axis[2].errorbar(range(0,deltas), growth_rate[2][deltas * y:deltas * (y+1)], marker='.', label=r"$\phi$ = "+str(y+2)+r"$E_{pb}$", color=colours[y])
        axis[2].set_title(r'$E_{pb}=3kT$')
        axis[2].set(xlabel='$\Delta$$\mu$ in multiples of $kT$', ylabel='Growth Rate')
        axis[2].set_xlim(xmin, xmax)
        axis[2].set_ylim(ymin, ymax*1.05)           
        axis[2].legend()
    
    print(tme.time() - start_time)
    plt.savefig('IKEA make_plot_final_50000.png')
    #plt.savefig('make_plotA_final3.pdf')
    #    # plt.plot([x*k*T for x in deltaMu], growth_rate[0:13], label=2)
   # dummy2=run_simulation(30, deltaMu[4], phi[2], Epb, T, time)
   # print(line_to_array(dummy2[1],30))
   # seaborn.heatmap(line_to_array(dummy2[1],30))
   # plt.xlabel('deltaMu in multiples of kT')
   # plt.ylabel('growth rate')
   # plt.title('Monomers only: no of bonds per molecule, Epb/kT is 2')
   # plt.legend()
