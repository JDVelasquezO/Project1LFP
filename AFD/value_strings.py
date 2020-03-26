from AFD import AFD

afd = AFD('afd1')

afd.setStates('A')
afd.setStates('B')
afd.setStates('C')
afd.setStates('D')

afd.setAlphabet('a')
afd.setAlphabet('b')

afd.setInitialState('A')

afd.setAcceptanceStates('D')

afd.setTransitions('A,A;a')
afd.setTransitions('A,C;b')
afd.setTransitions('C,B;a')
afd.setTransitions('B,C;b')
afd.setTransitions('B,A;a')
afd.setTransitions('C,D;b')

afd.evaluateString('a b a b b')