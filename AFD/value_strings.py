from AFD import AFD

afd = AFD('afd1')

afd.setStates('A')
afd.setStates('B')
afd.setStates('C')

afd.setAlphabet('0')
afd.setAlphabet('1')

afd.setInitialState('A')

afd.setAcceptanceStates('C')

afd.setTransitions('A,A;1')
afd.setTransitions('A,B;0')
afd.setTransitions('B,B;1')
afd.setTransitions('B,C;0')
afd.setTransitions('C,C;0')
afd.setTransitions('C,C;1')

afd.evaluateString('101010')