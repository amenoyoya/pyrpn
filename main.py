# encoding: utf-8
from RPN import Value, pn2rpn, eval_rpn_variable
import sqlite3
from contextlib import closing

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

# ポーランド記法でSQLクエリ定義
## 逆ポーランド記法: id 3 < gender "male" = and gender "female" = or
## => ((id < 3) and (gender = "male")) or (gender = "female")
## => ((id < ?) and (gender = ?)) or (gender = ?), [3, "male", "female"]
exp = pn2rpn(op, {
    'or': {
        'and': {
            '<': {'id': 3},
            '=': {'gender': 'male'},
        },
        '=': {'gender': 'female'},
    },
})

print([v if type(v) == str else v.value for v in exp])

# 演算実行
query = eval_rpn_variable(exp, op)
print(query[0].value, binds)

# sqlite3実行
with closing(sqlite3.connect('sample.db')) as conn:
    c = conn.cursor()
    c.execute('select * from users where ' + query[0].value, binds)
    print(c.fetchall())
