import re
from collections import defaultdict
from copy import deepcopy

import numpy as np

# TODO leggere i signals all'inizio del parsing, poi nella sottorete generica (process) inserire il
# notify per i posti della rete superiore che hanno quel nome
# TODO mettere il controllo dell'esistenza del posto in make_place e toglierlo altrove
# TODO usare il moltiplicatore mult nelle funzioni make_xxx_arc
# TODO testare se mettendo i posti nella rete di sopra all'inizio, funziona lo stesso tutto
# TODO check numeri > 0
# TODO contatore globale per avere nomi univoci (correggere nomi transizioni già fatte)


from bisdl.gen.ModuleParser import ModuleParser
from bisdl.gen.ModuleListener import ModuleListener

tree = lambda: defaultdict(tree)


def _starts_with_number(s):
    numbers = [str(i) for i in range(0, 10)]
    return any([s.startswith(l) for l in numbers])


def _legit_node_name(n):
    if _starts_with_number(n):
        return "_" + n
    return n


def _get_places_from_mlist(mlist):
    table = str.maketrans(dict.fromkeys("[]"))
    return mlist.translate(table).split(",")


def _mlist_to_dict(mlist):
    d = dict()
    for x in mlist.split(","):
        if "*" in x:
            mult, molecule = x.split("*")
        else:
            mult, molecule = '1', x
        d[molecule] = mult
    return d


def recursive_replace(d, old_val, new_val):
    # check whether it's a dict, list, tuple, or scalar
    if isinstance(d, dict):
        items = d.items()
    elif isinstance(d, (list, tuple)):
        items = enumerate(d)
    else:
        # just a value, replace and return
        return str(d).replace(old_val, new_val)
    # now call ourself for every value and replace in the input
    for key, value in items:
        d[key] = recursive_replace(value, old_val, new_val)
    return d


# This class defines a complete listener for a parse tree produced by ModuleParser.
class ModuleListenerImpl(ModuleListener):

    def __init__(self):
        self.buf = list()
        self._parent_places = defaultdict(list)
        self._child_places = defaultdict(set)
        self._regulation_elems = defaultdict(dict)
        self._nodes = tree()
        self._paracrine_signals = list()
        self._place_coords = defaultdict(tuple)
        self._neighbors = defaultdict(list)
        self._def_processes = defaultdict()
        self._make_def = False
        self._t_names = defaultdict(int)
        self._juxtacrine_transitions = list()

    def _make_net(self, net_name, timescale):
        if not net_name.endswith("_net"):
            net_name += "_net"
        n = f'{net_name} = PetriNet("{net_name}", timescale={timescale})'
        self._nodes[net_name]["net"] = n

    def _make_place(self, net, place, net_token="", activation=0):
        tk = ((", [BlackToken()]" + (("*" + str(activation)) if activation > 0 else "")) if "_gene" in place else "") + net_token
        if place not in self._child_places[net]:
            self._child_places[net].add(place)
            s = net + ".add_place(Place(\"" + place + "\"" + tk + "))"
            self._nodes[net]["places"][place] = s

    def _unique_t_name(self, transition):
        self._t_names[transition] += 1
        return f"{transition}_{str(self._t_names[transition])}"

    def _make_transition(self, net, transition, rule=None):
        t = net + ".add_transition(Transition(\"" + transition + "\"" + (", " + rule if rule is not None else "") + "))"
        self._nodes[net]["transitions"][transition] = t

    def _make_input_arc(self, net, place, transition, mult="1", token_type="Value(dot)"):
        tk = token_type if mult == "1" else "MultiArc([" + token_type + "]*" + mult + ")"
        if net == self._parent_net:
            notify = "[" + ", ".join(self._parent_places[place]) + "]"
        else:
            parent_place = next((p for p, net_tokens in self._parent_places.items() if net in net_tokens), None) if "protein" in place else None
            notify = ("[" + self._parent_net + ".place(" + repr(parent_place) + ")]") if parent_place is not None else None
        a = net + ".add_input(\"" + place + "\", \"" + transition + "\", " + tk + ((", notify=" + notify) if notify is not None else "") + ")"
        if not "input_arcs" in self._nodes[net].keys():
            self._nodes[net]["input_arcs"] = list()
        self._nodes[net]["input_arcs"].append(a)

    def _make_output_arc(self, net, place, transition, mult="1", token_type="Value(dot)"):
        tk = token_type if mult == "1" else "MultiArc([" + token_type + "]*" + mult + ")"
        if net == self._parent_net:
            notify = "[" + ", ".join(self._parent_places[place]) + "]"
        else:
            parent_place = next((p for p, net_tokens in self._parent_places.items() if net in net_tokens), None) if "protein" in place else None
            notify = ("[" + self._parent_net + ".place(" + repr(parent_place) + ")]") if parent_place is not None else None
        a = net + ".add_output(\"" + place + "\", \"" + transition + "\", " + tk + ((", notify=" + notify) if notify is not None else "") + ")"
        if not "output_arcs" in self._nodes[net].keys():
            self._nodes[net]["output_arcs"] = list()
        self._nodes[net]["output_arcs"].append(a)

    def _build_neighborhood(self):
        for i, (n1, coord1) in enumerate(self._place_coords.items()):
            for j, (n2, coord2) in enumerate(self._place_coords.items()):
                if j > i:
                    if all([x == 0 for x in np.abs(np.subtract(coord1, coord2))]):
                        raise (Exception(
                            "Scope coordinates must be unique. " + n1 + ":" + str(coord1) + ", " + n2 + ":" + str(
                                coord2)))
                    if all([x <= 1 for x in np.abs(np.subtract(coord1, coord2))]):
                        self._neighbors[n1].append(n2)
        #return self._neighbors

    def _make_regulation(self, transitions, src, dest, mult):
        addToken = 0
        for regulation_type in self._regulation_elems:
            molecules = self._regulation_elems[regulation_type]
            if regulation_type == "INHIBITORS":
                #for _t in transitions:
                for molecule, count in molecules.items():
                    self._make_place(self._sub_net, molecule)
                    for i in range(int(count)):
                        _t = self._unique_t_name(src + "_inhibition_" + molecule)# + ("_" + str(i) if i > 0 else ""))
                        self._make_transition(self._sub_net, _t)
                        self._make_input_arc(self._sub_net, molecule, _t)
                        self._make_input_arc(self._sub_net, src, _t)
            elif regulation_type == "INDUCERS":
                for _t in transitions:
                    for molecule, count in molecules.items():
                        self._make_place(self._sub_net, molecule)
                        self._make_input_arc(self._sub_net, molecule, _t)
            elif regulation_type == "ACTIVATORS":
                for _t in transitions:
                    for molecule, count in molecules.items():
                        self._make_place(self._sub_net, molecule)
                        for i in range(int(count)):
                            addToken += 1
                            _tt = self._unique_t_name(_t + "_activated_" + molecule)# + ("_" + str(i) if i > 0 else ""))
                            self._make_transition(self._sub_net, _tt)
                            self._make_input_arc(self._sub_net, src, _tt)
                            if "gene" in src:
                                self._make_output_arc(self._sub_net, src, _tt)
                            self._make_input_arc(self._sub_net, molecule, _tt)
                            self._make_output_arc(self._sub_net, dest, _tt, mult)
        self._regulation_elems = defaultdict()
        return addToken

    def _make_header(self, ctx: ModuleParser.RootContext):
        header = f"from wrapping import *\n\n\n" \
                 f"class {self._module_name}(Module):\n" \
                 f"\tdef __init__(self, name):\n" \
                 f"\t\tsuper().__init__(name)\n\n" \
                 f"\tdef build_net_structure(self) -> PetriNet:\n" \
                 f"\t\tsuper(self.__class__, self).build_net_structure()\n"
        self._t = "\t\t"
        return header

    # Enter a parse tree produced by ModuleParser#root.
    def enterRoot(self, ctx: ModuleParser.RootContext):
        self._module_name = ctx.ID().getText()
        self._parent_net = self._module_name + "_net"
        timescale = ctx.timescale().INT().getText() if ctx.timescale() is not None else "1"
        self._make_net(self._parent_net, timescale)

    # Exit a parse tree produced by ModuleParser#root.
    def exitRoot(self, ctx: ModuleParser.RootContext):
        self.buf.append(self._make_header(ctx))
        self.buf.append(f'{self._t}# petri nets')
        [ self.buf.append(f'{self._t}{self._nodes[n]["net"]}') for n in reversed(self._nodes) ]
        for n in reversed(self._nodes):
            self.buf.append(f'\n{self._t}# {n} places')
            self.buf.append('\n'.join([ f'{self._t}{_t}' for _t in self._nodes[n]["places"].values() ]))
            self.buf.append(f'\n{self._t}# {n} transitions')
            self.buf.append('\n'.join([ f'{self._t}{_t}' for _t in self._nodes[n]["transitions"].values() ]))
        for n in self._nodes:
            self.buf.append(f'\n{self._t}# {n} arcs')
            self.buf.append('\n'.join([ f'{self._t}{_t}' for _t in self._nodes[n]["input_arcs"] ]))
            self.buf.append('\n'.join([ f'{self._t}{_t}' for _t in self._nodes[n]["output_arcs"] ]))
        self.buf.append(f'\n{self._t}return {self._parent_net}\n')


    # Enter a parse tree produced by ModuleParser#scopes.
    def enterScopes(self, ctx: ModuleParser.ScopesContext):
        # LAMMERDA
        for scope in ctx.scope():
            _scope_id = scope.ID().getText()
            self._parent_places[_scope_id] = list()
            self._place_coords[scope.ID().getText()] = tuple(int(x) for x in scope.coords().getText().strip('()').split(","))
            for processes in scope.getChildren():
                if type(processes) == ModuleParser.ProcessesContext:
                    for process in processes.getChildren():
                        if type(process) == ModuleParser.ProcessContext:
                            pass
                            #_net = process.ID().getText() + "_net"
                            #self._parent_places[scope.ID().getText()].append(_net)  # risale a processes e da là a scope
                            #self._make_net(_net, process.timescale().INT().getText())



                            #for process_type in process.getChildren():
                            #    if type(process_type) == ModuleParser.Process_typeContext:
                            #        for child in process_type.getChildren():
                            #            if type(child) == ModuleParser.TranscriptionContext:
                            #                self._make_place(_net, child.GENE().getText())
                            #                self._make_place(_net, child.MRNA().getText())

    # Exit a parse tree produced by ModuleParser#scopes.
    def exitScopes(self, ctx: ModuleParser.ScopesContext):
        self._build_neighborhood()
        for place, nets in self._parent_places.items():
            net_tokens = ", [ " + ", ".join(nets) + " ]" if len(nets) > 0 else ""
            self._make_place(self._parent_net, place, net_tokens)
        # TODO assert all src_ and dest_ scopes exist
        for _jt in self._juxtacrine_transitions:
            net, transition, rule, src_scope, dest_scope = _jt
            self._make_transition(net, transition, rule)
            self._make_input_arc(net, src_scope, transition, token_type=f"Variable('x')")
            self._make_output_arc(net, dest_scope, transition,
                                  token_type=f"Expression('x.replace(\"protein\", \"receptor_active_protein\")')")

    def exitScope(self, ctx:ModuleParser.ScopeContext):
        self._place_coords[ctx.ID().getText()] = tuple(int(x) for x in ctx.coords().getText().strip('()').split(","))

    # Enter a parse tree produced by ModuleParser#processes.
    def enterProcesses(self, ctx: ModuleParser.ProcessesContext):
        __curr_scope_id = ctx.parentCtx.ID().getText()
        p_names = [ p.ID().getText() for p in ctx.getChildren() if type(p) == ModuleParser.ProcessContext ]
        duplicates = set([x for x in p_names if p_names.count(x) > 1])
        if duplicates:
            raise Exception(f'Duplicate PROCESS names {p_names} in SCOPE {__curr_scope_id}')

    # Enter a parse tree produced by ModuleParser#process.
    def enterProcess(self, ctx: ModuleParser.ProcessContext):
        _p_id = ctx.ID().getText()
        __curr_scope_id = ctx.parentCtx.parentCtx.ID().getText()
        if _p_id not in self._def_processes.keys():
            data = defaultdict()
            data['COUNT'] = 0
            data['TIMESCALE'] = ctx.timescale().INT().getText()
            data['ARCS'] = list()
            self._def_processes[_p_id] = data
        else:
            self._def_processes[_p_id]['COUNT'] += 1
            data = self._def_processes[_p_id]

        _net = f'{_p_id}_{data["COUNT"]}_net'
        # se il PROCESS esisteva già (cioè count>0):
        # copia le stringhe di quella net/process (places, transitions, in/out arcs)
        # e sostituisci il nome della net
        if data['COUNT'] > 0:
            self._nodes[_net] = deepcopy(self._nodes[f'{_p_id}_0_net'])
            recursive_replace(self._nodes[_net], "0", str(data['COUNT']))

        # SNAKES needs unique transition names...
        list_t = defaultdict()
        for t in self._nodes[_net]['transitions'].keys():
            _t = self._unique_t_name(t)
            list_t[_t] = self._nodes[_net]['transitions'][t].replace(t, _t)
            self._nodes[_net]['input_arcs'] = [_a.replace(t, _t) for _a in self._nodes[_net]['input_arcs']]
            self._nodes[_net]['output_arcs'] = [_a.replace(t, _t) for _a in self._nodes[_net]['output_arcs']]
            self._nodes[_net]['input_arcs'] = [re.sub(r'place\(\'\w+\'\)', f"place('{__curr_scope_id}')", _a) for _a in self._nodes[_net]['input_arcs']]
            self._nodes[_net]['output_arcs'] = [re.sub(r'place\(\'\w+\'\)', f"place('{__curr_scope_id}')", _a) for _a in self._nodes[_net]['output_arcs']]
        self._nodes[_net]['transitions'] = deepcopy(list_t)
        self._make_net(_net, data['TIMESCALE'])
        self._parent_places[__curr_scope_id].append(_net)

        self._sub_net = _net

    # Exit a parse tree produced by ModuleParser#transcription.
    def exitTranscription(self, ctx: ModuleParser.TranscriptionContext):
        gene = ctx.GENE().getText()
        mult = ctx.mult().INT().getText() if ctx.mult() is not None else "1"
        mrna = ctx.MRNA().getText()
        _transitions = list()
        # for i in range(int(mult)):
        transition = self._unique_t_name(f"{gene}_transcription")  # + ("_" + str(i) if i > 0 else "")
        _transitions.append(transition)
        self._make_transition(self._sub_net, transition)
        self._make_input_arc(self._sub_net, gene, transition)
        self._make_output_arc(self._sub_net, gene, transition)
        self._make_output_arc(self._sub_net, mrna, transition, mult=mult)
        addToken = self._make_regulation(_transitions, gene, mrna, mult=mult)
        self._make_place(self._sub_net, gene, activation=addToken)
        self._make_place(self._sub_net, mrna)

    # Exit a parse tree produced by ModuleParser#translation.
    def exitTranslation(self, ctx: ModuleParser.TranslationContext):
        mrna = ctx.MRNA().getText()
        mult = ctx.mult().INT().getText() if ctx.mult() is not None else "1"
        protein = ctx.PROTEIN().getText()
        self._make_place(self._sub_net, mrna)
        self._make_place(self._sub_net, protein)
        _transitions = list()
        # for i in range(int(mult)):
        transition = self._unique_t_name(f"{mrna}_translation")  # + ("_" + str(i) if i > 0 else "")
        _transitions.append(transition)
        self._make_transition(self._sub_net, transition)
        self._make_input_arc(self._sub_net, mrna, transition)
        self._make_output_arc(self._sub_net, protein, transition, mult=mult)
        # self._make_regulation(_transitions, mrna, protein)
        addToken = self._make_regulation(_transitions, mrna, protein, mult=mult)
        self._make_place(self._sub_net, protein)

    # Exit a parse tree produced by ModuleParser#degradation.
    def exitDegradation(self, ctx: ModuleParser.DegradationContext):
        molecule = ctx.MRNA().getText() if ctx.MRNA() else ctx.PROTEIN().getText()
        mult = ctx.mult().INT().getText() if ctx.mult() is not None else "1"
        self._make_place(self._sub_net, molecule)
        for i in range(int(mult)):
            transition = self._unique_t_name(molecule + "_degradation" + ("_" + str(i) if i > 0 else ""))
            self._make_transition(self._sub_net, transition)
            self._make_input_arc(self._sub_net, molecule, transition)

    # Exit a parse tree produced by ModuleParser#protein_complex_formation.
    def exitProtein_complex_formation(self, ctx: ModuleParser.Protein_complex_formationContext):
        pass

    # Exit a parse tree produced by ModuleParser#enzymatic_reaction.
    def exitEnzymatic_reaction(self, ctx: ModuleParser.Enzymatic_reactionContext):
        e = ctx.PROTEIN().getText()
        l0 = ctx.m_list()[0].getText()
        l1 = ctx.m_list()[1].getText()
        proteins_in = _mlist_to_dict(l0)
        proteins_out = _mlist_to_dict(l1)
        transition = self._unique_t_name(f"enzymatic_reaction")
        self._make_transition(self._sub_net, transition)
        self._make_place(self._sub_net, e)
        self._make_input_arc(self._sub_net, e, transition)
        self._make_output_arc(self._sub_net, e, transition) # altrimenti se il marking è 0 la transizione non scatta mai! -> usa degradation
        for p in proteins_in:
            self._make_place(self._sub_net, p)
            self._make_input_arc(self._sub_net, p, transition)
        for p in proteins_out:
            self._make_place(self._sub_net, p)
            self._make_output_arc(self._sub_net, p, transition)

    # Exit a parse tree produced by ModuleParser#type_inhibitors.
    def exitType_inhibitors(self, ctx: ModuleParser.Type_inhibitorsContext):
        d = _mlist_to_dict(ctx.parentCtx.m_list().getText())
        self._regulation_elems["INHIBITORS"] = d

    # Exit a parse tree produced by ModuleParser#type_inducers.
    def exitType_inducers(self, ctx: ModuleParser.Type_inducersContext):
        d = _mlist_to_dict(ctx.parentCtx.m_list().getText())
        self._regulation_elems["INDUCERS"] = d

    # Exit a parse tree produced by ModuleParser#type_activators.
    def exitType_activators(self, ctx: ModuleParser.Type_activatorsContext):
        d = _mlist_to_dict(ctx.parentCtx.m_list().getText())
        self._regulation_elems["ACTIVATORS"] = d

    # Exit a parse tree produced by ModuleParser#m_list.
    def exitM_list(self, ctx: ModuleParser.M_listContext):
        pass

    # TODO va inserita invece la logica di notification da reti inferiori a posti nella rete superiore (molecule sotto == posto sopra)
    # idea: cerco nelle strutture dati d'appoggio se nella rete sotto c'è la molecola (posto), allora mi segno che è da notificare al suo posto padre
    # Exit a parse tree produced by ModuleParser#paracrine_signals.
    def exitParacrine_signals(self, ctx: ModuleParser.Paracrine_signalsContext):
        net = self._parent_net
        molecules = set([m.getText() for m in ctx.molecule()])
        rule = "Expression(\"" + (" or ".join([("str(x) == " + repr(m)) for m in molecules])) + "\")"
        for n1, n1_neighbors in self._neighbors.items():
            for n2 in n1_neighbors:
                transition = self._unique_t_name(f"paracrine_signaling_{n1}_{n2}")
                self._make_transition(net, transition, rule)
                self._make_input_arc(net, n1, transition, token_type=f"Variable('x')")
                self._make_output_arc(net, n2, transition, token_type=f"Variable('x')")

                transition = self._unique_t_name(f"paracrine_signaling_{n2}_{n1}")
                self._make_transition(net, transition, rule)
                self._make_input_arc(net, n2, transition, token_type="Variable('x')")
                self._make_output_arc(net, n1, transition, token_type="Variable('x')")

    # TODO in una versione futura si potrebbe rimuovere la necessità di scrivere un JUXTACRINE_SIGNAL per ogni vicino:
    # TODO il vicinato viene costruito dopo il signaling! spostare la roba qua sotto in un altro listener (oppure spostare build_neighborhood)
    # TODO forse meglio cercare le coordinate dello scope dest e calcolare la distanza dentro questa funzione, senza spostare nulla
    # Exit a parse tree produced by ModuleParser#juxtacrine_signal.
    def exitJuxtacrine_signal(self, ctx: ModuleParser.Juxtacrine_signalContext):
        src_scope = ctx.parentCtx.ID().getText()
        dest_scope = ctx.ID().getText()
        #if src_scope in self._neighbors[dest_scope] or dest_scope in self._neighbors[src_scope]:
        molecule = ctx.PROTEIN().getText()
        net = self._parent_net
        rule = f"Expression(\"str(x) == {repr(molecule)}\")"
        transition = self._unique_t_name(f"juxtacrine_signaling_{molecule}_{src_scope}_{dest_scope}")
        self._juxtacrine_transitions.append((net, transition, rule, src_scope, dest_scope))
