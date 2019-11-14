l = []

print('何か入力してください。入力された文字をファイル(input.txt)に書き出します。')
while True:
    s = input('終了するときは"p" >')
    if s == 'p':
        break
    l.append(s)

with open('input.txt', 'w', encoding = 'utf_8') as f:
    f.write('\n'.join(l))

        
