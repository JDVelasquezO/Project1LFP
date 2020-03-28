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
        while True:
            print("Menu de  Gramáticas")
            print("1. Ingresar No Terminales")
            print("2. Ingresar Terminales")
            print("3. No Terminal Inicial")
            print("4. Producciones")
            print("5. Evaluar Cadenas")
            print("6. Salir")
            opcGram = int(input('Escoje una opcion: '))

            os.system('clear')

            if opcGram == 1:
                n_NT = int(input("Numero de No Terminales: "))
                i = 1
                for i in range(n_NT):
                    nt = input(f"NT {i}: ")
                    self.grammar.setNonTerminals(nt)

            if opcGram == 2:
                n_T = int(input("Numero de Terminales: "))
                i = 1
                for i in range(n_T):
                    t = input(f"Terminal {i}: ")
                    self.grammar.setTerminals(t)

            if opcGram == 3:
                init_nt = input("Digita el NT inicial: ")
                self.grammar.setInitialNT(init_nt)

            if opcGram == 4:
                print("Ingresar las producciones con la notación BNF")
                print("Notacion BNF: <NT> > <E>")
                n_prods = int(input("Numero de gramaticas: "))

                for i in range(n_prods):
                    prod = input(f"Produccion {i}: ")
                    self.grammar.setProductions(prod)

            if opcGram == 5:
                string = input("Introducir la cadena a evaluar: ")
            
            if opcGram == 6:
                break