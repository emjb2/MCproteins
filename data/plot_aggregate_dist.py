from data.monomer_dimer_tetramer import monomer_dimer_tetramer
from matplotlib import pyplot as plt

def plot_aggregate_dist():
    data2 = monomer_dimer_tetramer()[1]
    concentration = [[], [], []]
    supersaturation = [range(13), range(13), range(13)]
    for j in range(13):
        for i in range(3):
            concentration[i].append(data2[j+i*13])

    colours = ['lightskyblue', 'gold', 'mediumvioletred']
    labels = ['monomer', 'dimer', 'tetramer']
    for i in range(3):
        plt.plot(supersaturation[i], concentration[i], color = colours[i], marker = '.', label = labels[i])
    plt.title("Ke et al: concentration of monomers, dimers and tetramers in solution")
    plt.xlabel('Supersaturation'), 
    plt.ylabel('Relative Concentration')
    plt.xlim(0, 12)
    plt.ylim(0, max(data2)*1.1)
    plt.legend()
    plt.savefig('IKEA aggregate_dist.png')
    plt.show()

