from AFD import AFD

afd = AFD('afd1')

afd.setStates('S')
afd.setStates('A')
afd.setStates('B')
afd.setStates('AP')
afd.setStates('BP')

afd.setAlphabet('a')
afd.setAlphabet('b')
afd.setAlphabet('0')
afd.setAlphabet('1')
afd.setAlphabet('m')
afd.setAlphabet('s')

afd.setInitialState('S')

afd.setAcceptanceStates('AP')
afd.setAcceptanceStates('BP')

afd.setTransitions('S,A;a')
afd.setTransitions('A,AP;0')
afd.setTransitions('AP,AP;0')
afd.setTransitions('AP,AP;1')
afd.setTransitions('S,B;b')
afd.setTransitions('B,BP;m')
afd.setTransitions('BP,BP;s')

afd.evaluateString('bmss')