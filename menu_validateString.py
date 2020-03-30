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
            wait_for("", "\n")

        if opc == 5:
            break