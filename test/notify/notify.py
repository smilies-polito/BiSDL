from wrapping import *


class notify(Module):
	def __init__(self, name):
		super().__init__(name)

	def build_net_structure(self) -> PetriNet:
		super(self.__class__, self).build_net_structure()

		# petri nets
		cell_2_process_0_net = PetriNet("cell_2_process_0_net", timescale=1)
		cell_1_process3_0_net = PetriNet("cell_1_process3_0_net", timescale=2)
		cell_1_process2_0_net = PetriNet("cell_1_process2_0_net", timescale=1)
		cell_1_process1_0_net = PetriNet("cell_1_process1_0_net", timescale=1)
		notify_net = PetriNet("notify_net", timescale=1)

		# cell_2_process_0_net places
		cell_2_process_0_net.add_place(Place("pluto_gene", [BlackToken()]))
		cell_2_process_0_net.add_place(Place("pluto_mrna"))
		cell_2_process_0_net.add_place(Place("pluto_protein"))
		cell_2_process_0_net.add_place(Place("quiquoqua_receptor_active_protein"))
		cell_2_process_0_net.add_place(Place("paperino_protein"))

		# cell_2_process_0_net transitions
		cell_2_process_0_net.add_transition(Transition("pluto_gene_transcription_1"))
		cell_2_process_0_net.add_transition(Transition("pluto_mrna_translation_1"))
		cell_2_process_0_net.add_transition(Transition("enzymatic_reaction_2"))

		# cell_1_process3_0_net places
		cell_1_process3_0_net.add_place(Place("quiquoqua_gene", [BlackToken()]))
		cell_1_process3_0_net.add_place(Place("quiquoqua_mrna"))
		cell_1_process3_0_net.add_place(Place("quiquoqua_protein"))

		# cell_1_process3_0_net transitions
		cell_1_process3_0_net.add_transition(Transition("quiquoqua_gene_transcription_1"))
		cell_1_process3_0_net.add_transition(Transition("quiquoqua_mrna_translation_1"))

		# cell_1_process2_0_net places
		cell_1_process2_0_net.add_place(Place("paperino_receptor_active_protein"))
		cell_1_process2_0_net.add_place(Place("pippo_protein"))
		cell_1_process2_0_net.add_place(Place("quiquoqua_protein"))

		# cell_1_process2_0_net transitions
		cell_1_process2_0_net.add_transition(Transition("enzymatic_reaction_1"))

		# cell_1_process1_0_net places
		cell_1_process1_0_net.add_place(Place("pippo_gene", [BlackToken()]))
		cell_1_process1_0_net.add_place(Place("pippo_mrna"))
		cell_1_process1_0_net.add_place(Place("pippo_protein"))

		# cell_1_process1_0_net transitions
		cell_1_process1_0_net.add_transition(Transition("pippo_gene_transcription_1"))
		cell_1_process1_0_net.add_transition(Transition("pippo_mrna_translation_1"))

		# notify_net places
		notify_net.add_place(Place("cell_1", [ cell_1_process1_0_net, cell_1_process2_0_net, cell_1_process3_0_net ]))
		notify_net.add_place(Place("cell_2", [ cell_2_process_0_net ]))

		# notify_net transitions
		notify_net.add_transition(Transition("juxtacrine_signaling_quiquoqua_protein_cell_1_cell_2_1", Expression("str(x) == 'quiquoqua_protein'")))
		notify_net.add_transition(Transition("juxtacrine_signaling_paperino_protein_cell_2_cell_1_1", Expression("str(x) == 'paperino_protein'")))

		# notify_net arcs
		notify_net.add_input("cell_1", "juxtacrine_signaling_quiquoqua_protein_cell_1_cell_2_1", Variable('x'), notify=[cell_1_process1_0_net, cell_1_process2_0_net, cell_1_process3_0_net])
		notify_net.add_input("cell_2", "juxtacrine_signaling_paperino_protein_cell_2_cell_1_1", Variable('x'), notify=[cell_2_process_0_net])
		notify_net.add_output("cell_2", "juxtacrine_signaling_quiquoqua_protein_cell_1_cell_2_1", Expression('x.replace("protein", "receptor_active_protein")'), notify=[cell_2_process_0_net])
		notify_net.add_output("cell_1", "juxtacrine_signaling_paperino_protein_cell_2_cell_1_1", Expression('x.replace("protein", "receptor_active_protein")'), notify=[cell_1_process1_0_net, cell_1_process2_0_net, cell_1_process3_0_net])

		# cell_1_process1_0_net arcs
		cell_1_process1_0_net.add_input("pippo_gene", "pippo_gene_transcription_1", Value(dot))
		cell_1_process1_0_net.add_input("pippo_mrna", "pippo_mrna_translation_1", Value(dot))
		cell_1_process1_0_net.add_output("pippo_gene", "pippo_gene_transcription_1", Value(dot))
		cell_1_process1_0_net.add_output("pippo_mrna", "pippo_gene_transcription_1", Value(dot))
		cell_1_process1_0_net.add_output("pippo_protein", "pippo_mrna_translation_1", MultiArc([Value(dot)]*5), notify=[notify_net.place('cell_1')])

		# cell_1_process2_0_net arcs
		cell_1_process2_0_net.add_input("paperino_receptor_active_protein", "enzymatic_reaction_1", Value(dot), notify=[notify_net.place('cell_1')])
		cell_1_process2_0_net.add_input("pippo_protein", "enzymatic_reaction_1", Value(dot), notify=[notify_net.place('cell_1')])
		cell_1_process2_0_net.add_output("paperino_receptor_active_protein", "enzymatic_reaction_1", Value(dot), notify=[notify_net.place('cell_1')])
		cell_1_process2_0_net.add_output("quiquoqua_protein", "enzymatic_reaction_1", Value(dot), notify=[notify_net.place('cell_1')])

		# cell_1_process3_0_net arcs
		cell_1_process3_0_net.add_input("quiquoqua_gene", "quiquoqua_gene_transcription_1", Value(dot))
		cell_1_process3_0_net.add_input("quiquoqua_mrna", "quiquoqua_mrna_translation_1", Value(dot))
		cell_1_process3_0_net.add_output("quiquoqua_gene", "quiquoqua_gene_transcription_1", Value(dot))
		cell_1_process3_0_net.add_output("quiquoqua_mrna", "quiquoqua_gene_transcription_1", Value(dot))
		cell_1_process3_0_net.add_output("quiquoqua_protein", "quiquoqua_mrna_translation_1", Value(dot), notify=[notify_net.place('cell_1')])

		# cell_2_process_0_net arcs
		cell_2_process_0_net.add_input("pluto_gene", "pluto_gene_transcription_1", Value(dot))
		cell_2_process_0_net.add_input("pluto_mrna", "pluto_mrna_translation_1", Value(dot))
		cell_2_process_0_net.add_input("quiquoqua_receptor_active_protein", "enzymatic_reaction_2", Value(dot), notify=[notify_net.place('cell_2')])
		cell_2_process_0_net.add_input("pluto_protein", "enzymatic_reaction_2", Value(dot), notify=[notify_net.place('cell_2')])
		cell_2_process_0_net.add_output("pluto_gene", "pluto_gene_transcription_1", Value(dot))
		cell_2_process_0_net.add_output("pluto_mrna", "pluto_gene_transcription_1", Value(dot))
		cell_2_process_0_net.add_output("pluto_protein", "pluto_mrna_translation_1", Value(dot), notify=[notify_net.place('cell_2')])
		cell_2_process_0_net.add_output("quiquoqua_receptor_active_protein", "enzymatic_reaction_2", Value(dot), notify=[notify_net.place('cell_2')])
		cell_2_process_0_net.add_output("paperino_protein", "enzymatic_reaction_2", Value(dot), notify=[notify_net.place('cell_2')])

		return notify_net
