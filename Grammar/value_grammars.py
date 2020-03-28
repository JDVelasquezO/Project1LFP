from Grammar import Grammar

grammar = Grammar("grammar1")

grammar.setNonTerminals("A")

grammar.setTerminals("a")
grammar.setTerminals("b")

grammar.setProductions("A>Aa")
grammar.setProductions("A>b")

print(grammar.getTransformedGrammar("grammar1"))
