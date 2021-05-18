from wrapping import *


class signaling(Module):
	def __init__(self, name):
		super().__init__(name)

	def build_net_structure(self) -> PetriNet:
		super(self.__class__, self).build_net_structure()

		# petri nets
		cell_2_process_0_net = PetriNet("cell_2_process_0_net", timescale=1)
		cell_1_process_0_net = PetriNet("cell_1_process_0_net", timescale=1)
		signaling_net = PetriNet("signaling_net", timescale=1)

		# cell_2_process_0_net places
		cell_2_process_0_net.add_place(Place("pluto_gene", [BlackToken()]))
		cell_2_process_0_net.add_place(Place("pluto_mrna"))
		cell_2_process_0_net.add_place(Place("pluto_protein"))
		cell_2_process_0_net.add_place(Place("pippo_receptor_active_protein"))
		cell_2_process_0_net.add_place(Place("paperino_protein"))

		# cell_2_process_0_net transitions
		cell_2_process_0_net.add_transition(Transition("pluto_gene_transcription_1"))
		cell_2_process_0_net.add_transition(Transition("pluto_mrna_translation_1"))
		cell_2_process_0_net.add_transition(Transition("enzymatic_reaction_1"))

		# cell_1_process_0_net places
		cell_1_process_0_net.add_place(Place("pippo_gene", [BlackToken()]))
		cell_1_process_0_net.add_place(Place("pippo_mrna"))
		cell_1_process_0_net.add_place(Place("pippo_protein"))

		# cell_1_process_0_net transitions
		cell_1_process_0_net.add_transition(Transition("pippo_gene_transcription_1"))
		cell_1_process_0_net.add_transition(Transition("pippo_mrna_translation_1"))

		# signaling_net places
		signaling_net.add_place(Place("cell_1", [ cell_1_process_0_net ]))
		signaling_net.add_place(Place("cell_2", [ cell_2_process_0_net ]))

		# signaling_net transitions
		signaling_net.add_transition(Transition("juxtacrine_signaling_pippo_protein_cell_1_cell_2_1", Expression("str(x) == 'pippo_protein'")))

		# signaling_net arcs
		signaling_net.add_input("cell_1", "juxtacrine_signaling_pippo_protein_cell_1_cell_2_1", Variable('x'), notify=[cell_1_process_0_net])
		signaling_net.add_output("cell_2", "juxtacrine_signaling_pippo_protein_cell_1_cell_2_1", Expression('x.replace("protein", "receptor_active_protein")'), notify=[])

		# cell_1_process_0_net arcs
		cell_1_process_0_net.add_input("pippo_gene", "pippo_gene_transcription_1", Value(dot))
		cell_1_process_0_net.add_input("pippo_mrna", "pippo_mrna_translation_1", Value(dot))
		cell_1_process_0_net.add_output("pippo_gene", "pippo_gene_transcription_1", Value(dot))
		cell_1_process_0_net.add_output("pippo_mrna", "pippo_gene_transcription_1", Value(dot))
		cell_1_process_0_net.add_output("pippo_protein", "pippo_mrna_translation_1", Value(dot), notify=[signaling_net.place('cell_1')])

		# cell_2_process_0_net arcs
		cell_2_process_0_net.add_input("pluto_gene", "pluto_gene_transcription_1", Value(dot))
		cell_2_process_0_net.add_input("pluto_mrna", "pluto_mrna_translation_1", Value(dot))
		cell_2_process_0_net.add_input("pippo_receptor_active_protein", "enzymatic_reaction_1", Value(dot), notify=[signaling_net.place('cell_2')])
		cell_2_process_0_net.add_input("pluto_protein", "enzymatic_reaction_1", Value(dot), notify=[signaling_net.place('cell_2')])
		cell_2_process_0_net.add_output("pluto_gene", "pluto_gene_transcription_1", Value(dot))
		cell_2_process_0_net.add_output("pluto_mrna", "pluto_gene_transcription_1", Value(dot))
		cell_2_process_0_net.add_output("pluto_protein", "pluto_mrna_translation_1", Value(dot), notify=[signaling_net.place('cell_2')])
		cell_2_process_0_net.add_output("pippo_receptor_active_protein", "enzymatic_reaction_1", Value(dot), notify=[signaling_net.place('cell_2')])
		cell_2_process_0_net.add_output("paperino_protein", "enzymatic_reaction_1", Value(dot), notify=[signaling_net.place('cell_2')])

		return signaling_net
