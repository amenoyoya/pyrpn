# encoding: utf-8

from libs.rpn import RPN

# 組み込み変数
variables = {
    'HALF': 0.5,
    'TEN': 10,
}

# 逆ポーランド記法で計算実行
## [1 2 + HALF - TEN * 1 2 / /]
## => ((1 + 2 - HALF) * TEN) / (1 / 2) 
## => ((1 + 2 - 0.5) * 10) / (1 / 2)
## => 50.0
exp = [1, 2, '+', 'HALF', '-', 'TEN', '*', 1, 2, '/', '/']
answer = RPN.eval(exp, variables)
print(RPN.explain(answer))
