with open('sampletext.txt', 'r', encoding = 'utf_8') as f:
    r = f.read()
print(r.replace('\n', ' '))
print(type(r))
