from petrisim.utils import *


class Diopo(Module):
	def __init__(self, name: str = None):
		if not name:
			name = __class__.__name__
		super().__init__(name)

	def build_net_structure(self) -> PetriNet:

		# petri nets
		controller_0_net = PetriNet("controller_0_net", timescale=1)
		diopo_net = PetriNet("diopo_net", timescale=1)

		# controller_0_net places
		controller_0_net.add_place(Place("Lux1_protein"))
		controller_0_net.add_place(Place("SAM_molecule"))
		controller_0_net.add_place(Place("ACP_molecule"))
		controller_0_net.add_place(Place("_3OC6HSL_molecule"))

		# controller_0_net transitions
		controller_0_net.add_transition(Transition("enzymatic_reaction_1"))

		# diopo_net places
		diopo_net.add_place(Place("controller_compartment", [ controller_0_net ]))

		# diopo_net transitions


		# diopo_net arcs



		# controller_0_net arcs
		controller_0_net.add_input("Lux1_protein", "enzymatic_reaction_1", Value(dot), notify=[diopo_net.place('controller_compartment')])
		controller_0_net.add_input("SAM_molecule", "enzymatic_reaction_1", Value(dot), notify=[diopo_net.place('controller_compartment')])
		controller_0_net.add_input("ACP_molecule", "enzymatic_reaction_1", Value(dot), notify=[diopo_net.place('controller_compartment')])
		controller_0_net.add_output("Lux1_protein", "enzymatic_reaction_1", Value(dot), notify=[diopo_net.place('controller_compartment')])
		controller_0_net.add_output("_3OC6HSL_molecule", "enzymatic_reaction_1", Value(dot), notify=[diopo_net.place('controller_compartment')])
		return diopo_net
