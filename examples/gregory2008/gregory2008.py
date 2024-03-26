from petrisim.utils import *


class Gregory2008(Module):
	def __init__(self, name: str = None):
		if not name:
			name = __class__.__name__
		super().__init__(name)

	def build_net_structure(self) -> PetriNet:

		# petri nets
		transconjugant_0_net = PetriNet("transconjugant_0_net", timescale=1)
		donor_0_net = PetriNet("donor_0_net", timescale=1)
		gregory2008_net = PetriNet("gregory2008_net", timescale=1)

		# transconjugant_0_net places
		transconjugant_0_net.add_place(Place("R_plasmid_molecule"))
		transconjugant_0_net.add_place(Place("R_protein_molecule"))
		transconjugant_0_net.add_place(Place("R_plasmid_strand_molecule"))

		# transconjugant_0_net transitions
		transconjugant_0_net.add_transition(Transition("process_4"))
		transconjugant_0_net.add_transition(Transition("process_5"))
		transconjugant_0_net.add_transition(Transition("R_plasmid_strand_molecule_inhibition_R_plasmid_molecule_1"))
		transconjugant_0_net.add_transition(Transition("R_protein_molecule_degradation_2"))
		transconjugant_0_net.add_transition(Transition("R_plasmid_strand_molecule_degradation_1"))

		# donor_0_net places
		donor_0_net.add_place(Place("R_plasmid_molecule"))
		donor_0_net.add_place(Place("R_protein_molecule"))
		donor_0_net.add_place(Place("pilus_molecule"))
		donor_0_net.add_place(Place("R_plasmid_strand_molecule"))

		# donor_0_net transitions
		donor_0_net.add_transition(Transition("process_1"))
		donor_0_net.add_transition(Transition("process_2"))
		donor_0_net.add_transition(Transition("process_3"))
		donor_0_net.add_transition(Transition("R_protein_molecule_degradation_1"))
		donor_0_net.add_transition(Transition("pilus_molecule_degradation_1"))

		# gregory2008_net places
		gregory2008_net.add_place(Place("donor", [ donor_0_net ]))
		gregory2008_net.add_place(Place("transconjugant", [ transconjugant_0_net ]))

		# gregory2008_net transitions
		gregory2008_net.add_transition(Transition("juxtacrine_signaling_R_plasmid_strand_molecule_donor_transconjugant_1", Expression("str(x) == 'R_plasmid_strand_molecule'")))

		# gregory2008_net arcs
		gregory2008_net.add_input("donor", "juxtacrine_signaling_R_plasmid_strand_molecule_donor_transconjugant_1", Variable('x'), notify=[donor_0_net])
		gregory2008_net.add_output("transconjugant", "juxtacrine_signaling_R_plasmid_strand_molecule_donor_transconjugant_1", Expression('x.replace("protein", "receptor_active_protein")'), notify=[transconjugant_0_net])

		# donor_0_net arcs
		donor_0_net.add_input("R_plasmid_molecule", "process_1", Value(dot), notify=[gregory2008_net.place('donor')])
		donor_0_net.add_input("pilus_molecule", "process_2", Value(dot), notify=[gregory2008_net.place('donor')])
		donor_0_net.add_input("R_plasmid_molecule", "process_3", Value(dot), notify=[gregory2008_net.place('donor')])
		donor_0_net.add_input("pilus_molecule", "process_3", MultiArc([Value(dot)]*10), notify=[gregory2008_net.place('donor')])
		donor_0_net.add_input("R_protein_molecule", "R_protein_molecule_degradation_1", Value(dot), notify=[gregory2008_net.place('donor')])
		donor_0_net.add_input("pilus_molecule", "pilus_molecule_degradation_1", Value(dot), notify=[gregory2008_net.place('donor')])
		donor_0_net.add_output("R_protein_molecule", "process_1", MultiArc([Value(dot)]*5), notify=[gregory2008_net.place('donor')])
		donor_0_net.add_output("R_plasmid_molecule", "process_1", Value(dot), notify=[gregory2008_net.place('donor')])
		donor_0_net.add_output("pilus_molecule", "process_2", MultiArc([Value(dot)]*5), notify=[gregory2008_net.place('donor')])
		donor_0_net.add_output("R_plasmid_strand_molecule", "process_3", Value(dot), notify=[gregory2008_net.place('donor')])
		donor_0_net.add_output("R_plasmid_molecule", "process_3", Value(dot), notify=[gregory2008_net.place('donor')])

		# transconjugant_0_net arcs
		transconjugant_0_net.add_input("R_plasmid_molecule", "process_4", Value(dot), notify=[gregory2008_net.place('transconjugant')])
		transconjugant_0_net.add_input("R_plasmid_strand_molecule", "process_5", Value(dot), notify=[gregory2008_net.place('transconjugant')])
		transconjugant_0_net.add_input("R_plasmid_molecule", "R_plasmid_strand_molecule_inhibition_R_plasmid_molecule_1", Value(dot), notify=[gregory2008_net.place('transconjugant')])
		transconjugant_0_net.add_input("R_plasmid_strand_molecule", "R_plasmid_strand_molecule_inhibition_R_plasmid_molecule_1", Value(dot), notify=[gregory2008_net.place('transconjugant')])
		transconjugant_0_net.add_input("R_protein_molecule", "R_protein_molecule_degradation_2", Value(dot), notify=[gregory2008_net.place('transconjugant')])
		transconjugant_0_net.add_input("R_plasmid_strand_molecule", "R_plasmid_strand_molecule_degradation_1", Value(dot), notify=[gregory2008_net.place('transconjugant')])
		transconjugant_0_net.add_output("R_protein_molecule", "process_4", MultiArc([Value(dot)]*5), notify=[gregory2008_net.place('transconjugant')])
		transconjugant_0_net.add_output("R_plasmid_molecule", "process_4", Value(dot), notify=[gregory2008_net.place('transconjugant')])
		transconjugant_0_net.add_output("R_plasmid_molecule", "process_5", Value(dot), notify=[gregory2008_net.place('transconjugant')])
		return gregory2008_net
