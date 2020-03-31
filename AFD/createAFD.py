import os
from AFD.AFD import AFD

class CreateAFD:

    afd = AFD("")
    array_afd = []
    
    def name(self):
        os.system('clear')
        print('Bienvenido a AFD')
        nameAFD = input('Introduzca el nombre del AFD: ')
        self.afd = AFD(nameAFD)
        self.array_afd.append(self.afd)

    def returnAFD(self):
        return self.afd

    def menuAFD(self):
        while True:
            print("Menu de AFD")
            print("1. Ingresar Estados")
            print("2. Ingresar Alfabeto")
            print("3. Estado Inicial")
            print("4. Estados de aceptación")
            print("5. Transiciones")
            print("6. Ayuda")
            print("7. Regresar")
            opcAFD = int(input('Escoje una opcion: '))
            
            os.system('clear')
            
            if opcAFD == 1:
                # n_states = int(input("Numero de estados: "))
                # i = 1
                # for i in range(n_states):
                #     state = input(f"Estado {i}: ")
                #     self.afd.setStates(state)
                state = input("Ingresar estado: ")
                os.system('clear')
                while (not self.afd.setStates(state)):
                    print("Ese simbolo ya existe. Escribir otro:")
                    state = input("Ingresar estado: ")
                os.system('clear')

            if opcAFD == 2:
                # n_words = int(input("Numero de palabras en el alfabeto: "))
                # i = 1
                # for i in range(n_words):
                #     word = input(f"Palabra no {i}: ")
                #     self.afd.setAlphabet(word)
                word = input("Ingresar palabra de alfabeto: ")
                os.system('clear')
                while (not self.afd.setAlphabet(word)):
                    print("Ese simbolo ya existe. Escribir otro:")
                    word = input("Ingresar estado: ")
                os.system('clear')
            
            if opcAFD == 3:
                print("Estados existentes")

                for state in self.afd.getStates():
                    print(f"Estado {state}")
                initial_state = input("Coloque el nombre del estado inicial: ")
                
                if initial_state not in self.afd.getStates():
                    print(f"El estado {initial_state} no pertenece al conjunto de estados")
                    initial_state = input("Coloque el nombre del estado inicial: ")
                else:
                    self.afd.setInitialState(initial_state)
                    os.system('clear')

            if opcAFD == 4:
                print("Estados existentes")
                for state in self.afd.getStates():
                    print(f"Estado {state}")
                # n_accept_state = int(input("Coloque el numero del estado de aceptación: "))

                # i = 1
                # for i in range(n_accept_state):
                while True:
                    state = input(f"Ingresar estado de aceptación: ")
                    os.system('clear')
                    while (not self.afd.setAcceptanceStates(state)):
                        print("Error. Pruebe con otro estado ")
                        state = input(f"Ingresar estado de aceptación: ")
                    os.system('clear')

                    if state not in self.afd.getStates():
                        print(f"El estado {state} no pertenece al conjunto de estados")
                    else:
                        self.afd.setAcceptanceStates(state)
                        os.system('clear')
                        break
            
            if opcAFD == 5:
                print("1. Modo 1")
                print("2. Modo 2")
                mode = int(input("Escojer un modo de ingresar transiciones: "))

                os.system('clear')
                if mode == 1:
                    print("Modo 1")
                    print("Ingresar con la siguiente notación: A,B;a")
                    print("Estados existentes")
                    for state in self.afd.getStates():
                        print(f"Estado {state}")

                    print("Palabras existentes")
                    for word in self.afd.getAlphabet():
                        print(f"Estado {word}")
                    
                    # n_transition = int(input("Numero de transiciones: "))

                    # i = 1
                    # for i in range(n_transition):
                    trans = input(f"Ingresar Transicion: ")
                    os.system('clear')
                    while (not self.afd.setTransitions(trans)):
                        print("Error en transición. Ingrese otra")
                        trans = input(f"Ingresar Transicion: ")
                        os.system('clear')

                elif mode == 2:
                    print("En proceso")

            if opcAFD == 6:
                os.system('clear')
                print("Lenguajes Formales de Programación")
                print("Aux: Elmer Real")
                print("2")
            
            if opcAFD == 7:
                break
