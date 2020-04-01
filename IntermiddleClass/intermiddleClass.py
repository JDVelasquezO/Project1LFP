import sys
sys.path.append('./AFD')
sys.path.append('./Grammar')
from AFD import AFD
from Grammar import Grammar

class IntermiddleClass:
  
    def transformGrammar(self, afd, string):
        non_terminals = afd.states
        terminals = afd.alphabet
        initial_nt = afd.initialState
        productions = afd.transitions
        epsilon_prod = ""
        msg = ""

        for item in afd.getAcceptanceStates():
            prod = {
                'fS': item,
                't': 'epsilon',
                'lS': ""
            }
            # epsilon_prod = f"{item}>epsilon"
            productions.append(prod)

        for item in productions:
            item["String"] = f"{item['fS']}>{item['t']} {item['lS']}"
        
        grammar = Grammar(afd.getName())
        for nt in non_terminals:
            grammar.setNonTerminals(nt)
        
        for t in terminals:
            grammar.setTerminals(t)

        grammar.setInitialNT(initial_nt)

        for p in productions:
            grammar.setProductions(p['String'])

        grammarExtended = grammar.evaluateString(string)
        msg = f"{grammarExtended}"
        return msg
    
    def transformAFD(self, grammar, string):
        states = grammar.non_terminals
        alphabet = grammar.terminals
        acceptanceStates = grammar.epsilon_prods
        transitions = grammar.productions
        initial_state = grammar.initial_non_terminal
        msg = ''

        # Agregar un AFD
        afd = AFD(grammar.getName())

        for item in states:
            afd.setStates(item)

        for item in alphabet:
            afd.setAlphabet(item)

        afd.setInitialState(initial_state)

        for item in acceptanceStates:
            state = item['NT']
            afd.setAcceptanceStates(state)

        for item in transitions:
            # print(item)
            if len(item['E']) > 1:
                if item['E'][0] != 'epsilon':
                    trans = f"{item['NT']},{item['E'][1]};{item['E'][0]}"
                    afd.setTransitions(trans)
        
        msg += afd.evaluateString(string)
        return msg