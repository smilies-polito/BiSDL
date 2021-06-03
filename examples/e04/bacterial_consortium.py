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
		target_0_net.add_place(Place("LuxR_gene", [BlackToken()]))
		target_0_net.add_place(Place("LuxR_mrna"))
		target_0_net.add_place(Place("LuxR_protein"))
		target_0_net.add_place(Place("_3OC6HSL_molecule"))
		target_0_net.add_place(Place("_3OC6HSL_LuxR_complex"))
		target_0_net.add_place(Place("GFP_gene", [BlackToken()]))
		target_0_net.add_place(Place("GFP_mrna"))
		target_0_net.add_place(Place("GFP_protein"))
		target_0_net.add_place(Place("Lac1_protein"))

		# target_0_net transitions
		target_0_net.add_transition(Transition("LuxR_gene_transcription_1"))
		target_0_net.add_transition(Transition("LuxR_mrna_translation_1"))
		target_0_net.add_transition(Transition("LuxR_protein_degradation_1"))
		target_0_net.add_transition(Transition("protein_complex_formation_1"))
		target_0_net.add_transition(Transition("GFP_gene_transcription_1"))
		target_0_net.add_transition(Transition("GFP_mrna_translation_1"))
		target_0_net.add_transition(Transition("GFP_protein_degradation_1"))
		target_0_net.add_transition(Transition("Lac1_protein_degradation_2"))

		# controller_0_net places
		controller_0_net.add_place(Place("Lux1_gene", [BlackToken()]))
		controller_0_net.add_place(Place("Lux1_mrna"))
		controller_0_net.add_place(Place("Lux1_protein"))
		controller_0_net.add_place(Place("Lac1_protein"))
		controller_0_net.add_place(Place("SAM_molecule"))
		controller_0_net.add_place(Place("ACP_molecule"))
		controller_0_net.add_place(Place("_3OC6HSL_molecule"))

		# controller_0_net transitions
		controller_0_net.add_transition(Transition("Lux1_gene_transcription_1"))
		controller_0_net.add_transition(Transition("Lux1_mrna_translation_1"))
		controller_0_net.add_transition(Transition("Lux1_mrna_inhibition_Lac1_protein_1"))
		controller_0_net.add_transition(Transition("Lux1_protein_degradation_1"))
		controller_0_net.add_transition(Transition("Lac1_protein_degradation_1"))
		controller_0_net.add_transition(Transition("enzymatic_reaction_1"))

		# bacterialconsortium_net places
		bacterialconsortium_net.add_place(Place("controller_compartment", [ controller_0_net ]))
		bacterialconsortium_net.add_place(Place("target_compartment", [ target_0_net ]))

		# bacterialconsortium_net transitions
		bacterialconsortium_net.add_transition(Transition("diffusion_controller_compartment_target_compartment_1", Expression("str(x) == 'Lac1_protein' or str(x) == '_3OC6HSL_molecule'")))
		bacterialconsortium_net.add_transition(Transition("diffusion_target_compartment_controller_compartment_1", Expression("str(x) == 'Lac1_protein' or str(x) == '_3OC6HSL_molecule'")))

		# bacterialconsortium_net arcs
		bacterialconsortium_net.add_input("controller_compartment", "diffusion_controller_compartment_target_compartment_1", Variable('x'), notify=[controller_0_net])
		bacterialconsortium_net.add_input("target_compartment", "diffusion_target_compartment_controller_compartment_1", Variable('x'), notify=[target_0_net])
		bacterialconsortium_net.add_output("target_compartment", "diffusion_controller_compartment_target_compartment_1", Variable('x'), notify=[target_0_net])
		bacterialconsortium_net.add_output("controller_compartment", "diffusion_target_compartment_controller_compartment_1", Variable('x'), notify=[controller_0_net])

		# controller_0_net arcs
		controller_0_net.add_input("Lux1_gene", "Lux1_gene_transcription_1", Value(dot))
		controller_0_net.add_input("Lux1_mrna", "Lux1_mrna_translation_1", Value(dot))
		controller_0_net.add_input("Lac1_protein", "Lux1_mrna_inhibition_Lac1_protein_1", Value(dot), notify=[bacterialconsortium_net.place('controller_compartment')])
		controller_0_net.add_input("Lux1_mrna", "Lux1_mrna_inhibition_Lac1_protein_1", Value(dot))
		controller_0_net.add_input("Lux1_protein", "Lux1_protein_degradation_1", Value(dot), notify=[bacterialconsortium_net.place('controller_compartment')])
		controller_0_net.add_input("Lac1_protein", "Lac1_protein_degradation_1", Value(dot), notify=[bacterialconsortium_net.place('controller_compartment')])
		controller_0_net.add_input("Lux1_protein", "enzymatic_reaction_1", Value(dot), notify=[bacterialconsortium_net.place('controller_compartment')])
		controller_0_net.add_input("SAM_molecule", "enzymatic_reaction_1", Value(dot), notify=[bacterialconsortium_net.place('controller_compartment')])
		controller_0_net.add_input("ACP_molecule", "enzymatic_reaction_1", Value(dot), notify=[bacterialconsortium_net.place('controller_compartment')])
		controller_0_net.add_output("Lux1_gene", "Lux1_gene_transcription_1", Value(dot))
		controller_0_net.add_output("Lux1_mrna", "Lux1_gene_transcription_1", Value(dot))
		controller_0_net.add_output("Lux1_protein", "Lux1_mrna_translation_1", Value(dot), notify=[bacterialconsortium_net.place('controller_compartment')])
		controller_0_net.add_output("Lux1_protein", "enzymatic_reaction_1", Value(dot), notify=[bacterialconsortium_net.place('controller_compartment')])
		controller_0_net.add_output("_3OC6HSL_molecule", "enzymatic_reaction_1", Value(dot), notify=[bacterialconsortium_net.place('controller_compartment')])

		# target_0_net arcs
		target_0_net.add_input("LuxR_gene", "LuxR_gene_transcription_1", Value(dot))
		target_0_net.add_input("LuxR_mrna", "LuxR_mrna_translation_1", Value(dot))
		target_0_net.add_input("LuxR_protein", "LuxR_protein_degradation_1", Value(dot), notify=[bacterialconsortium_net.place('target_compartment')])
		target_0_net.add_input("_3OC6HSL_molecule", "protein_complex_formation_1", Value(dot), notify=[bacterialconsortium_net.place('target_compartment')])
		target_0_net.add_input("LuxR_protein", "protein_complex_formation_1", Value(dot), notify=[bacterialconsortium_net.place('target_compartment')])
		target_0_net.add_input("GFP_gene", "GFP_gene_transcription_1", Value(dot))
		target_0_net.add_input("_3OC6HSL_LuxR_complex", "GFP_gene_transcription_1", Value(dot), notify=[bacterialconsortium_net.place('target_compartment')])
		target_0_net.add_input("GFP_mrna", "GFP_mrna_translation_1", Value(dot))
		target_0_net.add_input("GFP_protein", "GFP_protein_degradation_1", Value(dot), notify=[bacterialconsortium_net.place('target_compartment')])
		target_0_net.add_input("Lac1_protein", "Lac1_protein_degradation_2", Value(dot), notify=[bacterialconsortium_net.place('target_compartment')])
		target_0_net.add_output("LuxR_gene", "LuxR_gene_transcription_1", Value(dot))
		target_0_net.add_output("LuxR_mrna", "LuxR_gene_transcription_1", Value(dot))
		target_0_net.add_output("LuxR_protein", "LuxR_mrna_translation_1", Value(dot), notify=[bacterialconsortium_net.place('target_compartment')])
		target_0_net.add_output("_3OC6HSL_LuxR_complex", "protein_complex_formation_1", Value(dot), notify=[bacterialconsortium_net.place('target_compartment')])
		target_0_net.add_output("GFP_gene", "GFP_gene_transcription_1", Value(dot))
		target_0_net.add_output("GFP_mrna", "GFP_gene_transcription_1", Value(dot))
		target_0_net.add_output("GFP_protein", "GFP_mrna_translation_1", Value(dot), notify=[bacterialconsortium_net.place('target_compartment')])
		return bacterialconsortium_net
