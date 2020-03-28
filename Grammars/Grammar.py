class Grammar():
    
    name = ""
    non_terminals = []
    terminals = []
    productions = []

    def __init__(self, name):
        self.name = name

    def setNonTerminals(self, nTerminal):
        self.non_terminals.append(nTerminal)

    def setTerminals(self, terminal):
        self.terminals.append(terminal)

    def setProductions(self, production):
        self.productions.append(production)

    def getNonTerminals(self):
        return self.non_terminals

    def getTerminals(self):
        return self.terminals

    def getProductions(self):
        return self.productions