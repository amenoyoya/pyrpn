# encoding: utf-8
'''
ポーランド記法
{
    演算子: [引数, ...],
    演算子: {変数: 値}
}
'''
from RPN import Value, Variable, eval_rpn_variable

def pn2rpn(exp, operators):
    rpn = []
    def convert(exp, operators, rpn):
        for key, value in exp.items():
            op = operators[key]
            
            if op is None:
                rpn += Value(str(Variable(key)), Value.CHUNK)
            
            if type(value) == dict:
                convert(value, operators, rpn)
            elif type(value) == list:
                rpn += [Value(v) for v in value]
            else:
                rpn += [Value(value)]
            
            if op is not None:
                rpn += key
        return rpn
    return convert(exp, operators, rpn)

op = {
    '+': lambda x, y: Value(x.value + y.value),
    '-': lambda x, y: Value(x.value - y.value),
    '*': lambda x, y: Value(x.value * y.value),
    '/': lambda x, y: Value(x.value / y.value),
}

rpn = pn2rpn(
    {
        '+': {
            '*': {
                '-': [123, 23],
                '/': [50, 2]
            },
            '-': [550, 50]
        }
    }, op)

print([e if type(e) == str else e.value for e in rpn])
print([e.value for e in eval_rpn_variable(rpn, op)])
