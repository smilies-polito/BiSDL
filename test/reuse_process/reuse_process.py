from wrapping import *


class reuse_process(Module):
	def __init__(self, name):
		super().__init__(name)

	def build_net_structure(self) -> PetriNet:
		super(self.__class__, self).build_net_structure()

		# petri nets
		first_proc_1_net = PetriNet("first_proc_1_net", timescale=1)
		second_proc_0_net = PetriNet("second_proc_0_net", timescale=1)
		first_proc_0_net = PetriNet("first_proc_0_net", timescale=1)
		reuse_process_net = PetriNet("reuse_process_net", timescale=1)

		# first_proc_1_net places
		first_proc_1_net.add_place(Place("aa_gene", [BlackToken()]))
		first_proc_1_net.add_place(Place("aa_mrna"))
		first_proc_1_net.add_place(Place("aa_protein"))

		# first_proc_1_net transitions
		first_proc_1_net.add_transition(Transition("aa_gene_transcription_1_1"))
		first_proc_1_net.add_transition(Transition("aa_mrna_translation_1_1"))

		# second_proc_0_net places
		second_proc_0_net.add_place(Place("aa_receptor_active_protein"))
		second_proc_0_net.add_place(Place("bb_protein"))
		second_proc_0_net.add_place(Place("cc_protein"))

		# second_proc_0_net transitions
		second_proc_0_net.add_transition(Transition("enzymatic_reaction_1"))

		# first_proc_0_net places
		first_proc_0_net.add_place(Place("aa_gene", [BlackToken()]))
		first_proc_0_net.add_place(Place("aa_mrna"))
		first_proc_0_net.add_place(Place("aa_protein"))

		# first_proc_0_net transitions
		first_proc_0_net.add_transition(Transition("aa_gene_transcription_1"))
		first_proc_0_net.add_transition(Transition("aa_mrna_translation_1"))

		# reuse_process_net places
		reuse_process_net.add_place(Place("cell_1", [ first_proc_0_net ]))
		reuse_process_net.add_place(Place("cell_2", [ second_proc_0_net ]))
		reuse_process_net.add_place(Place("cell_3", [ first_proc_1_net ]))

		# reuse_process_net transitions
		reuse_process_net.add_transition(Transition("juxtacrine_signaling_aa_protein_cell_1_cell_2_1", Expression("str(x) == 'aa_protein'")))
		reuse_process_net.add_transition(Transition("juxtacrine_signaling_aa_protein_cell_3_cell_2_1", Expression("str(x) == 'aa_protein'")))

		# reuse_process_net arcs
		reuse_process_net.add_input("cell_1", "juxtacrine_signaling_aa_protein_cell_1_cell_2_1", Variable('x'), notify=[first_proc_0_net])
		reuse_process_net.add_input("cell_3", "juxtacrine_signaling_aa_protein_cell_3_cell_2_1", Variable('x'), notify=[first_proc_1_net])
		reuse_process_net.add_output("cell_2", "juxtacrine_signaling_aa_protein_cell_1_cell_2_1", Expression('x.replace("protein", "receptor_active_protein")'), notify=[])
		reuse_process_net.add_output("cell_2", "juxtacrine_signaling_aa_protein_cell_3_cell_2_1", Expression('x.replace("protein", "receptor_active_protein")'), notify=[second_proc_0_net])

		# first_proc_0_net arcs
		first_proc_0_net.add_input("aa_gene", "aa_gene_transcription_1", Value(dot))
		first_proc_0_net.add_input("aa_mrna", "aa_mrna_translation_1", Value(dot))
		first_proc_0_net.add_output("aa_gene", "aa_gene_transcription_1", Value(dot))
		first_proc_0_net.add_output("aa_mrna", "aa_gene_transcription_1", Value(dot))
		first_proc_0_net.add_output("aa_protein", "aa_mrna_translation_1", Value(dot), notify=[reuse_process_net.place('cell_1')])

		# second_proc_0_net arcs
		second_proc_0_net.add_input("aa_receptor_active_protein", "enzymatic_reaction_1", Value(dot), notify=[reuse_process_net.place('cell_2')])
		second_proc_0_net.add_input("bb_protein", "enzymatic_reaction_1", Value(dot), notify=[reuse_process_net.place('cell_2')])
		second_proc_0_net.add_output("aa_receptor_active_protein", "enzymatic_reaction_1", Value(dot), notify=[reuse_process_net.place('cell_2')])
		second_proc_0_net.add_output("cc_protein", "enzymatic_reaction_1", Value(dot), notify=[reuse_process_net.place('cell_2')])

		# first_proc_1_net arcs
		first_proc_1_net.add_input("aa_gene", "aa_gene_transcription_1_1", Value(dot))
		first_proc_1_net.add_input("aa_mrna", "aa_mrna_translation_1_1", Value(dot))
		first_proc_1_net.add_output("aa_gene", "aa_gene_transcription_1_1", Value(dot))
		first_proc_1_net.add_output("aa_mrna", "aa_gene_transcription_1_1", Value(dot))
		first_proc_1_net.add_output("aa_protein", "aa_mrna_translation_1_1", Value(dot), notify=[reuse_process_net.place('cell_3')])

		return reuse_process_net
