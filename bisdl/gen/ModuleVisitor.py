# Generated from bisdl/Module.g4 by ANTLR 4.9.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ModuleParser import ModuleParser
else:
    from ModuleParser import ModuleParser

# This class defines a complete generic visitor for a parse tree produced by ModuleParser.

class ModuleVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ModuleParser#root.
    def visitRoot(self, ctx:ModuleParser.RootContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ModuleParser#timescale.
    def visitTimescale(self, ctx:ModuleParser.TimescaleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ModuleParser#scopes.
    def visitScopes(self, ctx:ModuleParser.ScopesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ModuleParser#scope.
    def visitScope(self, ctx:ModuleParser.ScopeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ModuleParser#coords.
    def visitCoords(self, ctx:ModuleParser.CoordsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ModuleParser#processes.
    def visitProcesses(self, ctx:ModuleParser.ProcessesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ModuleParser#process.
    def visitProcess(self, ctx:ModuleParser.ProcessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ModuleParser#process_type.
    def visitProcess_type(self, ctx:ModuleParser.Process_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ModuleParser#transcription.
    def visitTranscription(self, ctx:ModuleParser.TranscriptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ModuleParser#translation.
    def visitTranslation(self, ctx:ModuleParser.TranslationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ModuleParser#degradation.
    def visitDegradation(self, ctx:ModuleParser.DegradationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ModuleParser#protein_complex_formation.
    def visitProtein_complex_formation(self, ctx:ModuleParser.Protein_complex_formationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ModuleParser#enzymatic_reaction.
    def visitEnzymatic_reaction(self, ctx:ModuleParser.Enzymatic_reactionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ModuleParser#custom_process.
    def visitCustom_process(self, ctx:ModuleParser.Custom_processContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ModuleParser#regulation.
    def visitRegulation(self, ctx:ModuleParser.RegulationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ModuleParser#type_inhibitors.
    def visitType_inhibitors(self, ctx:ModuleParser.Type_inhibitorsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ModuleParser#type_inducers.
    def visitType_inducers(self, ctx:ModuleParser.Type_inducersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ModuleParser#type_activators.
    def visitType_activators(self, ctx:ModuleParser.Type_activatorsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ModuleParser#m_list.
    def visitM_list(self, ctx:ModuleParser.M_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ModuleParser#type_gene.
    def visitType_gene(self, ctx:ModuleParser.Type_geneContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ModuleParser#type_mrna.
    def visitType_mrna(self, ctx:ModuleParser.Type_mrnaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ModuleParser#type_protein.
    def visitType_protein(self, ctx:ModuleParser.Type_proteinContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ModuleParser#type_molecule.
    def visitType_molecule(self, ctx:ModuleParser.Type_moleculeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ModuleParser#type_complex.
    def visitType_complex(self, ctx:ModuleParser.Type_complexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ModuleParser#signal.
    def visitSignal(self, ctx:ModuleParser.SignalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ModuleParser#signals.
    def visitSignals(self, ctx:ModuleParser.SignalsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ModuleParser#paracrine_signals.
    def visitParacrine_signals(self, ctx:ModuleParser.Paracrine_signalsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ModuleParser#juxtacrine_signal.
    def visitJuxtacrine_signal(self, ctx:ModuleParser.Juxtacrine_signalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ModuleParser#diffusion.
    def visitDiffusion(self, ctx:ModuleParser.DiffusionContext):
        return self.visitChildren(ctx)



del ModuleParser