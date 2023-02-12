#from numba import jit
from aggregate_model.take_stepA import take_stepA
from math import e
import numpy as np
from general_functions.div_zero_error import div_zero_error
from general_functions.unit_test_C_sum import unit_test_C_sum
from general_functions.find_type import find_type
from general_functions.neg_to_zero import neg_to_zero
from general_functions.calc_mol_dist import calc_mol_dist

#Note the distribution of monomers to dimers to tetramers is found from:
#Journal of Crystal Growth
#Volume 110, Issues 1–2, 1 March 1991, Pages 60-65
#Journal of Crystal Growth
#Estimation of the initial equilibrium constants in the formation of tetragonal lysozyme nuclei
#Marc Lee Pusey


# @jit
def run_simulationA(n, deltaMu, phi, Epb, T, time):
    k = 1.380649 * (10 ** (-23))
    # attachment_rate = e **(deltaMu/(k*T))
    failed_attachments = 0
    attachment_attempts = 0
    attachment_count = 0
    removal_count = 0
    stacks = [1] * (n ** 2)
    mol_dist = calc_mol_dist(deltaMu,T)
    # This next line just ignores tetramers
    #mol_dist[2] = 0
    #sum_mol_dist = mol_dist[0] + mol_dist[1]
    #mol_dist = [mol_dist[0]/sum_mol_dist, mol_dist[1]/sum_mol_dist, 0]
    for i in range(0, time):
        ans = take_stepA(n, deltaMu, phi, Epb, T, stacks, mol_dist, attachment_attempts, attachment_count, removal_count, failed_attachments)
        stacks = ans[0]
        attachment_attempts = ans[1]
        attachment_count = ans[2]
        removal_count = ans[3]
        failed_attachments = ans[4]
    # THIS ONE return [neg_to_zero((5*sum(a-b for a,b in zip([a*b for a,b in zip(k_plus,C_plus)], [a*b for a,b in zip(k_,C)])))), stacks]
    # return [(1-math.e**(-deltaMu/(k*T)))*(attachment/summ), stacks]
    return [sum(stacks) / time, stacks]
    # return (1-math.exp(-deltaMu/(k*T)))*(np.dot(k_plus, C_plus))
    # print(div_zero_error((attachment_count-removal_count),attachment_attempts))
    # return [div_zero_error((attachment_count-removal_count),attachment_attempts), stacks]
    