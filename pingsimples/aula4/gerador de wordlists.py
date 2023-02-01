import itertools
stringer = input('string a ser permutada:')
resultado = itertools.permutations(stringer, len(stringer))
for i in resultado:
    print(''.join(i))