from AHIR_strep_pardec.AHIR_strep_run_simulation_pardec import AHIR_strep_run_simulation_pardec
from general_functions.line_to_array import line_to_array
import seaborn
import matplotlib.pyplot as plt

k = 1.380649*(10**(-23))

def check_surface(time):
    dummy2=AHIR_strep_run_simulation_pardec(30, time, 12*k*290, 290, 1)
    maxx = max(dummy2[1])
    seaborn.heatmap(line_to_array(dummy2[1],30), vmin=0, vmax=maxx)
    plt.show()