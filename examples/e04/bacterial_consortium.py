from petrisim.utils import *


class Bacterialconsortium(Module):
	def __init__(self, name: str = None):
		if not name:
			name = __class__.__name__
		super().__init__(name)

	def build_net_structure(self) -> PetriNet:

		# petri nets
		target_0_net = PetriNet("target_0_net", timescale=1)
		controller_0_net = PetriNet("controller_0_net", timescale=1)
		bacterialconsortium_net = PetriNet("bacterialconsortium_net", timescale=1)

		# target_0_net places
		target_0_net.add_place(Place("_3OC6HSL_protein"))
		target_0_net.add_place(Place("GFP_gene", [BlackToken()]))
		target_0_net.add_place(Place("GFP_mrna"))
		target_0_net.add_place(Place("GFP_protein"))

		# target_0_net transitions
		target_0_net.add_transition(Transition("GFP_gene_transcription_1"))
		target_0_net.add_transition(Transition("GFP_mrna_translation_1"))

		# controller_0_net places
		controller_0_net.add_place(Place("_3OC6HSL_gene", [BlackToken()]))
		controller_0_net.add_place(Place("_3OC6HSL_mrna"))
		controller_0_net.add_place(Place("_3OC6HSL_protein"))
		controller_0_net.add_place(Place("Lac1_protein"))

		# controller_0_net transitions
		controller_0_net.add_transition(Transition("_3OC6HSL_gene_transcription_1"))
		controller_0_net.add_transition(Transition("_3OC6HSL_mrna_translation_1"))
		controller_0_net.add_transition(Transition("_3OC6HSL_mrna_inhibition_Lac1_protein_1"))
		controller_0_net.add_transition(Transition("_3OC6HSL_mrna_inhibition_Lac1_protein_2"))
		controller_0_net.add_transition(Transition("_3OC6HSL_mrna_inhibition_Lac1_protein_3"))

		# bacterialconsortium_net places
		bacterialconsortium_net.add_place(Place("controller_compartment", [ controller_0_net ]))
		bacterialconsortium_net.add_place(Place("target_compartment", [ target_0_net ]))

		# bacterialconsortium_net transitions
		bacterialconsortium_net.add_transition(Transition("diffusion_controller_compartment_target_compartment_1", Expression("'_protein' in str(x)")))
		bacterialconsortium_net.add_transition(Transition("diffusion_target_compartment_controller_compartment_1", Expression("'_protein' in str(x)")))

		# bacterialconsortium_net arcs
		bacterialconsortium_net.add_input("controller_compartment", "diffusion_controller_compartment_target_compartment_1", Variable('x'), notify=[controller_0_net])
		bacterialconsortium_net.add_input("target_compartment", "diffusion_target_compartment_controller_compartment_1", Variable('x'), notify=[target_0_net])
		bacterialconsortium_net.add_output("target_compartment", "diffusion_controller_compartment_target_compartment_1", Variable('x'), notify=[target_0_net])
		bacterialconsortium_net.add_output("controller_compartment", "diffusion_target_compartment_controller_compartment_1", Variable('x'), notify=[controller_0_net])

		# controller_0_net arcs
		controller_0_net.add_input("_3OC6HSL_gene", "_3OC6HSL_gene_transcription_1", Value(dot))
		controller_0_net.add_input("_3OC6HSL_mrna", "_3OC6HSL_mrna_translation_1", Value(dot))
		controller_0_net.add_input("Lac1_protein", "_3OC6HSL_mrna_inhibition_Lac1_protein_1", Value(dot), notify=[bacterialconsortium_net.place('controller_compartment')])
		controller_0_net.add_input("_3OC6HSL_mrna", "_3OC6HSL_mrna_inhibition_Lac1_protein_1", Value(dot))
		controller_0_net.add_input("Lac1_protein", "_3OC6HSL_mrna_inhibition_Lac1_protein_2", Value(dot), notify=[bacterialconsortium_net.place('controller_compartment')])
		controller_0_net.add_input("_3OC6HSL_mrna", "_3OC6HSL_mrna_inhibition_Lac1_protein_2", Value(dot))
		controller_0_net.add_input("Lac1_protein", "_3OC6HSL_mrna_inhibition_Lac1_protein_3", Value(dot), notify=[bacterialconsortium_net.place('controller_compartment')])
		controller_0_net.add_input("_3OC6HSL_mrna", "_3OC6HSL_mrna_inhibition_Lac1_protein_3", Value(dot))
		controller_0_net.add_output("_3OC6HSL_gene", "_3OC6HSL_gene_transcription_1", Value(dot))
		controller_0_net.add_output("_3OC6HSL_mrna", "_3OC6HSL_gene_transcription_1", Value(dot))
		controller_0_net.add_output("_3OC6HSL_protein", "_3OC6HSL_mrna_translation_1", Value(dot), notify=[bacterialconsortium_net.place('controller_compartment')])

		# target_0_net arcs
		target_0_net.add_input("GFP_gene", "GFP_gene_transcription_1", Value(dot))
		target_0_net.add_input("_3OC6HSL_protein", "GFP_gene_transcription_1", Value(dot), notify=[bacterialconsortium_net.place('target_compartment')])
		target_0_net.add_input("GFP_mrna", "GFP_mrna_translation_1", Value(dot))
		target_0_net.add_output("GFP_gene", "GFP_gene_transcription_1", Value(dot))
		target_0_net.add_output("GFP_mrna", "GFP_gene_transcription_1", Value(dot))
		target_0_net.add_output("GFP_protein", "GFP_mrna_translation_1", Value(dot), notify=[bacterialconsortium_net.place('target_compartment')])
		return bacterialconsortium_net
