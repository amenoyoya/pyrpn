# encoding: utf-8
from RPN import Value, eval_rpn

''' 四則演算用逆ポーランド演算 '''
# 演算子定義
op = {
    '+': lambda x, y: Value(x.value + y.value),
    '-': lambda x, y: Value(x.value - y.value),
    '*': lambda x, y: Value(x.value * y.value),
    '/': lambda x, y: Value(x.value / y.value),
}

# 組み込み変数定義
var = {
    'ten': 10,
    'hundred': 100,
    'pi': 3.14,
}

# 計算式定義
## 1 2 + 3 * 4 - ten * hundred / pi +
## => ((1 + 2) * 3 - 4) * ten / hundred + pi
## => ((1 + 2) * 3 - 4) * 10 / 100 + 3.14
## => 3.64
exp = [
    Value(1), Value(2), op['+'], Value(3), op['*'], Value(4), op['-'], Value(var['ten']), op['*'], Value(var['hundred']), op['/'], Value(var['pi']), op['+']
]

# 演算実行
ans = eval_rpn(exp)
print(ans[0].value)
