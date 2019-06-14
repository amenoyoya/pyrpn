# encoding: utf-8

from RPN import Value, eval_rpn_variable, pn2rpn

op = {
    '+': lambda x, y: Value(x.value + y.value),
    '-': lambda x, y: Value(x.value - y.value),
    '*': lambda x, y: Value(x.value * y.value),
    '/': lambda x, y: Value(x.value / y.value),
}

rpn = pn2rpn(op, {
    '+': {
        '*': {
            '-': [123, 23],
            '/': [50, 2]
        },
        '-': [550, 50]
    }
})

print([e if type(e) == str else e.value for e in rpn])
print([e.value for e in eval_rpn_variable(rpn, op)])
