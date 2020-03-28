import os
from Grammars.Grammar import Grammar

class CreateGrammar():
    
    grammar = Grammar("")

    def name(self):
        os.system('clear')
        print('Bienvenido a Gramáticas')
        nameGrammar = input('Introduzca el nombre de la gramática: ')
        self.grammar = Grammar(nameGrammar)

    def menuGrammar(self):
        print("Menu de  Gramáticas")