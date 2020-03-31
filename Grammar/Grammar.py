import sys
# sys.path.append('./AFD')
# from AFD import AFD

class Grammar():
    
    name = ""
    non_terminals = []
    terminals = []
    productions = []
    initial_non_terminal = ""
    all_grams = []
    epsilon_prods = []

    def __init__(self, name):
        self.name = name

    def setNonTerminals(self, nTerminal):
        if nTerminal in self.non_terminals:
            return False
        else:
            self.non_terminals.append(nTerminal)
            return True

    def setTerminals(self, terminal):
        if terminal in self.terminals:
            return False
        else:
            self.terminals.append(terminal)
            return True

    def setInitialNT(self, iNT):
        if iNT not in self.non_terminals:
            return False
        else:
            self.initial_non_terminal = iNT
            return True

    def createProduction(self, production):
        nt = production.split(">")[0].strip()
        exp = production.split(">")[1].strip()
        objectProduction = {}

        if nt in self.non_terminals:

            objectProduction = {
                "NT": nt,
                "E": [],
                "String": f"{production}"
            }

        if exp == "epsilon":
            objectProduction["E"].append(exp)
            self.epsilon_prods.append(objectProduction)
        else:
            for e in exp:
                if e in self.terminals or e in self.non_terminals:
                    objectProduction["E"].append(e)
        
        self.productions.append(objectProduction)

    def setProductions(self, production):
        if production in self.productions:
            return False
        else:
            if "|" in production:
                newProd = production.split("|")
                for item in newProd:
                    production = item
                    self.createProduction(production)

            else:
                self.createProduction(production)

            return True

    def keepGrams(self, gram):
        self.all_grams.append(gram)

    def getName(self):
        return self.name

    def getGrams(self):
        return self.all_grams

    def getTransformedGrammar(self, name):
        new_Prods = []
        saved_Prods = []
        productions = []
        new_Prod = {}
        new_Prod_epsilon = {}
        new_Grammar = {}
        actualStatus = ""
        msgNotRecursion = ""

        if self.name == name:
            NT_derived = ""

            for production in self.productions:
                if production["NT"] == production["E"][0]:
                    NT_derived = production["NT"] + "'"

                    new_Prod["NT"] = NT_derived
                    new_Prod["E"] = [f"{production['E'][1]}", f"{NT_derived}"]
                    new_Prod["String"] = f"{new_Prod['NT']}>{new_Prod['E'][0]} {new_Prod['E'][1]}"
                    new_Prod_epsilon["NT"] = NT_derived
                    new_Prod_epsilon["E"] = ["epsilon"]
                    new_Prod_epsilon["String"] = f"{new_Prod['NT']}>epsilon"
                    self.epsilon_prods.append(new_Prod_epsilon)
                    new_Prods.append(new_Prod)
                    new_Prods.append(new_Prod_epsilon)
                    saved_Prods.append(production)
                    
                    productions.append(new_Prod)
                    productions.append(new_Prod_epsilon)

                    new_Prod = {}
                    new_Prod_epsilon = {}
                    NT_derived = ""
            
                if production["NT"] != production["E"][0]:
                    for savedProds in saved_Prods:
                        if production["NT"] == savedProds["NT"]:
                            NT_derived = production["NT"] + "'"
                            new_T = production["E"][0]
                            new_E =  [f"{new_T}", f"{NT_derived}"]

                            new_Grammar["NT"] = production["NT"]
                            new_Grammar["E"] = new_E
                            new_Grammar["String"] = f"{new_Grammar['NT']}>{new_Grammar['E'][0]} {new_Grammar['E'][1]}"
                            new_Prods.append(new_Grammar)
                            productions.append(new_Grammar)
                            new_Grammar = {}
                            break
                    
                    if production["NT"] not in saved_Prods:
                        msgNotRecursion += f"{production['String']} no tiene recursividad \n"
                        productions.append(production)

        unrepairedString = "Cadena original: \n"
        for prod in self.productions:
            unrepairedString += f"{prod['String']}\n"
        unrepairedString += "---------------------------------------\n"

        repairedString = "Cadena arreglada: \n"
        repairedString += msgNotRecursion
        for prod in new_Prods:
            repairedString += prod['String'] + "\n"

        self.productions = productions
            
        return unrepairedString + repairedString

    def onlyEvaluate(self, word):
        for item in self.non_terminals:
            if item not in self.non_terminals:
                return False
        if "No termina en epsilon" in self.evaluateString(word):
            return False
        return True

    def evaluateString(self, words):
        actual = self.initial_non_terminal
        msgFinal = f"{actual} -> "
        tActual = ""
        signal = True
        for w in words:
            for item in self.productions:
                if w == item['E'][0]:
                    nowTerminal = item['NT']
                    if len(item['E']) > 1:
                        nextTerminal = item['E'][1]

                    if nowTerminal == actual:
                        msgFinal += f"{tActual}{w}{nextTerminal} -> "
                        actual = nextTerminal
                        tActual += w
                        break
            
        for item in self.epsilon_prods:
            if actual == item['NT']:
                if item['E'][0] == 'epsilon':
                    msgFinal += f"{tActual}(epsilon) -> {words}"
                    signal = False
                    break
        
        if signal:
            msgFinal += "No termina en epsilon"
            
        return msgFinal

    def setInitialNT(self, nt):
        self.initial_non_terminal = nt

    def getNonTerminals(self):
        return self.non_terminals

    def getTerminals(self):
        return self.terminals

    def getProductions(self):
        return self.productions
