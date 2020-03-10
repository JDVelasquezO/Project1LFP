import os
class CreateAFD:
    
    states = []
    
    def name(self):
        os.system('clear')
        print('Bienvenido a AFD')
        nameAFD = input('Introduzca el nombre del AFD: ')

    def menuAFD(self):
        print("1. Ingresar Estados")
        print("2. Ingresar Alfabeto")
        print("3. Estado Inicial")
        print("4. Estados de aceptación")
        print("5. Transiciones")
        print("6. Regresar")
        opcAFD = int(input('Escoje una opcion:'))
        
        os.system('clear')
        if opcAFD == 1:
            nStates = int(input("Numero de estados:"))
            i = 1
            for i in range(nStates):
                state = input(f"Estado {i}: ")
                self.states.append(state)

        print("Estados existentes")
        for state in self.states:
            print(f"Estado {state}")
            

