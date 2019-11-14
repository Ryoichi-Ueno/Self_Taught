l = ['The', 'fox', 'jumped', 'over', 'the', 'fence', '.']
print(' '.join(l).replace(' .', '.'))
print(' '.join(l)[:-2] + ' '.join(l)[-1:])
