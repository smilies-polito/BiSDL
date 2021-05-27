from petrisim.utils import *


class E01(Module):
	def __init__(self, name):
		super().__init__(name)

	def build_net_structure(self) -> PetriNet:
		super(self.__class__, self).build_net_structure()

		# petri nets
		p2_0_net = PetriNet("p2_0_net", timescale=1)
		p1_0_net = PetriNet("p1_0_net", timescale=1)
		E01_net = PetriNet("E01_net", timescale=10)

		# p2_0_net places
		p2_0_net.add_place(Place("B_molecule"))

		# p2_0_net transitions
		p2_0_net.add_transition(Transition("B_molecule_degradation_1"))

		# p1_0_net places
		p1_0_net.add_place(Place("A_molecule"))
		p1_0_net.add_place(Place("B_molecule"))

		# p1_0_net transitions
		p1_0_net.add_transition(Transition("process_1"))

		# E01_net places
		E01_net.add_place(Place("s1", [ p1_0_net ]))
		E01_net.add_place(Place("s2", [ p2_0_net ]))

		# E01_net transitions
		E01_net.add_transition(Transition("juxtacrine_signaling_A_molecule_s1_s2_1", Expression("str(x) == 'A_molecule'")))

		# E01_net arcs
		E01_net.add_input("s1", "juxtacrine_signaling_A_molecule_s1_s2_1", Variable('x'), notify=[p1_0_net])
		E01_net.add_output("s2", "juxtacrine_signaling_A_molecule_s1_s2_1", Expression('x.replace("protein", "receptor_active_protein")'), notify=[p2_0_net])

		# p1_0_net arcs
		p1_0_net.add_input("A_molecule", "process_1", Value(dot), notify=[E01_net.place('s1')])
		p1_0_net.add_output("B_molecule", "process_1", MultiArc([Value(dot)]*3), notify=[E01_net.place('s1')])

		# p2_0_net arcs
		p2_0_net.add_input("B_molecule", "B_molecule_degradation_1", Value(dot), notify=[E01_net.place('s2')])


		return E01_net
