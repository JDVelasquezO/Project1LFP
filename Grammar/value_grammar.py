import sys, os

sys.path.append('./Grammar')
from Grammar import Grammar
sys.path.append('./IntermiddleClass')
from intermiddleClass import IntermiddleClass

from menu_validateString import menuValidateString
from press_enter import wait_for

def value_grammar(file, name):
    grammar = Grammar(name)
    iClass = IntermiddleClass()

    lines = file.read().split("\n")
    non_terminals = []
    terminals = []
    productions = []
    epsilon_prods = []

    iNT = lines[0][0]

    for line in lines:
        arrayLine = line.split('>')
        non_terminal = arrayLine[0]
        non_terminals.append(non_terminal)

        produceds = arrayLine[1]
        if produceds != 'epsilon':  
            terminal = produceds[0]
            terminals.append(terminal)

        last_non_terminal = produceds[2]
        non_terminals.append(last_non_terminal)

        productions.append(line)

    newNonTerminals = set(non_terminals)
    for nt in newNonTerminals:
        grammar.setNonTerminals(nt)
    
    newTerminals = set(terminals)
    for t in newTerminals:
        grammar.setTerminals(t)

    grammar.setInitialNT(iNT)

    for prod in productions:
        grammar.setProductions(prod)
    
    string = input('Ingresar la cadena a evaluar: ')
    if (grammar.onlyEvaluate(string)):
        print("----------------------Cadena válida----------------------")
    else:
        print("----------------------Cadena invalida----------------------")

    print("\n----------------------Gramatica expandida----------------------")
    print(grammar.evaluateString(string))
    print("\n----------------------Transformada en ruta de AFD----------------------")
    print(iClass.transformAFD(grammar, string))
    file.close()
    wait_for("Presionar enter para continuar", "\n")
    os.system('clear')
    