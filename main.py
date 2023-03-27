from monomer_model.make_plot import make_plot
from aggregate_model.make_plotA import make_plotA
from aggregate_model.make_single_plotA import make_single_plotA
from aggregate_model.make_size_investigation import make_size_investigation
from monomer_model.make_plot_final import make_plot_final
from AHIR_strep.make_plot_AHIR_strep import make_plot_AHIR_strep
from AHIR_strep_pardec.make_plot_AHIR_strep_pardec import make_plot_AHIR_strep_pardec
from AHIR_strep_pardec.check_surface import check_surface
from monomer_model.make_Ke_comparison_plot import make_Ke_comparison_plot
from monomer_model.calibrate_lattice_size import calibrate_lattice_size
from monomer_model.calibrate_time_steps import calibrate_time_steps
from general_functions.plot_nadarajah2 import plot_nadarajah2
from aggregate_model.make_plotA_final import make_plotA_final
from general_functions.monomer_dimer_tetramer import plot_monomer_dimer_tetramer
from monomer_model.make_plot_final_surface import make_plot_final_surface
from aggregate_model.make_plotA_final_surface import make_plotA_final_surface
from aggregate_model.nadarajah_comparison import nadarajah_comparison
from AHIR_strep.make_plot_final_AHIR_strep import make_plot_final_AHIR_strep
from AHIR_strep.make_plot_final_surface_AHIR_strep import make_plot_final_surface_AHIR_strep
from AHIR_strep_pardec.make_plot_final_pardec import make_plot_final_pardec
from AHIR_strep_pardec.final_surface_pardec import final_surface_pardec
from monomer_model.calibrate_lattice_size_roughness import calibrate_lattice_size_roughness
from monomer_model.calibrate_time_steps_roughness import calibrate_time_steps_roughness
from monomer_model.make_Ke_comparison_plot_2 import make_Ke_comparison_plot_2
from data.plot_aggregate_dist import plot_aggregate_dist
from data.nadarajah_data_plot import nadarajah_data_plot
from AHIR_strep.make_plot_final_AHIR_strep_same_detach import make_plot_final_AHIR_strep_same_detach
from AHIR_strep.make_plot_final_surface_AHIR_strep_same_detach import make_plot_final_surface_AHIR_strep_same_detach
from AHIR_strep_pardec.run_a_bunch import run_a_bunch
from AHIR_strep_pardec.run_a_bunch_all_fuldec import run_a_bunch_all_fuldec
from AHIR_strep_pardec.run_a_bunch_surface import run_a_bunch_surface
from AHIR_strep_pardec.run_a_bunch_all_fuldec_surface import run_a_bunch_all_fuldec_surface
from aggregate_model.new_make_plot import new_make_plot
from AHIR_strep_pardec.best_strep_level import best_strep_level
from AHIR_strep_pardec.check_different_phi import check_different_phi
from AHIR_strep_pardec.check_different_phi_surface import check_different_phi_surface

if __name__ == "__main__":
  # make_plot(30,200000,13)
  # make_plotA(30, 2000, 13)
  # make_single_plotA(30,200000,13)
  # make_size_investigation([30, 200, 1000], 1000, 13)
  # make_plot_final(30,1000,20)
  # make_plot_AHIR_strep(29,20000,13)
  # make_plot_AHIR_strep_pardec(29,200,20)
  # check_surface(200000)
  # make_Ke_comparison_plot(30,200000,13)
  # make_Ke_comparison_plot_2(30,200000,13)
  # calibrate_lattice_size(10000, 13)
  # calibrate_lattice_size_roughness(50000,13)
  #T1 calibrate_time_steps(30, 13)
  #T2 calibrate_time_steps_roughness(30, 13)
  # plot_nadarajah2()
  # make_plotA(30, 100, 13)
  # make_plotA_final(30, 100000, 13)
  # plot_monomer_dimer_tetramer()
  # plot_monomer_dimer_tetramer()
  # make_plot_final_surface(30, 1000, 15)
  # make_plotA_final_surface(30, 50000, 13)
  # nadarajah_comparison(30,50000,13)
  # make_plot_final_AHIR_strep(30,100000,20)
  # make_plot_final_surface_AHIR_strep(30,50000,20)
  # make_plot_final_pardec(30,50000,20)
  # final_surface_pardec(30,50000,20)
 # calibrate_time_steps(30, 13)
  calibrate_time_steps_roughness(30, 13)
 # make_Ke_comparison_plot(30,200000,13)
 # make_Ke_comparison_plot_2(30,200000,13)
 # make_plot_final(30,50000,20)
 # make_plot_final_surface(30,50000,20)
 # make_plotA(30,100000,13)
 # make_plotA_final_surface(30,10000,13)
 # nadarajah_data_plot()
 # make_plotA_final(30, 100000, 13)
 # make_plot_final_AHIR_strep(30,1000,20)
 
 
 # make_plot_final_surface_AHIR_strep(30,50000,20)
 # make_plot_final_surface_AHIR_strep_same_detach(30,50000,20)
 # make_plot_final_AHIR_strep_same_detach(30,50000,20)
  
  
  
  #run_a_bunch(30,200000,20)
  #run_a_bunch_all_fuldec(30,200000,20)
  #run_a_bunch_surface(30,200000,20)
  #run_a_bunch_all_fuldec_surface(30,200000,20)
  #make_Ke_comparison_plot(30,200000,13)
  #make_Ke_comparison_plot_2(30,200000,20)
  #new_make_plot(30, 50000, 13)


  #best_strep_level(30,100000)
  # once you've found this level then trial a bunch of different phi and Epb just to check.
  # Dan seems to think strong phi is bad.

  #check_different_phi(30,50000,20)
  #check_different_phi_surface(30,50000,20)