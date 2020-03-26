import os
class CreateAFD:
    
    states = []
    words = []
    initial_state = ""
    states_acceptance = []
    transitions = []
    transition = {}
    data_input = []
    
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
            print("6. Cadena a evaluar")
            print("7. Regresar")
            opcAFD = int(input('Escoje una opcion: '))
            
            os.system('clear')
            if opcAFD == 1:
                n_states = int(input("Numero de estados: "))
                i = 1
                for i in range(n_states):
                    state = input(f"Estado {i}: ")
                    self.states.append(state)
            
            if opcAFD == 2:
                n_words = int(input("Numero de palabras en el alfabeto: "))
                i = 1
                for i in range(n_words):
                    word = input(f"Palabra no {i}: ")
                    self.words.append(word)
            
            if opcAFD == 3:
                print("Estados existentes")
                for state in self.states:
                    print(f"Estado {state}")
                self.initial_state = input("Coloque el nombre del estado inicial: ")
                
                if self.initial_state not in self.states:
                    print(f"El estado {self.initial_state} no pertenece al conjunto de estados")
                else:
                    print(f"El estado {self.initial_state} es inicial ahora")

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
            
            if opcAFD == 5:
                print("1. Modo 1")
                print("2. Modo 2")
                mode = int(input("Escojer un modo de transiciones: "))

                if mode == 1:
                    print("Modo 1")
                    print("Ingresar con la siguiente notación: A,B;a")
                    print("Estados existentes")
                    for state in self.states:
                        print(f"Estado {state}")

                    print("Palabras existentes")
                    for word in self.words:
                        print(f"Estado {word}")
                    
                    n_transition = int(input("Numero de transiciones: "))

                    i = 1
                    for i in range(n_transition):
                        trans = input(f"Transicion {i}: ")
                        newTrans = trans.split(";")

                        # key = newTrans[0]
                        # value = newTrans[1]

                        # self.transition = {
                        #     "key": key,
                        #     "value": value
                        # }
                        self.transitions.append(newTrans)

            if opcAFD == 6:

                words = input("Escriba la palabra a evaluar: ")

                word = words.split(";")
                
                for w in word:
                    print(w)

                # n_inputEvaluate = int(input("Numero de palabras a evaluar: "))

                # i = 1
                # for i in range(n_inputEvaluate):
                #     data = input(f"Palabra no {i}: ")
                #     self.data_input.append(data)

                # # actual = self.initial_state
                # values = []
                # for t in self.transitions:
                #     values.append(t["value"])

                # # j = 0
                # # for i in self.data_input:
                # #     if i == values[j]:
                # #         print(f"Existe {i} en la posicion {j} = {values[j]}")
                # #     j = j + 1
            
            if opcAFD == 7:
                break
