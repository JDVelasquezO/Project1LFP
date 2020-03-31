from Grammar import Grammar

grammar = Grammar("gram2")

grammar.setNonTerminals("A")
grammar.setNonTerminals("B")

grammar.setTerminals("1")
grammar.setTerminals("0")

grammar.setInitialNT("A")

grammar.setProductions("A>0 B | A>1 A | A>epsilon")
grammar.setProductions("B>0 B | B>1 A")

if (grammar.onlyEvaluate('0101')):
    print("Cadena válida")
else:
    print("Cadena invalida")

print(grammar.evaluateString("0101"))
