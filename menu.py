from AFD.createAFD import CreateAFD
from Grammars.CreateGrammar import CreateGrammar

def menu():    
    while True:
        print("Menú")
        print("1. Crear AFD")
        print("2. Crear gramática")
        print("3. Evaluar cadenas")
        print("4. Reportes")
        print("5. Cargar Archivo")
        print("6. Salir")
        opc = int(input("Escoje una opcion: "))

        if opc == 1:
            afd = CreateAFD()
            afd.name()
            afd.menuAFD()

        elif opc == 2:
            grammar = CreateGrammar()
            grammar.name()
            grammar.menuGrammar()
            
        if opc == 6:
            break
