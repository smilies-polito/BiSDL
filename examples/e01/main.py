from petrisim.utils import *


class E01(Module):
	def __init__(self, name: str = None):
		if not name:
			name = __class__.__name__
		super().__init__(name)

	def build_net_structure(self) -> PetriNet:
		# petri nets
		p2_0_net = PetriNet("p2_0_net", timescale=1)
		p1_0_net = PetriNet("p1_0_net", timescale=1)
		e01_net = PetriNet("e01_net", timescale=10)

		# p2_0_net places
		p2_0_net.add_place(Place("B_molecule"))

		# p2_0_net transitions
		p2_0_net.add_transition(Transition("B_molecule_degradation_1"))

		# p1_0_net places
		p1_0_net.add_place(Place("A_molecule"))
		p1_0_net.add_place(Place("B_molecule"))

		# p1_0_net transitions
		p1_0_net.add_transition(Transition("process_1"))

		# e01_net places
		e01_net.add_place(Place("s1", [ p1_0_net ]))
		e01_net.add_place(Place("s2", [ p2_0_net ]))

		# e01_net transitions
		e01_net.add_transition(Transition("juxtacrine_signaling_A_molecule_s1_s2_1", Expression("str(x) == 'A_molecule'")))

		# e01_net arcs
		e01_net.add_input("s1", "juxtacrine_signaling_A_molecule_s1_s2_1", Variable('x'), notify=[p1_0_net])
		e01_net.add_output("s2", "juxtacrine_signaling_A_molecule_s1_s2_1", Expression('x.replace("protein", "receptor_active_protein")'), notify=[p2_0_net])

		# p1_0_net arcs
		p1_0_net.add_input("A_molecule", "process_1", Value(dot), notify=[e01_net.place('s1')])
		p1_0_net.add_output("B_molecule", "process_1", MultiArc([Value(dot)]*3), notify=[e01_net.place('s1')])

		# p2_0_net arcs
		p2_0_net.add_input("B_molecule", "B_molecule_degradation_1", Value(dot), notify=[e01_net.place('s2')])


		return e01_net


if __name__ == "__main__":
	import os
	from petrisim.simulator import *
	test_module = E01()
	output_path = os.path.join(".", "results")
	n_steps = 100
	s = Simulator(m=test_module, output_path=output_path, draw_nets=False)
	s.draw_nets(os.path.join(output_path, "../topology"))

	marking = test_module.get_marking()
	marking['e01_net']['s1'].add(["A_molecule"]*50)
	marking['p1_0_net']['A_molecule'].add([BlackToken()]*50)
	s.set_initial_marking(marking)

	# execute step-by-step
	for _ in range(n_steps//2):
		s.step()
	# resume with straightforward execution
	s.execute(n_steps//2)
	s.make_charts()
	with open(os.path.join(output_path, "ascii_net_structure.txt"), 'w') as fp:
		print(test_module, file=fp)
