import sys
from Grammar import Grammar
sys.path.append('./IntermiddleClass')
from intermiddleClass import IntermiddleClass

grammar = Grammar("grammar1")
iClass = IntermiddleClass()

grammar.setNonTerminals("A")
grammar.setNonTerminals("B")
grammar.setNonTerminals("S")

grammar.setTerminals("a")
grammar.setTerminals("b")
grammar.setTerminals("0")
grammar.setTerminals("1")
grammar.setTerminals("s")
grammar.setTerminals("m")

grammar.setInitialNT("S")

grammar.setProductions("S>a A")
grammar.setProductions("S>b B")
grammar.setProductions("A>A 0")
grammar.setProductions("A>A 1")
grammar.setProductions("A>0")
grammar.setProductions("B>B s")
grammar.setProductions("B>m")

print(grammar.getTransformedGrammar("grammar1"))
print(grammar.evaluateString("a0010"))
print("\n")
print(iClass.transformAFD(grammar, 'a0010'))