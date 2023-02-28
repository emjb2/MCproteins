#from numba import jit
from aggregate_model.run_simulationA import run_simulationA
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
from general_functions.line_to_array import line_to_array
import seaborn
from data.data_Ke_et_al import get_me_data
import data.nadarajah_data as nadarajah_data
import time as tme
from general_functions.monomer_dimer_tetramer import plot_monomer_dimer_tetramer
from statistics import stdev, mean

# @jit
def make_plotA_final_surface(n, time, deltas):
    start_time = tme.time()
    # first set our parameters
    k = 1.380649 * (10 ** (-23))
    T = 290
    Epb = [1*k*T, 2*k*T, 3*k*T]
    deltaMu = [x*k*T for x in range(0, deltas)]
    surface_roughness = [[], [], []]
    errors =[[],[],[]]
    def phi(Epb):
        return [2*Epb, 3*Epb, 4*Epb, 5*Epb]
    j=0
    colours =['b', 'y', 'g', 'r']
    figure, axis = plt.subplots(1, 3, figsize=(15,7))
    figure.tight_layout(pad=5.0)
    for h in range(3):
        for i in phi(Epb[h]):
            for x in deltaMu:
                temp = []
                for g in range(3):
                    temp.append(stdev(run_simulationA(n, x, i, Epb[h], T, time)[1]))
                surface_roughness[h].append(mean(temp))
                errors[h].append(stdev(temp))
                j += 1
                print(j)
    for y in range(0,4):
        axis[0].errorbar(range(0,deltas), surface_roughness[0][deltas * y:deltas * (y+1)], errors[0][deltas * y:deltas * (y+1)], marker = '.', label=r"$\phi$ = "+str(y+2)+r"$E_{pb}$")
        #axis[0].plot(range(0,deltas), ke_data[0][13 * y:deltas * (y+1)], colours[-y-1])
        axis[0].set_title(r'$E_{pb}=1kT$')
        axis[0].set(xlabel=r'$\Delta$$\mu$ in multiples of $kT$', ylabel='Surface Roughness')
        axis[0].legend()
        #axis[1].plot(range(0,deltas), ke_data[1][deltas * y:deltas * (y+1)], colours[-y-1])
        axis[1].errorbar(range(0,deltas), surface_roughness[1][deltas * y:deltas * (y+1)], errors[1][deltas * y:deltas * (y+1)], marker = '.', label=r"$\phi$ = "+str(y+2)+r"$E_{pb}$")
        axis[1].set_title(r'$E_{pb}=2kT$')
        axis[1].set(xlabel='$\Delta$$\mu$ in multiples of $kT$', ylabel='Surface Roughness')
        axis[1].legend()
        #axis[2].plot(range(0,deltas), ke_data[2][deltas * y:deltas * (y+1)], colours[-y-1])
        axis[2].errorbar(range(0,deltas), surface_roughness[2][deltas * y:deltas * (y+1)], errors[2][deltas * y:deltas * (y+1)], marker = '.', label=r"$\phi$ = "+str(y+2)+r"$E_{pb}$")
        axis[2].set_title(r'$E_{pb}=3kT$')
        axis[2].set(xlabel='$\Delta$$\mu$ in multiples of $kT$', ylabel='Surface Roughness')
        axis[2].legend()
    
    print(tme.time() - start_time)
    #plt.savefig('make_plotA_final2.png')
    #plt.savefig('make_plotA_final2.pdf')
    plt.show()
