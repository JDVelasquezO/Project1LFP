import os
from AFD.AFD import AFD
from press_enter import wait_for

def menuValidateString(afd, gramm):

    while True:
        os.system('clear')
        print("Menú Validar Cadenas")
        print("1. Solo validar")
        print("2. Ruta de AFD")
        print("3. Expandir con gramáticas")
        print("4. Ayuda")
        print("5. Salir")
        opc = int(input("Escoje una opcion: "))

        if opc == 1:
            name = input("Ingrese el nombre de la gramatica: ")
            for item in afd.array_afd:
                if (name == item.getName()):
                    afdClass = afd.returnAFD()
                    string = input("Ingrese la cadena a evaluar: ")
                    if (afdClass.onlyEvaluate(string)):
                        print("Cadena válida")
                    else:
                        print("Cadena invalida")
                else:
                    break
            
            for item in gramm.array_grammar:
                if (name == item.getName()):
                    grammClass = gramm.getGrammar()
                    string = input("Ingrese la cadena a evaluar: ")
                    if (grammClass.onlyEvaluate(string)):
                        print("Cadena válida")
                    else:
                        print("Cadena invalida")
                else:
                    break

            wait_for("", "\n")

        if opc == 2:
            name = input("Ingrese el nombre de la gramatica: ")
            for item in afd.array_afd:
                if (name == item.getName()):
                    afdClass = afd.returnAFD()
                    string = input("Ingrese la cadena a evaluar: ")
                    print(afdClass.evaluateString(string))
            wait_for("", "\n")

        if opc == 3:
            name = input("Ingrese el nombre de la gramatica: ")
            for item in gramm.array_grammar:
                if (name == item.getName()):
                    gramClass = gramm.getGrammar()
                    string = input("Ingrese la cadena a evaluar: ")
                    print(gramClass.evaluateString(string))
            wait_for("", "\n")

        if opc == 4:
            os.system('clear')
            print("Lenguajes Formales de Programación")
            print("Aux: Elmer Real")
            print("2")

        if opc == 5:
            break