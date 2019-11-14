def sample(a, b, c, d = 2, e = 3):
    """ a,b,c,d,eすべてをかけ合わせた結果を返す

        @param a 数値
        @param b 数値
        @param c 数値
        @param d 数値
        @param e 数値
        戻り値 a*b*c*d*eの結果
    """
    print(a)
    print(b)
    print(c)
    print(d)
    print(e)
    print(type(d))
    print(type(e))

    return a * b * c * d * e

    
try:
    a = int(input('数値を入力してください（1つ目） >'))
    b = int(input('数値を入力してください（2つ目） >'))
    c = int(input('数値を入力してください（3つ目） >'))
#    d = 0
#    e = 0
    params = [a, b, c]
    s = input('数値を入力してください（（4つ目:省略可）')
    if not (s == ''):
        d = int(s)
        params.append(d)
        s = input('数値を入力してください（（5つ目:省略可）')
        if not (s == ''):
            e = int(s)
            params.append(e)

    print(params)
    print(str(sample(*params)))
except(ValueError):
    print('入力値が不正です')
    
