def nijyou(i):
    """ 引数を二乗した結果を返す

        @param i 入力値
    """
    return i ** 2

try:
    print(str(nijyou(int(input('数値を入力してください >')))))
except(ValueError):
    print('入力値が数値ではありません。')
