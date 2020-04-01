import os, sys
from AFD.value_file import value_file
sys.path.append('./Grammar')
from value_grammar import value_grammar
from menu_validateString import menuValidateString

def menu_files():    
    while True:
        print("Menú De Archivos")
        print("1. Cargar un archivo AFD")
        print("2. Cargar un archivo Gramática")
        print("3. Salir")
        opc = int(input("Escoje una opcion: "))

        if opc == 1:
            route = './files/test.afd'
            routeArray = route.split('/')
            name = routeArray[-1].split(".")[0]
            file = open(route, 'r')
            print('Archivo cargado correctamente\n')
            os.system('clear')
            value_file(file, name)

        if opc == 2:
            route = './files/test.grm'
            routeArray = route.split('/')
            name = routeArray[-1].split(".")[0]
            file = open(route, 'r')
            print('Archivo cargado correctamente\n')
            os.system('clear')
            value_grammar(file, name)
        
        if opc == 3:
            os.system('clear')
            break
