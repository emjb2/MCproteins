#from numba import jit
from monomer_model.make_plot import make_plot
from aggregate_model.make_plotA import make_plotA
from aggregate_model.make_single_plotA import make_single_plotA
from aggregate_model.make_size_investigation import make_size_investigation
from monomer_model.make_plot_final import make_plot_final

if __name__ == "__main__":
  # make_plot(30,200000,13)
  # make_plotA(30, 2000, 13)
  # make_single_plotA(30,200000,13)
  # make_size_investigation([30, 200, 1000], 1000, 13)
  make_plot_final(30,200000,13)
