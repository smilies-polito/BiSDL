from petrisim.utils import *


class Pt(Module):
	def __init__(self, name: str = None):
		if not name:
			name = __class__.__name__
		super().__init__(name)

	def build_net_structure(self) -> PetriNet:

		# petri nets
		transconjugant_0_net = PetriNet("transconjugant_0_net", timescale=2)
		pilus_0_net = PetriNet("pilus_0_net", timescale=4)
		donor_0_net = PetriNet("donor_0_net", timescale=2)
		pt_net = PetriNet("pt_net", timescale=1)

		# transconjugant_0_net places
		transconjugant_0_net.add_place(Place("linear_plasmid_molecule"))
		transconjugant_0_net.add_place(Place("circular_plasmid_molecule"))
		transconjugant_0_net.add_place(Place("R_mrna"))
		transconjugant_0_net.add_place(Place("R_protein"))
		transconjugant_0_net.add_place(Place("pilus_mrna"))
		transconjugant_0_net.add_place(Place("pilus_protein"))

		# transconjugant_0_net transitions
		transconjugant_0_net.add_transition(Transition("process_5"))
		transconjugant_0_net.add_transition(Transition("process_6"))
		transconjugant_0_net.add_transition(Transition("R_mrna_translation_2"))
		transconjugant_0_net.add_transition(Transition("process_7"))
		transconjugant_0_net.add_transition(Transition("pilus_mrna_translation_2"))
		transconjugant_0_net.add_transition(Transition("R_mrna_degradation_2"))
		transconjugant_0_net.add_transition(Transition("pilus_mrna_degradation_2"))
		transconjugant_0_net.add_transition(Transition("R_protein_degradation_2"))
		transconjugant_0_net.add_transition(Transition("pilus_protein_degradation_2"))

		# pilus_0_net places
		pilus_0_net.add_place(Place("linear_plasmid_molecule"))

		# pilus_0_net transitions
		pilus_0_net.add_transition(Transition("process_4"))

		# donor_0_net places
		donor_0_net.add_place(Place("circular_plasmid_molecule"))
		donor_0_net.add_place(Place("R_mrna"))
		donor_0_net.add_place(Place("R_protein"))
		donor_0_net.add_place(Place("pilus_mrna"))
		donor_0_net.add_place(Place("pilus_protein"))
		donor_0_net.add_place(Place("linear_plasmid_molecule"))

		# donor_0_net transitions
		donor_0_net.add_transition(Transition("process_1"))
		donor_0_net.add_transition(Transition("R_mrna_translation_1"))
		donor_0_net.add_transition(Transition("process_2"))
		donor_0_net.add_transition(Transition("pilus_mrna_translation_1"))
		donor_0_net.add_transition(Transition("process_3"))
		donor_0_net.add_transition(Transition("R_mrna_degradation_1"))
		donor_0_net.add_transition(Transition("pilus_mrna_degradation_1"))
		donor_0_net.add_transition(Transition("R_protein_degradation_1"))
		donor_0_net.add_transition(Transition("pilus_protein_degradation_1"))

		# pt_net places
		pt_net.add_place(Place("donor", [ donor_0_net ]))
		pt_net.add_place(Place("pilus", [ pilus_0_net ]))
		pt_net.add_place(Place("transconjugant", [ transconjugant_0_net ]))

		# pt_net transitions
		pt_net.add_transition(Transition("juxtacrine_signaling_linear_plasmid_molecule_donor_pilus_1", Expression("str(x) == 'linear_plasmid_molecule'")))
		pt_net.add_transition(Transition("juxtacrine_signaling_linear_plasmid_molecule_pilus_transconjugant_1", Expression("str(x) == 'linear_plasmid_molecule'")))

		# pt_net arcs
		pt_net.add_input("donor", "juxtacrine_signaling_linear_plasmid_molecule_donor_pilus_1", Variable('x'), notify=[donor_0_net])
		pt_net.add_input("pilus", "juxtacrine_signaling_linear_plasmid_molecule_pilus_transconjugant_1", Variable('x'), notify=[pilus_0_net])
		pt_net.add_output("pilus", "juxtacrine_signaling_linear_plasmid_molecule_donor_pilus_1", Expression('x.replace("protein", "receptor_active_protein")'), notify=[pilus_0_net])
		pt_net.add_output("transconjugant", "juxtacrine_signaling_linear_plasmid_molecule_pilus_transconjugant_1", Expression('x.replace("protein", "receptor_active_protein")'), notify=[transconjugant_0_net])

		# donor_0_net arcs
		donor_0_net.add_input("circular_plasmid_molecule", "process_1", Value(dot), notify=[pt_net.place('donor')])
		donor_0_net.add_input("R_mrna", "R_mrna_translation_1", Value(dot))
		donor_0_net.add_input("circular_plasmid_molecule", "process_2", Value(dot), notify=[pt_net.place('donor')])
		donor_0_net.add_input("pilus_mrna", "pilus_mrna_translation_1", Value(dot))
		donor_0_net.add_input("circular_plasmid_molecule", "process_3", Value(dot), notify=[pt_net.place('donor')])
		donor_0_net.add_input("pilus_protein", "process_3", MultiArc([Value(dot)]*2), notify=[pt_net.place('donor')])
		donor_0_net.add_input("R_mrna", "R_mrna_degradation_1", Value(dot))
		donor_0_net.add_input("pilus_mrna", "pilus_mrna_degradation_1", Value(dot))
		donor_0_net.add_input("R_protein", "R_protein_degradation_1", Value(dot), notify=[pt_net.place('donor')])
		donor_0_net.add_input("pilus_protein", "pilus_protein_degradation_1", Value(dot), notify=[pt_net.place('donor')])
		donor_0_net.add_output("R_mrna", "process_1", Value(dot))
		donor_0_net.add_output("circular_plasmid_molecule", "process_1", Value(dot), notify=[pt_net.place('donor')])
		donor_0_net.add_output("R_protein", "R_mrna_translation_1", Value(dot), notify=[pt_net.place('donor')])
		donor_0_net.add_output("pilus_mrna", "process_2", Value(dot))
		donor_0_net.add_output("circular_plasmid_molecule", "process_2", Value(dot), notify=[pt_net.place('donor')])
		donor_0_net.add_output("pilus_protein", "pilus_mrna_translation_1", Value(dot), notify=[pt_net.place('donor')])
		donor_0_net.add_output("circular_plasmid_molecule", "process_3", Value(dot), notify=[pt_net.place('donor')])
		donor_0_net.add_output("linear_plasmid_molecule", "process_3", Value(dot), notify=[pt_net.place('donor')])

		# pilus_0_net arcs
		pilus_0_net.add_input("linear_plasmid_molecule", "process_4", Value(dot), notify=[pt_net.place('pilus')])
		pilus_0_net.add_output("linear_plasmid_molecule", "process_4", Value(dot), notify=[pt_net.place('pilus')])

		# transconjugant_0_net arcs
		transconjugant_0_net.add_input("linear_plasmid_molecule", "process_5", Value(dot), notify=[pt_net.place('transconjugant')])
		transconjugant_0_net.add_input("circular_plasmid_molecule", "process_6", Value(dot), notify=[pt_net.place('transconjugant')])
		transconjugant_0_net.add_input("R_mrna", "R_mrna_translation_2", Value(dot))
		transconjugant_0_net.add_input("circular_plasmid_molecule", "process_7", Value(dot), notify=[pt_net.place('transconjugant')])
		transconjugant_0_net.add_input("pilus_mrna", "pilus_mrna_translation_2", Value(dot))
		transconjugant_0_net.add_input("R_mrna", "R_mrna_degradation_2", Value(dot))
		transconjugant_0_net.add_input("pilus_mrna", "pilus_mrna_degradation_2", Value(dot))
		transconjugant_0_net.add_input("R_protein", "R_protein_degradation_2", Value(dot), notify=[pt_net.place('transconjugant')])
		transconjugant_0_net.add_input("pilus_protein", "pilus_protein_degradation_2", Value(dot), notify=[pt_net.place('transconjugant')])
		transconjugant_0_net.add_output("circular_plasmid_molecule", "process_5", Value(dot), notify=[pt_net.place('transconjugant')])
		transconjugant_0_net.add_output("R_mrna", "process_6", Value(dot))
		transconjugant_0_net.add_output("circular_plasmid_molecule", "process_6", Value(dot), notify=[pt_net.place('transconjugant')])
		transconjugant_0_net.add_output("R_protein", "R_mrna_translation_2", Value(dot), notify=[pt_net.place('transconjugant')])
		transconjugant_0_net.add_output("pilus_mrna", "process_7", Value(dot))
		transconjugant_0_net.add_output("circular_plasmid_molecule", "process_7", Value(dot), notify=[pt_net.place('transconjugant')])
		transconjugant_0_net.add_output("pilus_protein", "pilus_mrna_translation_2", Value(dot), notify=[pt_net.place('transconjugant')])
		return pt_net
