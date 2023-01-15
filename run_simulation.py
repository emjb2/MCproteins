import take_step
import math
import numpy as np
from div_zero_error import div_zero_error


def run_simulation(n, deltaMu, phi, Epb, T, time):
    k = 1.380649 * (10 ** (-23))
    stacks = [0] * (n ** 2)
    NSi = np.zeros((time + 1, 5))
    NFi = np.zeros((time + 1, 5))
    NSi[0, :] = [0, 0, 0, 0, n ** 2]
    NFi[0,:] = [0, 0, 0, 0, 0]
    attachment = (math.e ** (deltaMu / (k * T)))
    detachment = math.e ** ((phi / (k * T)) - (1 * Epb / (k * T)))
    migration = math.e ** ((phi / (k * T)) - ((1 * Epb) / (k * T)) + (Epb / (2 * k * T)))
    summ = attachment + detachment
    k_plus = [5*attachment/(summ*9), attachment/(summ*9), attachment/(summ*9), attachment/(summ*9), attachment/(summ*9)]
    print(k_plus)
    # k_ = [0] * 5
    # for i in range(0,5):
    #     k_[i] = (math.exp(phi/(k*T)-(Epb*i)/(k*T))/math.exp(deltaMu/(k*T)))*k_plus[i]
    # print(k_)
    F_attempted = [0, 0, 0, 0, 0]
    F_completed = [0, 0, 0, 0, 0]
    S_attempted = [0, 0, 0, 0, 0]
    S_completed = [0, 0, 0, 0, 0]
    for i in range(0, time):
        ans = take_step.take_step(n, deltaMu, phi, Epb, T, stacks)
        # returns [buckets, NSi_change_remove, NSi_change_add, NFi_change_remove_F, NFi_change_add_F]
        # [buckets, F_or_S, F_tried, F_succeed, S_tried, S_succeed]
        stacks = ans[0]
        if ans[1] == "F":
            F_attempted[ans[2]] += 1
            if ans[3] is not None:
                F_completed[ans[3]] += 1
        elif ans[1] == "S":
            S_attempted[ans[4]] += 1
            if ans[5]:
                S_completed[ans[5]] += 1
        NSi[i+1, :] = NSi[i, :]
        NFi[i+1, :] = NFi[i, :]
        for p in range(0, len(ans[6])):
            NSi[i+1, ans[6][p]] = NSi[i+1, ans[6][p]] - 1
        for p in range(0, len(ans[7])):
            NSi[i+1, ans[7][p]] = NSi[i+1, ans[7][p]] + 1
        for p in range(0, len(ans[8])):
            NFi[i+1, ans[8][p]] = NFi[i+1, ans[8][p]] - 1
        for p in range(0, len(ans[9])):
            NFi[i+1, ans[9][p]] = NFi[i+1, ans[9][p]] + 1
    # C = [0] * 5
    # C_plus = [0] * 5
    # for p in range(0,5):
    #     C[p] = sum(NSi[:, p]) / ((n ** 2) * (time+1))
    #     C_plus[p] = sum(NFi[:, p]) / ((n ** 2) * (time+1))
    # for x in range(0, 5):
    #     for p in range(0,time):
    #         k[x] += NSi[p+1, x] - NSi[p, x]
    #         k_plus[x] += NFi[p+1, x] - NFi[p, x]
    #     k[x] = k[x] / time
    #     k_plus[x] = k_plus[x] / time
    # C = [div_zero_error(a,b) for a,b in zip(S_completed, S_attempted)]
    C_plus = [div_zero_error(a, b) for a,b in zip(F_completed, F_attempted)]
    print(C_plus)
    # return sum(a-b for a,b in zip([a*b for a,b in zip(k_plus,C_plus)], [a*b for a,b in zip(k_,C)]))
    return sum(stacks) / time
    # return (1-math.exp(-deltaMu/(k*T)))*(np.dot(k_plus, C_plus))
