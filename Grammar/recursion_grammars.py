from Grammar import Grammar

grammar = Grammar("grammar1")

grammar.setNonTerminals("A")
grammar.setNonTerminals("B")
grammar.setNonTerminals("S")

grammar.setTerminals("a")
grammar.setTerminals("b")
grammar.setTerminals("0")
grammar.setTerminals("1")
grammar.setTerminals("s")
grammar.setTerminals("m")

grammar.setProductions("S>a A")
grammar.setProductions("S>b B")
grammar.setProductions("A>A 0")
grammar.setProductions("A>A 1")
grammar.setProductions("A>0")
grammar.setProductions("B>B s")
grammar.setProductions("B>m")

grammar.keepGrams(grammar)

# print(grammar.getTransformedGrammar("grammar1"))
print(grammar.getGrams())