# encoding: utf-8
'''
ポーランド記法
{
    演算子: [引数, ...],
    演算子: {変数: 値}
}
'''
from RPN import Value, Variable

def pn2rpn(exp):
    rpn = []
    def convert(exp, rpn):
        for key, value in exp.items():
            if type(key) == str:
                rpn += Value(str(Variable(key)), Value.CHUNK)

            if type(value) == dict:
                rpn += convert(value, rpn)
            elif type(value) == list:
                rpn += value
            else:
                rpn += [Value(value)]
            
            if callable(key):
                rpn += key
    return convert(exp, rpn)
