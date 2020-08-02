import itertools
import numpy
import sys

def get_zigzag_number(num):
    # 0, 1, 2番目のZig-Zag Numberは1と定義
    if (num == 0):
        return []
    elif (num == 1):
        return [(0,)]
    elif (num == 2):
        return [(0,1)] 
    else:
        # 長さnの順列全てを取得
        permlist = []
        for i in itertools.permutations(list(range(num))):
            permlist.append(i)
        front_sign = 0
        back_sign = 0
        alter_perm = []
        # i番目とi + 1番目の差をとって符号を取得し,
        # 前ステップで取得した i - 1番目とi番目の差の符号との積をとる
        for perm in permlist:
            for i in range(len(perm) - 1):
                # 最初は0番目と1番目の差の符号のみを取得する
                # 0番目と1番目の差の符号が正であれば交代順列の定義に反するので終了
                # 0番目と1番目の差の符号が負であれば次のステップへ
                if i == 0:
                    front_sign = numpy.sign(perm[i] - perm[i + 1])
                    if front_sign == 1:
                        break
                    continue
                back_sign = numpy.sign(perm[i] - perm[i + 1])
                # 積が1であれば符号が反転しておらず交代順列の定義に反するので終了
                if front_sign * back_sign == 1:
                    break
                # 積が-1であれば符号が反転しているので次のステップへ進む
                else:
                    front_sign = back_sign
                if i == len(perm) - 2:
                   # 交代順列であれば配列に格納
                    alter_perm.append(perm)
    return alter_perm

if __name__ == "__main__":
    args = sys.argv
    length = int(args[1])
    for perm in get_zigzag_number(length):
        print(perm)