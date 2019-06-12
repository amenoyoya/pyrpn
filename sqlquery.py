# encoding: utf-8
from RPN import Value, eval_rpn

''' SQL Query Builder '''

# bind values
binds = []

# x <op> y
def build(x, y, op):
    global binds
    exp = '('
    if x.type == Value.VALUE:
        binds += [x.value]
        exp += '?'
    else:
        exp += x.value
    exp += ' ' + op + ' '
    if y.type == Value.VALUE:
        binds += [y.value]
        exp += '?'
    else:
        exp += y.value
    exp += ')'
    return Value(exp, Value.CHUNK)

# 演算子定義
op = {
    '<': lambda x, y: build(x, y, '<'), '<=': lambda x, y: build(x, y, '<='),
    '>': lambda x, y: build(x, y, '>'), '>=': lambda x, y: build(x, y, '>='),
    '=': lambda x, y: build(x, y, '='), '!=': lambda x, y: build(x, y, '!='),
    'and': lambda x, y: build(x, y, 'and'), 'or': lambda x, y: build(x, y, 'or'),
    'like': lambda x, y: build(x, y, 'like')
}

# クエリ定義
## id 100 = name "%_admin_%" like and id 10 < or
## => ((id = 100) and (name like "%_admin_%")) or (id < 10)
## => ((id = ?) and (name like ?)) or (id < ?), [100, "%_admin_%", 10]
exp = [
    Value('id', Value.CHUNK), Value(100), op['='],
    Value('name', Value.CHUNK), Value('%_admin_%'), op['like'],
    op['and'],
    Value('id', Value.CHUNK), Value(10), op['<'],
    op['or']
]

# 演算実行
ans = eval_rpn(exp)
print(ans[0].value, binds)
