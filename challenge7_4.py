correct = [1, 3, 4, 6]
while True:
    a = input('数字を入力してください（"q"で終了）')
    if a == 'q':
        break
    elif not a.isnumeric():
        print('数字か、終了する場合はqを入力してください')
        continue
    elif int(a) in correct:
        print('正解！')
    else:
        print('残念！ハズレ！')
        
