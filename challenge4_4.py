def fun1(int):
    """ 引数を2で割った整数部分を返す関数

        @param int 割る対象の数値
        戻り値     intを2で割った値の整数部
    """
    return int // 2

def fun2(int):
    """ 引数に4をかけた数値を返す関数

        @param int 割る対象の数値
        戻り値     引数に4をかけた数値
    """
    print(int)
    return (int * 4)

try:
    num = int(input('数値を入力してください >'))
    print(str(fun2(fun1(num))))
except(ValueError):
    print('入力値が不正です')

    
