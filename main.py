# encoding: utf-8
from RPN import eval_rpn_variable

''' 四則演算用逆ポーランド演算 '''

# 演算子, 組み込み変数定義
op = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y,
    'ten':     10,
    'hundred': 100,
    'pi':      3.14,
}

# 計算式定義
## 1 2 + 3 * 4 - ten * hundred / pi +
## => ((1 + 2) * 3 - 4) * ten / hundred + pi
## => ((1 + 2) * 3 - 4) * 10 / 100 + 3.14
## => 3.64
exp = [
    1, 2, '+', 3, '*', 4, '-', 'ten', '*', 'hundred', '/', 'pi', '+'
]

# 演算実行
ans = eval_rpn_variable(exp, op)
print(ans[0])
