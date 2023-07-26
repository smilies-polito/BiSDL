from petrisim.utils import *


class Rgb(Module):
	def __init__(self, name: str = None):
		if not name:
			name = __class__.__name__
		super().__init__(name)

	def build_net_structure(self) -> PetriNet:

		# petri nets
		mCherry_production_21_net = PetriNet("mCherry_production_21_net", timescale=1)
		BFP_production_21_net = PetriNet("BFP_production_21_net", timescale=1)
		CD19_production_21_net = PetriNet("CD19_production_21_net", timescale=1)
		mCherry_production_20_net = PetriNet("mCherry_production_20_net", timescale=1)
		BFP_production_20_net = PetriNet("BFP_production_20_net", timescale=1)
		CD19_production_20_net = PetriNet("CD19_production_20_net", timescale=1)
		mCherry_production_19_net = PetriNet("mCherry_production_19_net", timescale=1)
		BFP_production_19_net = PetriNet("BFP_production_19_net", timescale=1)
		CD19_production_19_net = PetriNet("CD19_production_19_net", timescale=1)
		mCherry_production_18_net = PetriNet("mCherry_production_18_net", timescale=1)
		BFP_production_18_net = PetriNet("BFP_production_18_net", timescale=1)
		CD19_production_18_net = PetriNet("CD19_production_18_net", timescale=1)
		mCherry_production_17_net = PetriNet("mCherry_production_17_net", timescale=1)
		BFP_production_17_net = PetriNet("BFP_production_17_net", timescale=1)
		CD19_production_17_net = PetriNet("CD19_production_17_net", timescale=1)
		mCherry_production_16_net = PetriNet("mCherry_production_16_net", timescale=1)
		BFP_production_16_net = PetriNet("BFP_production_16_net", timescale=1)
		CD19_production_16_net = PetriNet("CD19_production_16_net", timescale=1)
		mCherry_production_15_net = PetriNet("mCherry_production_15_net", timescale=1)
		BFP_production_15_net = PetriNet("BFP_production_15_net", timescale=1)
		CD19_production_15_net = PetriNet("CD19_production_15_net", timescale=1)
		mCherry_production_14_net = PetriNet("mCherry_production_14_net", timescale=1)
		BFP_production_14_net = PetriNet("BFP_production_14_net", timescale=1)
		CD19_production_14_net = PetriNet("CD19_production_14_net", timescale=1)
		mCherry_production_13_net = PetriNet("mCherry_production_13_net", timescale=1)
		BFP_production_13_net = PetriNet("BFP_production_13_net", timescale=1)
		CD19_production_13_net = PetriNet("CD19_production_13_net", timescale=1)
		mCherry_production_12_net = PetriNet("mCherry_production_12_net", timescale=1)
		BFP_production_12_net = PetriNet("BFP_production_12_net", timescale=1)
		CD19_production_12_net = PetriNet("CD19_production_12_net", timescale=1)
		mCherry_production_11_net = PetriNet("mCherry_production_11_net", timescale=1)
		BFP_production_11_net = PetriNet("BFP_production_11_net", timescale=1)
		CD19_production_11_net = PetriNet("CD19_production_11_net", timescale=1)
		mCherry_production_10_net = PetriNet("mCherry_production_10_net", timescale=1)
		BFP_production_10_net = PetriNet("BFP_production_10_net", timescale=1)
		CD19_production_10_net = PetriNet("CD19_production_10_net", timescale=1)
		mCherry_production_9_net = PetriNet("mCherry_production_9_net", timescale=1)
		BFP_production_9_net = PetriNet("BFP_production_9_net", timescale=1)
		CD19_production_9_net = PetriNet("CD19_production_9_net", timescale=1)
		mCherry_production_8_net = PetriNet("mCherry_production_8_net", timescale=1)
		BFP_production_8_net = PetriNet("BFP_production_8_net", timescale=1)
		CD19_production_8_net = PetriNet("CD19_production_8_net", timescale=1)
		mCherry_production_7_net = PetriNet("mCherry_production_7_net", timescale=1)
		BFP_production_7_net = PetriNet("BFP_production_7_net", timescale=1)
		CD19_production_7_net = PetriNet("CD19_production_7_net", timescale=1)
		mCherry_production_6_net = PetriNet("mCherry_production_6_net", timescale=1)
		BFP_production_6_net = PetriNet("BFP_production_6_net", timescale=1)
		CD19_production_6_net = PetriNet("CD19_production_6_net", timescale=1)
		mCherry_production_5_net = PetriNet("mCherry_production_5_net", timescale=1)
		BFP_production_5_net = PetriNet("BFP_production_5_net", timescale=1)
		CD19_production_5_net = PetriNet("CD19_production_5_net", timescale=1)
		mCherry_production_4_net = PetriNet("mCherry_production_4_net", timescale=1)
		BFP_production_4_net = PetriNet("BFP_production_4_net", timescale=1)
		CD19_production_4_net = PetriNet("CD19_production_4_net", timescale=1)
		mCherry_production_3_net = PetriNet("mCherry_production_3_net", timescale=1)
		BFP_production_3_net = PetriNet("BFP_production_3_net", timescale=1)
		CD19_production_3_net = PetriNet("CD19_production_3_net", timescale=1)
		mCherry_production_2_net = PetriNet("mCherry_production_2_net", timescale=1)
		BFP_production_2_net = PetriNet("BFP_production_2_net", timescale=1)
		CD19_production_2_net = PetriNet("CD19_production_2_net", timescale=1)
		mCherry_production_1_net = PetriNet("mCherry_production_1_net", timescale=1)
		BFP_production_1_net = PetriNet("BFP_production_1_net", timescale=1)
		CD19_production_1_net = PetriNet("CD19_production_1_net", timescale=1)
		mCherry_production_0_net = PetriNet("mCherry_production_0_net", timescale=1)
		BFP_production_0_net = PetriNet("BFP_production_0_net", timescale=1)
		CD19_production_0_net = PetriNet("CD19_production_0_net", timescale=1)
		GFP_production_0_net = PetriNet("GFP_production_0_net", timescale=1)
		rgb_net = PetriNet("rgb_net", timescale=1)

		# mCherry_production_21_net places
		mCherry_production_21_net.add_place(Place("GFP_receptor_gene", [BlackToken()]))
		mCherry_production_21_net.add_place(Place("GFP_receptor_mrna"))
		mCherry_production_21_net.add_place(Place("GFP_receptor_protein"))
		mCherry_production_21_net.add_place(Place("GFP_receptor_active_protein"))
		mCherry_production_21_net.add_place(Place("GFP_activation_mediator_protein"))
		mCherry_production_21_net.add_place(Place("mCherry_gene", [BlackToken()]))
		mCherry_production_21_net.add_place(Place("mCherry_mrna"))
		mCherry_production_21_net.add_place(Place("mCherry_protein"))

		# mCherry_production_21_net transitions
		mCherry_production_21_net.add_transition(Transition("GFP_receptor_gene_transcription_1_21"))
		mCherry_production_21_net.add_transition(Transition("GFP_receptor_mrna_translation_1_21"))
		mCherry_production_21_net.add_transition(Transition("enzymatic_reaction_1_21"))
		mCherry_production_21_net.add_transition(Transition("GFP_receptor_active_protein_degradation_1_21"))
		mCherry_production_21_net.add_transition(Transition("mCherry_gene_transcription_1_21"))
		mCherry_production_21_net.add_transition(Transition("mCherry_mrna_translation_1_21"))
		mCherry_production_21_net.add_transition(Transition("mCherry_protein_degradation_1_21"))

		# BFP_production_21_net places
		BFP_production_21_net.add_place(Place("BFP_gene", [BlackToken()]))
		BFP_production_21_net.add_place(Place("BFP_mrna"))
		BFP_production_21_net.add_place(Place("BFP_protein"))

		# BFP_production_21_net transitions
		BFP_production_21_net.add_transition(Transition("BFP_gene_transcription_1_21"))
		BFP_production_21_net.add_transition(Transition("BFP_mrna_translation_1_21"))
		BFP_production_21_net.add_transition(Transition("BFP_protein_degradation_1_21"))

		# CD19_production_21_net places
		CD19_production_21_net.add_place(Place("CD19_gene", [BlackToken()]))
		CD19_production_21_net.add_place(Place("CD19_mrna"))
		CD19_production_21_net.add_place(Place("CD19_protein"))

		# CD19_production_21_net transitions
		CD19_production_21_net.add_transition(Transition("CD19_gene_transcription_1_21"))
		CD19_production_21_net.add_transition(Transition("CD19_mrna_translation_1_21"))
		CD19_production_21_net.add_transition(Transition("CD19_protein_degradation_1_21"))

		# mCherry_production_20_net places
		mCherry_production_20_net.add_place(Place("GFP_receptor_gene", [BlackToken()]))
		mCherry_production_20_net.add_place(Place("GFP_receptor_mrna"))
		mCherry_production_20_net.add_place(Place("GFP_receptor_protein"))
		mCherry_production_20_net.add_place(Place("GFP_receptor_active_protein"))
		mCherry_production_20_net.add_place(Place("GFP_activation_mediator_protein"))
		mCherry_production_20_net.add_place(Place("mCherry_gene", [BlackToken()]))
		mCherry_production_20_net.add_place(Place("mCherry_mrna"))
		mCherry_production_20_net.add_place(Place("mCherry_protein"))

		# mCherry_production_20_net transitions
		mCherry_production_20_net.add_transition(Transition("GFP_receptor_gene_transcription_1_20"))
		mCherry_production_20_net.add_transition(Transition("GFP_receptor_mrna_translation_1_20"))
		mCherry_production_20_net.add_transition(Transition("enzymatic_reaction_1_20"))
		mCherry_production_20_net.add_transition(Transition("GFP_receptor_active_protein_degradation_1_20"))
		mCherry_production_20_net.add_transition(Transition("mCherry_gene_transcription_1_20"))
		mCherry_production_20_net.add_transition(Transition("mCherry_mrna_translation_1_20"))
		mCherry_production_20_net.add_transition(Transition("mCherry_protein_degradation_1_20"))

		# BFP_production_20_net places
		BFP_production_20_net.add_place(Place("BFP_gene", [BlackToken()]))
		BFP_production_20_net.add_place(Place("BFP_mrna"))
		BFP_production_20_net.add_place(Place("BFP_protein"))

		# BFP_production_20_net transitions
		BFP_production_20_net.add_transition(Transition("BFP_gene_transcription_1_20"))
		BFP_production_20_net.add_transition(Transition("BFP_mrna_translation_1_20"))
		BFP_production_20_net.add_transition(Transition("BFP_protein_degradation_1_20"))

		# CD19_production_20_net places
		CD19_production_20_net.add_place(Place("CD19_gene", [BlackToken()]))
		CD19_production_20_net.add_place(Place("CD19_mrna"))
		CD19_production_20_net.add_place(Place("CD19_protein"))

		# CD19_production_20_net transitions
		CD19_production_20_net.add_transition(Transition("CD19_gene_transcription_1_20"))
		CD19_production_20_net.add_transition(Transition("CD19_mrna_translation_1_20"))
		CD19_production_20_net.add_transition(Transition("CD19_protein_degradation_1_20"))

		# mCherry_production_19_net places
		mCherry_production_19_net.add_place(Place("GFP_receptor_gene", [BlackToken()]))
		mCherry_production_19_net.add_place(Place("GFP_receptor_mrna"))
		mCherry_production_19_net.add_place(Place("GFP_receptor_protein"))
		mCherry_production_19_net.add_place(Place("GFP_receptor_active_protein"))
		mCherry_production_19_net.add_place(Place("GFP_activation_mediator_protein"))
		mCherry_production_19_net.add_place(Place("mCherry_gene", [BlackToken()]))
		mCherry_production_19_net.add_place(Place("mCherry_mrna"))
		mCherry_production_19_net.add_place(Place("mCherry_protein"))

		# mCherry_production_19_net transitions
		mCherry_production_19_net.add_transition(Transition("GFP_receptor_gene_transcription_1_19"))
		mCherry_production_19_net.add_transition(Transition("GFP_receptor_mrna_translation_1_19"))
		mCherry_production_19_net.add_transition(Transition("enzymatic_reaction_1_19"))
		mCherry_production_19_net.add_transition(Transition("GFP_receptor_active_protein_degradation_1_19"))
		mCherry_production_19_net.add_transition(Transition("mCherry_gene_transcription_1_19"))
		mCherry_production_19_net.add_transition(Transition("mCherry_mrna_translation_1_19"))
		mCherry_production_19_net.add_transition(Transition("mCherry_protein_degradation_1_19"))

		# BFP_production_19_net places
		BFP_production_19_net.add_place(Place("BFP_gene", [BlackToken()]))
		BFP_production_19_net.add_place(Place("BFP_mrna"))
		BFP_production_19_net.add_place(Place("BFP_protein"))

		# BFP_production_19_net transitions
		BFP_production_19_net.add_transition(Transition("BFP_gene_transcription_1_19"))
		BFP_production_19_net.add_transition(Transition("BFP_mrna_translation_1_19"))
		BFP_production_19_net.add_transition(Transition("BFP_protein_degradation_1_19"))

		# CD19_production_19_net places
		CD19_production_19_net.add_place(Place("CD19_gene", [BlackToken()]))
		CD19_production_19_net.add_place(Place("CD19_mrna"))
		CD19_production_19_net.add_place(Place("CD19_protein"))

		# CD19_production_19_net transitions
		CD19_production_19_net.add_transition(Transition("CD19_gene_transcription_1_19"))
		CD19_production_19_net.add_transition(Transition("CD19_mrna_translation_1_19"))
		CD19_production_19_net.add_transition(Transition("CD19_protein_degradation_1_19"))

		# mCherry_production_18_net places
		mCherry_production_18_net.add_place(Place("GFP_receptor_gene", [BlackToken()]))
		mCherry_production_18_net.add_place(Place("GFP_receptor_mrna"))
		mCherry_production_18_net.add_place(Place("GFP_receptor_protein"))
		mCherry_production_18_net.add_place(Place("GFP_receptor_active_protein"))
		mCherry_production_18_net.add_place(Place("GFP_activation_mediator_protein"))
		mCherry_production_18_net.add_place(Place("mCherry_gene", [BlackToken()]))
		mCherry_production_18_net.add_place(Place("mCherry_mrna"))
		mCherry_production_18_net.add_place(Place("mCherry_protein"))

		# mCherry_production_18_net transitions
		mCherry_production_18_net.add_transition(Transition("GFP_receptor_gene_transcription_1_18"))
		mCherry_production_18_net.add_transition(Transition("GFP_receptor_mrna_translation_1_18"))
		mCherry_production_18_net.add_transition(Transition("enzymatic_reaction_1_18"))
		mCherry_production_18_net.add_transition(Transition("GFP_receptor_active_protein_degradation_1_18"))
		mCherry_production_18_net.add_transition(Transition("mCherry_gene_transcription_1_18"))
		mCherry_production_18_net.add_transition(Transition("mCherry_mrna_translation_1_18"))
		mCherry_production_18_net.add_transition(Transition("mCherry_protein_degradation_1_18"))

		# BFP_production_18_net places
		BFP_production_18_net.add_place(Place("BFP_gene", [BlackToken()]))
		BFP_production_18_net.add_place(Place("BFP_mrna"))
		BFP_production_18_net.add_place(Place("BFP_protein"))

		# BFP_production_18_net transitions
		BFP_production_18_net.add_transition(Transition("BFP_gene_transcription_1_18"))
		BFP_production_18_net.add_transition(Transition("BFP_mrna_translation_1_18"))
		BFP_production_18_net.add_transition(Transition("BFP_protein_degradation_1_18"))

		# CD19_production_18_net places
		CD19_production_18_net.add_place(Place("CD19_gene", [BlackToken()]))
		CD19_production_18_net.add_place(Place("CD19_mrna"))
		CD19_production_18_net.add_place(Place("CD19_protein"))

		# CD19_production_18_net transitions
		CD19_production_18_net.add_transition(Transition("CD19_gene_transcription_1_18"))
		CD19_production_18_net.add_transition(Transition("CD19_mrna_translation_1_18"))
		CD19_production_18_net.add_transition(Transition("CD19_protein_degradation_1_18"))

		# mCherry_production_17_net places
		mCherry_production_17_net.add_place(Place("GFP_receptor_gene", [BlackToken()]))
		mCherry_production_17_net.add_place(Place("GFP_receptor_mrna"))
		mCherry_production_17_net.add_place(Place("GFP_receptor_protein"))
		mCherry_production_17_net.add_place(Place("GFP_receptor_active_protein"))
		mCherry_production_17_net.add_place(Place("GFP_activation_mediator_protein"))
		mCherry_production_17_net.add_place(Place("mCherry_gene", [BlackToken()]))
		mCherry_production_17_net.add_place(Place("mCherry_mrna"))
		mCherry_production_17_net.add_place(Place("mCherry_protein"))

		# mCherry_production_17_net transitions
		mCherry_production_17_net.add_transition(Transition("GFP_receptor_gene_transcription_1_17"))
		mCherry_production_17_net.add_transition(Transition("GFP_receptor_mrna_translation_1_17"))
		mCherry_production_17_net.add_transition(Transition("enzymatic_reaction_1_17"))
		mCherry_production_17_net.add_transition(Transition("GFP_receptor_active_protein_degradation_1_17"))
		mCherry_production_17_net.add_transition(Transition("mCherry_gene_transcription_1_17"))
		mCherry_production_17_net.add_transition(Transition("mCherry_mrna_translation_1_17"))
		mCherry_production_17_net.add_transition(Transition("mCherry_protein_degradation_1_17"))

		# BFP_production_17_net places
		BFP_production_17_net.add_place(Place("BFP_gene", [BlackToken()]))
		BFP_production_17_net.add_place(Place("BFP_mrna"))
		BFP_production_17_net.add_place(Place("BFP_protein"))

		# BFP_production_17_net transitions
		BFP_production_17_net.add_transition(Transition("BFP_gene_transcription_1_17"))
		BFP_production_17_net.add_transition(Transition("BFP_mrna_translation_1_17"))
		BFP_production_17_net.add_transition(Transition("BFP_protein_degradation_1_17"))

		# CD19_production_17_net places
		CD19_production_17_net.add_place(Place("CD19_gene", [BlackToken()]))
		CD19_production_17_net.add_place(Place("CD19_mrna"))
		CD19_production_17_net.add_place(Place("CD19_protein"))

		# CD19_production_17_net transitions
		CD19_production_17_net.add_transition(Transition("CD19_gene_transcription_1_17"))
		CD19_production_17_net.add_transition(Transition("CD19_mrna_translation_1_17"))
		CD19_production_17_net.add_transition(Transition("CD19_protein_degradation_1_17"))

		# mCherry_production_16_net places
		mCherry_production_16_net.add_place(Place("GFP_receptor_gene", [BlackToken()]))
		mCherry_production_16_net.add_place(Place("GFP_receptor_mrna"))
		mCherry_production_16_net.add_place(Place("GFP_receptor_protein"))
		mCherry_production_16_net.add_place(Place("GFP_receptor_active_protein"))
		mCherry_production_16_net.add_place(Place("GFP_activation_mediator_protein"))
		mCherry_production_16_net.add_place(Place("mCherry_gene", [BlackToken()]))
		mCherry_production_16_net.add_place(Place("mCherry_mrna"))
		mCherry_production_16_net.add_place(Place("mCherry_protein"))

		# mCherry_production_16_net transitions
		mCherry_production_16_net.add_transition(Transition("GFP_receptor_gene_transcription_1_16"))
		mCherry_production_16_net.add_transition(Transition("GFP_receptor_mrna_translation_1_16"))
		mCherry_production_16_net.add_transition(Transition("enzymatic_reaction_1_16"))
		mCherry_production_16_net.add_transition(Transition("GFP_receptor_active_protein_degradation_1_16"))
		mCherry_production_16_net.add_transition(Transition("mCherry_gene_transcription_1_16"))
		mCherry_production_16_net.add_transition(Transition("mCherry_mrna_translation_1_16"))
		mCherry_production_16_net.add_transition(Transition("mCherry_protein_degradation_1_16"))

		# BFP_production_16_net places
		BFP_production_16_net.add_place(Place("BFP_gene", [BlackToken()]))
		BFP_production_16_net.add_place(Place("BFP_mrna"))
		BFP_production_16_net.add_place(Place("BFP_protein"))

		# BFP_production_16_net transitions
		BFP_production_16_net.add_transition(Transition("BFP_gene_transcription_1_16"))
		BFP_production_16_net.add_transition(Transition("BFP_mrna_translation_1_16"))
		BFP_production_16_net.add_transition(Transition("BFP_protein_degradation_1_16"))

		# CD19_production_16_net places
		CD19_production_16_net.add_place(Place("CD19_gene", [BlackToken()]))
		CD19_production_16_net.add_place(Place("CD19_mrna"))
		CD19_production_16_net.add_place(Place("CD19_protein"))

		# CD19_production_16_net transitions
		CD19_production_16_net.add_transition(Transition("CD19_gene_transcription_1_16"))
		CD19_production_16_net.add_transition(Transition("CD19_mrna_translation_1_16"))
		CD19_production_16_net.add_transition(Transition("CD19_protein_degradation_1_16"))

		# mCherry_production_15_net places
		mCherry_production_15_net.add_place(Place("GFP_receptor_gene", [BlackToken()]))
		mCherry_production_15_net.add_place(Place("GFP_receptor_mrna"))
		mCherry_production_15_net.add_place(Place("GFP_receptor_protein"))
		mCherry_production_15_net.add_place(Place("GFP_receptor_active_protein"))
		mCherry_production_15_net.add_place(Place("GFP_activation_mediator_protein"))
		mCherry_production_15_net.add_place(Place("mCherry_gene", [BlackToken()]))
		mCherry_production_15_net.add_place(Place("mCherry_mrna"))
		mCherry_production_15_net.add_place(Place("mCherry_protein"))

		# mCherry_production_15_net transitions
		mCherry_production_15_net.add_transition(Transition("GFP_receptor_gene_transcription_1_15"))
		mCherry_production_15_net.add_transition(Transition("GFP_receptor_mrna_translation_1_15"))
		mCherry_production_15_net.add_transition(Transition("enzymatic_reaction_1_15"))
		mCherry_production_15_net.add_transition(Transition("GFP_receptor_active_protein_degradation_1_15"))
		mCherry_production_15_net.add_transition(Transition("mCherry_gene_transcription_1_15"))
		mCherry_production_15_net.add_transition(Transition("mCherry_mrna_translation_1_15"))
		mCherry_production_15_net.add_transition(Transition("mCherry_protein_degradation_1_15"))

		# BFP_production_15_net places
		BFP_production_15_net.add_place(Place("BFP_gene", [BlackToken()]))
		BFP_production_15_net.add_place(Place("BFP_mrna"))
		BFP_production_15_net.add_place(Place("BFP_protein"))

		# BFP_production_15_net transitions
		BFP_production_15_net.add_transition(Transition("BFP_gene_transcription_1_15"))
		BFP_production_15_net.add_transition(Transition("BFP_mrna_translation_1_15"))
		BFP_production_15_net.add_transition(Transition("BFP_protein_degradation_1_15"))

		# CD19_production_15_net places
		CD19_production_15_net.add_place(Place("CD19_gene", [BlackToken()]))
		CD19_production_15_net.add_place(Place("CD19_mrna"))
		CD19_production_15_net.add_place(Place("CD19_protein"))

		# CD19_production_15_net transitions
		CD19_production_15_net.add_transition(Transition("CD19_gene_transcription_1_15"))
		CD19_production_15_net.add_transition(Transition("CD19_mrna_translation_1_15"))
		CD19_production_15_net.add_transition(Transition("CD19_protein_degradation_1_15"))

		# mCherry_production_14_net places
		mCherry_production_14_net.add_place(Place("GFP_receptor_gene", [BlackToken()]))
		mCherry_production_14_net.add_place(Place("GFP_receptor_mrna"))
		mCherry_production_14_net.add_place(Place("GFP_receptor_protein"))
		mCherry_production_14_net.add_place(Place("GFP_receptor_active_protein"))
		mCherry_production_14_net.add_place(Place("GFP_activation_mediator_protein"))
		mCherry_production_14_net.add_place(Place("mCherry_gene", [BlackToken()]))
		mCherry_production_14_net.add_place(Place("mCherry_mrna"))
		mCherry_production_14_net.add_place(Place("mCherry_protein"))

		# mCherry_production_14_net transitions
		mCherry_production_14_net.add_transition(Transition("GFP_receptor_gene_transcription_1_14"))
		mCherry_production_14_net.add_transition(Transition("GFP_receptor_mrna_translation_1_14"))
		mCherry_production_14_net.add_transition(Transition("enzymatic_reaction_1_14"))
		mCherry_production_14_net.add_transition(Transition("GFP_receptor_active_protein_degradation_1_14"))
		mCherry_production_14_net.add_transition(Transition("mCherry_gene_transcription_1_14"))
		mCherry_production_14_net.add_transition(Transition("mCherry_mrna_translation_1_14"))
		mCherry_production_14_net.add_transition(Transition("mCherry_protein_degradation_1_14"))

		# BFP_production_14_net places
		BFP_production_14_net.add_place(Place("BFP_gene", [BlackToken()]))
		BFP_production_14_net.add_place(Place("BFP_mrna"))
		BFP_production_14_net.add_place(Place("BFP_protein"))

		# BFP_production_14_net transitions
		BFP_production_14_net.add_transition(Transition("BFP_gene_transcription_1_14"))
		BFP_production_14_net.add_transition(Transition("BFP_mrna_translation_1_14"))
		BFP_production_14_net.add_transition(Transition("BFP_protein_degradation_1_14"))

		# CD19_production_14_net places
		CD19_production_14_net.add_place(Place("CD19_gene", [BlackToken()]))
		CD19_production_14_net.add_place(Place("CD19_mrna"))
		CD19_production_14_net.add_place(Place("CD19_protein"))

		# CD19_production_14_net transitions
		CD19_production_14_net.add_transition(Transition("CD19_gene_transcription_1_14"))
		CD19_production_14_net.add_transition(Transition("CD19_mrna_translation_1_14"))
		CD19_production_14_net.add_transition(Transition("CD19_protein_degradation_1_14"))

		# mCherry_production_13_net places
		mCherry_production_13_net.add_place(Place("GFP_receptor_gene", [BlackToken()]))
		mCherry_production_13_net.add_place(Place("GFP_receptor_mrna"))
		mCherry_production_13_net.add_place(Place("GFP_receptor_protein"))
		mCherry_production_13_net.add_place(Place("GFP_receptor_active_protein"))
		mCherry_production_13_net.add_place(Place("GFP_activation_mediator_protein"))
		mCherry_production_13_net.add_place(Place("mCherry_gene", [BlackToken()]))
		mCherry_production_13_net.add_place(Place("mCherry_mrna"))
		mCherry_production_13_net.add_place(Place("mCherry_protein"))

		# mCherry_production_13_net transitions
		mCherry_production_13_net.add_transition(Transition("GFP_receptor_gene_transcription_1_13"))
		mCherry_production_13_net.add_transition(Transition("GFP_receptor_mrna_translation_1_13"))
		mCherry_production_13_net.add_transition(Transition("enzymatic_reaction_1_13"))
		mCherry_production_13_net.add_transition(Transition("GFP_receptor_active_protein_degradation_1_13"))
		mCherry_production_13_net.add_transition(Transition("mCherry_gene_transcription_1_13"))
		mCherry_production_13_net.add_transition(Transition("mCherry_mrna_translation_1_13"))
		mCherry_production_13_net.add_transition(Transition("mCherry_protein_degradation_1_13"))

		# BFP_production_13_net places
		BFP_production_13_net.add_place(Place("BFP_gene", [BlackToken()]))
		BFP_production_13_net.add_place(Place("BFP_mrna"))
		BFP_production_13_net.add_place(Place("BFP_protein"))

		# BFP_production_13_net transitions
		BFP_production_13_net.add_transition(Transition("BFP_gene_transcription_1_13"))
		BFP_production_13_net.add_transition(Transition("BFP_mrna_translation_1_13"))
		BFP_production_13_net.add_transition(Transition("BFP_protein_degradation_1_13"))

		# CD19_production_13_net places
		CD19_production_13_net.add_place(Place("CD19_gene", [BlackToken()]))
		CD19_production_13_net.add_place(Place("CD19_mrna"))
		CD19_production_13_net.add_place(Place("CD19_protein"))

		# CD19_production_13_net transitions
		CD19_production_13_net.add_transition(Transition("CD19_gene_transcription_1_13"))
		CD19_production_13_net.add_transition(Transition("CD19_mrna_translation_1_13"))
		CD19_production_13_net.add_transition(Transition("CD19_protein_degradation_1_13"))

		# mCherry_production_12_net places
		mCherry_production_12_net.add_place(Place("GFP_receptor_gene", [BlackToken()]))
		mCherry_production_12_net.add_place(Place("GFP_receptor_mrna"))
		mCherry_production_12_net.add_place(Place("GFP_receptor_protein"))
		mCherry_production_12_net.add_place(Place("GFP_receptor_active_protein"))
		mCherry_production_12_net.add_place(Place("GFP_activation_mediator_protein"))
		mCherry_production_12_net.add_place(Place("mCherry_gene", [BlackToken()]))
		mCherry_production_12_net.add_place(Place("mCherry_mrna"))
		mCherry_production_12_net.add_place(Place("mCherry_protein"))

		# mCherry_production_12_net transitions
		mCherry_production_12_net.add_transition(Transition("GFP_receptor_gene_transcription_1_12"))
		mCherry_production_12_net.add_transition(Transition("GFP_receptor_mrna_translation_1_12"))
		mCherry_production_12_net.add_transition(Transition("enzymatic_reaction_1_12"))
		mCherry_production_12_net.add_transition(Transition("GFP_receptor_active_protein_degradation_1_12"))
		mCherry_production_12_net.add_transition(Transition("mCherry_gene_transcription_1_12"))
		mCherry_production_12_net.add_transition(Transition("mCherry_mrna_translation_1_12"))
		mCherry_production_12_net.add_transition(Transition("mCherry_protein_degradation_1_12"))

		# BFP_production_12_net places
		BFP_production_12_net.add_place(Place("BFP_gene", [BlackToken()]))
		BFP_production_12_net.add_place(Place("BFP_mrna"))
		BFP_production_12_net.add_place(Place("BFP_protein"))

		# BFP_production_12_net transitions
		BFP_production_12_net.add_transition(Transition("BFP_gene_transcription_1_12"))
		BFP_production_12_net.add_transition(Transition("BFP_mrna_translation_1_12"))
		BFP_production_12_net.add_transition(Transition("BFP_protein_degradation_1_12"))

		# CD19_production_12_net places
		CD19_production_12_net.add_place(Place("CD19_gene", [BlackToken()]))
		CD19_production_12_net.add_place(Place("CD19_mrna"))
		CD19_production_12_net.add_place(Place("CD19_protein"))

		# CD19_production_12_net transitions
		CD19_production_12_net.add_transition(Transition("CD19_gene_transcription_1_12"))
		CD19_production_12_net.add_transition(Transition("CD19_mrna_translation_1_12"))
		CD19_production_12_net.add_transition(Transition("CD19_protein_degradation_1_12"))

		# mCherry_production_11_net places
		mCherry_production_11_net.add_place(Place("GFP_receptor_gene", [BlackToken()]))
		mCherry_production_11_net.add_place(Place("GFP_receptor_mrna"))
		mCherry_production_11_net.add_place(Place("GFP_receptor_protein"))
		mCherry_production_11_net.add_place(Place("GFP_receptor_active_protein"))
		mCherry_production_11_net.add_place(Place("GFP_activation_mediator_protein"))
		mCherry_production_11_net.add_place(Place("mCherry_gene", [BlackToken()]))
		mCherry_production_11_net.add_place(Place("mCherry_mrna"))
		mCherry_production_11_net.add_place(Place("mCherry_protein"))

		# mCherry_production_11_net transitions
		mCherry_production_11_net.add_transition(Transition("GFP_receptor_gene_transcription_1_11"))
		mCherry_production_11_net.add_transition(Transition("GFP_receptor_mrna_translation_1_11"))
		mCherry_production_11_net.add_transition(Transition("enzymatic_reaction_1_11"))
		mCherry_production_11_net.add_transition(Transition("GFP_receptor_active_protein_degradation_1_11"))
		mCherry_production_11_net.add_transition(Transition("mCherry_gene_transcription_1_11"))
		mCherry_production_11_net.add_transition(Transition("mCherry_mrna_translation_1_11"))
		mCherry_production_11_net.add_transition(Transition("mCherry_protein_degradation_1_11"))

		# BFP_production_11_net places
		BFP_production_11_net.add_place(Place("BFP_gene", [BlackToken()]))
		BFP_production_11_net.add_place(Place("BFP_mrna"))
		BFP_production_11_net.add_place(Place("BFP_protein"))

		# BFP_production_11_net transitions
		BFP_production_11_net.add_transition(Transition("BFP_gene_transcription_1_11"))
		BFP_production_11_net.add_transition(Transition("BFP_mrna_translation_1_11"))
		BFP_production_11_net.add_transition(Transition("BFP_protein_degradation_1_11"))

		# CD19_production_11_net places
		CD19_production_11_net.add_place(Place("CD19_gene", [BlackToken()]))
		CD19_production_11_net.add_place(Place("CD19_mrna"))
		CD19_production_11_net.add_place(Place("CD19_protein"))

		# CD19_production_11_net transitions
		CD19_production_11_net.add_transition(Transition("CD19_gene_transcription_1_11"))
		CD19_production_11_net.add_transition(Transition("CD19_mrna_translation_1_11"))
		CD19_production_11_net.add_transition(Transition("CD19_protein_degradation_1_11"))

		# mCherry_production_10_net places
		mCherry_production_10_net.add_place(Place("GFP_receptor_gene", [BlackToken()]))
		mCherry_production_10_net.add_place(Place("GFP_receptor_mrna"))
		mCherry_production_10_net.add_place(Place("GFP_receptor_protein"))
		mCherry_production_10_net.add_place(Place("GFP_receptor_active_protein"))
		mCherry_production_10_net.add_place(Place("GFP_activation_mediator_protein"))
		mCherry_production_10_net.add_place(Place("mCherry_gene", [BlackToken()]))
		mCherry_production_10_net.add_place(Place("mCherry_mrna"))
		mCherry_production_10_net.add_place(Place("mCherry_protein"))

		# mCherry_production_10_net transitions
		mCherry_production_10_net.add_transition(Transition("GFP_receptor_gene_transcription_1_10"))
		mCherry_production_10_net.add_transition(Transition("GFP_receptor_mrna_translation_1_10"))
		mCherry_production_10_net.add_transition(Transition("enzymatic_reaction_1_10"))
		mCherry_production_10_net.add_transition(Transition("GFP_receptor_active_protein_degradation_1_10"))
		mCherry_production_10_net.add_transition(Transition("mCherry_gene_transcription_1_10"))
		mCherry_production_10_net.add_transition(Transition("mCherry_mrna_translation_1_10"))
		mCherry_production_10_net.add_transition(Transition("mCherry_protein_degradation_1_10"))

		# BFP_production_10_net places
		BFP_production_10_net.add_place(Place("BFP_gene", [BlackToken()]))
		BFP_production_10_net.add_place(Place("BFP_mrna"))
		BFP_production_10_net.add_place(Place("BFP_protein"))

		# BFP_production_10_net transitions
		BFP_production_10_net.add_transition(Transition("BFP_gene_transcription_1_10"))
		BFP_production_10_net.add_transition(Transition("BFP_mrna_translation_1_10"))
		BFP_production_10_net.add_transition(Transition("BFP_protein_degradation_1_10"))

		# CD19_production_10_net places
		CD19_production_10_net.add_place(Place("CD19_gene", [BlackToken()]))
		CD19_production_10_net.add_place(Place("CD19_mrna"))
		CD19_production_10_net.add_place(Place("CD19_protein"))

		# CD19_production_10_net transitions
		CD19_production_10_net.add_transition(Transition("CD19_gene_transcription_1_10"))
		CD19_production_10_net.add_transition(Transition("CD19_mrna_translation_1_10"))
		CD19_production_10_net.add_transition(Transition("CD19_protein_degradation_1_10"))

		# mCherry_production_9_net places
		mCherry_production_9_net.add_place(Place("GFP_receptor_gene", [BlackToken()]))
		mCherry_production_9_net.add_place(Place("GFP_receptor_mrna"))
		mCherry_production_9_net.add_place(Place("GFP_receptor_protein"))
		mCherry_production_9_net.add_place(Place("GFP_receptor_active_protein"))
		mCherry_production_9_net.add_place(Place("GFP_activation_mediator_protein"))
		mCherry_production_9_net.add_place(Place("mCherry_gene", [BlackToken()]))
		mCherry_production_9_net.add_place(Place("mCherry_mrna"))
		mCherry_production_9_net.add_place(Place("mCherry_protein"))

		# mCherry_production_9_net transitions
		mCherry_production_9_net.add_transition(Transition("GFP_receptor_gene_transcription_1_9"))
		mCherry_production_9_net.add_transition(Transition("GFP_receptor_mrna_translation_1_9"))
		mCherry_production_9_net.add_transition(Transition("enzymatic_reaction_1_9"))
		mCherry_production_9_net.add_transition(Transition("GFP_receptor_active_protein_degradation_1_9"))
		mCherry_production_9_net.add_transition(Transition("mCherry_gene_transcription_1_9"))
		mCherry_production_9_net.add_transition(Transition("mCherry_mrna_translation_1_9"))
		mCherry_production_9_net.add_transition(Transition("mCherry_protein_degradation_1_9"))

		# BFP_production_9_net places
		BFP_production_9_net.add_place(Place("BFP_gene", [BlackToken()]))
		BFP_production_9_net.add_place(Place("BFP_mrna"))
		BFP_production_9_net.add_place(Place("BFP_protein"))

		# BFP_production_9_net transitions
		BFP_production_9_net.add_transition(Transition("BFP_gene_transcription_1_9"))
		BFP_production_9_net.add_transition(Transition("BFP_mrna_translation_1_9"))
		BFP_production_9_net.add_transition(Transition("BFP_protein_degradation_1_9"))

		# CD19_production_9_net places
		CD19_production_9_net.add_place(Place("CD19_gene", [BlackToken()]))
		CD19_production_9_net.add_place(Place("CD19_mrna"))
		CD19_production_9_net.add_place(Place("CD19_protein"))

		# CD19_production_9_net transitions
		CD19_production_9_net.add_transition(Transition("CD19_gene_transcription_1_9"))
		CD19_production_9_net.add_transition(Transition("CD19_mrna_translation_1_9"))
		CD19_production_9_net.add_transition(Transition("CD19_protein_degradation_1_9"))

		# mCherry_production_8_net places
		mCherry_production_8_net.add_place(Place("GFP_receptor_gene", [BlackToken()]))
		mCherry_production_8_net.add_place(Place("GFP_receptor_mrna"))
		mCherry_production_8_net.add_place(Place("GFP_receptor_protein"))
		mCherry_production_8_net.add_place(Place("GFP_receptor_active_protein"))
		mCherry_production_8_net.add_place(Place("GFP_activation_mediator_protein"))
		mCherry_production_8_net.add_place(Place("mCherry_gene", [BlackToken()]))
		mCherry_production_8_net.add_place(Place("mCherry_mrna"))
		mCherry_production_8_net.add_place(Place("mCherry_protein"))

		# mCherry_production_8_net transitions
		mCherry_production_8_net.add_transition(Transition("GFP_receptor_gene_transcription_1_8"))
		mCherry_production_8_net.add_transition(Transition("GFP_receptor_mrna_translation_1_8"))
		mCherry_production_8_net.add_transition(Transition("enzymatic_reaction_1_8"))
		mCherry_production_8_net.add_transition(Transition("GFP_receptor_active_protein_degradation_1_8"))
		mCherry_production_8_net.add_transition(Transition("mCherry_gene_transcription_1_8"))
		mCherry_production_8_net.add_transition(Transition("mCherry_mrna_translation_1_8"))
		mCherry_production_8_net.add_transition(Transition("mCherry_protein_degradation_1_8"))

		# BFP_production_8_net places
		BFP_production_8_net.add_place(Place("BFP_gene", [BlackToken()]))
		BFP_production_8_net.add_place(Place("BFP_mrna"))
		BFP_production_8_net.add_place(Place("BFP_protein"))

		# BFP_production_8_net transitions
		BFP_production_8_net.add_transition(Transition("BFP_gene_transcription_1_8"))
		BFP_production_8_net.add_transition(Transition("BFP_mrna_translation_1_8"))
		BFP_production_8_net.add_transition(Transition("BFP_protein_degradation_1_8"))

		# CD19_production_8_net places
		CD19_production_8_net.add_place(Place("CD19_gene", [BlackToken()]))
		CD19_production_8_net.add_place(Place("CD19_mrna"))
		CD19_production_8_net.add_place(Place("CD19_protein"))

		# CD19_production_8_net transitions
		CD19_production_8_net.add_transition(Transition("CD19_gene_transcription_1_8"))
		CD19_production_8_net.add_transition(Transition("CD19_mrna_translation_1_8"))
		CD19_production_8_net.add_transition(Transition("CD19_protein_degradation_1_8"))

		# mCherry_production_7_net places
		mCherry_production_7_net.add_place(Place("GFP_receptor_gene", [BlackToken()]))
		mCherry_production_7_net.add_place(Place("GFP_receptor_mrna"))
		mCherry_production_7_net.add_place(Place("GFP_receptor_protein"))
		mCherry_production_7_net.add_place(Place("GFP_receptor_active_protein"))
		mCherry_production_7_net.add_place(Place("GFP_activation_mediator_protein"))
		mCherry_production_7_net.add_place(Place("mCherry_gene", [BlackToken()]))
		mCherry_production_7_net.add_place(Place("mCherry_mrna"))
		mCherry_production_7_net.add_place(Place("mCherry_protein"))

		# mCherry_production_7_net transitions
		mCherry_production_7_net.add_transition(Transition("GFP_receptor_gene_transcription_1_7"))
		mCherry_production_7_net.add_transition(Transition("GFP_receptor_mrna_translation_1_7"))
		mCherry_production_7_net.add_transition(Transition("enzymatic_reaction_1_7"))
		mCherry_production_7_net.add_transition(Transition("GFP_receptor_active_protein_degradation_1_7"))
		mCherry_production_7_net.add_transition(Transition("mCherry_gene_transcription_1_7"))
		mCherry_production_7_net.add_transition(Transition("mCherry_mrna_translation_1_7"))
		mCherry_production_7_net.add_transition(Transition("mCherry_protein_degradation_1_7"))

		# BFP_production_7_net places
		BFP_production_7_net.add_place(Place("BFP_gene", [BlackToken()]))
		BFP_production_7_net.add_place(Place("BFP_mrna"))
		BFP_production_7_net.add_place(Place("BFP_protein"))

		# BFP_production_7_net transitions
		BFP_production_7_net.add_transition(Transition("BFP_gene_transcription_1_7"))
		BFP_production_7_net.add_transition(Transition("BFP_mrna_translation_1_7"))
		BFP_production_7_net.add_transition(Transition("BFP_protein_degradation_1_7"))

		# CD19_production_7_net places
		CD19_production_7_net.add_place(Place("CD19_gene", [BlackToken()]))
		CD19_production_7_net.add_place(Place("CD19_mrna"))
		CD19_production_7_net.add_place(Place("CD19_protein"))

		# CD19_production_7_net transitions
		CD19_production_7_net.add_transition(Transition("CD19_gene_transcription_1_7"))
		CD19_production_7_net.add_transition(Transition("CD19_mrna_translation_1_7"))
		CD19_production_7_net.add_transition(Transition("CD19_protein_degradation_1_7"))

		# mCherry_production_6_net places
		mCherry_production_6_net.add_place(Place("GFP_receptor_gene", [BlackToken()]))
		mCherry_production_6_net.add_place(Place("GFP_receptor_mrna"))
		mCherry_production_6_net.add_place(Place("GFP_receptor_protein"))
		mCherry_production_6_net.add_place(Place("GFP_receptor_active_protein"))
		mCherry_production_6_net.add_place(Place("GFP_activation_mediator_protein"))
		mCherry_production_6_net.add_place(Place("mCherry_gene", [BlackToken()]))
		mCherry_production_6_net.add_place(Place("mCherry_mrna"))
		mCherry_production_6_net.add_place(Place("mCherry_protein"))

		# mCherry_production_6_net transitions
		mCherry_production_6_net.add_transition(Transition("GFP_receptor_gene_transcription_1_6"))
		mCherry_production_6_net.add_transition(Transition("GFP_receptor_mrna_translation_1_6"))
		mCherry_production_6_net.add_transition(Transition("enzymatic_reaction_1_6"))
		mCherry_production_6_net.add_transition(Transition("GFP_receptor_active_protein_degradation_1_6"))
		mCherry_production_6_net.add_transition(Transition("mCherry_gene_transcription_1_6"))
		mCherry_production_6_net.add_transition(Transition("mCherry_mrna_translation_1_6"))
		mCherry_production_6_net.add_transition(Transition("mCherry_protein_degradation_1_6"))

		# BFP_production_6_net places
		BFP_production_6_net.add_place(Place("BFP_gene", [BlackToken()]))
		BFP_production_6_net.add_place(Place("BFP_mrna"))
		BFP_production_6_net.add_place(Place("BFP_protein"))

		# BFP_production_6_net transitions
		BFP_production_6_net.add_transition(Transition("BFP_gene_transcription_1_6"))
		BFP_production_6_net.add_transition(Transition("BFP_mrna_translation_1_6"))
		BFP_production_6_net.add_transition(Transition("BFP_protein_degradation_1_6"))

		# CD19_production_6_net places
		CD19_production_6_net.add_place(Place("CD19_gene", [BlackToken()]))
		CD19_production_6_net.add_place(Place("CD19_mrna"))
		CD19_production_6_net.add_place(Place("CD19_protein"))

		# CD19_production_6_net transitions
		CD19_production_6_net.add_transition(Transition("CD19_gene_transcription_1_6"))
		CD19_production_6_net.add_transition(Transition("CD19_mrna_translation_1_6"))
		CD19_production_6_net.add_transition(Transition("CD19_protein_degradation_1_6"))

		# mCherry_production_5_net places
		mCherry_production_5_net.add_place(Place("GFP_receptor_gene", [BlackToken()]))
		mCherry_production_5_net.add_place(Place("GFP_receptor_mrna"))
		mCherry_production_5_net.add_place(Place("GFP_receptor_protein"))
		mCherry_production_5_net.add_place(Place("GFP_receptor_active_protein"))
		mCherry_production_5_net.add_place(Place("GFP_activation_mediator_protein"))
		mCherry_production_5_net.add_place(Place("mCherry_gene", [BlackToken()]))
		mCherry_production_5_net.add_place(Place("mCherry_mrna"))
		mCherry_production_5_net.add_place(Place("mCherry_protein"))

		# mCherry_production_5_net transitions
		mCherry_production_5_net.add_transition(Transition("GFP_receptor_gene_transcription_1_5"))
		mCherry_production_5_net.add_transition(Transition("GFP_receptor_mrna_translation_1_5"))
		mCherry_production_5_net.add_transition(Transition("enzymatic_reaction_1_5"))
		mCherry_production_5_net.add_transition(Transition("GFP_receptor_active_protein_degradation_1_5"))
		mCherry_production_5_net.add_transition(Transition("mCherry_gene_transcription_1_5"))
		mCherry_production_5_net.add_transition(Transition("mCherry_mrna_translation_1_5"))
		mCherry_production_5_net.add_transition(Transition("mCherry_protein_degradation_1_5"))

		# BFP_production_5_net places
		BFP_production_5_net.add_place(Place("BFP_gene", [BlackToken()]))
		BFP_production_5_net.add_place(Place("BFP_mrna"))
		BFP_production_5_net.add_place(Place("BFP_protein"))

		# BFP_production_5_net transitions
		BFP_production_5_net.add_transition(Transition("BFP_gene_transcription_1_5"))
		BFP_production_5_net.add_transition(Transition("BFP_mrna_translation_1_5"))
		BFP_production_5_net.add_transition(Transition("BFP_protein_degradation_1_5"))

		# CD19_production_5_net places
		CD19_production_5_net.add_place(Place("CD19_gene", [BlackToken()]))
		CD19_production_5_net.add_place(Place("CD19_mrna"))
		CD19_production_5_net.add_place(Place("CD19_protein"))

		# CD19_production_5_net transitions
		CD19_production_5_net.add_transition(Transition("CD19_gene_transcription_1_5"))
		CD19_production_5_net.add_transition(Transition("CD19_mrna_translation_1_5"))
		CD19_production_5_net.add_transition(Transition("CD19_protein_degradation_1_5"))

		# mCherry_production_4_net places
		mCherry_production_4_net.add_place(Place("GFP_receptor_gene", [BlackToken()]))
		mCherry_production_4_net.add_place(Place("GFP_receptor_mrna"))
		mCherry_production_4_net.add_place(Place("GFP_receptor_protein"))
		mCherry_production_4_net.add_place(Place("GFP_receptor_active_protein"))
		mCherry_production_4_net.add_place(Place("GFP_activation_mediator_protein"))
		mCherry_production_4_net.add_place(Place("mCherry_gene", [BlackToken()]))
		mCherry_production_4_net.add_place(Place("mCherry_mrna"))
		mCherry_production_4_net.add_place(Place("mCherry_protein"))

		# mCherry_production_4_net transitions
		mCherry_production_4_net.add_transition(Transition("GFP_receptor_gene_transcription_1_4"))
		mCherry_production_4_net.add_transition(Transition("GFP_receptor_mrna_translation_1_4"))
		mCherry_production_4_net.add_transition(Transition("enzymatic_reaction_1_4"))
		mCherry_production_4_net.add_transition(Transition("GFP_receptor_active_protein_degradation_1_4"))
		mCherry_production_4_net.add_transition(Transition("mCherry_gene_transcription_1_4"))
		mCherry_production_4_net.add_transition(Transition("mCherry_mrna_translation_1_4"))
		mCherry_production_4_net.add_transition(Transition("mCherry_protein_degradation_1_4"))

		# BFP_production_4_net places
		BFP_production_4_net.add_place(Place("BFP_gene", [BlackToken()]))
		BFP_production_4_net.add_place(Place("BFP_mrna"))
		BFP_production_4_net.add_place(Place("BFP_protein"))

		# BFP_production_4_net transitions
		BFP_production_4_net.add_transition(Transition("BFP_gene_transcription_1_4"))
		BFP_production_4_net.add_transition(Transition("BFP_mrna_translation_1_4"))
		BFP_production_4_net.add_transition(Transition("BFP_protein_degradation_1_4"))

		# CD19_production_4_net places
		CD19_production_4_net.add_place(Place("CD19_gene", [BlackToken()]))
		CD19_production_4_net.add_place(Place("CD19_mrna"))
		CD19_production_4_net.add_place(Place("CD19_protein"))

		# CD19_production_4_net transitions
		CD19_production_4_net.add_transition(Transition("CD19_gene_transcription_1_4"))
		CD19_production_4_net.add_transition(Transition("CD19_mrna_translation_1_4"))
		CD19_production_4_net.add_transition(Transition("CD19_protein_degradation_1_4"))

		# mCherry_production_3_net places
		mCherry_production_3_net.add_place(Place("GFP_receptor_gene", [BlackToken()]))
		mCherry_production_3_net.add_place(Place("GFP_receptor_mrna"))
		mCherry_production_3_net.add_place(Place("GFP_receptor_protein"))
		mCherry_production_3_net.add_place(Place("GFP_receptor_active_protein"))
		mCherry_production_3_net.add_place(Place("GFP_activation_mediator_protein"))
		mCherry_production_3_net.add_place(Place("mCherry_gene", [BlackToken()]))
		mCherry_production_3_net.add_place(Place("mCherry_mrna"))
		mCherry_production_3_net.add_place(Place("mCherry_protein"))

		# mCherry_production_3_net transitions
		mCherry_production_3_net.add_transition(Transition("GFP_receptor_gene_transcription_1_3"))
		mCherry_production_3_net.add_transition(Transition("GFP_receptor_mrna_translation_1_3"))
		mCherry_production_3_net.add_transition(Transition("enzymatic_reaction_1_3"))
		mCherry_production_3_net.add_transition(Transition("GFP_receptor_active_protein_degradation_1_3"))
		mCherry_production_3_net.add_transition(Transition("mCherry_gene_transcription_1_3"))
		mCherry_production_3_net.add_transition(Transition("mCherry_mrna_translation_1_3"))
		mCherry_production_3_net.add_transition(Transition("mCherry_protein_degradation_1_3"))

		# BFP_production_3_net places
		BFP_production_3_net.add_place(Place("BFP_gene", [BlackToken()]))
		BFP_production_3_net.add_place(Place("BFP_mrna"))
		BFP_production_3_net.add_place(Place("BFP_protein"))

		# BFP_production_3_net transitions
		BFP_production_3_net.add_transition(Transition("BFP_gene_transcription_1_3"))
		BFP_production_3_net.add_transition(Transition("BFP_mrna_translation_1_3"))
		BFP_production_3_net.add_transition(Transition("BFP_protein_degradation_1_3"))

		# CD19_production_3_net places
		CD19_production_3_net.add_place(Place("CD19_gene", [BlackToken()]))
		CD19_production_3_net.add_place(Place("CD19_mrna"))
		CD19_production_3_net.add_place(Place("CD19_protein"))

		# CD19_production_3_net transitions
		CD19_production_3_net.add_transition(Transition("CD19_gene_transcription_1_3"))
		CD19_production_3_net.add_transition(Transition("CD19_mrna_translation_1_3"))
		CD19_production_3_net.add_transition(Transition("CD19_protein_degradation_1_3"))

		# mCherry_production_2_net places
		mCherry_production_2_net.add_place(Place("GFP_receptor_gene", [BlackToken()]))
		mCherry_production_2_net.add_place(Place("GFP_receptor_mrna"))
		mCherry_production_2_net.add_place(Place("GFP_receptor_protein"))
		mCherry_production_2_net.add_place(Place("GFP_receptor_active_protein"))
		mCherry_production_2_net.add_place(Place("GFP_activation_mediator_protein"))
		mCherry_production_2_net.add_place(Place("mCherry_gene", [BlackToken()]))
		mCherry_production_2_net.add_place(Place("mCherry_mrna"))
		mCherry_production_2_net.add_place(Place("mCherry_protein"))

		# mCherry_production_2_net transitions
		mCherry_production_2_net.add_transition(Transition("GFP_receptor_gene_transcription_1_2"))
		mCherry_production_2_net.add_transition(Transition("GFP_receptor_mrna_translation_1_2"))
		mCherry_production_2_net.add_transition(Transition("enzymatic_reaction_1_2"))
		mCherry_production_2_net.add_transition(Transition("GFP_receptor_active_protein_degradation_1_2"))
		mCherry_production_2_net.add_transition(Transition("mCherry_gene_transcription_1_2"))
		mCherry_production_2_net.add_transition(Transition("mCherry_mrna_translation_1_2"))
		mCherry_production_2_net.add_transition(Transition("mCherry_protein_degradation_1_2"))

		# BFP_production_2_net places
		BFP_production_2_net.add_place(Place("BFP_gene", [BlackToken()]))
		BFP_production_2_net.add_place(Place("BFP_mrna"))
		BFP_production_2_net.add_place(Place("BFP_protein"))

		# BFP_production_2_net transitions
		BFP_production_2_net.add_transition(Transition("BFP_gene_transcription_1_2"))
		BFP_production_2_net.add_transition(Transition("BFP_mrna_translation_1_2"))
		BFP_production_2_net.add_transition(Transition("BFP_protein_degradation_1_2"))

		# CD19_production_2_net places
		CD19_production_2_net.add_place(Place("CD19_gene", [BlackToken()]))
		CD19_production_2_net.add_place(Place("CD19_mrna"))
		CD19_production_2_net.add_place(Place("CD19_protein"))

		# CD19_production_2_net transitions
		CD19_production_2_net.add_transition(Transition("CD19_gene_transcription_1_2"))
		CD19_production_2_net.add_transition(Transition("CD19_mrna_translation_1_2"))
		CD19_production_2_net.add_transition(Transition("CD19_protein_degradation_1_2"))

		# mCherry_production_1_net places
		mCherry_production_1_net.add_place(Place("GFP_receptor_gene", [BlackToken()]))
		mCherry_production_1_net.add_place(Place("GFP_receptor_mrna"))
		mCherry_production_1_net.add_place(Place("GFP_receptor_protein"))
		mCherry_production_1_net.add_place(Place("GFP_receptor_active_protein"))
		mCherry_production_1_net.add_place(Place("GFP_activation_mediator_protein"))
		mCherry_production_1_net.add_place(Place("mCherry_gene", [BlackToken()]))
		mCherry_production_1_net.add_place(Place("mCherry_mrna"))
		mCherry_production_1_net.add_place(Place("mCherry_protein"))

		# mCherry_production_1_net transitions
		mCherry_production_1_net.add_transition(Transition("GFP_receptor_gene_transcription_1_1"))
		mCherry_production_1_net.add_transition(Transition("GFP_receptor_mrna_translation_1_1"))
		mCherry_production_1_net.add_transition(Transition("enzymatic_reaction_1_1"))
		mCherry_production_1_net.add_transition(Transition("GFP_receptor_active_protein_degradation_1_1"))
		mCherry_production_1_net.add_transition(Transition("mCherry_gene_transcription_1_1"))
		mCherry_production_1_net.add_transition(Transition("mCherry_mrna_translation_1_1"))
		mCherry_production_1_net.add_transition(Transition("mCherry_protein_degradation_1_1"))

		# BFP_production_1_net places
		BFP_production_1_net.add_place(Place("BFP_gene", [BlackToken()]))
		BFP_production_1_net.add_place(Place("BFP_mrna"))
		BFP_production_1_net.add_place(Place("BFP_protein"))

		# BFP_production_1_net transitions
		BFP_production_1_net.add_transition(Transition("BFP_gene_transcription_1_1"))
		BFP_production_1_net.add_transition(Transition("BFP_mrna_translation_1_1"))
		BFP_production_1_net.add_transition(Transition("BFP_protein_degradation_1_1"))

		# CD19_production_1_net places
		CD19_production_1_net.add_place(Place("CD19_gene", [BlackToken()]))
		CD19_production_1_net.add_place(Place("CD19_mrna"))
		CD19_production_1_net.add_place(Place("CD19_protein"))

		# CD19_production_1_net transitions
		CD19_production_1_net.add_transition(Transition("CD19_gene_transcription_1_1"))
		CD19_production_1_net.add_transition(Transition("CD19_mrna_translation_1_1"))
		CD19_production_1_net.add_transition(Transition("CD19_protein_degradation_1_1"))

		# mCherry_production_0_net places
		mCherry_production_0_net.add_place(Place("GFP_receptor_gene", [BlackToken()]))
		mCherry_production_0_net.add_place(Place("GFP_receptor_mrna"))
		mCherry_production_0_net.add_place(Place("GFP_receptor_protein"))
		mCherry_production_0_net.add_place(Place("GFP_receptor_active_protein"))
		mCherry_production_0_net.add_place(Place("GFP_activation_mediator_protein"))
		mCherry_production_0_net.add_place(Place("mCherry_gene", [BlackToken()]))
		mCherry_production_0_net.add_place(Place("mCherry_mrna"))
		mCherry_production_0_net.add_place(Place("mCherry_protein"))

		# mCherry_production_0_net transitions
		mCherry_production_0_net.add_transition(Transition("GFP_receptor_gene_transcription_1"))
		mCherry_production_0_net.add_transition(Transition("GFP_receptor_mrna_translation_1"))
		mCherry_production_0_net.add_transition(Transition("enzymatic_reaction_1"))
		mCherry_production_0_net.add_transition(Transition("GFP_receptor_active_protein_degradation_1"))
		mCherry_production_0_net.add_transition(Transition("mCherry_gene_transcription_1"))
		mCherry_production_0_net.add_transition(Transition("mCherry_mrna_translation_1"))
		mCherry_production_0_net.add_transition(Transition("mCherry_protein_degradation_1"))

		# BFP_production_0_net places
		BFP_production_0_net.add_place(Place("BFP_gene", [BlackToken()]))
		BFP_production_0_net.add_place(Place("BFP_mrna"))
		BFP_production_0_net.add_place(Place("BFP_protein"))

		# BFP_production_0_net transitions
		BFP_production_0_net.add_transition(Transition("BFP_gene_transcription_1"))
		BFP_production_0_net.add_transition(Transition("BFP_mrna_translation_1"))
		BFP_production_0_net.add_transition(Transition("BFP_protein_degradation_1"))

		# CD19_production_0_net places
		CD19_production_0_net.add_place(Place("CD19_gene", [BlackToken()]))
		CD19_production_0_net.add_place(Place("CD19_mrna"))
		CD19_production_0_net.add_place(Place("CD19_protein"))

		# CD19_production_0_net transitions
		CD19_production_0_net.add_transition(Transition("CD19_gene_transcription_1"))
		CD19_production_0_net.add_transition(Transition("CD19_mrna_translation_1"))
		CD19_production_0_net.add_transition(Transition("CD19_protein_degradation_1"))

		# GFP_production_0_net places
		GFP_production_0_net.add_place(Place("CD19_receptor_active_protein"))
		GFP_production_0_net.add_place(Place("GFP_gene", [BlackToken()]))
		GFP_production_0_net.add_place(Place("GFP_mrna"))
		GFP_production_0_net.add_place(Place("GFP_protein"))

		# GFP_production_0_net transitions
		GFP_production_0_net.add_transition(Transition("GFP_gene_transcription_1"))
		GFP_production_0_net.add_transition(Transition("GFP_mrna_translation_1"))
		GFP_production_0_net.add_transition(Transition("CD19_receptor_active_protein_degradation_1"))
		GFP_production_0_net.add_transition(Transition("GFP_protein_degradation_1"))

		# rgb_net places
		rgb_net.add_place(Place("green_3_3", [ GFP_production_0_net ]))
		rgb_net.add_place(Place("grey_0_0", [ CD19_production_0_net, BFP_production_0_net, mCherry_production_0_net ]))
		rgb_net.add_place(Place("red_3_2", [ CD19_production_1_net, BFP_production_1_net, mCherry_production_1_net ]))
		rgb_net.add_place(Place("red_3_4", [ CD19_production_2_net, BFP_production_2_net, mCherry_production_2_net ]))
		rgb_net.add_place(Place("red_2_2", [ CD19_production_3_net, BFP_production_3_net, mCherry_production_3_net ]))
		rgb_net.add_place(Place("red_2_3", [ CD19_production_4_net, BFP_production_4_net, mCherry_production_4_net ]))
		rgb_net.add_place(Place("red_2_4", [ CD19_production_5_net, BFP_production_5_net, mCherry_production_5_net ]))
		rgb_net.add_place(Place("red_4_2", [ CD19_production_6_net, BFP_production_6_net, mCherry_production_6_net ]))
		rgb_net.add_place(Place("red_4_3", [ CD19_production_7_net, BFP_production_7_net, mCherry_production_7_net ]))
		rgb_net.add_place(Place("red_4_4", [ CD19_production_8_net, BFP_production_8_net, mCherry_production_8_net ]))
		rgb_net.add_place(Place("blue_1_2", [ CD19_production_9_net, BFP_production_9_net, mCherry_production_9_net ]))
		rgb_net.add_place(Place("blue_1_3", [ CD19_production_10_net, BFP_production_10_net, mCherry_production_10_net ]))
		rgb_net.add_place(Place("blue_1_4", [ CD19_production_11_net, BFP_production_11_net, mCherry_production_11_net ]))
		rgb_net.add_place(Place("blue_2_1", [ CD19_production_12_net, BFP_production_12_net, mCherry_production_12_net ]))
		rgb_net.add_place(Place("blue_2_5", [ CD19_production_13_net, BFP_production_13_net, mCherry_production_13_net ]))
		rgb_net.add_place(Place("blue_3_1", [ CD19_production_14_net, BFP_production_14_net, mCherry_production_14_net, CD19_production_16_net, BFP_production_16_net, mCherry_production_16_net ]))
		rgb_net.add_place(Place("blue_3_5", [ CD19_production_15_net, BFP_production_15_net, mCherry_production_15_net ]))
		rgb_net.add_place(Place("blue_4_1", [ CD19_production_17_net, BFP_production_17_net, mCherry_production_17_net ]))
		rgb_net.add_place(Place("blue_4_5", [ CD19_production_18_net, BFP_production_18_net, mCherry_production_18_net ]))
		rgb_net.add_place(Place("blue_5_2", [ CD19_production_19_net, BFP_production_19_net, mCherry_production_19_net ]))
		rgb_net.add_place(Place("blue_5_3", [ CD19_production_20_net, BFP_production_20_net, mCherry_production_20_net ]))
		rgb_net.add_place(Place("blue_5_4", [ CD19_production_21_net, BFP_production_21_net, mCherry_production_21_net ]))

		# rgb_net transitions
		rgb_net.add_transition(Transition("juxtacrine_signaling_GFP_protein_green_3_3_red_2_2_1", Expression("str(x) == 'GFP_protein'")))
		rgb_net.add_transition(Transition("juxtacrine_signaling_GFP_protein_green_3_3_red_2_3_1", Expression("str(x) == 'GFP_protein'")))
		rgb_net.add_transition(Transition("juxtacrine_signaling_GFP_protein_green_3_3_red_2_4_1", Expression("str(x) == 'GFP_protein'")))
		rgb_net.add_transition(Transition("juxtacrine_signaling_GFP_protein_green_3_3_red_3_2_1", Expression("str(x) == 'GFP_protein'")))
		rgb_net.add_transition(Transition("juxtacrine_signaling_GFP_protein_green_3_3_red_3_4_1", Expression("str(x) == 'GFP_protein'")))
		rgb_net.add_transition(Transition("juxtacrine_signaling_GFP_protein_green_3_3_red_4_2_1", Expression("str(x) == 'GFP_protein'")))
		rgb_net.add_transition(Transition("juxtacrine_signaling_GFP_protein_green_3_3_red_4_3_1", Expression("str(x) == 'GFP_protein'")))
		rgb_net.add_transition(Transition("juxtacrine_signaling_GFP_protein_green_3_3_red_4_4_1", Expression("str(x) == 'GFP_protein'")))
		rgb_net.add_transition(Transition("juxtacrine_signaling_CD19_protein_red_3_2_green_3_3_1", Expression("str(x) == 'CD19_protein'")))
		rgb_net.add_transition(Transition("juxtacrine_signaling_CD19_protein_red_3_4_green_3_3_1", Expression("str(x) == 'CD19_protein'")))
		rgb_net.add_transition(Transition("juxtacrine_signaling_CD19_protein_red_2_2_green_3_3_1", Expression("str(x) == 'CD19_protein'")))
		rgb_net.add_transition(Transition("juxtacrine_signaling_CD19_protein_red_2_3_green_3_3_1", Expression("str(x) == 'CD19_protein'")))
		rgb_net.add_transition(Transition("juxtacrine_signaling_CD19_protein_red_2_4_green_3_3_1", Expression("str(x) == 'CD19_protein'")))
		rgb_net.add_transition(Transition("juxtacrine_signaling_CD19_protein_red_4_2_green_3_3_1", Expression("str(x) == 'CD19_protein'")))
		rgb_net.add_transition(Transition("juxtacrine_signaling_CD19_protein_red_4_3_green_3_3_1", Expression("str(x) == 'CD19_protein'")))
		rgb_net.add_transition(Transition("juxtacrine_signaling_CD19_protein_red_4_4_green_3_3_1", Expression("str(x) == 'CD19_protein'")))

		# rgb_net arcs
		rgb_net.add_input("green_3_3", "juxtacrine_signaling_GFP_protein_green_3_3_red_2_2_1", Variable('x'), notify=[GFP_production_0_net])
		rgb_net.add_input("green_3_3", "juxtacrine_signaling_GFP_protein_green_3_3_red_2_3_1", Variable('x'), notify=[GFP_production_0_net])
		rgb_net.add_input("green_3_3", "juxtacrine_signaling_GFP_protein_green_3_3_red_2_4_1", Variable('x'), notify=[GFP_production_0_net])
		rgb_net.add_input("green_3_3", "juxtacrine_signaling_GFP_protein_green_3_3_red_3_2_1", Variable('x'), notify=[GFP_production_0_net])
		rgb_net.add_input("green_3_3", "juxtacrine_signaling_GFP_protein_green_3_3_red_3_4_1", Variable('x'), notify=[GFP_production_0_net])
		rgb_net.add_input("green_3_3", "juxtacrine_signaling_GFP_protein_green_3_3_red_4_2_1", Variable('x'), notify=[GFP_production_0_net])
		rgb_net.add_input("green_3_3", "juxtacrine_signaling_GFP_protein_green_3_3_red_4_3_1", Variable('x'), notify=[GFP_production_0_net])
		rgb_net.add_input("green_3_3", "juxtacrine_signaling_GFP_protein_green_3_3_red_4_4_1", Variable('x'), notify=[GFP_production_0_net])
		rgb_net.add_input("red_3_2", "juxtacrine_signaling_CD19_protein_red_3_2_green_3_3_1", Variable('x'), notify=[CD19_production_1_net, BFP_production_1_net, mCherry_production_1_net])
		rgb_net.add_input("red_3_4", "juxtacrine_signaling_CD19_protein_red_3_4_green_3_3_1", Variable('x'), notify=[CD19_production_2_net, BFP_production_2_net, mCherry_production_2_net])
		rgb_net.add_input("red_2_2", "juxtacrine_signaling_CD19_protein_red_2_2_green_3_3_1", Variable('x'), notify=[CD19_production_3_net, BFP_production_3_net, mCherry_production_3_net])
		rgb_net.add_input("red_2_3", "juxtacrine_signaling_CD19_protein_red_2_3_green_3_3_1", Variable('x'), notify=[CD19_production_4_net, BFP_production_4_net, mCherry_production_4_net])
		rgb_net.add_input("red_2_4", "juxtacrine_signaling_CD19_protein_red_2_4_green_3_3_1", Variable('x'), notify=[CD19_production_5_net, BFP_production_5_net, mCherry_production_5_net])
		rgb_net.add_input("red_4_2", "juxtacrine_signaling_CD19_protein_red_4_2_green_3_3_1", Variable('x'), notify=[CD19_production_6_net, BFP_production_6_net, mCherry_production_6_net])
		rgb_net.add_input("red_4_3", "juxtacrine_signaling_CD19_protein_red_4_3_green_3_3_1", Variable('x'), notify=[CD19_production_7_net, BFP_production_7_net, mCherry_production_7_net])
		rgb_net.add_input("red_4_4", "juxtacrine_signaling_CD19_protein_red_4_4_green_3_3_1", Variable('x'), notify=[CD19_production_8_net, BFP_production_8_net, mCherry_production_8_net])
		rgb_net.add_output("red_2_2", "juxtacrine_signaling_GFP_protein_green_3_3_red_2_2_1", Expression('x.replace("protein", "receptor_active_protein")'), notify=[CD19_production_3_net, BFP_production_3_net, mCherry_production_3_net])
		rgb_net.add_output("red_2_3", "juxtacrine_signaling_GFP_protein_green_3_3_red_2_3_1", Expression('x.replace("protein", "receptor_active_protein")'), notify=[CD19_production_4_net, BFP_production_4_net, mCherry_production_4_net])
		rgb_net.add_output("red_2_4", "juxtacrine_signaling_GFP_protein_green_3_3_red_2_4_1", Expression('x.replace("protein", "receptor_active_protein")'), notify=[CD19_production_5_net, BFP_production_5_net, mCherry_production_5_net])
		rgb_net.add_output("red_3_2", "juxtacrine_signaling_GFP_protein_green_3_3_red_3_2_1", Expression('x.replace("protein", "receptor_active_protein")'), notify=[CD19_production_1_net, BFP_production_1_net, mCherry_production_1_net])
		rgb_net.add_output("red_3_4", "juxtacrine_signaling_GFP_protein_green_3_3_red_3_4_1", Expression('x.replace("protein", "receptor_active_protein")'), notify=[CD19_production_2_net, BFP_production_2_net, mCherry_production_2_net])
		rgb_net.add_output("red_4_2", "juxtacrine_signaling_GFP_protein_green_3_3_red_4_2_1", Expression('x.replace("protein", "receptor_active_protein")'), notify=[CD19_production_6_net, BFP_production_6_net, mCherry_production_6_net])
		rgb_net.add_output("red_4_3", "juxtacrine_signaling_GFP_protein_green_3_3_red_4_3_1", Expression('x.replace("protein", "receptor_active_protein")'), notify=[CD19_production_7_net, BFP_production_7_net, mCherry_production_7_net])
		rgb_net.add_output("red_4_4", "juxtacrine_signaling_GFP_protein_green_3_3_red_4_4_1", Expression('x.replace("protein", "receptor_active_protein")'), notify=[CD19_production_8_net, BFP_production_8_net, mCherry_production_8_net])
		rgb_net.add_output("green_3_3", "juxtacrine_signaling_CD19_protein_red_3_2_green_3_3_1", Expression('x.replace("protein", "receptor_active_protein")'), notify=[GFP_production_0_net])
		rgb_net.add_output("green_3_3", "juxtacrine_signaling_CD19_protein_red_3_4_green_3_3_1", Expression('x.replace("protein", "receptor_active_protein")'), notify=[GFP_production_0_net])
		rgb_net.add_output("green_3_3", "juxtacrine_signaling_CD19_protein_red_2_2_green_3_3_1", Expression('x.replace("protein", "receptor_active_protein")'), notify=[GFP_production_0_net])
		rgb_net.add_output("green_3_3", "juxtacrine_signaling_CD19_protein_red_2_3_green_3_3_1", Expression('x.replace("protein", "receptor_active_protein")'), notify=[GFP_production_0_net])
		rgb_net.add_output("green_3_3", "juxtacrine_signaling_CD19_protein_red_2_4_green_3_3_1", Expression('x.replace("protein", "receptor_active_protein")'), notify=[GFP_production_0_net])
		rgb_net.add_output("green_3_3", "juxtacrine_signaling_CD19_protein_red_4_2_green_3_3_1", Expression('x.replace("protein", "receptor_active_protein")'), notify=[GFP_production_0_net])
		rgb_net.add_output("green_3_3", "juxtacrine_signaling_CD19_protein_red_4_3_green_3_3_1", Expression('x.replace("protein", "receptor_active_protein")'), notify=[GFP_production_0_net])
		rgb_net.add_output("green_3_3", "juxtacrine_signaling_CD19_protein_red_4_4_green_3_3_1", Expression('x.replace("protein", "receptor_active_protein")'), notify=[GFP_production_0_net])

		# GFP_production_0_net arcs
		GFP_production_0_net.add_input("GFP_gene", "GFP_gene_transcription_1", Value(dot))
		GFP_production_0_net.add_input("CD19_receptor_active_protein", "GFP_gene_transcription_1", Value(dot), notify=[rgb_net.place('green_3_3')])
		GFP_production_0_net.add_input("GFP_mrna", "GFP_mrna_translation_1", Value(dot))
		GFP_production_0_net.add_input("CD19_receptor_active_protein", "CD19_receptor_active_protein_degradation_1", Value(dot), notify=[rgb_net.place('green_3_3')])
		GFP_production_0_net.add_input("GFP_protein", "GFP_protein_degradation_1", Value(dot), notify=[rgb_net.place('green_3_3')])
		GFP_production_0_net.add_output("GFP_gene", "GFP_gene_transcription_1", Value(dot))
		GFP_production_0_net.add_output("GFP_mrna", "GFP_gene_transcription_1", Value(dot))
		GFP_production_0_net.add_output("GFP_protein", "GFP_mrna_translation_1", MultiArc([Value(dot)]*12), notify=[rgb_net.place('green_3_3')])

		# CD19_production_0_net arcs
		CD19_production_0_net.add_input("CD19_gene", "CD19_gene_transcription_1", Value(dot))
		CD19_production_0_net.add_input("CD19_mrna", "CD19_mrna_translation_1", Value(dot))
		CD19_production_0_net.add_input("CD19_protein", "CD19_protein_degradation_1", Value(dot), notify=[rgb_net.place('grey_0_0')])
		CD19_production_0_net.add_output("CD19_gene", "CD19_gene_transcription_1", Value(dot))
		CD19_production_0_net.add_output("CD19_mrna", "CD19_gene_transcription_1", Value(dot))
		CD19_production_0_net.add_output("CD19_protein", "CD19_mrna_translation_1", MultiArc([Value(dot)]*2), notify=[rgb_net.place('grey_0_0')])

		# BFP_production_0_net arcs
		BFP_production_0_net.add_input("BFP_gene", "BFP_gene_transcription_1", Value(dot))
		BFP_production_0_net.add_input("BFP_mrna", "BFP_mrna_translation_1", Value(dot))
		BFP_production_0_net.add_input("BFP_protein", "BFP_protein_degradation_1", Value(dot), notify=[rgb_net.place('grey_0_0')])
		BFP_production_0_net.add_output("BFP_gene", "BFP_gene_transcription_1", Value(dot))
		BFP_production_0_net.add_output("BFP_mrna", "BFP_gene_transcription_1", Value(dot))
		BFP_production_0_net.add_output("BFP_protein", "BFP_mrna_translation_1", MultiArc([Value(dot)]*2), notify=[rgb_net.place('grey_0_0')])

		# mCherry_production_0_net arcs
		mCherry_production_0_net.add_input("GFP_receptor_gene", "GFP_receptor_gene_transcription_1", Value(dot))
		mCherry_production_0_net.add_input("GFP_receptor_mrna", "GFP_receptor_mrna_translation_1", Value(dot))
		mCherry_production_0_net.add_input("GFP_receptor_active_protein", "enzymatic_reaction_1", Value(dot), notify=[rgb_net.place('grey_0_0')])
		mCherry_production_0_net.add_input("GFP_receptor_protein", "enzymatic_reaction_1", Value(dot), notify=[rgb_net.place('grey_0_0')])
		mCherry_production_0_net.add_input("GFP_receptor_active_protein", "GFP_receptor_active_protein_degradation_1", Value(dot), notify=[rgb_net.place('grey_0_0')])
		mCherry_production_0_net.add_input("mCherry_gene", "mCherry_gene_transcription_1", Value(dot))
		mCherry_production_0_net.add_input("GFP_activation_mediator_protein", "mCherry_gene_transcription_1", Value(dot), notify=[rgb_net.place('grey_0_0')])
		mCherry_production_0_net.add_input("mCherry_mrna", "mCherry_mrna_translation_1", Value(dot))
		mCherry_production_0_net.add_input("mCherry_protein", "mCherry_protein_degradation_1", Value(dot), notify=[rgb_net.place('grey_0_0')])
		mCherry_production_0_net.add_output("GFP_receptor_gene", "GFP_receptor_gene_transcription_1", Value(dot))
		mCherry_production_0_net.add_output("GFP_receptor_mrna", "GFP_receptor_gene_transcription_1", Value(dot))
		mCherry_production_0_net.add_output("GFP_receptor_protein", "GFP_receptor_mrna_translation_1", Value(dot), notify=[rgb_net.place('grey_0_0')])
		mCherry_production_0_net.add_output("GFP_receptor_active_protein", "enzymatic_reaction_1", Value(dot), notify=[rgb_net.place('grey_0_0')])
		mCherry_production_0_net.add_output("GFP_activation_mediator_protein", "enzymatic_reaction_1", Value(dot), notify=[rgb_net.place('grey_0_0')])
		mCherry_production_0_net.add_output("mCherry_gene", "mCherry_gene_transcription_1", Value(dot))
		mCherry_production_0_net.add_output("mCherry_mrna", "mCherry_gene_transcription_1", Value(dot))
		mCherry_production_0_net.add_output("mCherry_protein", "mCherry_mrna_translation_1", MultiArc([Value(dot)]*3), notify=[rgb_net.place('grey_0_0')])

		# CD19_production_1_net arcs
		CD19_production_1_net.add_input("CD19_gene", "CD19_gene_transcription_1_1", Value(dot))
		CD19_production_1_net.add_input("CD19_mrna", "CD19_mrna_translation_1_1", Value(dot))
		CD19_production_1_net.add_input("CD19_protein", "CD19_protein_degradation_1_1", Value(dot), notify=[rgb_net.place('red_3_2')])
		CD19_production_1_net.add_output("CD19_gene", "CD19_gene_transcription_1_1", Value(dot))
		CD19_production_1_net.add_output("CD19_mrna", "CD19_gene_transcription_1_1", Value(dot))
		CD19_production_1_net.add_output("CD19_protein", "CD19_mrna_translation_1_1", MultiArc([Value(dot)]*2), notify=[rgb_net.place('red_3_2')])

		# BFP_production_1_net arcs
		BFP_production_1_net.add_input("BFP_gene", "BFP_gene_transcription_1_1", Value(dot))
		BFP_production_1_net.add_input("BFP_mrna", "BFP_mrna_translation_1_1", Value(dot))
		BFP_production_1_net.add_input("BFP_protein", "BFP_protein_degradation_1_1", Value(dot), notify=[rgb_net.place('red_3_2')])
		BFP_production_1_net.add_output("BFP_gene", "BFP_gene_transcription_1_1", Value(dot))
		BFP_production_1_net.add_output("BFP_mrna", "BFP_gene_transcription_1_1", Value(dot))
		BFP_production_1_net.add_output("BFP_protein", "BFP_mrna_translation_1_1", MultiArc([Value(dot)]*2), notify=[rgb_net.place('red_3_2')])

		# mCherry_production_1_net arcs
		mCherry_production_1_net.add_input("GFP_receptor_gene", "GFP_receptor_gene_transcription_1_1", Value(dot))
		mCherry_production_1_net.add_input("GFP_receptor_mrna", "GFP_receptor_mrna_translation_1_1", Value(dot))
		mCherry_production_1_net.add_input("GFP_receptor_active_protein", "enzymatic_reaction_1_1", Value(dot), notify=[rgb_net.place('red_3_2')])
		mCherry_production_1_net.add_input("GFP_receptor_protein", "enzymatic_reaction_1_1", Value(dot), notify=[rgb_net.place('red_3_2')])
		mCherry_production_1_net.add_input("GFP_receptor_active_protein", "GFP_receptor_active_protein_degradation_1_1", Value(dot), notify=[rgb_net.place('red_3_2')])
		mCherry_production_1_net.add_input("mCherry_gene", "mCherry_gene_transcription_1_1", Value(dot))
		mCherry_production_1_net.add_input("GFP_activation_mediator_protein", "mCherry_gene_transcription_1_1", Value(dot), notify=[rgb_net.place('red_3_2')])
		mCherry_production_1_net.add_input("mCherry_mrna", "mCherry_mrna_translation_1_1", Value(dot))
		mCherry_production_1_net.add_input("mCherry_protein", "mCherry_protein_degradation_1_1", Value(dot), notify=[rgb_net.place('red_3_2')])
		mCherry_production_1_net.add_output("GFP_receptor_gene", "GFP_receptor_gene_transcription_1_1", Value(dot))
		mCherry_production_1_net.add_output("GFP_receptor_mrna", "GFP_receptor_gene_transcription_1_1", Value(dot))
		mCherry_production_1_net.add_output("GFP_receptor_protein", "GFP_receptor_mrna_translation_1_1", Value(dot), notify=[rgb_net.place('red_3_2')])
		mCherry_production_1_net.add_output("GFP_receptor_active_protein", "enzymatic_reaction_1_1", Value(dot), notify=[rgb_net.place('red_3_2')])
		mCherry_production_1_net.add_output("GFP_activation_mediator_protein", "enzymatic_reaction_1_1", Value(dot), notify=[rgb_net.place('red_3_2')])
		mCherry_production_1_net.add_output("mCherry_gene", "mCherry_gene_transcription_1_1", Value(dot))
		mCherry_production_1_net.add_output("mCherry_mrna", "mCherry_gene_transcription_1_1", Value(dot))
		mCherry_production_1_net.add_output("mCherry_protein", "mCherry_mrna_translation_1_1", MultiArc([Value(dot)]*3), notify=[rgb_net.place('red_3_2')])

		# CD19_production_2_net arcs
		CD19_production_2_net.add_input("CD19_gene", "CD19_gene_transcription_1_2", Value(dot))
		CD19_production_2_net.add_input("CD19_mrna", "CD19_mrna_translation_1_2", Value(dot))
		CD19_production_2_net.add_input("CD19_protein", "CD19_protein_degradation_1_2", Value(dot), notify=[rgb_net.place('red_3_4')])
		CD19_production_2_net.add_output("CD19_gene", "CD19_gene_transcription_1_2", Value(dot))
		CD19_production_2_net.add_output("CD19_mrna", "CD19_gene_transcription_1_2", Value(dot))
		CD19_production_2_net.add_output("CD19_protein", "CD19_mrna_translation_1_2", MultiArc([Value(dot)]*2), notify=[rgb_net.place('red_3_4')])

		# BFP_production_2_net arcs
		BFP_production_2_net.add_input("BFP_gene", "BFP_gene_transcription_1_2", Value(dot))
		BFP_production_2_net.add_input("BFP_mrna", "BFP_mrna_translation_1_2", Value(dot))
		BFP_production_2_net.add_input("BFP_protein", "BFP_protein_degradation_1_2", Value(dot), notify=[rgb_net.place('red_3_4')])
		BFP_production_2_net.add_output("BFP_gene", "BFP_gene_transcription_1_2", Value(dot))
		BFP_production_2_net.add_output("BFP_mrna", "BFP_gene_transcription_1_2", Value(dot))
		BFP_production_2_net.add_output("BFP_protein", "BFP_mrna_translation_1_2", MultiArc([Value(dot)]*2), notify=[rgb_net.place('red_3_4')])

		# mCherry_production_2_net arcs
		mCherry_production_2_net.add_input("GFP_receptor_gene", "GFP_receptor_gene_transcription_1_2", Value(dot))
		mCherry_production_2_net.add_input("GFP_receptor_mrna", "GFP_receptor_mrna_translation_1_2", Value(dot))
		mCherry_production_2_net.add_input("GFP_receptor_active_protein", "enzymatic_reaction_1_2", Value(dot), notify=[rgb_net.place('red_3_4')])
		mCherry_production_2_net.add_input("GFP_receptor_protein", "enzymatic_reaction_1_2", Value(dot), notify=[rgb_net.place('red_3_4')])
		mCherry_production_2_net.add_input("GFP_receptor_active_protein", "GFP_receptor_active_protein_degradation_1_2", Value(dot), notify=[rgb_net.place('red_3_4')])
		mCherry_production_2_net.add_input("mCherry_gene", "mCherry_gene_transcription_1_2", Value(dot))
		mCherry_production_2_net.add_input("GFP_activation_mediator_protein", "mCherry_gene_transcription_1_2", Value(dot), notify=[rgb_net.place('red_3_4')])
		mCherry_production_2_net.add_input("mCherry_mrna", "mCherry_mrna_translation_1_2", Value(dot))
		mCherry_production_2_net.add_input("mCherry_protein", "mCherry_protein_degradation_1_2", Value(dot), notify=[rgb_net.place('red_3_4')])
		mCherry_production_2_net.add_output("GFP_receptor_gene", "GFP_receptor_gene_transcription_1_2", Value(dot))
		mCherry_production_2_net.add_output("GFP_receptor_mrna", "GFP_receptor_gene_transcription_1_2", Value(dot))
		mCherry_production_2_net.add_output("GFP_receptor_protein", "GFP_receptor_mrna_translation_1_2", Value(dot), notify=[rgb_net.place('red_3_4')])
		mCherry_production_2_net.add_output("GFP_receptor_active_protein", "enzymatic_reaction_1_2", Value(dot), notify=[rgb_net.place('red_3_4')])
		mCherry_production_2_net.add_output("GFP_activation_mediator_protein", "enzymatic_reaction_1_2", Value(dot), notify=[rgb_net.place('red_3_4')])
		mCherry_production_2_net.add_output("mCherry_gene", "mCherry_gene_transcription_1_2", Value(dot))
		mCherry_production_2_net.add_output("mCherry_mrna", "mCherry_gene_transcription_1_2", Value(dot))
		mCherry_production_2_net.add_output("mCherry_protein", "mCherry_mrna_translation_1_2", MultiArc([Value(dot)]*3), notify=[rgb_net.place('red_3_4')])

		# CD19_production_3_net arcs
		CD19_production_3_net.add_input("CD19_gene", "CD19_gene_transcription_1_3", Value(dot))
		CD19_production_3_net.add_input("CD19_mrna", "CD19_mrna_translation_1_3", Value(dot))
		CD19_production_3_net.add_input("CD19_protein", "CD19_protein_degradation_1_3", Value(dot), notify=[rgb_net.place('red_2_2')])
		CD19_production_3_net.add_output("CD19_gene", "CD19_gene_transcription_1_3", Value(dot))
		CD19_production_3_net.add_output("CD19_mrna", "CD19_gene_transcription_1_3", Value(dot))
		CD19_production_3_net.add_output("CD19_protein", "CD19_mrna_translation_1_3", MultiArc([Value(dot)]*2), notify=[rgb_net.place('red_2_2')])

		# BFP_production_3_net arcs
		BFP_production_3_net.add_input("BFP_gene", "BFP_gene_transcription_1_3", Value(dot))
		BFP_production_3_net.add_input("BFP_mrna", "BFP_mrna_translation_1_3", Value(dot))
		BFP_production_3_net.add_input("BFP_protein", "BFP_protein_degradation_1_3", Value(dot), notify=[rgb_net.place('red_2_2')])
		BFP_production_3_net.add_output("BFP_gene", "BFP_gene_transcription_1_3", Value(dot))
		BFP_production_3_net.add_output("BFP_mrna", "BFP_gene_transcription_1_3", Value(dot))
		BFP_production_3_net.add_output("BFP_protein", "BFP_mrna_translation_1_3", MultiArc([Value(dot)]*2), notify=[rgb_net.place('red_2_2')])

		# mCherry_production_3_net arcs
		mCherry_production_3_net.add_input("GFP_receptor_gene", "GFP_receptor_gene_transcription_1_3", Value(dot))
		mCherry_production_3_net.add_input("GFP_receptor_mrna", "GFP_receptor_mrna_translation_1_3", Value(dot))
		mCherry_production_3_net.add_input("GFP_receptor_active_protein", "enzymatic_reaction_1_3", Value(dot), notify=[rgb_net.place('red_2_2')])
		mCherry_production_3_net.add_input("GFP_receptor_protein", "enzymatic_reaction_1_3", Value(dot), notify=[rgb_net.place('red_2_2')])
		mCherry_production_3_net.add_input("GFP_receptor_active_protein", "GFP_receptor_active_protein_degradation_1_3", Value(dot), notify=[rgb_net.place('red_2_2')])
		mCherry_production_3_net.add_input("mCherry_gene", "mCherry_gene_transcription_1_3", Value(dot))
		mCherry_production_3_net.add_input("GFP_activation_mediator_protein", "mCherry_gene_transcription_1_3", Value(dot), notify=[rgb_net.place('red_2_2')])
		mCherry_production_3_net.add_input("mCherry_mrna", "mCherry_mrna_translation_1_3", Value(dot))
		mCherry_production_3_net.add_input("mCherry_protein", "mCherry_protein_degradation_1_3", Value(dot), notify=[rgb_net.place('red_2_2')])
		mCherry_production_3_net.add_output("GFP_receptor_gene", "GFP_receptor_gene_transcription_1_3", Value(dot))
		mCherry_production_3_net.add_output("GFP_receptor_mrna", "GFP_receptor_gene_transcription_1_3", Value(dot))
		mCherry_production_3_net.add_output("GFP_receptor_protein", "GFP_receptor_mrna_translation_1_3", Value(dot), notify=[rgb_net.place('red_2_2')])
		mCherry_production_3_net.add_output("GFP_receptor_active_protein", "enzymatic_reaction_1_3", Value(dot), notify=[rgb_net.place('red_2_2')])
		mCherry_production_3_net.add_output("GFP_activation_mediator_protein", "enzymatic_reaction_1_3", Value(dot), notify=[rgb_net.place('red_2_2')])
		mCherry_production_3_net.add_output("mCherry_gene", "mCherry_gene_transcription_1_3", Value(dot))
		mCherry_production_3_net.add_output("mCherry_mrna", "mCherry_gene_transcription_1_3", Value(dot))
		mCherry_production_3_net.add_output("mCherry_protein", "mCherry_mrna_translation_1_3", MultiArc([Value(dot)]*3), notify=[rgb_net.place('red_2_2')])

		# CD19_production_4_net arcs
		CD19_production_4_net.add_input("CD19_gene", "CD19_gene_transcription_1_4", Value(dot))
		CD19_production_4_net.add_input("CD19_mrna", "CD19_mrna_translation_1_4", Value(dot))
		CD19_production_4_net.add_input("CD19_protein", "CD19_protein_degradation_1_4", Value(dot), notify=[rgb_net.place('red_2_3')])
		CD19_production_4_net.add_output("CD19_gene", "CD19_gene_transcription_1_4", Value(dot))
		CD19_production_4_net.add_output("CD19_mrna", "CD19_gene_transcription_1_4", Value(dot))
		CD19_production_4_net.add_output("CD19_protein", "CD19_mrna_translation_1_4", MultiArc([Value(dot)]*2), notify=[rgb_net.place('red_2_3')])

		# BFP_production_4_net arcs
		BFP_production_4_net.add_input("BFP_gene", "BFP_gene_transcription_1_4", Value(dot))
		BFP_production_4_net.add_input("BFP_mrna", "BFP_mrna_translation_1_4", Value(dot))
		BFP_production_4_net.add_input("BFP_protein", "BFP_protein_degradation_1_4", Value(dot), notify=[rgb_net.place('red_2_3')])
		BFP_production_4_net.add_output("BFP_gene", "BFP_gene_transcription_1_4", Value(dot))
		BFP_production_4_net.add_output("BFP_mrna", "BFP_gene_transcription_1_4", Value(dot))
		BFP_production_4_net.add_output("BFP_protein", "BFP_mrna_translation_1_4", MultiArc([Value(dot)]*2), notify=[rgb_net.place('red_2_3')])

		# mCherry_production_4_net arcs
		mCherry_production_4_net.add_input("GFP_receptor_gene", "GFP_receptor_gene_transcription_1_4", Value(dot))
		mCherry_production_4_net.add_input("GFP_receptor_mrna", "GFP_receptor_mrna_translation_1_4", Value(dot))
		mCherry_production_4_net.add_input("GFP_receptor_active_protein", "enzymatic_reaction_1_4", Value(dot), notify=[rgb_net.place('red_2_3')])
		mCherry_production_4_net.add_input("GFP_receptor_protein", "enzymatic_reaction_1_4", Value(dot), notify=[rgb_net.place('red_2_3')])
		mCherry_production_4_net.add_input("GFP_receptor_active_protein", "GFP_receptor_active_protein_degradation_1_4", Value(dot), notify=[rgb_net.place('red_2_3')])
		mCherry_production_4_net.add_input("mCherry_gene", "mCherry_gene_transcription_1_4", Value(dot))
		mCherry_production_4_net.add_input("GFP_activation_mediator_protein", "mCherry_gene_transcription_1_4", Value(dot), notify=[rgb_net.place('red_2_3')])
		mCherry_production_4_net.add_input("mCherry_mrna", "mCherry_mrna_translation_1_4", Value(dot))
		mCherry_production_4_net.add_input("mCherry_protein", "mCherry_protein_degradation_1_4", Value(dot), notify=[rgb_net.place('red_2_3')])
		mCherry_production_4_net.add_output("GFP_receptor_gene", "GFP_receptor_gene_transcription_1_4", Value(dot))
		mCherry_production_4_net.add_output("GFP_receptor_mrna", "GFP_receptor_gene_transcription_1_4", Value(dot))
		mCherry_production_4_net.add_output("GFP_receptor_protein", "GFP_receptor_mrna_translation_1_4", Value(dot), notify=[rgb_net.place('red_2_3')])
		mCherry_production_4_net.add_output("GFP_receptor_active_protein", "enzymatic_reaction_1_4", Value(dot), notify=[rgb_net.place('red_2_3')])
		mCherry_production_4_net.add_output("GFP_activation_mediator_protein", "enzymatic_reaction_1_4", Value(dot), notify=[rgb_net.place('red_2_3')])
		mCherry_production_4_net.add_output("mCherry_gene", "mCherry_gene_transcription_1_4", Value(dot))
		mCherry_production_4_net.add_output("mCherry_mrna", "mCherry_gene_transcription_1_4", Value(dot))
		mCherry_production_4_net.add_output("mCherry_protein", "mCherry_mrna_translation_1_4", MultiArc([Value(dot)]*3), notify=[rgb_net.place('red_2_3')])

		# CD19_production_5_net arcs
		CD19_production_5_net.add_input("CD19_gene", "CD19_gene_transcription_1_5", Value(dot))
		CD19_production_5_net.add_input("CD19_mrna", "CD19_mrna_translation_1_5", Value(dot))
		CD19_production_5_net.add_input("CD19_protein", "CD19_protein_degradation_1_5", Value(dot), notify=[rgb_net.place('red_2_4')])
		CD19_production_5_net.add_output("CD19_gene", "CD19_gene_transcription_1_5", Value(dot))
		CD19_production_5_net.add_output("CD19_mrna", "CD19_gene_transcription_1_5", Value(dot))
		CD19_production_5_net.add_output("CD19_protein", "CD19_mrna_translation_1_5", MultiArc([Value(dot)]*2), notify=[rgb_net.place('red_2_4')])

		# BFP_production_5_net arcs
		BFP_production_5_net.add_input("BFP_gene", "BFP_gene_transcription_1_5", Value(dot))
		BFP_production_5_net.add_input("BFP_mrna", "BFP_mrna_translation_1_5", Value(dot))
		BFP_production_5_net.add_input("BFP_protein", "BFP_protein_degradation_1_5", Value(dot), notify=[rgb_net.place('red_2_4')])
		BFP_production_5_net.add_output("BFP_gene", "BFP_gene_transcription_1_5", Value(dot))
		BFP_production_5_net.add_output("BFP_mrna", "BFP_gene_transcription_1_5", Value(dot))
		BFP_production_5_net.add_output("BFP_protein", "BFP_mrna_translation_1_5", MultiArc([Value(dot)]*2), notify=[rgb_net.place('red_2_4')])

		# mCherry_production_5_net arcs
		mCherry_production_5_net.add_input("GFP_receptor_gene", "GFP_receptor_gene_transcription_1_5", Value(dot))
		mCherry_production_5_net.add_input("GFP_receptor_mrna", "GFP_receptor_mrna_translation_1_5", Value(dot))
		mCherry_production_5_net.add_input("GFP_receptor_active_protein", "enzymatic_reaction_1_5", Value(dot), notify=[rgb_net.place('red_2_4')])
		mCherry_production_5_net.add_input("GFP_receptor_protein", "enzymatic_reaction_1_5", Value(dot), notify=[rgb_net.place('red_2_4')])
		mCherry_production_5_net.add_input("GFP_receptor_active_protein", "GFP_receptor_active_protein_degradation_1_5", Value(dot), notify=[rgb_net.place('red_2_4')])
		mCherry_production_5_net.add_input("mCherry_gene", "mCherry_gene_transcription_1_5", Value(dot))
		mCherry_production_5_net.add_input("GFP_activation_mediator_protein", "mCherry_gene_transcription_1_5", Value(dot), notify=[rgb_net.place('red_2_4')])
		mCherry_production_5_net.add_input("mCherry_mrna", "mCherry_mrna_translation_1_5", Value(dot))
		mCherry_production_5_net.add_input("mCherry_protein", "mCherry_protein_degradation_1_5", Value(dot), notify=[rgb_net.place('red_2_4')])
		mCherry_production_5_net.add_output("GFP_receptor_gene", "GFP_receptor_gene_transcription_1_5", Value(dot))
		mCherry_production_5_net.add_output("GFP_receptor_mrna", "GFP_receptor_gene_transcription_1_5", Value(dot))
		mCherry_production_5_net.add_output("GFP_receptor_protein", "GFP_receptor_mrna_translation_1_5", Value(dot), notify=[rgb_net.place('red_2_4')])
		mCherry_production_5_net.add_output("GFP_receptor_active_protein", "enzymatic_reaction_1_5", Value(dot), notify=[rgb_net.place('red_2_4')])
		mCherry_production_5_net.add_output("GFP_activation_mediator_protein", "enzymatic_reaction_1_5", Value(dot), notify=[rgb_net.place('red_2_4')])
		mCherry_production_5_net.add_output("mCherry_gene", "mCherry_gene_transcription_1_5", Value(dot))
		mCherry_production_5_net.add_output("mCherry_mrna", "mCherry_gene_transcription_1_5", Value(dot))
		mCherry_production_5_net.add_output("mCherry_protein", "mCherry_mrna_translation_1_5", MultiArc([Value(dot)]*3), notify=[rgb_net.place('red_2_4')])

		# CD19_production_6_net arcs
		CD19_production_6_net.add_input("CD19_gene", "CD19_gene_transcription_1_6", Value(dot))
		CD19_production_6_net.add_input("CD19_mrna", "CD19_mrna_translation_1_6", Value(dot))
		CD19_production_6_net.add_input("CD19_protein", "CD19_protein_degradation_1_6", Value(dot), notify=[rgb_net.place('red_4_2')])
		CD19_production_6_net.add_output("CD19_gene", "CD19_gene_transcription_1_6", Value(dot))
		CD19_production_6_net.add_output("CD19_mrna", "CD19_gene_transcription_1_6", Value(dot))
		CD19_production_6_net.add_output("CD19_protein", "CD19_mrna_translation_1_6", MultiArc([Value(dot)]*2), notify=[rgb_net.place('red_4_2')])

		# BFP_production_6_net arcs
		BFP_production_6_net.add_input("BFP_gene", "BFP_gene_transcription_1_6", Value(dot))
		BFP_production_6_net.add_input("BFP_mrna", "BFP_mrna_translation_1_6", Value(dot))
		BFP_production_6_net.add_input("BFP_protein", "BFP_protein_degradation_1_6", Value(dot), notify=[rgb_net.place('red_4_2')])
		BFP_production_6_net.add_output("BFP_gene", "BFP_gene_transcription_1_6", Value(dot))
		BFP_production_6_net.add_output("BFP_mrna", "BFP_gene_transcription_1_6", Value(dot))
		BFP_production_6_net.add_output("BFP_protein", "BFP_mrna_translation_1_6", MultiArc([Value(dot)]*2), notify=[rgb_net.place('red_4_2')])

		# mCherry_production_6_net arcs
		mCherry_production_6_net.add_input("GFP_receptor_gene", "GFP_receptor_gene_transcription_1_6", Value(dot))
		mCherry_production_6_net.add_input("GFP_receptor_mrna", "GFP_receptor_mrna_translation_1_6", Value(dot))
		mCherry_production_6_net.add_input("GFP_receptor_active_protein", "enzymatic_reaction_1_6", Value(dot), notify=[rgb_net.place('red_4_2')])
		mCherry_production_6_net.add_input("GFP_receptor_protein", "enzymatic_reaction_1_6", Value(dot), notify=[rgb_net.place('red_4_2')])
		mCherry_production_6_net.add_input("GFP_receptor_active_protein", "GFP_receptor_active_protein_degradation_1_6", Value(dot), notify=[rgb_net.place('red_4_2')])
		mCherry_production_6_net.add_input("mCherry_gene", "mCherry_gene_transcription_1_6", Value(dot))
		mCherry_production_6_net.add_input("GFP_activation_mediator_protein", "mCherry_gene_transcription_1_6", Value(dot), notify=[rgb_net.place('red_4_2')])
		mCherry_production_6_net.add_input("mCherry_mrna", "mCherry_mrna_translation_1_6", Value(dot))
		mCherry_production_6_net.add_input("mCherry_protein", "mCherry_protein_degradation_1_6", Value(dot), notify=[rgb_net.place('red_4_2')])
		mCherry_production_6_net.add_output("GFP_receptor_gene", "GFP_receptor_gene_transcription_1_6", Value(dot))
		mCherry_production_6_net.add_output("GFP_receptor_mrna", "GFP_receptor_gene_transcription_1_6", Value(dot))
		mCherry_production_6_net.add_output("GFP_receptor_protein", "GFP_receptor_mrna_translation_1_6", Value(dot), notify=[rgb_net.place('red_4_2')])
		mCherry_production_6_net.add_output("GFP_receptor_active_protein", "enzymatic_reaction_1_6", Value(dot), notify=[rgb_net.place('red_4_2')])
		mCherry_production_6_net.add_output("GFP_activation_mediator_protein", "enzymatic_reaction_1_6", Value(dot), notify=[rgb_net.place('red_4_2')])
		mCherry_production_6_net.add_output("mCherry_gene", "mCherry_gene_transcription_1_6", Value(dot))
		mCherry_production_6_net.add_output("mCherry_mrna", "mCherry_gene_transcription_1_6", Value(dot))
		mCherry_production_6_net.add_output("mCherry_protein", "mCherry_mrna_translation_1_6", MultiArc([Value(dot)]*3), notify=[rgb_net.place('red_4_2')])

		# CD19_production_7_net arcs
		CD19_production_7_net.add_input("CD19_gene", "CD19_gene_transcription_1_7", Value(dot))
		CD19_production_7_net.add_input("CD19_mrna", "CD19_mrna_translation_1_7", Value(dot))
		CD19_production_7_net.add_input("CD19_protein", "CD19_protein_degradation_1_7", Value(dot), notify=[rgb_net.place('red_4_3')])
		CD19_production_7_net.add_output("CD19_gene", "CD19_gene_transcription_1_7", Value(dot))
		CD19_production_7_net.add_output("CD19_mrna", "CD19_gene_transcription_1_7", Value(dot))
		CD19_production_7_net.add_output("CD19_protein", "CD19_mrna_translation_1_7", MultiArc([Value(dot)]*2), notify=[rgb_net.place('red_4_3')])

		# BFP_production_7_net arcs
		BFP_production_7_net.add_input("BFP_gene", "BFP_gene_transcription_1_7", Value(dot))
		BFP_production_7_net.add_input("BFP_mrna", "BFP_mrna_translation_1_7", Value(dot))
		BFP_production_7_net.add_input("BFP_protein", "BFP_protein_degradation_1_7", Value(dot), notify=[rgb_net.place('red_4_3')])
		BFP_production_7_net.add_output("BFP_gene", "BFP_gene_transcription_1_7", Value(dot))
		BFP_production_7_net.add_output("BFP_mrna", "BFP_gene_transcription_1_7", Value(dot))
		BFP_production_7_net.add_output("BFP_protein", "BFP_mrna_translation_1_7", MultiArc([Value(dot)]*2), notify=[rgb_net.place('red_4_3')])

		# mCherry_production_7_net arcs
		mCherry_production_7_net.add_input("GFP_receptor_gene", "GFP_receptor_gene_transcription_1_7", Value(dot))
		mCherry_production_7_net.add_input("GFP_receptor_mrna", "GFP_receptor_mrna_translation_1_7", Value(dot))
		mCherry_production_7_net.add_input("GFP_receptor_active_protein", "enzymatic_reaction_1_7", Value(dot), notify=[rgb_net.place('red_4_3')])
		mCherry_production_7_net.add_input("GFP_receptor_protein", "enzymatic_reaction_1_7", Value(dot), notify=[rgb_net.place('red_4_3')])
		mCherry_production_7_net.add_input("GFP_receptor_active_protein", "GFP_receptor_active_protein_degradation_1_7", Value(dot), notify=[rgb_net.place('red_4_3')])
		mCherry_production_7_net.add_input("mCherry_gene", "mCherry_gene_transcription_1_7", Value(dot))
		mCherry_production_7_net.add_input("GFP_activation_mediator_protein", "mCherry_gene_transcription_1_7", Value(dot), notify=[rgb_net.place('red_4_3')])
		mCherry_production_7_net.add_input("mCherry_mrna", "mCherry_mrna_translation_1_7", Value(dot))
		mCherry_production_7_net.add_input("mCherry_protein", "mCherry_protein_degradation_1_7", Value(dot), notify=[rgb_net.place('red_4_3')])
		mCherry_production_7_net.add_output("GFP_receptor_gene", "GFP_receptor_gene_transcription_1_7", Value(dot))
		mCherry_production_7_net.add_output("GFP_receptor_mrna", "GFP_receptor_gene_transcription_1_7", Value(dot))
		mCherry_production_7_net.add_output("GFP_receptor_protein", "GFP_receptor_mrna_translation_1_7", Value(dot), notify=[rgb_net.place('red_4_3')])
		mCherry_production_7_net.add_output("GFP_receptor_active_protein", "enzymatic_reaction_1_7", Value(dot), notify=[rgb_net.place('red_4_3')])
		mCherry_production_7_net.add_output("GFP_activation_mediator_protein", "enzymatic_reaction_1_7", Value(dot), notify=[rgb_net.place('red_4_3')])
		mCherry_production_7_net.add_output("mCherry_gene", "mCherry_gene_transcription_1_7", Value(dot))
		mCherry_production_7_net.add_output("mCherry_mrna", "mCherry_gene_transcription_1_7", Value(dot))
		mCherry_production_7_net.add_output("mCherry_protein", "mCherry_mrna_translation_1_7", MultiArc([Value(dot)]*3), notify=[rgb_net.place('red_4_3')])

		# CD19_production_8_net arcs
		CD19_production_8_net.add_input("CD19_gene", "CD19_gene_transcription_1_8", Value(dot))
		CD19_production_8_net.add_input("CD19_mrna", "CD19_mrna_translation_1_8", Value(dot))
		CD19_production_8_net.add_input("CD19_protein", "CD19_protein_degradation_1_8", Value(dot), notify=[rgb_net.place('red_4_4')])
		CD19_production_8_net.add_output("CD19_gene", "CD19_gene_transcription_1_8", Value(dot))
		CD19_production_8_net.add_output("CD19_mrna", "CD19_gene_transcription_1_8", Value(dot))
		CD19_production_8_net.add_output("CD19_protein", "CD19_mrna_translation_1_8", MultiArc([Value(dot)]*2), notify=[rgb_net.place('red_4_4')])

		# BFP_production_8_net arcs
		BFP_production_8_net.add_input("BFP_gene", "BFP_gene_transcription_1_8", Value(dot))
		BFP_production_8_net.add_input("BFP_mrna", "BFP_mrna_translation_1_8", Value(dot))
		BFP_production_8_net.add_input("BFP_protein", "BFP_protein_degradation_1_8", Value(dot), notify=[rgb_net.place('red_4_4')])
		BFP_production_8_net.add_output("BFP_gene", "BFP_gene_transcription_1_8", Value(dot))
		BFP_production_8_net.add_output("BFP_mrna", "BFP_gene_transcription_1_8", Value(dot))
		BFP_production_8_net.add_output("BFP_protein", "BFP_mrna_translation_1_8", MultiArc([Value(dot)]*2), notify=[rgb_net.place('red_4_4')])

		# mCherry_production_8_net arcs
		mCherry_production_8_net.add_input("GFP_receptor_gene", "GFP_receptor_gene_transcription_1_8", Value(dot))
		mCherry_production_8_net.add_input("GFP_receptor_mrna", "GFP_receptor_mrna_translation_1_8", Value(dot))
		mCherry_production_8_net.add_input("GFP_receptor_active_protein", "enzymatic_reaction_1_8", Value(dot), notify=[rgb_net.place('red_4_4')])
		mCherry_production_8_net.add_input("GFP_receptor_protein", "enzymatic_reaction_1_8", Value(dot), notify=[rgb_net.place('red_4_4')])
		mCherry_production_8_net.add_input("GFP_receptor_active_protein", "GFP_receptor_active_protein_degradation_1_8", Value(dot), notify=[rgb_net.place('red_4_4')])
		mCherry_production_8_net.add_input("mCherry_gene", "mCherry_gene_transcription_1_8", Value(dot))
		mCherry_production_8_net.add_input("GFP_activation_mediator_protein", "mCherry_gene_transcription_1_8", Value(dot), notify=[rgb_net.place('red_4_4')])
		mCherry_production_8_net.add_input("mCherry_mrna", "mCherry_mrna_translation_1_8", Value(dot))
		mCherry_production_8_net.add_input("mCherry_protein", "mCherry_protein_degradation_1_8", Value(dot), notify=[rgb_net.place('red_4_4')])
		mCherry_production_8_net.add_output("GFP_receptor_gene", "GFP_receptor_gene_transcription_1_8", Value(dot))
		mCherry_production_8_net.add_output("GFP_receptor_mrna", "GFP_receptor_gene_transcription_1_8", Value(dot))
		mCherry_production_8_net.add_output("GFP_receptor_protein", "GFP_receptor_mrna_translation_1_8", Value(dot), notify=[rgb_net.place('red_4_4')])
		mCherry_production_8_net.add_output("GFP_receptor_active_protein", "enzymatic_reaction_1_8", Value(dot), notify=[rgb_net.place('red_4_4')])
		mCherry_production_8_net.add_output("GFP_activation_mediator_protein", "enzymatic_reaction_1_8", Value(dot), notify=[rgb_net.place('red_4_4')])
		mCherry_production_8_net.add_output("mCherry_gene", "mCherry_gene_transcription_1_8", Value(dot))
		mCherry_production_8_net.add_output("mCherry_mrna", "mCherry_gene_transcription_1_8", Value(dot))
		mCherry_production_8_net.add_output("mCherry_protein", "mCherry_mrna_translation_1_8", MultiArc([Value(dot)]*3), notify=[rgb_net.place('red_4_4')])

		# CD19_production_9_net arcs
		CD19_production_9_net.add_input("CD19_gene", "CD19_gene_transcription_1_9", Value(dot))
		CD19_production_9_net.add_input("CD19_mrna", "CD19_mrna_translation_1_9", Value(dot))
		CD19_production_9_net.add_input("CD19_protein", "CD19_protein_degradation_1_9", Value(dot), notify=[rgb_net.place('blue_1_2')])
		CD19_production_9_net.add_output("CD19_gene", "CD19_gene_transcription_1_9", Value(dot))
		CD19_production_9_net.add_output("CD19_mrna", "CD19_gene_transcription_1_9", Value(dot))
		CD19_production_9_net.add_output("CD19_protein", "CD19_mrna_translation_1_9", MultiArc([Value(dot)]*2), notify=[rgb_net.place('blue_1_2')])

		# BFP_production_9_net arcs
		BFP_production_9_net.add_input("BFP_gene", "BFP_gene_transcription_1_9", Value(dot))
		BFP_production_9_net.add_input("BFP_mrna", "BFP_mrna_translation_1_9", Value(dot))
		BFP_production_9_net.add_input("BFP_protein", "BFP_protein_degradation_1_9", Value(dot), notify=[rgb_net.place('blue_1_2')])
		BFP_production_9_net.add_output("BFP_gene", "BFP_gene_transcription_1_9", Value(dot))
		BFP_production_9_net.add_output("BFP_mrna", "BFP_gene_transcription_1_9", Value(dot))
		BFP_production_9_net.add_output("BFP_protein", "BFP_mrna_translation_1_9", MultiArc([Value(dot)]*2), notify=[rgb_net.place('blue_1_2')])

		# mCherry_production_9_net arcs
		mCherry_production_9_net.add_input("GFP_receptor_gene", "GFP_receptor_gene_transcription_1_9", Value(dot))
		mCherry_production_9_net.add_input("GFP_receptor_mrna", "GFP_receptor_mrna_translation_1_9", Value(dot))
		mCherry_production_9_net.add_input("GFP_receptor_active_protein", "enzymatic_reaction_1_9", Value(dot), notify=[rgb_net.place('blue_1_2')])
		mCherry_production_9_net.add_input("GFP_receptor_protein", "enzymatic_reaction_1_9", Value(dot), notify=[rgb_net.place('blue_1_2')])
		mCherry_production_9_net.add_input("GFP_receptor_active_protein", "GFP_receptor_active_protein_degradation_1_9", Value(dot), notify=[rgb_net.place('blue_1_2')])
		mCherry_production_9_net.add_input("mCherry_gene", "mCherry_gene_transcription_1_9", Value(dot))
		mCherry_production_9_net.add_input("GFP_activation_mediator_protein", "mCherry_gene_transcription_1_9", Value(dot), notify=[rgb_net.place('blue_1_2')])
		mCherry_production_9_net.add_input("mCherry_mrna", "mCherry_mrna_translation_1_9", Value(dot))
		mCherry_production_9_net.add_input("mCherry_protein", "mCherry_protein_degradation_1_9", Value(dot), notify=[rgb_net.place('blue_1_2')])
		mCherry_production_9_net.add_output("GFP_receptor_gene", "GFP_receptor_gene_transcription_1_9", Value(dot))
		mCherry_production_9_net.add_output("GFP_receptor_mrna", "GFP_receptor_gene_transcription_1_9", Value(dot))
		mCherry_production_9_net.add_output("GFP_receptor_protein", "GFP_receptor_mrna_translation_1_9", Value(dot), notify=[rgb_net.place('blue_1_2')])
		mCherry_production_9_net.add_output("GFP_receptor_active_protein", "enzymatic_reaction_1_9", Value(dot), notify=[rgb_net.place('blue_1_2')])
		mCherry_production_9_net.add_output("GFP_activation_mediator_protein", "enzymatic_reaction_1_9", Value(dot), notify=[rgb_net.place('blue_1_2')])
		mCherry_production_9_net.add_output("mCherry_gene", "mCherry_gene_transcription_1_9", Value(dot))
		mCherry_production_9_net.add_output("mCherry_mrna", "mCherry_gene_transcription_1_9", Value(dot))
		mCherry_production_9_net.add_output("mCherry_protein", "mCherry_mrna_translation_1_9", MultiArc([Value(dot)]*3), notify=[rgb_net.place('blue_1_2')])

		# CD19_production_10_net arcs
		CD19_production_10_net.add_input("CD19_gene", "CD19_gene_transcription_1_10", Value(dot))
		CD19_production_10_net.add_input("CD19_mrna", "CD19_mrna_translation_1_10", Value(dot))
		CD19_production_10_net.add_input("CD19_protein", "CD19_protein_degradation_1_10", Value(dot), notify=[rgb_net.place('blue_1_3')])
		CD19_production_10_net.add_output("CD19_gene", "CD19_gene_transcription_1_10", Value(dot))
		CD19_production_10_net.add_output("CD19_mrna", "CD19_gene_transcription_1_10", Value(dot))
		CD19_production_10_net.add_output("CD19_protein", "CD19_mrna_translation_1_10", MultiArc([Value(dot)]*2), notify=[rgb_net.place('blue_1_3')])

		# BFP_production_10_net arcs
		BFP_production_10_net.add_input("BFP_gene", "BFP_gene_transcription_1_10", Value(dot))
		BFP_production_10_net.add_input("BFP_mrna", "BFP_mrna_translation_1_10", Value(dot))
		BFP_production_10_net.add_input("BFP_protein", "BFP_protein_degradation_1_10", Value(dot), notify=[rgb_net.place('blue_1_3')])
		BFP_production_10_net.add_output("BFP_gene", "BFP_gene_transcription_1_10", Value(dot))
		BFP_production_10_net.add_output("BFP_mrna", "BFP_gene_transcription_1_10", Value(dot))
		BFP_production_10_net.add_output("BFP_protein", "BFP_mrna_translation_1_10", MultiArc([Value(dot)]*2), notify=[rgb_net.place('blue_1_3')])

		# mCherry_production_10_net arcs
		mCherry_production_10_net.add_input("GFP_receptor_gene", "GFP_receptor_gene_transcription_1_10", Value(dot))
		mCherry_production_10_net.add_input("GFP_receptor_mrna", "GFP_receptor_mrna_translation_1_10", Value(dot))
		mCherry_production_10_net.add_input("GFP_receptor_active_protein", "enzymatic_reaction_1_10", Value(dot), notify=[rgb_net.place('blue_1_3')])
		mCherry_production_10_net.add_input("GFP_receptor_protein", "enzymatic_reaction_1_10", Value(dot), notify=[rgb_net.place('blue_1_3')])
		mCherry_production_10_net.add_input("GFP_receptor_active_protein", "GFP_receptor_active_protein_degradation_1_10", Value(dot), notify=[rgb_net.place('blue_1_3')])
		mCherry_production_10_net.add_input("mCherry_gene", "mCherry_gene_transcription_1_10", Value(dot))
		mCherry_production_10_net.add_input("GFP_activation_mediator_protein", "mCherry_gene_transcription_1_10", Value(dot), notify=[rgb_net.place('blue_1_3')])
		mCherry_production_10_net.add_input("mCherry_mrna", "mCherry_mrna_translation_1_10", Value(dot))
		mCherry_production_10_net.add_input("mCherry_protein", "mCherry_protein_degradation_1_10", Value(dot), notify=[rgb_net.place('blue_1_3')])
		mCherry_production_10_net.add_output("GFP_receptor_gene", "GFP_receptor_gene_transcription_1_10", Value(dot))
		mCherry_production_10_net.add_output("GFP_receptor_mrna", "GFP_receptor_gene_transcription_1_10", Value(dot))
		mCherry_production_10_net.add_output("GFP_receptor_protein", "GFP_receptor_mrna_translation_1_10", Value(dot), notify=[rgb_net.place('blue_1_3')])
		mCherry_production_10_net.add_output("GFP_receptor_active_protein", "enzymatic_reaction_1_10", Value(dot), notify=[rgb_net.place('blue_1_3')])
		mCherry_production_10_net.add_output("GFP_activation_mediator_protein", "enzymatic_reaction_1_10", Value(dot), notify=[rgb_net.place('blue_1_3')])
		mCherry_production_10_net.add_output("mCherry_gene", "mCherry_gene_transcription_1_10", Value(dot))
		mCherry_production_10_net.add_output("mCherry_mrna", "mCherry_gene_transcription_1_10", Value(dot))
		mCherry_production_10_net.add_output("mCherry_protein", "mCherry_mrna_translation_1_10", MultiArc([Value(dot)]*3), notify=[rgb_net.place('blue_1_3')])

		# CD19_production_11_net arcs
		CD19_production_11_net.add_input("CD19_gene", "CD19_gene_transcription_1_11", Value(dot))
		CD19_production_11_net.add_input("CD19_mrna", "CD19_mrna_translation_1_11", Value(dot))
		CD19_production_11_net.add_input("CD19_protein", "CD19_protein_degradation_1_11", Value(dot), notify=[rgb_net.place('blue_1_4')])
		CD19_production_11_net.add_output("CD19_gene", "CD19_gene_transcription_1_11", Value(dot))
		CD19_production_11_net.add_output("CD19_mrna", "CD19_gene_transcription_1_11", Value(dot))
		CD19_production_11_net.add_output("CD19_protein", "CD19_mrna_translation_1_11", MultiArc([Value(dot)]*2), notify=[rgb_net.place('blue_1_4')])

		# BFP_production_11_net arcs
		BFP_production_11_net.add_input("BFP_gene", "BFP_gene_transcription_1_11", Value(dot))
		BFP_production_11_net.add_input("BFP_mrna", "BFP_mrna_translation_1_11", Value(dot))
		BFP_production_11_net.add_input("BFP_protein", "BFP_protein_degradation_1_11", Value(dot), notify=[rgb_net.place('blue_1_4')])
		BFP_production_11_net.add_output("BFP_gene", "BFP_gene_transcription_1_11", Value(dot))
		BFP_production_11_net.add_output("BFP_mrna", "BFP_gene_transcription_1_11", Value(dot))
		BFP_production_11_net.add_output("BFP_protein", "BFP_mrna_translation_1_11", MultiArc([Value(dot)]*2), notify=[rgb_net.place('blue_1_4')])

		# mCherry_production_11_net arcs
		mCherry_production_11_net.add_input("GFP_receptor_gene", "GFP_receptor_gene_transcription_1_11", Value(dot))
		mCherry_production_11_net.add_input("GFP_receptor_mrna", "GFP_receptor_mrna_translation_1_11", Value(dot))
		mCherry_production_11_net.add_input("GFP_receptor_active_protein", "enzymatic_reaction_1_11", Value(dot), notify=[rgb_net.place('blue_1_4')])
		mCherry_production_11_net.add_input("GFP_receptor_protein", "enzymatic_reaction_1_11", Value(dot), notify=[rgb_net.place('blue_1_4')])
		mCherry_production_11_net.add_input("GFP_receptor_active_protein", "GFP_receptor_active_protein_degradation_1_11", Value(dot), notify=[rgb_net.place('blue_1_4')])
		mCherry_production_11_net.add_input("mCherry_gene", "mCherry_gene_transcription_1_11", Value(dot))
		mCherry_production_11_net.add_input("GFP_activation_mediator_protein", "mCherry_gene_transcription_1_11", Value(dot), notify=[rgb_net.place('blue_1_4')])
		mCherry_production_11_net.add_input("mCherry_mrna", "mCherry_mrna_translation_1_11", Value(dot))
		mCherry_production_11_net.add_input("mCherry_protein", "mCherry_protein_degradation_1_11", Value(dot), notify=[rgb_net.place('blue_1_4')])
		mCherry_production_11_net.add_output("GFP_receptor_gene", "GFP_receptor_gene_transcription_1_11", Value(dot))
		mCherry_production_11_net.add_output("GFP_receptor_mrna", "GFP_receptor_gene_transcription_1_11", Value(dot))
		mCherry_production_11_net.add_output("GFP_receptor_protein", "GFP_receptor_mrna_translation_1_11", Value(dot), notify=[rgb_net.place('blue_1_4')])
		mCherry_production_11_net.add_output("GFP_receptor_active_protein", "enzymatic_reaction_1_11", Value(dot), notify=[rgb_net.place('blue_1_4')])
		mCherry_production_11_net.add_output("GFP_activation_mediator_protein", "enzymatic_reaction_1_11", Value(dot), notify=[rgb_net.place('blue_1_4')])
		mCherry_production_11_net.add_output("mCherry_gene", "mCherry_gene_transcription_1_11", Value(dot))
		mCherry_production_11_net.add_output("mCherry_mrna", "mCherry_gene_transcription_1_11", Value(dot))
		mCherry_production_11_net.add_output("mCherry_protein", "mCherry_mrna_translation_1_11", MultiArc([Value(dot)]*3), notify=[rgb_net.place('blue_1_4')])

		# CD19_production_12_net arcs
		CD19_production_12_net.add_input("CD19_gene", "CD19_gene_transcription_1_12", Value(dot))
		CD19_production_12_net.add_input("CD19_mrna", "CD19_mrna_translation_1_12", Value(dot))
		CD19_production_12_net.add_input("CD19_protein", "CD19_protein_degradation_1_12", Value(dot), notify=[rgb_net.place('blue_2_1')])
		CD19_production_12_net.add_output("CD19_gene", "CD19_gene_transcription_1_12", Value(dot))
		CD19_production_12_net.add_output("CD19_mrna", "CD19_gene_transcription_1_12", Value(dot))
		CD19_production_12_net.add_output("CD19_protein", "CD19_mrna_translation_1_12", MultiArc([Value(dot)]*2), notify=[rgb_net.place('blue_2_1')])

		# BFP_production_12_net arcs
		BFP_production_12_net.add_input("BFP_gene", "BFP_gene_transcription_1_12", Value(dot))
		BFP_production_12_net.add_input("BFP_mrna", "BFP_mrna_translation_1_12", Value(dot))
		BFP_production_12_net.add_input("BFP_protein", "BFP_protein_degradation_1_12", Value(dot), notify=[rgb_net.place('blue_2_1')])
		BFP_production_12_net.add_output("BFP_gene", "BFP_gene_transcription_1_12", Value(dot))
		BFP_production_12_net.add_output("BFP_mrna", "BFP_gene_transcription_1_12", Value(dot))
		BFP_production_12_net.add_output("BFP_protein", "BFP_mrna_translation_1_12", MultiArc([Value(dot)]*2), notify=[rgb_net.place('blue_2_1')])

		# mCherry_production_12_net arcs
		mCherry_production_12_net.add_input("GFP_receptor_gene", "GFP_receptor_gene_transcription_1_12", Value(dot))
		mCherry_production_12_net.add_input("GFP_receptor_mrna", "GFP_receptor_mrna_translation_1_12", Value(dot))
		mCherry_production_12_net.add_input("GFP_receptor_active_protein", "enzymatic_reaction_1_12", Value(dot), notify=[rgb_net.place('blue_2_1')])
		mCherry_production_12_net.add_input("GFP_receptor_protein", "enzymatic_reaction_1_12", Value(dot), notify=[rgb_net.place('blue_2_1')])
		mCherry_production_12_net.add_input("GFP_receptor_active_protein", "GFP_receptor_active_protein_degradation_1_12", Value(dot), notify=[rgb_net.place('blue_2_1')])
		mCherry_production_12_net.add_input("mCherry_gene", "mCherry_gene_transcription_1_12", Value(dot))
		mCherry_production_12_net.add_input("GFP_activation_mediator_protein", "mCherry_gene_transcription_1_12", Value(dot), notify=[rgb_net.place('blue_2_1')])
		mCherry_production_12_net.add_input("mCherry_mrna", "mCherry_mrna_translation_1_12", Value(dot))
		mCherry_production_12_net.add_input("mCherry_protein", "mCherry_protein_degradation_1_12", Value(dot), notify=[rgb_net.place('blue_2_1')])
		mCherry_production_12_net.add_output("GFP_receptor_gene", "GFP_receptor_gene_transcription_1_12", Value(dot))
		mCherry_production_12_net.add_output("GFP_receptor_mrna", "GFP_receptor_gene_transcription_1_12", Value(dot))
		mCherry_production_12_net.add_output("GFP_receptor_protein", "GFP_receptor_mrna_translation_1_12", Value(dot), notify=[rgb_net.place('blue_2_1')])
		mCherry_production_12_net.add_output("GFP_receptor_active_protein", "enzymatic_reaction_1_12", Value(dot), notify=[rgb_net.place('blue_2_1')])
		mCherry_production_12_net.add_output("GFP_activation_mediator_protein", "enzymatic_reaction_1_12", Value(dot), notify=[rgb_net.place('blue_2_1')])
		mCherry_production_12_net.add_output("mCherry_gene", "mCherry_gene_transcription_1_12", Value(dot))
		mCherry_production_12_net.add_output("mCherry_mrna", "mCherry_gene_transcription_1_12", Value(dot))
		mCherry_production_12_net.add_output("mCherry_protein", "mCherry_mrna_translation_1_12", MultiArc([Value(dot)]*3), notify=[rgb_net.place('blue_2_1')])

		# CD19_production_13_net arcs
		CD19_production_13_net.add_input("CD19_gene", "CD19_gene_transcription_1_13", Value(dot))
		CD19_production_13_net.add_input("CD19_mrna", "CD19_mrna_translation_1_13", Value(dot))
		CD19_production_13_net.add_input("CD19_protein", "CD19_protein_degradation_1_13", Value(dot), notify=[rgb_net.place('blue_2_5')])
		CD19_production_13_net.add_output("CD19_gene", "CD19_gene_transcription_1_13", Value(dot))
		CD19_production_13_net.add_output("CD19_mrna", "CD19_gene_transcription_1_13", Value(dot))
		CD19_production_13_net.add_output("CD19_protein", "CD19_mrna_translation_1_13", MultiArc([Value(dot)]*2), notify=[rgb_net.place('blue_2_5')])

		# BFP_production_13_net arcs
		BFP_production_13_net.add_input("BFP_gene", "BFP_gene_transcription_1_13", Value(dot))
		BFP_production_13_net.add_input("BFP_mrna", "BFP_mrna_translation_1_13", Value(dot))
		BFP_production_13_net.add_input("BFP_protein", "BFP_protein_degradation_1_13", Value(dot), notify=[rgb_net.place('blue_2_5')])
		BFP_production_13_net.add_output("BFP_gene", "BFP_gene_transcription_1_13", Value(dot))
		BFP_production_13_net.add_output("BFP_mrna", "BFP_gene_transcription_1_13", Value(dot))
		BFP_production_13_net.add_output("BFP_protein", "BFP_mrna_translation_1_13", MultiArc([Value(dot)]*2), notify=[rgb_net.place('blue_2_5')])

		# mCherry_production_13_net arcs
		mCherry_production_13_net.add_input("GFP_receptor_gene", "GFP_receptor_gene_transcription_1_13", Value(dot))
		mCherry_production_13_net.add_input("GFP_receptor_mrna", "GFP_receptor_mrna_translation_1_13", Value(dot))
		mCherry_production_13_net.add_input("GFP_receptor_active_protein", "enzymatic_reaction_1_13", Value(dot), notify=[rgb_net.place('blue_2_5')])
		mCherry_production_13_net.add_input("GFP_receptor_protein", "enzymatic_reaction_1_13", Value(dot), notify=[rgb_net.place('blue_2_5')])
		mCherry_production_13_net.add_input("GFP_receptor_active_protein", "GFP_receptor_active_protein_degradation_1_13", Value(dot), notify=[rgb_net.place('blue_2_5')])
		mCherry_production_13_net.add_input("mCherry_gene", "mCherry_gene_transcription_1_13", Value(dot))
		mCherry_production_13_net.add_input("GFP_activation_mediator_protein", "mCherry_gene_transcription_1_13", Value(dot), notify=[rgb_net.place('blue_2_5')])
		mCherry_production_13_net.add_input("mCherry_mrna", "mCherry_mrna_translation_1_13", Value(dot))
		mCherry_production_13_net.add_input("mCherry_protein", "mCherry_protein_degradation_1_13", Value(dot), notify=[rgb_net.place('blue_2_5')])
		mCherry_production_13_net.add_output("GFP_receptor_gene", "GFP_receptor_gene_transcription_1_13", Value(dot))
		mCherry_production_13_net.add_output("GFP_receptor_mrna", "GFP_receptor_gene_transcription_1_13", Value(dot))
		mCherry_production_13_net.add_output("GFP_receptor_protein", "GFP_receptor_mrna_translation_1_13", Value(dot), notify=[rgb_net.place('blue_2_5')])
		mCherry_production_13_net.add_output("GFP_receptor_active_protein", "enzymatic_reaction_1_13", Value(dot), notify=[rgb_net.place('blue_2_5')])
		mCherry_production_13_net.add_output("GFP_activation_mediator_protein", "enzymatic_reaction_1_13", Value(dot), notify=[rgb_net.place('blue_2_5')])
		mCherry_production_13_net.add_output("mCherry_gene", "mCherry_gene_transcription_1_13", Value(dot))
		mCherry_production_13_net.add_output("mCherry_mrna", "mCherry_gene_transcription_1_13", Value(dot))
		mCherry_production_13_net.add_output("mCherry_protein", "mCherry_mrna_translation_1_13", MultiArc([Value(dot)]*3), notify=[rgb_net.place('blue_2_5')])

		# CD19_production_14_net arcs
		CD19_production_14_net.add_input("CD19_gene", "CD19_gene_transcription_1_14", Value(dot))
		CD19_production_14_net.add_input("CD19_mrna", "CD19_mrna_translation_1_14", Value(dot))
		CD19_production_14_net.add_input("CD19_protein", "CD19_protein_degradation_1_14", Value(dot), notify=[rgb_net.place('blue_3_1')])
		CD19_production_14_net.add_output("CD19_gene", "CD19_gene_transcription_1_14", Value(dot))
		CD19_production_14_net.add_output("CD19_mrna", "CD19_gene_transcription_1_14", Value(dot))
		CD19_production_14_net.add_output("CD19_protein", "CD19_mrna_translation_1_14", MultiArc([Value(dot)]*2), notify=[rgb_net.place('blue_3_1')])

		# BFP_production_14_net arcs
		BFP_production_14_net.add_input("BFP_gene", "BFP_gene_transcription_1_14", Value(dot))
		BFP_production_14_net.add_input("BFP_mrna", "BFP_mrna_translation_1_14", Value(dot))
		BFP_production_14_net.add_input("BFP_protein", "BFP_protein_degradation_1_14", Value(dot), notify=[rgb_net.place('blue_3_1')])
		BFP_production_14_net.add_output("BFP_gene", "BFP_gene_transcription_1_14", Value(dot))
		BFP_production_14_net.add_output("BFP_mrna", "BFP_gene_transcription_1_14", Value(dot))
		BFP_production_14_net.add_output("BFP_protein", "BFP_mrna_translation_1_14", MultiArc([Value(dot)]*2), notify=[rgb_net.place('blue_3_1')])

		# mCherry_production_14_net arcs
		mCherry_production_14_net.add_input("GFP_receptor_gene", "GFP_receptor_gene_transcription_1_14", Value(dot))
		mCherry_production_14_net.add_input("GFP_receptor_mrna", "GFP_receptor_mrna_translation_1_14", Value(dot))
		mCherry_production_14_net.add_input("GFP_receptor_active_protein", "enzymatic_reaction_1_14", Value(dot), notify=[rgb_net.place('blue_3_1')])
		mCherry_production_14_net.add_input("GFP_receptor_protein", "enzymatic_reaction_1_14", Value(dot), notify=[rgb_net.place('blue_3_1')])
		mCherry_production_14_net.add_input("GFP_receptor_active_protein", "GFP_receptor_active_protein_degradation_1_14", Value(dot), notify=[rgb_net.place('blue_3_1')])
		mCherry_production_14_net.add_input("mCherry_gene", "mCherry_gene_transcription_1_14", Value(dot))
		mCherry_production_14_net.add_input("GFP_activation_mediator_protein", "mCherry_gene_transcription_1_14", Value(dot), notify=[rgb_net.place('blue_3_1')])
		mCherry_production_14_net.add_input("mCherry_mrna", "mCherry_mrna_translation_1_14", Value(dot))
		mCherry_production_14_net.add_input("mCherry_protein", "mCherry_protein_degradation_1_14", Value(dot), notify=[rgb_net.place('blue_3_1')])
		mCherry_production_14_net.add_output("GFP_receptor_gene", "GFP_receptor_gene_transcription_1_14", Value(dot))
		mCherry_production_14_net.add_output("GFP_receptor_mrna", "GFP_receptor_gene_transcription_1_14", Value(dot))
		mCherry_production_14_net.add_output("GFP_receptor_protein", "GFP_receptor_mrna_translation_1_14", Value(dot), notify=[rgb_net.place('blue_3_1')])
		mCherry_production_14_net.add_output("GFP_receptor_active_protein", "enzymatic_reaction_1_14", Value(dot), notify=[rgb_net.place('blue_3_1')])
		mCherry_production_14_net.add_output("GFP_activation_mediator_protein", "enzymatic_reaction_1_14", Value(dot), notify=[rgb_net.place('blue_3_1')])
		mCherry_production_14_net.add_output("mCherry_gene", "mCherry_gene_transcription_1_14", Value(dot))
		mCherry_production_14_net.add_output("mCherry_mrna", "mCherry_gene_transcription_1_14", Value(dot))
		mCherry_production_14_net.add_output("mCherry_protein", "mCherry_mrna_translation_1_14", MultiArc([Value(dot)]*3), notify=[rgb_net.place('blue_3_1')])

		# CD19_production_15_net arcs
		CD19_production_15_net.add_input("CD19_gene", "CD19_gene_transcription_1_15", Value(dot))
		CD19_production_15_net.add_input("CD19_mrna", "CD19_mrna_translation_1_15", Value(dot))
		CD19_production_15_net.add_input("CD19_protein", "CD19_protein_degradation_1_15", Value(dot), notify=[rgb_net.place('blue_3_5')])
		CD19_production_15_net.add_output("CD19_gene", "CD19_gene_transcription_1_15", Value(dot))
		CD19_production_15_net.add_output("CD19_mrna", "CD19_gene_transcription_1_15", Value(dot))
		CD19_production_15_net.add_output("CD19_protein", "CD19_mrna_translation_1_15", MultiArc([Value(dot)]*2), notify=[rgb_net.place('blue_3_5')])

		# BFP_production_15_net arcs
		BFP_production_15_net.add_input("BFP_gene", "BFP_gene_transcription_1_15", Value(dot))
		BFP_production_15_net.add_input("BFP_mrna", "BFP_mrna_translation_1_15", Value(dot))
		BFP_production_15_net.add_input("BFP_protein", "BFP_protein_degradation_1_15", Value(dot), notify=[rgb_net.place('blue_3_5')])
		BFP_production_15_net.add_output("BFP_gene", "BFP_gene_transcription_1_15", Value(dot))
		BFP_production_15_net.add_output("BFP_mrna", "BFP_gene_transcription_1_15", Value(dot))
		BFP_production_15_net.add_output("BFP_protein", "BFP_mrna_translation_1_15", MultiArc([Value(dot)]*2), notify=[rgb_net.place('blue_3_5')])

		# mCherry_production_15_net arcs
		mCherry_production_15_net.add_input("GFP_receptor_gene", "GFP_receptor_gene_transcription_1_15", Value(dot))
		mCherry_production_15_net.add_input("GFP_receptor_mrna", "GFP_receptor_mrna_translation_1_15", Value(dot))
		mCherry_production_15_net.add_input("GFP_receptor_active_protein", "enzymatic_reaction_1_15", Value(dot), notify=[rgb_net.place('blue_3_5')])
		mCherry_production_15_net.add_input("GFP_receptor_protein", "enzymatic_reaction_1_15", Value(dot), notify=[rgb_net.place('blue_3_5')])
		mCherry_production_15_net.add_input("GFP_receptor_active_protein", "GFP_receptor_active_protein_degradation_1_15", Value(dot), notify=[rgb_net.place('blue_3_5')])
		mCherry_production_15_net.add_input("mCherry_gene", "mCherry_gene_transcription_1_15", Value(dot))
		mCherry_production_15_net.add_input("GFP_activation_mediator_protein", "mCherry_gene_transcription_1_15", Value(dot), notify=[rgb_net.place('blue_3_5')])
		mCherry_production_15_net.add_input("mCherry_mrna", "mCherry_mrna_translation_1_15", Value(dot))
		mCherry_production_15_net.add_input("mCherry_protein", "mCherry_protein_degradation_1_15", Value(dot), notify=[rgb_net.place('blue_3_5')])
		mCherry_production_15_net.add_output("GFP_receptor_gene", "GFP_receptor_gene_transcription_1_15", Value(dot))
		mCherry_production_15_net.add_output("GFP_receptor_mrna", "GFP_receptor_gene_transcription_1_15", Value(dot))
		mCherry_production_15_net.add_output("GFP_receptor_protein", "GFP_receptor_mrna_translation_1_15", Value(dot), notify=[rgb_net.place('blue_3_5')])
		mCherry_production_15_net.add_output("GFP_receptor_active_protein", "enzymatic_reaction_1_15", Value(dot), notify=[rgb_net.place('blue_3_5')])
		mCherry_production_15_net.add_output("GFP_activation_mediator_protein", "enzymatic_reaction_1_15", Value(dot), notify=[rgb_net.place('blue_3_5')])
		mCherry_production_15_net.add_output("mCherry_gene", "mCherry_gene_transcription_1_15", Value(dot))
		mCherry_production_15_net.add_output("mCherry_mrna", "mCherry_gene_transcription_1_15", Value(dot))
		mCherry_production_15_net.add_output("mCherry_protein", "mCherry_mrna_translation_1_15", MultiArc([Value(dot)]*3), notify=[rgb_net.place('blue_3_5')])

		# CD19_production_16_net arcs
		CD19_production_16_net.add_input("CD19_gene", "CD19_gene_transcription_1_16", Value(dot))
		CD19_production_16_net.add_input("CD19_mrna", "CD19_mrna_translation_1_16", Value(dot))
		CD19_production_16_net.add_input("CD19_protein", "CD19_protein_degradation_1_16", Value(dot), notify=[rgb_net.place('blue_3_1')])
		CD19_production_16_net.add_output("CD19_gene", "CD19_gene_transcription_1_16", Value(dot))
		CD19_production_16_net.add_output("CD19_mrna", "CD19_gene_transcription_1_16", Value(dot))
		CD19_production_16_net.add_output("CD19_protein", "CD19_mrna_translation_1_16", MultiArc([Value(dot)]*2), notify=[rgb_net.place('blue_3_1')])

		# BFP_production_16_net arcs
		BFP_production_16_net.add_input("BFP_gene", "BFP_gene_transcription_1_16", Value(dot))
		BFP_production_16_net.add_input("BFP_mrna", "BFP_mrna_translation_1_16", Value(dot))
		BFP_production_16_net.add_input("BFP_protein", "BFP_protein_degradation_1_16", Value(dot), notify=[rgb_net.place('blue_3_1')])
		BFP_production_16_net.add_output("BFP_gene", "BFP_gene_transcription_1_16", Value(dot))
		BFP_production_16_net.add_output("BFP_mrna", "BFP_gene_transcription_1_16", Value(dot))
		BFP_production_16_net.add_output("BFP_protein", "BFP_mrna_translation_1_16", MultiArc([Value(dot)]*2), notify=[rgb_net.place('blue_3_1')])

		# mCherry_production_16_net arcs
		mCherry_production_16_net.add_input("GFP_receptor_gene", "GFP_receptor_gene_transcription_1_16", Value(dot))
		mCherry_production_16_net.add_input("GFP_receptor_mrna", "GFP_receptor_mrna_translation_1_16", Value(dot))
		mCherry_production_16_net.add_input("GFP_receptor_active_protein", "enzymatic_reaction_1_16", Value(dot), notify=[rgb_net.place('blue_3_1')])
		mCherry_production_16_net.add_input("GFP_receptor_protein", "enzymatic_reaction_1_16", Value(dot), notify=[rgb_net.place('blue_3_1')])
		mCherry_production_16_net.add_input("GFP_receptor_active_protein", "GFP_receptor_active_protein_degradation_1_16", Value(dot), notify=[rgb_net.place('blue_3_1')])
		mCherry_production_16_net.add_input("mCherry_gene", "mCherry_gene_transcription_1_16", Value(dot))
		mCherry_production_16_net.add_input("GFP_activation_mediator_protein", "mCherry_gene_transcription_1_16", Value(dot), notify=[rgb_net.place('blue_3_1')])
		mCherry_production_16_net.add_input("mCherry_mrna", "mCherry_mrna_translation_1_16", Value(dot))
		mCherry_production_16_net.add_input("mCherry_protein", "mCherry_protein_degradation_1_16", Value(dot), notify=[rgb_net.place('blue_3_1')])
		mCherry_production_16_net.add_output("GFP_receptor_gene", "GFP_receptor_gene_transcription_1_16", Value(dot))
		mCherry_production_16_net.add_output("GFP_receptor_mrna", "GFP_receptor_gene_transcription_1_16", Value(dot))
		mCherry_production_16_net.add_output("GFP_receptor_protein", "GFP_receptor_mrna_translation_1_16", Value(dot), notify=[rgb_net.place('blue_3_1')])
		mCherry_production_16_net.add_output("GFP_receptor_active_protein", "enzymatic_reaction_1_16", Value(dot), notify=[rgb_net.place('blue_3_1')])
		mCherry_production_16_net.add_output("GFP_activation_mediator_protein", "enzymatic_reaction_1_16", Value(dot), notify=[rgb_net.place('blue_3_1')])
		mCherry_production_16_net.add_output("mCherry_gene", "mCherry_gene_transcription_1_16", Value(dot))
		mCherry_production_16_net.add_output("mCherry_mrna", "mCherry_gene_transcription_1_16", Value(dot))
		mCherry_production_16_net.add_output("mCherry_protein", "mCherry_mrna_translation_1_16", MultiArc([Value(dot)]*3), notify=[rgb_net.place('blue_3_1')])

		# CD19_production_17_net arcs
		CD19_production_17_net.add_input("CD19_gene", "CD19_gene_transcription_1_17", Value(dot))
		CD19_production_17_net.add_input("CD19_mrna", "CD19_mrna_translation_1_17", Value(dot))
		CD19_production_17_net.add_input("CD19_protein", "CD19_protein_degradation_1_17", Value(dot), notify=[rgb_net.place('blue_4_1')])
		CD19_production_17_net.add_output("CD19_gene", "CD19_gene_transcription_1_17", Value(dot))
		CD19_production_17_net.add_output("CD19_mrna", "CD19_gene_transcription_1_17", Value(dot))
		CD19_production_17_net.add_output("CD19_protein", "CD19_mrna_translation_1_17", MultiArc([Value(dot)]*2), notify=[rgb_net.place('blue_4_1')])

		# BFP_production_17_net arcs
		BFP_production_17_net.add_input("BFP_gene", "BFP_gene_transcription_1_17", Value(dot))
		BFP_production_17_net.add_input("BFP_mrna", "BFP_mrna_translation_1_17", Value(dot))
		BFP_production_17_net.add_input("BFP_protein", "BFP_protein_degradation_1_17", Value(dot), notify=[rgb_net.place('blue_4_1')])
		BFP_production_17_net.add_output("BFP_gene", "BFP_gene_transcription_1_17", Value(dot))
		BFP_production_17_net.add_output("BFP_mrna", "BFP_gene_transcription_1_17", Value(dot))
		BFP_production_17_net.add_output("BFP_protein", "BFP_mrna_translation_1_17", MultiArc([Value(dot)]*2), notify=[rgb_net.place('blue_4_1')])

		# mCherry_production_17_net arcs
		mCherry_production_17_net.add_input("GFP_receptor_gene", "GFP_receptor_gene_transcription_1_17", Value(dot))
		mCherry_production_17_net.add_input("GFP_receptor_mrna", "GFP_receptor_mrna_translation_1_17", Value(dot))
		mCherry_production_17_net.add_input("GFP_receptor_active_protein", "enzymatic_reaction_1_17", Value(dot), notify=[rgb_net.place('blue_4_1')])
		mCherry_production_17_net.add_input("GFP_receptor_protein", "enzymatic_reaction_1_17", Value(dot), notify=[rgb_net.place('blue_4_1')])
		mCherry_production_17_net.add_input("GFP_receptor_active_protein", "GFP_receptor_active_protein_degradation_1_17", Value(dot), notify=[rgb_net.place('blue_4_1')])
		mCherry_production_17_net.add_input("mCherry_gene", "mCherry_gene_transcription_1_17", Value(dot))
		mCherry_production_17_net.add_input("GFP_activation_mediator_protein", "mCherry_gene_transcription_1_17", Value(dot), notify=[rgb_net.place('blue_4_1')])
		mCherry_production_17_net.add_input("mCherry_mrna", "mCherry_mrna_translation_1_17", Value(dot))
		mCherry_production_17_net.add_input("mCherry_protein", "mCherry_protein_degradation_1_17", Value(dot), notify=[rgb_net.place('blue_4_1')])
		mCherry_production_17_net.add_output("GFP_receptor_gene", "GFP_receptor_gene_transcription_1_17", Value(dot))
		mCherry_production_17_net.add_output("GFP_receptor_mrna", "GFP_receptor_gene_transcription_1_17", Value(dot))
		mCherry_production_17_net.add_output("GFP_receptor_protein", "GFP_receptor_mrna_translation_1_17", Value(dot), notify=[rgb_net.place('blue_4_1')])
		mCherry_production_17_net.add_output("GFP_receptor_active_protein", "enzymatic_reaction_1_17", Value(dot), notify=[rgb_net.place('blue_4_1')])
		mCherry_production_17_net.add_output("GFP_activation_mediator_protein", "enzymatic_reaction_1_17", Value(dot), notify=[rgb_net.place('blue_4_1')])
		mCherry_production_17_net.add_output("mCherry_gene", "mCherry_gene_transcription_1_17", Value(dot))
		mCherry_production_17_net.add_output("mCherry_mrna", "mCherry_gene_transcription_1_17", Value(dot))
		mCherry_production_17_net.add_output("mCherry_protein", "mCherry_mrna_translation_1_17", MultiArc([Value(dot)]*3), notify=[rgb_net.place('blue_4_1')])

		# CD19_production_18_net arcs
		CD19_production_18_net.add_input("CD19_gene", "CD19_gene_transcription_1_18", Value(dot))
		CD19_production_18_net.add_input("CD19_mrna", "CD19_mrna_translation_1_18", Value(dot))
		CD19_production_18_net.add_input("CD19_protein", "CD19_protein_degradation_1_18", Value(dot), notify=[rgb_net.place('blue_4_5')])
		CD19_production_18_net.add_output("CD19_gene", "CD19_gene_transcription_1_18", Value(dot))
		CD19_production_18_net.add_output("CD19_mrna", "CD19_gene_transcription_1_18", Value(dot))
		CD19_production_18_net.add_output("CD19_protein", "CD19_mrna_translation_1_18", MultiArc([Value(dot)]*2), notify=[rgb_net.place('blue_4_5')])

		# BFP_production_18_net arcs
		BFP_production_18_net.add_input("BFP_gene", "BFP_gene_transcription_1_18", Value(dot))
		BFP_production_18_net.add_input("BFP_mrna", "BFP_mrna_translation_1_18", Value(dot))
		BFP_production_18_net.add_input("BFP_protein", "BFP_protein_degradation_1_18", Value(dot), notify=[rgb_net.place('blue_4_5')])
		BFP_production_18_net.add_output("BFP_gene", "BFP_gene_transcription_1_18", Value(dot))
		BFP_production_18_net.add_output("BFP_mrna", "BFP_gene_transcription_1_18", Value(dot))
		BFP_production_18_net.add_output("BFP_protein", "BFP_mrna_translation_1_18", MultiArc([Value(dot)]*2), notify=[rgb_net.place('blue_4_5')])

		# mCherry_production_18_net arcs
		mCherry_production_18_net.add_input("GFP_receptor_gene", "GFP_receptor_gene_transcription_1_18", Value(dot))
		mCherry_production_18_net.add_input("GFP_receptor_mrna", "GFP_receptor_mrna_translation_1_18", Value(dot))
		mCherry_production_18_net.add_input("GFP_receptor_active_protein", "enzymatic_reaction_1_18", Value(dot), notify=[rgb_net.place('blue_4_5')])
		mCherry_production_18_net.add_input("GFP_receptor_protein", "enzymatic_reaction_1_18", Value(dot), notify=[rgb_net.place('blue_4_5')])
		mCherry_production_18_net.add_input("GFP_receptor_active_protein", "GFP_receptor_active_protein_degradation_1_18", Value(dot), notify=[rgb_net.place('blue_4_5')])
		mCherry_production_18_net.add_input("mCherry_gene", "mCherry_gene_transcription_1_18", Value(dot))
		mCherry_production_18_net.add_input("GFP_activation_mediator_protein", "mCherry_gene_transcription_1_18", Value(dot), notify=[rgb_net.place('blue_4_5')])
		mCherry_production_18_net.add_input("mCherry_mrna", "mCherry_mrna_translation_1_18", Value(dot))
		mCherry_production_18_net.add_input("mCherry_protein", "mCherry_protein_degradation_1_18", Value(dot), notify=[rgb_net.place('blue_4_5')])
		mCherry_production_18_net.add_output("GFP_receptor_gene", "GFP_receptor_gene_transcription_1_18", Value(dot))
		mCherry_production_18_net.add_output("GFP_receptor_mrna", "GFP_receptor_gene_transcription_1_18", Value(dot))
		mCherry_production_18_net.add_output("GFP_receptor_protein", "GFP_receptor_mrna_translation_1_18", Value(dot), notify=[rgb_net.place('blue_4_5')])
		mCherry_production_18_net.add_output("GFP_receptor_active_protein", "enzymatic_reaction_1_18", Value(dot), notify=[rgb_net.place('blue_4_5')])
		mCherry_production_18_net.add_output("GFP_activation_mediator_protein", "enzymatic_reaction_1_18", Value(dot), notify=[rgb_net.place('blue_4_5')])
		mCherry_production_18_net.add_output("mCherry_gene", "mCherry_gene_transcription_1_18", Value(dot))
		mCherry_production_18_net.add_output("mCherry_mrna", "mCherry_gene_transcription_1_18", Value(dot))
		mCherry_production_18_net.add_output("mCherry_protein", "mCherry_mrna_translation_1_18", MultiArc([Value(dot)]*3), notify=[rgb_net.place('blue_4_5')])

		# CD19_production_19_net arcs
		CD19_production_19_net.add_input("CD19_gene", "CD19_gene_transcription_1_19", Value(dot))
		CD19_production_19_net.add_input("CD19_mrna", "CD19_mrna_translation_1_19", Value(dot))
		CD19_production_19_net.add_input("CD19_protein", "CD19_protein_degradation_1_19", Value(dot), notify=[rgb_net.place('blue_5_2')])
		CD19_production_19_net.add_output("CD19_gene", "CD19_gene_transcription_1_19", Value(dot))
		CD19_production_19_net.add_output("CD19_mrna", "CD19_gene_transcription_1_19", Value(dot))
		CD19_production_19_net.add_output("CD19_protein", "CD19_mrna_translation_1_19", MultiArc([Value(dot)]*2), notify=[rgb_net.place('blue_5_2')])

		# BFP_production_19_net arcs
		BFP_production_19_net.add_input("BFP_gene", "BFP_gene_transcription_1_19", Value(dot))
		BFP_production_19_net.add_input("BFP_mrna", "BFP_mrna_translation_1_19", Value(dot))
		BFP_production_19_net.add_input("BFP_protein", "BFP_protein_degradation_1_19", Value(dot), notify=[rgb_net.place('blue_5_2')])
		BFP_production_19_net.add_output("BFP_gene", "BFP_gene_transcription_1_19", Value(dot))
		BFP_production_19_net.add_output("BFP_mrna", "BFP_gene_transcription_1_19", Value(dot))
		BFP_production_19_net.add_output("BFP_protein", "BFP_mrna_translation_1_19", MultiArc([Value(dot)]*2), notify=[rgb_net.place('blue_5_2')])

		# mCherry_production_19_net arcs
		mCherry_production_19_net.add_input("GFP_receptor_gene", "GFP_receptor_gene_transcription_1_19", Value(dot))
		mCherry_production_19_net.add_input("GFP_receptor_mrna", "GFP_receptor_mrna_translation_1_19", Value(dot))
		mCherry_production_19_net.add_input("GFP_receptor_active_protein", "enzymatic_reaction_1_19", Value(dot), notify=[rgb_net.place('blue_5_2')])
		mCherry_production_19_net.add_input("GFP_receptor_protein", "enzymatic_reaction_1_19", Value(dot), notify=[rgb_net.place('blue_5_2')])
		mCherry_production_19_net.add_input("GFP_receptor_active_protein", "GFP_receptor_active_protein_degradation_1_19", Value(dot), notify=[rgb_net.place('blue_5_2')])
		mCherry_production_19_net.add_input("mCherry_gene", "mCherry_gene_transcription_1_19", Value(dot))
		mCherry_production_19_net.add_input("GFP_activation_mediator_protein", "mCherry_gene_transcription_1_19", Value(dot), notify=[rgb_net.place('blue_5_2')])
		mCherry_production_19_net.add_input("mCherry_mrna", "mCherry_mrna_translation_1_19", Value(dot))
		mCherry_production_19_net.add_input("mCherry_protein", "mCherry_protein_degradation_1_19", Value(dot), notify=[rgb_net.place('blue_5_2')])
		mCherry_production_19_net.add_output("GFP_receptor_gene", "GFP_receptor_gene_transcription_1_19", Value(dot))
		mCherry_production_19_net.add_output("GFP_receptor_mrna", "GFP_receptor_gene_transcription_1_19", Value(dot))
		mCherry_production_19_net.add_output("GFP_receptor_protein", "GFP_receptor_mrna_translation_1_19", Value(dot), notify=[rgb_net.place('blue_5_2')])
		mCherry_production_19_net.add_output("GFP_receptor_active_protein", "enzymatic_reaction_1_19", Value(dot), notify=[rgb_net.place('blue_5_2')])
		mCherry_production_19_net.add_output("GFP_activation_mediator_protein", "enzymatic_reaction_1_19", Value(dot), notify=[rgb_net.place('blue_5_2')])
		mCherry_production_19_net.add_output("mCherry_gene", "mCherry_gene_transcription_1_19", Value(dot))
		mCherry_production_19_net.add_output("mCherry_mrna", "mCherry_gene_transcription_1_19", Value(dot))
		mCherry_production_19_net.add_output("mCherry_protein", "mCherry_mrna_translation_1_19", MultiArc([Value(dot)]*3), notify=[rgb_net.place('blue_5_2')])

		# CD19_production_20_net arcs
		CD19_production_20_net.add_input("CD19_gene", "CD19_gene_transcription_1_20", Value(dot))
		CD19_production_20_net.add_input("CD19_mrna", "CD19_mrna_translation_1_20", Value(dot))
		CD19_production_20_net.add_input("CD19_protein", "CD19_protein_degradation_1_20", Value(dot), notify=[rgb_net.place('blue_5_3')])
		CD19_production_20_net.add_output("CD19_gene", "CD19_gene_transcription_1_20", Value(dot))
		CD19_production_20_net.add_output("CD19_mrna", "CD19_gene_transcription_1_20", Value(dot))
		CD19_production_20_net.add_output("CD19_protein", "CD19_mrna_translation_1_20", MultiArc([Value(dot)]*2), notify=[rgb_net.place('blue_5_3')])

		# BFP_production_20_net arcs
		BFP_production_20_net.add_input("BFP_gene", "BFP_gene_transcription_1_20", Value(dot))
		BFP_production_20_net.add_input("BFP_mrna", "BFP_mrna_translation_1_20", Value(dot))
		BFP_production_20_net.add_input("BFP_protein", "BFP_protein_degradation_1_20", Value(dot), notify=[rgb_net.place('blue_5_3')])
		BFP_production_20_net.add_output("BFP_gene", "BFP_gene_transcription_1_20", Value(dot))
		BFP_production_20_net.add_output("BFP_mrna", "BFP_gene_transcription_1_20", Value(dot))
		BFP_production_20_net.add_output("BFP_protein", "BFP_mrna_translation_1_20", MultiArc([Value(dot)]*2), notify=[rgb_net.place('blue_5_3')])

		# mCherry_production_20_net arcs
		mCherry_production_20_net.add_input("GFP_receptor_gene", "GFP_receptor_gene_transcription_1_20", Value(dot))
		mCherry_production_20_net.add_input("GFP_receptor_mrna", "GFP_receptor_mrna_translation_1_20", Value(dot))
		mCherry_production_20_net.add_input("GFP_receptor_active_protein", "enzymatic_reaction_1_20", Value(dot), notify=[rgb_net.place('blue_5_3')])
		mCherry_production_20_net.add_input("GFP_receptor_protein", "enzymatic_reaction_1_20", Value(dot), notify=[rgb_net.place('blue_5_3')])
		mCherry_production_20_net.add_input("GFP_receptor_active_protein", "GFP_receptor_active_protein_degradation_1_20", Value(dot), notify=[rgb_net.place('blue_5_3')])
		mCherry_production_20_net.add_input("mCherry_gene", "mCherry_gene_transcription_1_20", Value(dot))
		mCherry_production_20_net.add_input("GFP_activation_mediator_protein", "mCherry_gene_transcription_1_20", Value(dot), notify=[rgb_net.place('blue_5_3')])
		mCherry_production_20_net.add_input("mCherry_mrna", "mCherry_mrna_translation_1_20", Value(dot))
		mCherry_production_20_net.add_input("mCherry_protein", "mCherry_protein_degradation_1_20", Value(dot), notify=[rgb_net.place('blue_5_3')])
		mCherry_production_20_net.add_output("GFP_receptor_gene", "GFP_receptor_gene_transcription_1_20", Value(dot))
		mCherry_production_20_net.add_output("GFP_receptor_mrna", "GFP_receptor_gene_transcription_1_20", Value(dot))
		mCherry_production_20_net.add_output("GFP_receptor_protein", "GFP_receptor_mrna_translation_1_20", Value(dot), notify=[rgb_net.place('blue_5_3')])
		mCherry_production_20_net.add_output("GFP_receptor_active_protein", "enzymatic_reaction_1_20", Value(dot), notify=[rgb_net.place('blue_5_3')])
		mCherry_production_20_net.add_output("GFP_activation_mediator_protein", "enzymatic_reaction_1_20", Value(dot), notify=[rgb_net.place('blue_5_3')])
		mCherry_production_20_net.add_output("mCherry_gene", "mCherry_gene_transcription_1_20", Value(dot))
		mCherry_production_20_net.add_output("mCherry_mrna", "mCherry_gene_transcription_1_20", Value(dot))
		mCherry_production_20_net.add_output("mCherry_protein", "mCherry_mrna_translation_1_20", MultiArc([Value(dot)]*3), notify=[rgb_net.place('blue_5_3')])

		# CD19_production_21_net arcs
		CD19_production_21_net.add_input("CD19_gene", "CD19_gene_transcription_1_21", Value(dot))
		CD19_production_21_net.add_input("CD19_mrna", "CD19_mrna_translation_1_21", Value(dot))
		CD19_production_21_net.add_input("CD19_protein", "CD19_protein_degradation_1_21", Value(dot), notify=[rgb_net.place('blue_5_4')])
		CD19_production_21_net.add_output("CD19_gene", "CD19_gene_transcription_1_21", Value(dot))
		CD19_production_21_net.add_output("CD19_mrna", "CD19_gene_transcription_1_21", Value(dot))
		CD19_production_21_net.add_output("CD19_protein", "CD19_mrna_translation_1_21", MultiArc([Value(dot)]*2), notify=[rgb_net.place('blue_5_4')])

		# BFP_production_21_net arcs
		BFP_production_21_net.add_input("BFP_gene", "BFP_gene_transcription_1_21", Value(dot))
		BFP_production_21_net.add_input("BFP_mrna", "BFP_mrna_translation_1_21", Value(dot))
		BFP_production_21_net.add_input("BFP_protein", "BFP_protein_degradation_1_21", Value(dot), notify=[rgb_net.place('blue_5_4')])
		BFP_production_21_net.add_output("BFP_gene", "BFP_gene_transcription_1_21", Value(dot))
		BFP_production_21_net.add_output("BFP_mrna", "BFP_gene_transcription_1_21", Value(dot))
		BFP_production_21_net.add_output("BFP_protein", "BFP_mrna_translation_1_21", MultiArc([Value(dot)]*2), notify=[rgb_net.place('blue_5_4')])

		# mCherry_production_21_net arcs
		mCherry_production_21_net.add_input("GFP_receptor_gene", "GFP_receptor_gene_transcription_1_21", Value(dot))
		mCherry_production_21_net.add_input("GFP_receptor_mrna", "GFP_receptor_mrna_translation_1_21", Value(dot))
		mCherry_production_21_net.add_input("GFP_receptor_active_protein", "enzymatic_reaction_1_21", Value(dot), notify=[rgb_net.place('blue_5_4')])
		mCherry_production_21_net.add_input("GFP_receptor_protein", "enzymatic_reaction_1_21", Value(dot), notify=[rgb_net.place('blue_5_4')])
		mCherry_production_21_net.add_input("GFP_receptor_active_protein", "GFP_receptor_active_protein_degradation_1_21", Value(dot), notify=[rgb_net.place('blue_5_4')])
		mCherry_production_21_net.add_input("mCherry_gene", "mCherry_gene_transcription_1_21", Value(dot))
		mCherry_production_21_net.add_input("GFP_activation_mediator_protein", "mCherry_gene_transcription_1_21", Value(dot), notify=[rgb_net.place('blue_5_4')])
		mCherry_production_21_net.add_input("mCherry_mrna", "mCherry_mrna_translation_1_21", Value(dot))
		mCherry_production_21_net.add_input("mCherry_protein", "mCherry_protein_degradation_1_21", Value(dot), notify=[rgb_net.place('blue_5_4')])
		mCherry_production_21_net.add_output("GFP_receptor_gene", "GFP_receptor_gene_transcription_1_21", Value(dot))
		mCherry_production_21_net.add_output("GFP_receptor_mrna", "GFP_receptor_gene_transcription_1_21", Value(dot))
		mCherry_production_21_net.add_output("GFP_receptor_protein", "GFP_receptor_mrna_translation_1_21", Value(dot), notify=[rgb_net.place('blue_5_4')])
		mCherry_production_21_net.add_output("GFP_receptor_active_protein", "enzymatic_reaction_1_21", Value(dot), notify=[rgb_net.place('blue_5_4')])
		mCherry_production_21_net.add_output("GFP_activation_mediator_protein", "enzymatic_reaction_1_21", Value(dot), notify=[rgb_net.place('blue_5_4')])
		mCherry_production_21_net.add_output("mCherry_gene", "mCherry_gene_transcription_1_21", Value(dot))
		mCherry_production_21_net.add_output("mCherry_mrna", "mCherry_gene_transcription_1_21", Value(dot))
		mCherry_production_21_net.add_output("mCherry_protein", "mCherry_mrna_translation_1_21", MultiArc([Value(dot)]*3), notify=[rgb_net.place('blue_5_4')])
		return rgb_net
