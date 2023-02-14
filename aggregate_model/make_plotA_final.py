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

# @jit
def make_plotA_final(n, time, deltas):
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
    figure, axis = plt.subplots(1, 3, figsize=(15,7))
    figure.tight_layout(pad=5.0)
    for h in range(3):
        for i in phi(Epb[h]):
            for x in deltaMu:
                temp_data = []
                for g in range(5):
                    temp_data.append(run_simulationA(n, x, i, Epb[h], T, time)[0])
                growth_rate[h].append(np.mean(temp_data))
                errorbars[h].append(np.std(temp_data))
                j += 1
                print(j)
    for y in range(0,4):
        axis[0].errorbar(range(0,deltas), growth_rate[0][deltas * y:deltas * (y+1)], yerr = errorbars[0][deltas * y:deltas * (y+1)], label=y+2)
        #axis[0].plot(range(0,deltas), ke_data[0][13 * y:deltas * (y+1)], colours[-y-1])
        axis[0].set_title(r'$E_{pb}$ is set to 1*($kT$)')
        axis[0].set(xlabel=r'$\Delta$$\mu$ in multiples of $kT$', ylabel='Growth Rate')
        axis[0].legend()
        #axis[1].plot(range(0,deltas), ke_data[1][deltas * y:deltas * (y+1)], colours[-y-1])
        axis[1].errorbar(range(0,deltas), growth_rate[1][deltas * y:deltas * (y+1)], yerr = errorbars[1][deltas * y:deltas * (y+1)], label=y+2)
        axis[1].set_title(r'$E_{pb}$ is set to 2*($kT$)')
        axis[1].set(xlabel='$\Delta$$\mu$ in multiples of $kT$', ylabel='Growth  Rate')
        axis[1].legend()
        #axis[2].plot(range(0,deltas), ke_data[2][deltas * y:deltas * (y+1)], colours[-y-1])
        axis[2].errorbar(range(0,deltas), growth_rate[2][deltas * y:deltas * (y+1)], yerr = errorbars[2][deltas * y:deltas * (y+1)], label=y+2)
        axis[2].set_title(r'$E_{pb}$ is set to 3*($kT$)')
        axis[2].set(xlabel='$\Delta$$\mu$ in multiples of $kT$', ylabel='Growth Rate')
        axis[2].legend()
    
    print(tme.time() - start_time)
    plt.savefig('make_plotA_final.png')
    plt.savefig('make_plotA_final.pdf')
    plt.show()
