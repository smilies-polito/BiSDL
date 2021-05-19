from wrapping import *


class timescale(Module):
	def __init__(self, name):
		super().__init__(name)

	def build_net_structure(self) -> PetriNet:
		super(self.__class__, self).build_net_structure()

		# petri nets
		cell_B_process_0_net = PetriNet("cell_B_process_0_net", timescale=10)
		cell_A_process_0_net = PetriNet("cell_A_process_0_net", timescale=5)
		timescale_net = PetriNet("timescale_net", timescale=15)

		# cell_B_process_0_net places
		cell_B_process_0_net.add_place(Place("a_receptor_active_protein"))
		cell_B_process_0_net.add_place(Place("b_protein"))
		cell_B_process_0_net.add_place(Place("c_protein"))

		# cell_B_process_0_net transitions
		cell_B_process_0_net.add_transition(Transition("enzymatic_reaction_1"))

		# cell_A_process_0_net places
		cell_A_process_0_net.add_place(Place("a_gene", [BlackToken()]))
		cell_A_process_0_net.add_place(Place("a_mrna"))
		cell_A_process_0_net.add_place(Place("a_protein"))

		# cell_A_process_0_net transitions
		cell_A_process_0_net.add_transition(Transition("a_gene_transcription_1"))
		cell_A_process_0_net.add_transition(Transition("a_mrna_translation_1"))

		# timescale_net places
		timescale_net.add_place(Place("cell_A", [ cell_A_process_0_net ]))
		timescale_net.add_place(Place("cell_B", [ cell_B_process_0_net ]))

		# timescale_net transitions
		timescale_net.add_transition(Transition("juxtacrine_signaling_a_protein_cell_A_cell_B_1", Expression("str(x) == 'a_protein'")))

		# timescale_net arcs
		timescale_net.add_input("cell_A", "juxtacrine_signaling_a_protein_cell_A_cell_B_1", Variable('x'), notify=[cell_A_process_0_net])
		timescale_net.add_output("cell_B", "juxtacrine_signaling_a_protein_cell_A_cell_B_1", Expression('x.replace("protein", "receptor_active_protein")'), notify=[cell_B_process_0_net])

		# cell_A_process_0_net arcs
		cell_A_process_0_net.add_input("a_gene", "a_gene_transcription_1", Value(dot))
		cell_A_process_0_net.add_input("a_mrna", "a_mrna_translation_1", Value(dot))
		cell_A_process_0_net.add_output("a_gene", "a_gene_transcription_1", Value(dot))
		cell_A_process_0_net.add_output("a_mrna", "a_gene_transcription_1", Value(dot))
		cell_A_process_0_net.add_output("a_protein", "a_mrna_translation_1", Value(dot), notify=[timescale_net.place('cell_A')])

		# cell_B_process_0_net arcs
		cell_B_process_0_net.add_input("a_receptor_active_protein", "enzymatic_reaction_1", Value(dot), notify=[timescale_net.place('cell_B')])
		cell_B_process_0_net.add_input("b_protein", "enzymatic_reaction_1", Value(dot), notify=[timescale_net.place('cell_B')])
		cell_B_process_0_net.add_output("a_receptor_active_protein", "enzymatic_reaction_1", Value(dot), notify=[timescale_net.place('cell_B')])
		cell_B_process_0_net.add_output("c_protein", "enzymatic_reaction_1", Value(dot), notify=[timescale_net.place('cell_B')])

		return timescale_net
