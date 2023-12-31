from petrisim.utils import *


class Bacterialconsortium(Module):
	def __init__(self, name: str = None):
		if not name:
			name = __class__.__name__
		super().__init__(name)

	def build_net_structure(self) -> PetriNet:

		# petri nets
		GFP_production_0_net = PetriNet("GFP_production_0_net", timescale=3)
		AHL_production_0_net = PetriNet("AHL_production_0_net", timescale=2)
		bacterialconsortium_net = PetriNet("bacterialconsortium_net", timescale=1)

		# GFP_production_0_net places
		GFP_production_0_net.add_place(Place("AHL_molecule"))
		GFP_production_0_net.add_place(Place("LuxR_gene", [BlackToken()]))
		GFP_production_0_net.add_place(Place("LuxR_mrna"))
		GFP_production_0_net.add_place(Place("LuxR_protein"))
		GFP_production_0_net.add_place(Place("LuxR_AHL_complex"))
		GFP_production_0_net.add_place(Place("GFP_reporter_gene", [BlackToken()]))
		GFP_production_0_net.add_place(Place("GFP_reporter_mrna"))
		GFP_production_0_net.add_place(Place("GFP_reporter_protein"))

		# GFP_production_0_net transitions
		GFP_production_0_net.add_transition(Transition("AHL_molecule_degradation_2"))
		GFP_production_0_net.add_transition(Transition("LuxR_gene_transcription_1"))
		GFP_production_0_net.add_transition(Transition("LuxR_mrna_translation_1"))
		GFP_production_0_net.add_transition(Transition("LuxR_protein_degradation_1"))
		GFP_production_0_net.add_transition(Transition("protein_complex_formation_1"))
		GFP_production_0_net.add_transition(Transition("protein_complex_formation_2"))
		GFP_production_0_net.add_transition(Transition("LuxR_AHL_complex_degradation_1"))
		GFP_production_0_net.add_transition(Transition("GFP_reporter_gene_transcription_1"))
		GFP_production_0_net.add_transition(Transition("GFP_reporter_mrna_translation_1"))
		GFP_production_0_net.add_transition(Transition("GFP_reporter_protein_degradation_1"))

		# AHL_production_0_net places
		AHL_production_0_net.add_place(Place("LacI_protein"))
		AHL_production_0_net.add_place(Place("SAM_molecule"))
		AHL_production_0_net.add_place(Place("LuxI_gene", [BlackToken()]))
		AHL_production_0_net.add_place(Place("LuxI_mrna"))
		AHL_production_0_net.add_place(Place("LuxI_protein"))
		AHL_production_0_net.add_place(Place("ACP_gene", [BlackToken()]))
		AHL_production_0_net.add_place(Place("ACP_mrna"))
		AHL_production_0_net.add_place(Place("ACP_protein"))
		AHL_production_0_net.add_place(Place("AHL_molecule"))

		# AHL_production_0_net transitions
		AHL_production_0_net.add_transition(Transition("LacI_protein_degradation_1"))
		AHL_production_0_net.add_transition(Transition("SAM_molecule_degradation_1"))
		AHL_production_0_net.add_transition(Transition("LuxI_gene_transcription_1"))
		AHL_production_0_net.add_transition(Transition("LuxI_gene_inhibition_LacI_protein_1"))
		AHL_production_0_net.add_transition(Transition("LuxI_gene_inhibition_LacI_protein_2"))
		AHL_production_0_net.add_transition(Transition("LuxI_gene_inhibition_LacI_protein_3"))
		AHL_production_0_net.add_transition(Transition("LuxI_gene_inhibition_LacI_protein_4"))
		AHL_production_0_net.add_transition(Transition("LuxI_gene_inhibition_LacI_protein_5"))
		AHL_production_0_net.add_transition(Transition("LuxI_mrna_translation_1"))
		AHL_production_0_net.add_transition(Transition("LuxI_mrna_inhibition_LacI_protein_1"))
		AHL_production_0_net.add_transition(Transition("LuxI_mrna_inhibition_LacI_protein_2"))
		AHL_production_0_net.add_transition(Transition("LuxI_mrna_inhibition_LacI_protein_3"))
		AHL_production_0_net.add_transition(Transition("LuxI_mrna_inhibition_LacI_protein_4"))
		AHL_production_0_net.add_transition(Transition("LuxI_mrna_inhibition_LacI_protein_5"))
		AHL_production_0_net.add_transition(Transition("LuxI_protein_degradation_1"))
		AHL_production_0_net.add_transition(Transition("ACP_gene_transcription_1"))
		AHL_production_0_net.add_transition(Transition("ACP_mrna_translation_1"))
		AHL_production_0_net.add_transition(Transition("ACP_protein_degradation_1"))
		AHL_production_0_net.add_transition(Transition("enzymatic_reaction_1"))
		AHL_production_0_net.add_transition(Transition("enzymatic_reaction_2"))
		AHL_production_0_net.add_transition(Transition("enzymatic_reaction_3"))
		AHL_production_0_net.add_transition(Transition("enzymatic_reaction_4"))
		AHL_production_0_net.add_transition(Transition("enzymatic_reaction_5"))
		AHL_production_0_net.add_transition(Transition("AHL_molecule_degradation_1"))

		# bacterialconsortium_net places
		bacterialconsortium_net.add_place(Place("producer", [ AHL_production_0_net ]))
		bacterialconsortium_net.add_place(Place("sensor", [ GFP_production_0_net ]))

		# bacterialconsortium_net transitions
		bacterialconsortium_net.add_transition(Transition("diffusion_AHL_molecule_1", Expression("str(x) == 'AHL_molecule'")))
		bacterialconsortium_net.add_transition(Transition("diffusion_AHL_molecule_2", Expression("str(x) == 'AHL_molecule'")))
		bacterialconsortium_net.add_transition(Transition("diffusion_AHL_molecule_3", Expression("str(x) == 'AHL_molecule'")))
		bacterialconsortium_net.add_transition(Transition("diffusion_AHL_molecule_4", Expression("str(x) == 'AHL_molecule'")))
		bacterialconsortium_net.add_transition(Transition("diffusion_AHL_molecule_5", Expression("str(x) == 'AHL_molecule'")))
		bacterialconsortium_net.add_transition(Transition("diffusion_AHL_molecule_6", Expression("str(x) == 'AHL_molecule'")))
		bacterialconsortium_net.add_transition(Transition("diffusion_AHL_molecule_7", Expression("str(x) == 'AHL_molecule'")))
		bacterialconsortium_net.add_transition(Transition("diffusion_AHL_molecule_8", Expression("str(x) == 'AHL_molecule'")))
		bacterialconsortium_net.add_transition(Transition("diffusion_AHL_molecule_9", Expression("str(x) == 'AHL_molecule'")))
		bacterialconsortium_net.add_transition(Transition("diffusion_AHL_molecule_10", Expression("str(x) == 'AHL_molecule'")))

		# bacterialconsortium_net arcs
		bacterialconsortium_net.add_input("producer", "diffusion_AHL_molecule_1", Variable('x'), notify=[AHL_production_0_net])
		bacterialconsortium_net.add_input("sensor", "diffusion_AHL_molecule_2", Variable('x'), notify=[GFP_production_0_net])
		bacterialconsortium_net.add_input("producer", "diffusion_AHL_molecule_3", Variable('x'), notify=[AHL_production_0_net])
		bacterialconsortium_net.add_input("sensor", "diffusion_AHL_molecule_4", Variable('x'), notify=[GFP_production_0_net])
		bacterialconsortium_net.add_input("producer", "diffusion_AHL_molecule_5", Variable('x'), notify=[AHL_production_0_net])
		bacterialconsortium_net.add_input("sensor", "diffusion_AHL_molecule_6", Variable('x'), notify=[GFP_production_0_net])
		bacterialconsortium_net.add_input("producer", "diffusion_AHL_molecule_7", Variable('x'), notify=[AHL_production_0_net])
		bacterialconsortium_net.add_input("sensor", "diffusion_AHL_molecule_8", Variable('x'), notify=[GFP_production_0_net])
		bacterialconsortium_net.add_input("producer", "diffusion_AHL_molecule_9", Variable('x'), notify=[AHL_production_0_net])
		bacterialconsortium_net.add_input("sensor", "diffusion_AHL_molecule_10", Variable('x'), notify=[GFP_production_0_net])
		bacterialconsortium_net.add_output("sensor", "diffusion_AHL_molecule_1", Variable('x'), notify=[GFP_production_0_net])
		bacterialconsortium_net.add_output("producer", "diffusion_AHL_molecule_2", Variable('x'), notify=[AHL_production_0_net])
		bacterialconsortium_net.add_output("sensor", "diffusion_AHL_molecule_3", Variable('x'), notify=[GFP_production_0_net])
		bacterialconsortium_net.add_output("producer", "diffusion_AHL_molecule_4", Variable('x'), notify=[AHL_production_0_net])
		bacterialconsortium_net.add_output("sensor", "diffusion_AHL_molecule_5", Variable('x'), notify=[GFP_production_0_net])
		bacterialconsortium_net.add_output("producer", "diffusion_AHL_molecule_6", Variable('x'), notify=[AHL_production_0_net])
		bacterialconsortium_net.add_output("sensor", "diffusion_AHL_molecule_7", Variable('x'), notify=[GFP_production_0_net])
		bacterialconsortium_net.add_output("producer", "diffusion_AHL_molecule_8", Variable('x'), notify=[AHL_production_0_net])
		bacterialconsortium_net.add_output("sensor", "diffusion_AHL_molecule_9", Variable('x'), notify=[GFP_production_0_net])
		bacterialconsortium_net.add_output("producer", "diffusion_AHL_molecule_10", Variable('x'), notify=[AHL_production_0_net])

		# AHL_production_0_net arcs
		AHL_production_0_net.add_input("LacI_protein", "LacI_protein_degradation_1", Value(dot), notify=[bacterialconsortium_net.place('producer')])
		AHL_production_0_net.add_input("SAM_molecule", "SAM_molecule_degradation_1", Value(dot), notify=[bacterialconsortium_net.place('producer')])
		AHL_production_0_net.add_input("LuxI_gene", "LuxI_gene_transcription_1", Value(dot))
		AHL_production_0_net.add_input("LacI_protein", "LuxI_gene_inhibition_LacI_protein_1", Value(dot), notify=[bacterialconsortium_net.place('producer')])
		AHL_production_0_net.add_input("LuxI_gene", "LuxI_gene_inhibition_LacI_protein_1", Value(dot))
		AHL_production_0_net.add_input("LacI_protein", "LuxI_gene_inhibition_LacI_protein_2", Value(dot), notify=[bacterialconsortium_net.place('producer')])
		AHL_production_0_net.add_input("LuxI_gene", "LuxI_gene_inhibition_LacI_protein_2", Value(dot))
		AHL_production_0_net.add_input("LacI_protein", "LuxI_gene_inhibition_LacI_protein_3", Value(dot), notify=[bacterialconsortium_net.place('producer')])
		AHL_production_0_net.add_input("LuxI_gene", "LuxI_gene_inhibition_LacI_protein_3", Value(dot))
		AHL_production_0_net.add_input("LacI_protein", "LuxI_gene_inhibition_LacI_protein_4", Value(dot), notify=[bacterialconsortium_net.place('producer')])
		AHL_production_0_net.add_input("LuxI_gene", "LuxI_gene_inhibition_LacI_protein_4", Value(dot))
		AHL_production_0_net.add_input("LacI_protein", "LuxI_gene_inhibition_LacI_protein_5", Value(dot), notify=[bacterialconsortium_net.place('producer')])
		AHL_production_0_net.add_input("LuxI_gene", "LuxI_gene_inhibition_LacI_protein_5", Value(dot))
		AHL_production_0_net.add_input("LuxI_mrna", "LuxI_mrna_translation_1", MultiArc([Value(dot)]*3))
		AHL_production_0_net.add_input("LacI_protein", "LuxI_mrna_inhibition_LacI_protein_1", Value(dot), notify=[bacterialconsortium_net.place('producer')])
		AHL_production_0_net.add_input("LuxI_mrna", "LuxI_mrna_inhibition_LacI_protein_1", Value(dot))
		AHL_production_0_net.add_input("LacI_protein", "LuxI_mrna_inhibition_LacI_protein_2", Value(dot), notify=[bacterialconsortium_net.place('producer')])
		AHL_production_0_net.add_input("LuxI_mrna", "LuxI_mrna_inhibition_LacI_protein_2", Value(dot))
		AHL_production_0_net.add_input("LacI_protein", "LuxI_mrna_inhibition_LacI_protein_3", Value(dot), notify=[bacterialconsortium_net.place('producer')])
		AHL_production_0_net.add_input("LuxI_mrna", "LuxI_mrna_inhibition_LacI_protein_3", Value(dot))
		AHL_production_0_net.add_input("LacI_protein", "LuxI_mrna_inhibition_LacI_protein_4", Value(dot), notify=[bacterialconsortium_net.place('producer')])
		AHL_production_0_net.add_input("LuxI_mrna", "LuxI_mrna_inhibition_LacI_protein_4", Value(dot))
		AHL_production_0_net.add_input("LacI_protein", "LuxI_mrna_inhibition_LacI_protein_5", Value(dot), notify=[bacterialconsortium_net.place('producer')])
		AHL_production_0_net.add_input("LuxI_mrna", "LuxI_mrna_inhibition_LacI_protein_5", Value(dot))
		AHL_production_0_net.add_input("LuxI_protein", "LuxI_protein_degradation_1", Value(dot), notify=[bacterialconsortium_net.place('producer')])
		AHL_production_0_net.add_input("ACP_gene", "ACP_gene_transcription_1", Value(dot))
		AHL_production_0_net.add_input("ACP_mrna", "ACP_mrna_translation_1", Value(dot))
		AHL_production_0_net.add_input("ACP_protein", "ACP_protein_degradation_1", Value(dot), notify=[bacterialconsortium_net.place('producer')])
		AHL_production_0_net.add_input("LuxI_protein", "enzymatic_reaction_1", MultiArc([Value(dot)]*3), notify=[bacterialconsortium_net.place('producer')])
		AHL_production_0_net.add_input("SAM_molecule", "enzymatic_reaction_1", Value(dot), notify=[bacterialconsortium_net.place('producer')])
		AHL_production_0_net.add_input("ACP_protein", "enzymatic_reaction_1", Value(dot), notify=[bacterialconsortium_net.place('producer')])
		AHL_production_0_net.add_input("LuxI_protein", "enzymatic_reaction_2", MultiArc([Value(dot)]*3), notify=[bacterialconsortium_net.place('producer')])
		AHL_production_0_net.add_input("SAM_molecule", "enzymatic_reaction_2", Value(dot), notify=[bacterialconsortium_net.place('producer')])
		AHL_production_0_net.add_input("ACP_protein", "enzymatic_reaction_2", Value(dot), notify=[bacterialconsortium_net.place('producer')])
		AHL_production_0_net.add_input("LuxI_protein", "enzymatic_reaction_3", MultiArc([Value(dot)]*3), notify=[bacterialconsortium_net.place('producer')])
		AHL_production_0_net.add_input("SAM_molecule", "enzymatic_reaction_3", Value(dot), notify=[bacterialconsortium_net.place('producer')])
		AHL_production_0_net.add_input("ACP_protein", "enzymatic_reaction_3", Value(dot), notify=[bacterialconsortium_net.place('producer')])
		AHL_production_0_net.add_input("LuxI_protein", "enzymatic_reaction_4", MultiArc([Value(dot)]*3), notify=[bacterialconsortium_net.place('producer')])
		AHL_production_0_net.add_input("SAM_molecule", "enzymatic_reaction_4", Value(dot), notify=[bacterialconsortium_net.place('producer')])
		AHL_production_0_net.add_input("ACP_protein", "enzymatic_reaction_4", Value(dot), notify=[bacterialconsortium_net.place('producer')])
		AHL_production_0_net.add_input("LuxI_protein", "enzymatic_reaction_5", MultiArc([Value(dot)]*3), notify=[bacterialconsortium_net.place('producer')])
		AHL_production_0_net.add_input("SAM_molecule", "enzymatic_reaction_5", Value(dot), notify=[bacterialconsortium_net.place('producer')])
		AHL_production_0_net.add_input("ACP_protein", "enzymatic_reaction_5", Value(dot), notify=[bacterialconsortium_net.place('producer')])
		AHL_production_0_net.add_input("AHL_molecule", "AHL_molecule_degradation_1", Value(dot), notify=[bacterialconsortium_net.place('producer')])
		AHL_production_0_net.add_output("LuxI_gene", "LuxI_gene_transcription_1", Value(dot))
		AHL_production_0_net.add_output("LuxI_mrna", "LuxI_gene_transcription_1", MultiArc([Value(dot)]*2))
		AHL_production_0_net.add_output("LuxI_gene", "LuxI_gene_inhibition_LacI_protein_1", Value(dot))
		AHL_production_0_net.add_output("LuxI_gene", "LuxI_gene_inhibition_LacI_protein_2", Value(dot))
		AHL_production_0_net.add_output("LuxI_gene", "LuxI_gene_inhibition_LacI_protein_3", Value(dot))
		AHL_production_0_net.add_output("LuxI_gene", "LuxI_gene_inhibition_LacI_protein_4", Value(dot))
		AHL_production_0_net.add_output("LuxI_gene", "LuxI_gene_inhibition_LacI_protein_5", Value(dot))
		AHL_production_0_net.add_output("LuxI_protein", "LuxI_mrna_translation_1", MultiArc([Value(dot)]*2), notify=[bacterialconsortium_net.place('producer')])
		AHL_production_0_net.add_output("ACP_gene", "ACP_gene_transcription_1", Value(dot))
		AHL_production_0_net.add_output("ACP_mrna", "ACP_gene_transcription_1", Value(dot))
		AHL_production_0_net.add_output("ACP_protein", "ACP_mrna_translation_1", MultiArc([Value(dot)]*4), notify=[bacterialconsortium_net.place('producer')])
		AHL_production_0_net.add_output("LuxI_protein", "enzymatic_reaction_1", MultiArc([Value(dot)]*3), notify=[bacterialconsortium_net.place('producer')])
		AHL_production_0_net.add_output("AHL_molecule", "enzymatic_reaction_1", Value(dot), notify=[bacterialconsortium_net.place('producer')])
		AHL_production_0_net.add_output("LuxI_protein", "enzymatic_reaction_2", MultiArc([Value(dot)]*3), notify=[bacterialconsortium_net.place('producer')])
		AHL_production_0_net.add_output("AHL_molecule", "enzymatic_reaction_2", Value(dot), notify=[bacterialconsortium_net.place('producer')])
		AHL_production_0_net.add_output("LuxI_protein", "enzymatic_reaction_3", MultiArc([Value(dot)]*3), notify=[bacterialconsortium_net.place('producer')])
		AHL_production_0_net.add_output("AHL_molecule", "enzymatic_reaction_3", Value(dot), notify=[bacterialconsortium_net.place('producer')])
		AHL_production_0_net.add_output("LuxI_protein", "enzymatic_reaction_4", MultiArc([Value(dot)]*3), notify=[bacterialconsortium_net.place('producer')])
		AHL_production_0_net.add_output("AHL_molecule", "enzymatic_reaction_4", Value(dot), notify=[bacterialconsortium_net.place('producer')])
		AHL_production_0_net.add_output("LuxI_protein", "enzymatic_reaction_5", MultiArc([Value(dot)]*3), notify=[bacterialconsortium_net.place('producer')])
		AHL_production_0_net.add_output("AHL_molecule", "enzymatic_reaction_5", Value(dot), notify=[bacterialconsortium_net.place('producer')])

		# GFP_production_0_net arcs
		GFP_production_0_net.add_input("AHL_molecule", "AHL_molecule_degradation_2", Value(dot), notify=[bacterialconsortium_net.place('sensor')])
		GFP_production_0_net.add_input("LuxR_gene", "LuxR_gene_transcription_1", Value(dot))
		GFP_production_0_net.add_input("LuxR_mrna", "LuxR_mrna_translation_1", Value(dot))
		GFP_production_0_net.add_input("LuxR_protein", "LuxR_protein_degradation_1", Value(dot), notify=[bacterialconsortium_net.place('sensor')])
		GFP_production_0_net.add_input("LuxR_protein", "protein_complex_formation_1", MultiArc([Value(dot)]*3), notify=[bacterialconsortium_net.place('sensor')])
		GFP_production_0_net.add_input("AHL_molecule", "protein_complex_formation_1", MultiArc([Value(dot)]*3), notify=[bacterialconsortium_net.place('sensor')])
		GFP_production_0_net.add_input("LuxR_protein", "protein_complex_formation_2", MultiArc([Value(dot)]*3), notify=[bacterialconsortium_net.place('sensor')])
		GFP_production_0_net.add_input("AHL_molecule", "protein_complex_formation_2", MultiArc([Value(dot)]*3), notify=[bacterialconsortium_net.place('sensor')])
		GFP_production_0_net.add_input("LuxR_AHL_complex", "LuxR_AHL_complex_degradation_1", Value(dot), notify=[bacterialconsortium_net.place('sensor')])
		GFP_production_0_net.add_input("GFP_reporter_gene", "GFP_reporter_gene_transcription_1", Value(dot))
		GFP_production_0_net.add_input("LuxR_AHL_complex", "GFP_reporter_gene_transcription_1", Value(dot), notify=[bacterialconsortium_net.place('sensor')])
		GFP_production_0_net.add_input("GFP_reporter_mrna", "GFP_reporter_mrna_translation_1", MultiArc([Value(dot)]*2))
		GFP_production_0_net.add_input("GFP_reporter_protein", "GFP_reporter_protein_degradation_1", Value(dot), notify=[bacterialconsortium_net.place('sensor')])
		GFP_production_0_net.add_output("LuxR_gene", "LuxR_gene_transcription_1", Value(dot))
		GFP_production_0_net.add_output("LuxR_mrna", "LuxR_gene_transcription_1", Value(dot))
		GFP_production_0_net.add_output("LuxR_protein", "LuxR_mrna_translation_1", MultiArc([Value(dot)]*4), notify=[bacterialconsortium_net.place('sensor')])
		GFP_production_0_net.add_output("LuxR_AHL_complex", "protein_complex_formation_1", MultiArc([Value(dot)]*3), notify=[bacterialconsortium_net.place('sensor')])
		GFP_production_0_net.add_output("LuxR_AHL_complex", "protein_complex_formation_2", MultiArc([Value(dot)]*3), notify=[bacterialconsortium_net.place('sensor')])
		GFP_production_0_net.add_output("GFP_reporter_gene", "GFP_reporter_gene_transcription_1", Value(dot))
		GFP_production_0_net.add_output("GFP_reporter_mrna", "GFP_reporter_gene_transcription_1", MultiArc([Value(dot)]*3))
		GFP_production_0_net.add_output("GFP_reporter_protein", "GFP_reporter_mrna_translation_1", MultiArc([Value(dot)]*2), notify=[bacterialconsortium_net.place('sensor')])
		return bacterialconsortium_net
