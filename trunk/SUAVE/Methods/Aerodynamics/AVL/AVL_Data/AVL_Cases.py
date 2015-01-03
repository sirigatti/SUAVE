# Tim Momose, October 2014

# ----------------------------------------------------------------------
#  Imports
# ----------------------------------------------------------------------

from SUAVE.Structure import Data


# ------------------------------------------------------------
#   Configuration
# ------------------------------------------------------------

class AVL_Cases(Data):

	def __defaults__(self):
		
		self.num_cases = 0
		self.cases = Data()


	def append_case(self,case):
		""" adds a case to the set of run cases """

		# assert database type
		if not isinstance(case,Data):
			raise Component_Exception, 'input component must be of type Data()'

		# store data with the appropriate case index
		# AVL uses indices starting from 1, not 0!
		self.num_cases += 1
		case.index = self.num_cases
		self.cases.append(case)

		return

# ------------------------------------------------------------
#  AVL Case
# ------------------------------------------------------------

class AVL_Run_Case(Data):
	def __defaults__(self):
		"""
		OUTPUTS:
			- 'aerodynamic' (CL, CD, CM)
			- 'body derivatives' (CMa,CNb,Clb,
			- 'stability derivatives (
			
		"""
		
		self.index = 0		# Will be overwritten when appended to an AVL_Cases structure
		self.tag   = 'Case'
		self.mass  = None
		
		self.conditions = Data()
		self.stability_and_control = Data()
		free = Data()
		aero = Data()
		
		free.mach     = None
		free.velocity = None
		free.density  = None
		free.gravitational_acceleration = None
		
		aero.parasite_drag    = None
		aero.angle_of_attack  = None
		aero.side_slip_angle  = None
		
		self.stability_and_control.control_deflections = None
		self.conditions.freestream = free
		self.conditions.aerodynamics = aero
		
		self.result_filename = None


	def append_control_deflection(self,control_tag,deflection):
		""" adds a control deflection case """
		control_deflection = Data()
		control_deflection.tag        = control_tag
		control_deflection.deflection = deflection
		if self.stability_and_control.control_deflections is None:
			self.stability_and_control.control_deflections = Data()
		self.stability_and_control.control_deflections.append(control_deflection)
		
		return
