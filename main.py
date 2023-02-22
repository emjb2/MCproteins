#from numba import jit
from monomer_model.make_plot import make_plot
from aggregate_model.make_plotA import make_plotA
from aggregate_model.make_single_plotA import make_single_plotA
from aggregate_model.make_size_investigation import make_size_investigation
from monomer_model.make_plot_final import make_plot_final
from AHIR_strep import make_plot_AHIR_strep
from AHIR_strep_pardec.make_plot_AHIR_strep_pardec import make_plot_AHIR_strep_pardec
from AHIR_strep_pardec.check_surface import check_surface

if __name__ == "__main__":
  # make_plot(30,200000,13)
  # make_plotA(30, 2000, 13)
  # make_single_plotA(30,200000,13)
  # make_size_investigation([30, 200, 1000], 1000, 13)
  # make_plot_final(30,200000,13)
  # make_plot_AHIR_strep.make_plot_AHIR_strep(29,20000,13)
  #make_plot_AHIR_strep_pardec(29,200,20)
  check_surface()