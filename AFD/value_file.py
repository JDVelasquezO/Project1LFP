import sys
from AFD.AFD import AFD
from menu_validateString import menuValidateString
sys.path.append('./IntermiddleClass')
from intermiddleClass import IntermiddleClass

def value_file(file, name):
    afd = AFD(name)
    iClass = IntermiddleClass()

    lines = file.read().split("\n")
    states = []
    alphabet = []
    transitions = []
    
    firstState = {
        'name': '',
        'status': ''
    }

    lastState = {
        'name': '',
        'status': ''
    }

    statesForEvaluate = []

    iState = lines[0][0]

    for line in lines:
        arrayLine = line.split(";")
        
        words = arrayLine[0]
        states.append(words[0])
        states.append(words[2])

        alphabet.append(words[4])
        
        statusState = arrayLine[1].split(",")
        firstStatus = statusState[0]
        lastStatus = statusState[1]

        firstState["name"] = words[0]
        firstState["status"] = firstStatus

        lastState["name"] = words[2]
        lastState["status"] = lastStatus

        if firstState['name'] == lastState['name']:
            if lastState not in statesForEvaluate:
                statesForEvaluate.append(lastState)
        else:
            if lastState not in statesForEvaluate:
                statesForEvaluate.append(lastState)
            
            if firstState not in statesForEvaluate:
                statesForEvaluate.append(firstState)
                
        firstState = {}
        lastState = {}

        newWord = f"{words[0]},{words[2]};{words[4]}"
        transitions.append(newWord)

    newStates = set(states)
    for state in newStates:
        afd.setStates(state)

    newAlphabet = set(alphabet)
    for word in newAlphabet:
        afd.setAlphabet(word)

    afd.setInitialState(iState)

    for state in statesForEvaluate:
        if state['status'] == 'true':
            afd.setAcceptanceStates(state['name'])

    for item in transitions:
        afd.setTransitions(item)

    string = input('Ingresar la cadena a evaluar: ')
    if (afd.onlyEvaluate(string)):
        print("Cadena válida")
    else:
        print("Cadena invalida")
    print("\n")
    print(afd.evaluateString(string))
    print("\n")
    print(iClass.transformGrammar(afd, string))

    file.close()
