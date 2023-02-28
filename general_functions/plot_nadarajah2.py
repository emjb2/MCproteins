from data.more_nadarajah_data import more_nadarajah_data
from matplotlib import pyplot as plt

def plot_nadarajah2():
    data = more_nadarajah_data()
    plt.plot(data[0][:12], data[1][:12], marker='.', color = 'r', label = "50mg/ml lysozyme")
    plt.plot(data[0][12:21], data[1][12:21], marker='.', color = 'g', label = "40mg/ml lysozyme")
    plt.plot(data[0][21:], data[1][21:], marker='.', color = 'b', label = "30mg/ml lysozyme")

    plt.title("Nadarajah et al: Protein Crystallisation Growth Rates")
    plt.xlabel("Growth Rate")
    plt.ylabel("Apparent Supersaturation")
    plt.legend()
    plt.show()