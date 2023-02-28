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
from AHIR_strep.AHIR_strep_run_simulation import AHIR_strep_run_simulation

# @jit
def make_plot_final_AHIR_strep(n, time, deltas):
    start_time = tme.time()
    # first set our parameters
    k = 1.380649 * (10 ** (-23))
    T = 290
    Epb = [1*k*T, 2*k*T, 3*k*T]
    deltaMu = [x*k*T for x in range(0, deltas)]
    growth_rate = [[], [], []]
    trial_slope = plot_monomer_dimer_tetramer()
    def phi(Epb):
        return [2*Epb, 3*Epb, 4*Epb, 5*Epb]
    j=0
    #figure, axis = plt.subplots(1, 3, figsize=(15,7))
    #figure.tight_layout(pad=5.0)
    trial_end=[]
    for h in range(1):
        for x in deltaMu:
            growth_rate[h].append(AHIR_strep_run_simulation(n, time, x, T))
            if x == 12*k*T and h == 0:
                trial_end.append(growth_rate[h][-1])
            j += 1
            print(j)
    trial_mean = sum(trial_end)/len(trial_end)
    colours =['b', 'orange', 'g', 'r']
    trial_points = []
    for i in range(13):
        trial_points.append(trial_slope*i+(trial_mean-12*trial_slope))
    for y in range(0,4):
    #    axis[0].plot(range(0,deltas), growth_rate[0][deltas * y:deltas * (y+1)], marker = '.', color = colours[y], label=r"$\phi$ = "+str(y+2)+r"$E_{pb}$")
        #axis[0].plot(range(0,deltas), ke_data[0][13 * y:deltas * (y+1)], colours[-y-1])
    #    axis[0].plot(range(13), trial_points)
    #    axis[0].set_title(r'$E_{pb}=1kT$')
    #    axis[0].set(xlabel=r'$\Delta$$\mu$ in multiples of $kT$', ylabel='Growth Rate')
    #    axis[0].set_ylim([0, 0.6])
    #    axis[0].legend()

        plt.plot(range(0,deltas), growth_rate[0][deltas * y:deltas * (y+1)], marker = '.', color = colours[y], label=r"$\phi$ = "+str(y+2)+r"$E_{pb}$")
        plt.plot(range(13), trial_points)
        plt.title(r'$E_{pb}=1kT$')
        plt.xlabel(r'$\Delta$$\mu$ in multiples of $kT$')
        plt.ylabel('Growth Rate')
        plt.ylim([0, 0.6])
        plt.legend()


        #axis[1].plot(range(0,deltas), ke_data[1][deltas * y:deltas * (y+1)], colours[-y-1])
    #    axis[1].plot(range(0,deltas), growth_rate[1][deltas * y:deltas * (y+1)], marker = '.', color = colours[y], label=r"$\phi$ = "+str(y+2)+r"$E_{pb}$")
    #    axis[1].set_title(r'$E_{pb}=2kT$')
    #    axis[1].set(xlabel='$\Delta$$\mu$ in multiples of $kT$', ylabel='Growth  Rate')
    #    axis[1].set_ylim([0, 0.6])
    #    axis[1].legend()
        #axis[2].plot(range(0,deltas), ke_data[2][deltas * y:deltas * (y+1)], colours[-y-1])
    #    axis[2].plot(range(0,deltas), growth_rate[2][deltas * y:deltas * (y+1)], marker = '.', color = colours[y], label=r"$\phi$ = "+str(y+2)+r"$E_{pb}$")
    #    axis[2].set_title(r'$E_{pb}=3kT$')
    #    axis[2].set(xlabel='$\Delta$$\mu$ in multiples of $kT$', ylabel='Growth Rate')
    #    axis[2].set_ylim([0, 0.6])
    #    axis[2].legend()
    
    print(tme.time() - start_time)
    #plt.savefig('make_plotA_final2.png')
    #plt.savefig('make_plotA_final2.pdf')
    plt.show()
