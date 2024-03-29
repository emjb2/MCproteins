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
from AHIR_strep.AHIR_strep_run_simulation_same_detach_AHIR_strep import AHIR_strep_run_simulation_same_detach_AHIR_strep
from statistics import stdev, mean

# @jit
def make_plot_final_surface_AHIR_strep_same_detach(n, time, deltas):
    start_time = tme.time()
    # first set our parameters
    k = 1.380649 * (10 ** (-23))
    T = 290
    Epb = [1*k*T, 2*k*T, 3*k*T]
    deltaMu = [x*k*T for x in range(0, deltas)]
    roughness = [[], [], []]
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
                for l in range(10):
                    soln = AHIR_strep_run_simulation_same_detach_AHIR_strep(n, time, x, T, Epb[h], phi(Epb[h])[g])[2]
                    soln2 = [x for x in soln if x != 0]
                    stdeviation = stdev(soln2)
                    temp.append(stdeviation)
                roughness[h].append(mean(temp))
                errors[h].append(stdev(temp))
                j += 1
                print(j)
    colours = ['mediumvioletred', 'lightskyblue', 'forestgreen', 'gold']
    intermediate = min(roughness[0]+roughness[1]+roughness[2])
    intermediate2 = max(roughness[0]+roughness[1]+roughness[2])
    errorbarlims = [max(errors[i]) for i in range(len(errors))]
    for y in range(0,4):
        [xmin, xmax, ymin, ymax] = [0, deltas-1, 0, intermediate2]
        axis[0].errorbar(range(0,deltas), roughness[0][deltas * y:deltas * (y+1)], errors[0][deltas * y:deltas * (y+1)], marker = '.', color = colours[y], label=r"$\phi$ = "+str(y+2)+r"$E_{pb}$")
        axis[0].set_title(r'$E_{pb}=1kT$')
        axis[0].set(xlabel=r'$\Delta$$\mu$ in multiples of $kT$', ylabel='Growth Rate')
        axis[0].set_xlim(xmin, xmax)
        axis[0].set_ylim(ymin, ymax + max(errorbarlims))
        axis[0].legend()
        axis[1].errorbar(range(0,deltas), roughness[1][deltas * y:deltas * (y+1)], errors[1][deltas * y:deltas * (y+1)], marker = '.', color = colours[y], label=r"$\phi$ = "+str(y+2)+r"$E_{pb}$")
        axis[1].set_title(r'$E_{pb}=2kT$')
        axis[1].set(xlabel='$\Delta$$\mu$ in multiples of $kT$', ylabel='Growth  Rate')
        axis[1].set_xlim(xmin, xmax)
        axis[1].set_ylim(ymin, ymax + max(errorbarlims))
        axis[1].legend()
        axis[2].errorbar(range(0,deltas), roughness[2][deltas * y:deltas * (y+1)], errors[2][deltas * y:deltas * (y+1)], marker = '.', color = colours[y], label=r"$\phi$ = "+str(y+2)+r"$E_{pb}$")
        axis[2].set_title(r'$E_{pb}=3kT$')
        axis[2].set(xlabel='$\Delta$$\mu$ in multiples of $kT$', ylabel='Growth Rate')
        axis[2].set_xlim(xmin, xmax)
        axis[2].set_ylim(ymin, ymax + max(errorbarlims))
        axis[2].legend()
    
    print(tme.time() - start_time)
    plt.savefig('IKEA AHIR strep surface same detach 50000.png')
