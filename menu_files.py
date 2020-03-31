import os
from AFD.value_file import value_file
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
            value_file(file, name)
        
        if opc == 3:
            os.system('clear')
            break
