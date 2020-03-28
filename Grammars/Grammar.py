class Grammar():
    
    name = ""
    non_terminals = []
    terminals = []
    productions = []
    initial_non_terminal = ""

    def __init__(self, name):
        self.name = name

    def setNonTerminals(self, nTerminal):
        self.non_terminals.append(nTerminal)

    def setTerminals(self, terminal):
        self.terminals.append(terminal)

    def setProductions(self, production):
        self.productions.append(production)

    def setInitialNT(self, nt):
        self.initial_non_terminal = nt

    def getNonTerminals(self):
        return self.non_terminals

    def getTerminals(self):
        return self.terminals

    def getProductions(self):
        return self.productions