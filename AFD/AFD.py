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
        return True

    def evaluateString(self, words):
        actual = self.initialState
        for w in words:
            if w in self.alphabet:
                for item in self.transitions:
                    if w == item['t']:
                        first = item['fS']
                        last = item['lS']

                        if first == actual:
                            print(f"Cadena Correcta: {first} -> {last} por {w}")
                            actual = last

                            if actual in self.acceptanceStates:
                                print("Se llego a  estado de aceptacion")
                                break

                            break

            else:
                print(f"{w} no pertenece al lenguaje")
                break
         