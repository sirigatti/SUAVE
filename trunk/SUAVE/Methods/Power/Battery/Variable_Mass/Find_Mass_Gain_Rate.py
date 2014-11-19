"""finds the mass gain rate of the battery from the ambient air"""
#by M. Vegh

""" SUAVE Methods for Energy Systems """

# ----------------------------------------------------------------------
#  Imports
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
#  Methods
# ----------------------------------------------------------------------

def Find_Mass_Gain_Rate(battery,power): #adds a battery that is optimized based on power and energy requirements and technology
    
    mdot=-(power) *(battery.mass_gain_factor)  #weight gain of battery (positive means mass loss)
                
    return mdot