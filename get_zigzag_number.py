from sympy import var, series, poly, tan, sec
import math
import sys


def get_zigzag_number(index):
    # シンボルxを定義
    x = var('x')

    # 級数展開を定義
    f = series(tan(x) + sec(x), x, n = index + 1)

    # 級数を多項式オブジェクトに変換
    g = poly(f)

    # すべての係数を取得
    coeffs = g.coeffs()
    coeffs.reverse()

    # ランダウのO記号の係数である1が先頭に入ってしまうので削除
    coeffs.pop(0)

    # 戻り値を取得
    coef = coeffs[index]
    coef = coef * math.factorial(index)
    return coef


if __name__ == "__main__":
    args = sys.argv
    index = int(args[1])
    print(get_zigzag_number(index))