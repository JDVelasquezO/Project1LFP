from AFD import AFD

afd = AFD('afd1')

afd.setStates('A')
afd.setStates('B')
afd.setStates('C')
afd.setStates('D')
afd.setStates('E')
afd.setStates('F')
afd.setStates('G')
afd.setStates('H')
afd.setStates('I')

afd.setAlphabet('c')
afd.setAlphabet('v')

afd.setInitialState('A')

afd.setAcceptanceStates('B')
afd.setAcceptanceStates('D')
afd.setAcceptanceStates('E')
afd.setAcceptanceStates('F')

afd.setTransitions('A,B;c')
afd.setTransitions('A,G;v')
afd.setTransitions('B,D;v')
afd.setTransitions('B,C;c')
afd.setTransitions('C,B;c')
afd.setTransitions('C,G;v')
afd.setTransitions('D,C;c')
afd.setTransitions('D,E;v')
afd.setTransitions('E,C;c')
afd.setTransitions('E,F;v')
afd.setTransitions('F,C;c')
afd.setTransitions('G,B;c')
afd.setTransitions('G,H;v')
afd.setTransitions('H,B;c')
afd.setTransitions('H,I;v')
afd.setTransitions('I,B;c')

# if (afd.onlyEvaluate('vvvcvvvcvc')):
#     print("Cadena válida")
# else:
#     print("Cadena invalida")

print(afd.evaluateString('vvvc'))