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
        self.states.append(state)

    def setAlphabet(self, word):
        self.alphabet.append(word)

    def setInitialState(self, state):
        if state in self.states:
            self.initialState = state

    def setAcceptanceStates(self, state):
        if state in self.states:
            self.acceptanceStates.append(state)

    def setTransitions(self, transition):
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
         