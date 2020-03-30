import os
from Grammar.Grammar import Grammar

class CreateGrammar():
    
    grammar = Grammar("")
    array_grammar = []

    def name(self):
        os.system('clear')
        print('Bienvenido a Gramáticas')
        nameGrammar = input('Introduzca el nombre de la gramática: ')
        self.grammar = Grammar(nameGrammar)
        self.array_grammar.append(self.grammar)

    def menuGrammar(self):
        while True:
            print("Menu de  Gramáticas")
            print("1. Ingresar No Terminales")
            print("2. Ingresar Terminales")
            print("3. No Terminal Inicial")
            print("4. Producciones")
            print("5. Mostrar Gramática Transformada")
            print("6. Ayuda")
            print("7. Salir")
            opcGram = int(input('Escoje una opcion: '))

            os.system('clear')

            if opcGram == 1:
                # n_NT = int(input("Numero de No Terminales: "))
                # i = 1
                # for i in range(n_NT):
                nt = input(f"Ingresar No Terminal: ")
                os.system('clear')
                while (not self.grammar.setNonTerminals(nt)):
                    print("Elemento ya existente. Intente con otro")
                    nt = input(f"Ingresar No Terminal: ")
                os.system('clear')

            if opcGram == 2:
                # n_T = int(input("Numero de Terminales: "))
                # i = 1
                # for i in range(n_T):
                t = input(f"Ingresar Terminal: ")
                os.system('clear')
                while (self.grammar.setTerminals(t)):
                    print("Elemento ya existente. Intente con otro")
                    t = input(f"Ingresar Terminal: ")
                os.system('clear')

            if opcGram == 3:
                init_nt = input("Digita el NT inicial: ")
                os.system('clear')
                while (not self.grammar.setInitialNT(init_nt)):
                    print("El NT no existe en el conjunto. Intente de nuevo")
                    init_nt = input("Digita el NT inicial: ")
                os.system('clear')

            if opcGram == 4:
                print("Ingresar las producciones con la notación BNF")
                print("Notacion BNF: <NT> > <E>")
                # n_prods = int(input("Numero de gramaticas: "))

                # for i in range(n_prods):
                prod = input(f"Ingresar Produccion: ")
                os.system('clear')
                while (not self.grammar.setProductions(prod)):
                    print("La producción ya existe. Intente de nuevo")
                os.system('clear')

            if opcGram == 5:
                name = input("Ingrese el nombre de la gramática: ")
                os.system('clear')
                while name != self.getName():
                    print("Ese nombre no esta registrado")
                    name = input("Ingrese el nombre de la gramática: ")
                print(self.grammar.getTransformedGrammar(name))
                os.system('clear')
            
            if opcGram == 6:
                os.system('clear')
                print("Lenguajes Formales de Programación")
                print("Aux: Elmer Real")
                print("2")

            if opcGram == 7:
                break