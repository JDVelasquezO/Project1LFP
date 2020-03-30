from AFD.createAFD import CreateAFD
from Grammar.CreateGrammar import CreateGrammar
from menu_validateString import menuValidateString
import os

def menu():    
    while True:
        print("Menú General")
        print("1. Crear AFD")
        print("2. Crear gramática")
        print("3. Evaluar cadenas")
        print("4. Reportes")
        print("5. Cargar Archivo")
        print("6. Salir")
        opc = int(input("Escoje una opcion: "))
        
        os.system('clear')

        if opc == 1:
            afd = CreateAFD()
            afd.name()
            afd.menuAFD()

        elif opc == 2:
            grammar = CreateGrammar()
            grammar.name()
            grammar.menuGrammar()

        elif opc == 3:
            os.system('clear')
            menuValidateString(afd, grammar)
             
        if opc == 6:
            break
