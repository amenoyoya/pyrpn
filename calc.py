# encoding: utf-8

from rpn import RPN, Value, Variable

# 日本語四則演算子
class Calc(RPN):
    operators = {
        '足す': lambda x, y: Value(x.value + y.value),
        '引く': lambda x, y: Value(x.value - y.value),
        '掛ける': lambda x, y: Value(x.value * y.value),
        '割る': lambda x, y: Value(x.value / y.value),
    }

# ポーランド記法から逆ポーランド記法構築
## (割る (掛ける (足す 1 2) (引く 5 10)) 3)
## => [1, 2, '+', 5, 10, '-', '*', 3, '/']
rpn = Calc.build({
    '割る': [
        {
            '掛ける': {
                '足す': [1, 2],
                '引く': [5, 10],
            }
        }, 3
    ]
})

print(Calc.explain(rpn))

# 逆ポーランド記法を計算
## [1, 2, '+', 5, 10, '-', '*', 3, '/']
## => {(1 + 2) * (5 -10)} / 3
## => -5.0
ans = Calc.eval(rpn)
print(Calc.explain(ans))
