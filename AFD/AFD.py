import sys
sys.path.append('./Grammar')
from Grammar import Grammar

class AFD():

    states = []
    alphabet = []
    acceptanceStates = []
    transitions = []
    name = ""
    initialState = ""
    
    def __init__(self, name):
        self.name = name
    
    def setStates(self, state):
        if state in self.states or state in self.alphabet:
            return False
        else:
            self.states.append(state)
            return True

    def setAlphabet(self, word):
        if word in self.states or word in self.alphabet:
            return False
        else:
            self.alphabet.append(word)
            return True

    def setInitialState(self, state):
        if state in self.states:
            self.initialState = state

    def setAcceptanceStates(self, state):
        if state in self.acceptanceStates:
            return False
        else:
            if state in self.states:
                self.acceptanceStates.append(state)
                return True

    def setTransitions(self, transition):
        if transition in self.transitions:
            return False
        else:
            words = transition.split(";")
            states = words[0]
            
            firstState = states.split(",")[0]
            lastState = states.split(",")[1]
            word = words[1]

            if firstState in self.states and lastState in self.states and word in self.alphabet:
                
                objectTransition = {
                    "fS": firstState,
                    "lS": lastState,
                    "t": word
                }

                self.transitions.append(objectTransition)
            
            return True

    def getName(self):
        return self.name

    def getStates(self):
        return self.states
    
    def getAlphabet(self):
        return self.alphabet

    def getInitialState(self):
        return self.initialState

    def getAcceptanceStates(self):
        return self.acceptanceStates

    def getTransitions(self):
        return self.transitions

    def onlyEvaluate(self, word):
        for w in word:
            if w not in self.alphabet:
                return False
        if " No se llego a estado de aceptacion" in self.evaluateString(word):
            return False
        return True

    def valuateAcceptState(self):
        return False

    def evaluateString(self, words):
        actual = self.initialState
        msgFinal = ""
        for w in words:
            if w in self.alphabet:
                for item in self.transitions:
                    if w == item['t']:
                        first = item['fS']
                        last = item['lS']

                        if first == actual:
                            msgFinal += f"{first},{last},{w};"
                            # print(f"{first}, {last}, {w};")
                            actual = last

                            if actual in self.acceptanceStates:
                                # print("Se llego a  estado de aceptacion")
                                break

                            break
        if actual not in self.acceptanceStates:
            msgFinal += " No se llego a estado de aceptacion"
            self.valuateAcceptState()
        else:
            msgFinal += " Válida"
            
        return msgFinal
         
    def transformGrammar(self, afd, string):
        non_terminals = afd.states
        terminals = afd.alphabet
        initial_nt = afd.initialState
        productions = afd.transitions
        epsilon_prod = ""

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
        
        grammar = Grammar(self.name)
        for nt in non_terminals:
            grammar.setNonTerminals(nt)
        
        for t in terminals:
            grammar.setTerminals(t)

        grammar.setInitialNT(initial_nt)

        for p in productions:
            grammar.setProductions(p['String'])

        return grammar.evaluateString(string)
