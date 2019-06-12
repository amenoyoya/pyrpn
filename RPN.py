# encoding: utf-8

# 関数の引数の数を取得するためにsignatureをimport
from inspect import signature
import re

class Variable:
    ''' 変数名として使える文字列か判定するクラス '''
    class NameError(Exception):
        def __str__(self):
            return 'Invalid character specified for variable name.'
    
    # 変数名には[アルファベット, 数字, _, .]のみ使用可能
    pattern = re.compile(r'^[a-zA-Z0-9_\.]+$')
    
    def __init__(self, variable_name):
        if Variable.pattern.match(variable_name) is None:
            raise Variable.NameError()
        self.name = variable_name
    
    def __str__(self):
        return self.name


class Value:
    ''' 値クラス '''
    VALUE = 0 # 値
    CHUNK = 1 # 遅延評価式

    def __init__(self, value, _type=VALUE):
        self.value = value
        self.type = _type


def eval_rpn(exp):
    ''' 逆ポーランド記法を計算する関数
    params:
        exp list: 逆ポーランド記法プログラムの配列
            el: [Value(1), Value(2), (lambda x, y: x.value + y.value)] => 1 + 2
    '''
    stack = []
    for e in exp:
        if callable(e):
            # 関数なら関数実行
            argc = len(signature(e).parameters) # 関数の引数の数を取得
            res = e(*stack[-argc:]) # stackの後ろから引数を取得し、関数実行
            stack = stack[:-argc] # 引数分をstackから削除
            if res is not None:
                stack.append(res) # 関数の戻り値をstack
        else:
            # 関数でない場合はstack
            stack.append(e)
    return stack
