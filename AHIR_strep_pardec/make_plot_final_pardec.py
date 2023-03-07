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
from matplotlib import colors
from AHIR_strep_pardec.AHIR_strep_run_simulation_pardec import AHIR_strep_run_simulation_pardec
from statistics import mean, stdev

# @jit
def make_plot_final_pardec(n, time, deltas):
    start_time = tme.time()
    # first set our parameters
    k = 1.380649 * (10 ** (-23))
    T = 290
    Epb = [1*k*T, 2*k*T, 3*k*T]
    deltaMu = [x*k*T for x in range(0, deltas)]
    growth_rate = [[], [], []]
    errors = [[],[],[]]
    def phi(Epb):
        return [2*Epb, 3*Epb, 4*Epb, 5*Epb]
    j=0
    figure, axis = plt.subplots(1, 3, figsize=(15,7))
    figure.tight_layout(pad=5.0)
    for h in range(3):
        for g in range(4):
            for x in deltaMu:
                temp = []
                for l in range(3):
                    temp.append(AHIR_strep_run_simulation_pardec(n, time, x, T, Epb[h], phi(Epb[h])[g])[0])
                growth_rate[h].append(mean(temp))
                errors[h].append(stdev(temp))
                print(growth_rate[h][-1])
                j += 1
                print(j)
    colours =['b', 'orange', 'g', 'r']
    for y in range(0,4):
        axis[0].errorbar(range(0,deltas), growth_rate[0][deltas * y:deltas * (y+1)], errors[0][deltas * y:deltas * (y+1)],marker = '.', color = colours[y], label=r"$\phi$ = "+str(y+2)+r"$E_{pb}$")
        axis[0].set_title(r'$E_{pb}=1kT$')
        axis[0].set(xlabel=r'$\Delta$$\mu$ in multiples of $kT$', ylabel='Growth Rate')
        #axis[0].set_ylim([0, 1])
        axis[0].legend()
        axis[1].errorbar(range(0,deltas), growth_rate[1][deltas * y:deltas * (y+1)], errors[1][deltas * y:deltas * (y+1)],marker = '.', color = colours[y], label=r"$\phi$ = "+str(y+2)+r"$E_{pb}$")
        axis[1].set_title(r'$E_{pb}=2kT$')
        axis[1].set(xlabel='$\Delta$$\mu$ in multiples of $kT$', ylabel='Growth  Rate')
        #axis[1].set_ylim([0, 1])
        axis[1].legend()
        axis[2].errorbar(range(0,deltas), growth_rate[2][deltas * y:deltas * (y+1)], errors[2][deltas * y:deltas * (y+1)],marker = '.', color = colours[y], label=r"$\phi$ = "+str(y+2)+r"$E_{pb}$")
        axis[2].set_title(r'$E_{pb}=3kT$')
        axis[2].set(xlabel='$\Delta$$\mu$ in multiples of $kT$', ylabel='Growth Rate')
        #axis[2].set_ylim([0, 1])
        axis[2].legend()
    
    print(tme.time() - start_time)
    #plt.savefig('final_pardec_model_50000_5repeats_20deltas.png')
    #plt.savefig('final_pardec_model_50000_5repeats_20deltas.pdf')
    plt.show()
