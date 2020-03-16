import os
class CreateAFD:
    
    states = []
    words = []
    states_acceptance = []
    
    def name(self):
        os.system('clear')
        print('Bienvenido a AFD')
        nameAFD = input('Introduzca el nombre del AFD: ')

    def menuAFD(self):
        while True:
            print("1. Ingresar Estados")
            print("2. Ingresar Alfabeto")
            print("3. Estado Inicial")
            print("4. Estados de aceptación")
            print("5. Transiciones")
            print("6. Regresar")
            opcAFD = int(input('Escoje una opcion: '))
            
            os.system('clear')
            if opcAFD == 1:
                nStates = int(input("Numero de estados: "))
                i = 1
                for i in range(nStates):
                    state = input(f"Estado {i}: ")
                    self.states.append(state)
            
            if opcAFD == 2:
                nWords = int(input("Numero de palabras en el alfabeto: "))
                i = 1
                for i in range(nWords):
                    word = input(f"Palabra no {i}: ")
                    self.words.append(word)
            
            if opcAFD == 3:
                print("Estados existentes")
                for state in self.states:
                    print(f"Estado {state}")
                initial_state = input("Coloque el nombre del estado inicial: ")
                
                if initial_state not in self.states:
                    print(f"El estado {initial_state} no pertenece al conjunto de estados")
                else:
                    print(f"El estado {initial_state} es inicial ahora")

            if opcAFD == 4:
                print("Estados existentes")
                for state in self.states:
                    print(f"Estado {state}")
                n_accept_state = int(input("Coloque el numero del estado de aceptación: "))

                i = 1
                for i in range(n_accept_state):
                    while True:
                        state = input(f"Estado de aceptación {i}: ")

                        if state not in self.states:
                            print(f"El estado {state} no pertenece al conjunto de estados")
                        else:
                            print(f"El estado {state} es de aceptación ahora")
                            self.states_acceptance.append(state)
                            break
            
            if opcAFD == 6:
                break

