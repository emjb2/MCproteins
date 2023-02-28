from numba import jit
from monomer_model.take_step import take_step
import math
import numpy as np
from general_functions.div_zero_error import div_zero_error
from general_functions.unit_test_C_sum import unit_test_C_sum
from general_functions.find_type import find_type
from general_functions.neg_to_zero import neg_to_zero

# @jit
def run_simulation(n, deltaMu, phi, Epb, T, time):
    k = 1.380649 * (10 ** (-23))
    stacks = [1] * (n ** 2)
    for i in range(0, time):
        # ans = take_step(n, deltaMu, phi, Epb, T, stacks)
        # stacks = ans[0]
        stacks = take_step(n, deltaMu, phi, Epb, T, stacks)
    #return [neg_to_zero((5*sum(a-b for a,b in zip([a*b for a,b in zip(k_plus,C_plus)], [a*b for a,b in zip(k_,C)])))), stacks]
    # return [(1-math.e**(-deltaMu/(k*T)))*(attachment/summ), stacks]
    return [(sum(stacks)-(n**2)) / time, stacks]
    # return (1-math.exp(-deltaMu/(k*T)))*(np.dot(k_plus, C_plus))
