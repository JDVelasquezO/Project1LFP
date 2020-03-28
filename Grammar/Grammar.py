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
        nt = production.split(">")[0]
        exp = production.split(">")[1]
        objectProduction = {}

        if nt in self.non_terminals:

            objectProduction = {
                "NT": nt,
                "E": []
            }

        for e in exp:
            if e in self.terminals or e in self.non_terminals:
                objectProduction["E"].append(e)
        
        self.productions.append(objectProduction)

    def getTransformedGrammar(self, name):
        new_Prod = {}
        new_Grammar = {}

        if self.name == name:
            NT_derived = ""

            for production in self.productions:
                if production["NT"] == production["E"][0]:
                    NT_derived = production["NT"] + "'"

                    new_Prod["NT"] = NT_derived
                    new_Prod["E"] = production["E"][1] + NT_derived
                    new_Prod["String"] = f"{new_Prod['NT']}>{new_Prod['E']}"
                
                if production["NT"] != production["E"][0]:
                    new_T = production["E"][0]
                    new_E =  new_T + NT_derived
                    new_Grammar["NT"] = production["NT"]
                    new_Grammar["E"] = new_E
                    new_Grammar["String"] = f"{new_Grammar['NT']}>{new_Grammar['E']}"
                    break
    
        return f"{new_Prod['String']}" + "\n" + f"{new_Grammar['String']}"
             
    def setInitialNT(self, nt):
        self.initial_non_terminal = nt

    def getNonTerminals(self):
        return self.non_terminals

    def getTerminals(self):
        return self.terminals

    def getProductions(self):
        return self.productions