import numpy as np
from matplotlib import pyplot as plt

class Backstrip(object):
  
  def __init__(self, rho_fill=None, porosity0 = 0.479, compaction_b = 0.42, \
                     lithology=[], rho_layers=[], z_layer_bottoms=[]):
    ###########################################
    # Class-wide constants; not always needed #
    ###########################################
    self.g = 9.8 # acceleration due to gravity
    self.E = 65E9 # Young's Modulus
    self.nu = 0.25 # Poisson's Ratio
    self.rho_m = 3300. # MantleDensity
    self.rho_fill = rho_fill # InfiillMaterialDensity
    
    #################################################################
    # Class-wide libraries of compaction constants by sediment type #
    #################################################################
      # From Backstrip-Mauricio.xls
      # From Table 8.1 North Sea
      # (Allen and Allen, p. 268) (from Slater and Christie (1981)
      self.compaction_decay_constants = {'sandstone':0.00027,
                                         'shaly sand':0.00039,
                                         'shale':0.00051,
                                         'chalk':0.00071}
    

    #####################
    # Input information #
    #####################
    self.rho_grain_layers = rho_layers # Layer average grain densities
                                       # (considering no porosity)
    self.z_layer_bottoms = z_layer_bottoms # Layer bottom elevations, 
                                           # bottom to top
                                           # with 0 being Earth's surface
                                           # This can be a list of numpy arrays
                                           # in the case of cross-sectional
                                           # profile or multiple wells / cores
                                           # / measured sections
                                           
    self.porosity_0 = porosity_0 # Often, $\Phi_0$
                                 # This is sea-floor porosity
                                 # Default value taken from 
                                 # Urgeles et al., 2010
                                 # for no particular reason
    self.compaction_b = compaction_b # Compaction exponential decay

    # DELETE ONCE SATISFIED WITH RELOACITON OF THIS!
    def dictionary_constants(self):
      """
      Phi = Phi_0 * exp(-b*z); z in meters
      """
      # From Backstrip-Mauricio.xls
      # From Table 8.1 North Sea
      # (Allen and Allen, p. 268) (from Slater and Christie (1981)
      self.compaction_decay_constants = {'sandstone':0.00027,
                                         'shaly sand':0.00039,
                                         'shale':0.00051,
                                         'chalk':0.00071}
      
      #################
      # Grain density #
      #################

      # From Backstrip-Mauricio.xls
      # From Table 8.1 North Sea
      # (Allen and Allen, p. 268) (from Slater and Christie (1981)
      self.density = {}
      self.density[''] = 

    def porosity(self):
      """
      Porosity = Porosity_0 * exp(-compaction_b * z)
      Here, z is given in meters
      """
      pass
    
    def decompact(self):
      pass
       

class LocalIsostasty(Backstrip):
  def __init__(self):
    pass


class FlexuralIsostasy1D(Backstrip):

  import gflex

  def __init__(self):
    ##########
    # SOLVER #
    ##########
    self.flex = gflex.F1D()
    self.flex.Quiet = True
    self.flex.Method = 'FD'
    self.flex.Solver = 'direct'
    
    #############
    # CONSTANTS #
    #############
    self.flex.g = self.g # acceleration due to gravity
    self.flex.E = self.E # Young's Modulus
    self.flex.nu = self.nu # Poisson's Ratio
    self.flex.rho_m = self.rho_m # MantleDensity
    self.flex.rho_fill = self.rho_fill # InfiillMaterialDensity



