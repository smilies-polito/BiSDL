from petrisim.utils import *


class Notify(Module):
	def __init__(self, name: str = None):
		if not name:
			name = __class__.__name__
		super().__init__(name)

	def build_net_structure(self) -> PetriNet:

		# petri nets
		cell_2_process_0_net = PetriNet("cell_2_process_0_net", timescale=1)
		cell_1_process_0_net = PetriNet("cell_1_process_0_net", timescale=1)
		notify_net = PetriNet("notify_net", timescale=1)

		# cell_2_process_0_net places
		cell_2_process_0_net.add_place(Place("pluto_gene", [BlackToken()]))
		cell_2_process_0_net.add_place(Place("pluto_mrna"))
		cell_2_process_0_net.add_place(Place("pluto_protein"))

		# cell_2_process_0_net transitions
		cell_2_process_0_net.add_transition(Transition("pluto_gene_transcription_1"))
		cell_2_process_0_net.add_transition(Transition("pluto_mrna_translation_1"))

		# cell_1_process_0_net places
		cell_1_process_0_net.add_place(Place("pippo_gene", [BlackToken()]))
		cell_1_process_0_net.add_place(Place("pippo_mrna"))
		cell_1_process_0_net.add_place(Place("pippo_protein"))

		# cell_1_process_0_net transitions
		cell_1_process_0_net.add_transition(Transition("pippo_gene_transcription_1"))
		cell_1_process_0_net.add_transition(Transition("pippo_mrna_translation_1"))

		# notify_net places
		notify_net.add_place(Place("cell_1", [ cell_1_process_0_net ]))
		notify_net.add_place(Place("cell_2", [ cell_2_process_0_net ]))

		# notify_net transitions
		notify_net.add_transition(Transition("diffusion_pippo_protein_1", Expression("str(x) == 'pippo_protein'")))
		notify_net.add_transition(Transition("diffusion_pippo_protein_2", Expression("str(x) == 'pippo_protein'")))
		notify_net.add_transition(Transition("diffusion_pluto_protein_1", Expression("str(x) == 'pluto_protein'")))
		notify_net.add_transition(Transition("diffusion_pluto_protein_2", Expression("str(x) == 'pluto_protein'")))

		# notify_net arcs
		notify_net.add_input("cell_1", "diffusion_pippo_protein_1", Variable('x'), notify=[cell_1_process_0_net])
		notify_net.add_input("cell_2", "diffusion_pippo_protein_2", Variable('x'), notify=[cell_2_process_0_net])
		notify_net.add_input("cell_1", "diffusion_pluto_protein_1", Variable('x'), notify=[cell_1_process_0_net])
		notify_net.add_input("cell_2", "diffusion_pluto_protein_2", Variable('x'), notify=[cell_2_process_0_net])
		notify_net.add_output("cell_2", "diffusion_pippo_protein_1", Variable('x'), notify=[cell_2_process_0_net])
		notify_net.add_output("cell_1", "diffusion_pippo_protein_2", Variable('x'), notify=[cell_1_process_0_net])
		notify_net.add_output("cell_2", "diffusion_pluto_protein_1", Variable('x'), notify=[cell_2_process_0_net])
		notify_net.add_output("cell_1", "diffusion_pluto_protein_2", Variable('x'), notify=[cell_1_process_0_net])

		# cell_1_process_0_net arcs
		cell_1_process_0_net.add_input("pippo_gene", "pippo_gene_transcription_1", Value(dot))
		cell_1_process_0_net.add_input("pippo_mrna", "pippo_mrna_translation_1", Value(dot))
		cell_1_process_0_net.add_output("pippo_gene", "pippo_gene_transcription_1", Value(dot))
		cell_1_process_0_net.add_output("pippo_mrna", "pippo_gene_transcription_1", Value(dot))
		cell_1_process_0_net.add_output("pippo_protein", "pippo_mrna_translation_1", MultiArc([Value(dot)]*5), notify=[notify_net.place('cell_1')])

		# cell_2_process_0_net arcs
		cell_2_process_0_net.add_input("pluto_gene", "pluto_gene_transcription_1", Value(dot))
		cell_2_process_0_net.add_input("pluto_mrna", "pluto_mrna_translation_1", Value(dot))
		cell_2_process_0_net.add_output("pluto_gene", "pluto_gene_transcription_1", Value(dot))
		cell_2_process_0_net.add_output("pluto_mrna", "pluto_gene_transcription_1", Value(dot))
		cell_2_process_0_net.add_output("pluto_protein", "pluto_mrna_translation_1", MultiArc([Value(dot)]*3), notify=[notify_net.place('cell_2')])
		return notify_net
